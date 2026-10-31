"""校验 props/、facades/ 的 PNG 和 JSON，并输出联系表 sheet.png。

用法：python tools/check.py [文件或目录 ...]   （默认检查 props/ facades/）
有错误时退出码为 1。chibi/ 是第三方原图，只查 RGBA、尺寸和来源表。
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
FIELDS = {"w", "h", "ax", "ay", "footprint_m", "height_m", "view", "refs", "confidence", "notes"}
CONFIDENCE = {"据资料", "部分推断", "中性占位"}
VIEWS = {"N", "E", "S", "W"}
SHADOW = (29, 42, 58)


def palette():
    cols = set()
    for line in (ROOT / "palette.gpl").read_text().splitlines()[4:]:
        parts = line.split()
        if len(parts) >= 3:
            cols.add(tuple(int(v) for v in parts[:3]))
    return cols


def check_png(png, pal, errors):
    err = lambda msg: errors.append(f"{png.relative_to(ROOT)}: {msg}")
    img = Image.open(png)
    if img.mode != "RGBA":
        err(f"要 RGBA，现在是 {img.mode}")
        return None
    meta_path = png.with_suffix(".json")
    if not meta_path.exists():
        err("缺同名 .json")
        return img
    meta = json.loads(meta_path.read_text())
    missing = FIELDS - meta.keys()
    if missing:
        err(f"json 缺字段 {sorted(missing)}")
    if (meta.get("w"), meta.get("h")) != img.size:
        err(f"json 写 {meta.get('w')}×{meta.get('h')}，图是 {img.size[0]}×{img.size[1]}")
    if not (0 <= meta.get("ax", -1) < img.width and 0 <= meta.get("ay", -1) < img.height):
        err("锚点 ax、ay 不在图内")
    if meta.get("view") not in VIEWS:
        err("view 要写 N、E、S 或 W")
    if meta.get("confidence") not in CONFIDENCE:
        err(f"confidence 要写 {'、'.join(sorted(CONFIDENCE))} 之一")
    if "@" in png.stem and png.stem.split("@")[1] != meta.get("view"):
        err("文件名里的视角和 json 的 view 不一致")
    allowed = set(pal)
    for c in meta.get("newColors", []):
        hexv = (c["hex"] if isinstance(c, dict) else c).lstrip("#")
        allowed.add(tuple(int(hexv[i:i + 2], 16) for i in (0, 2, 4)))
    bad = set()
    for _, (r, g, b, a) in img.getcolors(1 << 24):
        if a == 0:
            continue
        if a != 255 and (r, g, b) != SHADOW:
            bad.add("半透明（只有投影色 shadow 可以半透明）")
        elif (r, g, b) not in allowed and (r, g, b) != SHADOW:
            bad.add(f"色板外的颜色 #{r:02x}{g:02x}{b:02x}")
    for b in sorted(bad)[:8]:
        err(b)
    if len(bad) > 8:
        err(f"……另有 {len(bad) - 8} 处颜色问题")
    return img


def check_chibi(errors):
    chibi = ROOT / "chibi"
    if not (chibi / "README.md").exists():
        errors.append("chibi/: 缺 README.md（来源和许可证登记表）")
    for png in chibi.rglob("*.png"):
        img = Image.open(png)
        if img.mode != "RGBA":
            errors.append(f"{png.relative_to(ROOT)}: 要 RGBA")
        if img.size != (72, 128):
            errors.append(f"{png.relative_to(ROOT)}: 要 72×128（3 帧 × 4 个朝向，一帧 24×32），现在是 {img.width}×{img.height}")


def sheet(images, out):
    """1 倍和 2 倍并排，草地和铺装两种底色，左边放 24 px 高的人物剪影作比例参照"""
    pad, rows = 8, []
    for img in images:
        w = img.width * 3 + pad * 4
        h = img.height * 2 + pad * 2
        rows.append((img, w, h))
    if not rows:
        return
    W = max(w for _, w, _ in rows) * 2 + 40
    H = sum(h for _, _, h in rows)
    page = Image.new("RGBA", (W, H), (42, 36, 51, 255))
    y = 0
    for img, w, h in rows:
        for k, bg in enumerate([(126, 160, 82, 255), (216, 210, 196, 255)]):
            x0 = 40 + k * w
            ImageDraw.Draw(page).rectangle([x0, y, x0 + w - 2, y + h - 2], fill=bg)
            ImageDraw.Draw(page).rectangle([x0 + 4, y + h - pad - 24, x0 + 9, y + h - pad], fill=(42, 36, 51, 255))
            page.alpha_composite(img, (x0 + pad * 2, y + h - pad - img.height))
            big = img.resize((img.width * 2, img.height * 2), Image.NEAREST)
            page.alpha_composite(big, (x0 + pad * 3 + img.width, y + h - pad - big.height))
        y += h
    page.save(out)


def main():
    targets = [Path(a).resolve() for a in sys.argv[1:]] or [ROOT / "props", ROOT / "facades"]
    pngs = sorted(p for t in targets for p in ([t] if t.is_file() else t.rglob("*.png")) if "chibi" not in p.parts)
    pal, errors, images = palette(), [], []
    for png in pngs:
        img = check_png(png, pal, errors)
        if img is not None and img.mode == "RGBA":
            images.append(img)
    check_chibi(errors)
    sheet(images, ROOT / "sheet.png")
    for e in errors:
        print(e)
    print(f"{len(pngs)} 张图，{len(errors)} 个问题；联系表 sheet.png")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
