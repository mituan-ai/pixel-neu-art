# 像素东大 · Pixel NEU 美术素材

[像素东大 · Pixel NEU](https://github.com/mituan-ai) 是东北大学南湖校区的像素风多人校园漫游，由谜团 mituan 开发，**非官方作品**，与东北大学无隶属或授权关系。

这个仓库存放游戏用的美术源文件，欢迎投稿：路灯、长椅、车棚、雕塑、楼的立面、新发型、新衣服……游戏本体的代码不在这里。

## 目录

| 目录 | 内容 | 许可 |
|---|---|---|
| `props/` | 物件：雕塑、路灯、校车、树等，每个视角一张 PNG + 同名 JSON | CC-BY 4.0 |
| `facades/` | 楼的正立面图 | CC-BY 4.0 |
| `chibi/` | Q 版人物底模和发型，来自 OpenGameArt 的 Cabbit 24×32 系列 | CC0 1.0，来源见 `chibi/README.md` |
| `palette.gpl` | 全项目调色板（GIMP、Aseprite 都能导入） | CC-BY 4.0 |
| `tools/check.py` | 校验脚本，同时生成联系表 | CC-BY 4.0 |

## 比例和画法一览

- 1 m = 8 px，地面一格 16 px = 2 m，楼一层 30 px。
- 3/4 俯视：地面、屋顶正投影，立面按真实高度竖直画，没有透视。
- 光从屏幕左上来，投影朝右下。
- 只用 `palette.gpl` 的颜色。

完整规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

除 `chibi/` 外，本仓库的素材由谜团 mituan 及各位贡献者创作，按 [CC-BY 4.0](LICENSE) 发布。署名写「像素东大 · Pixel NEU 及贡献者」，并附本仓库链接。

`chibi/` 里的第三方文件是 CC0，作者和出处见 `chibi/README.md`；之后投稿到 `chibi/` 的原创部件同样按 CC-BY 4.0 发布。
