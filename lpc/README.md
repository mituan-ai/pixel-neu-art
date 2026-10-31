# LPC 角色素材

来自 [Universal LPC Spritesheet Character Generator](https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator)，提交 `86160e7507d6841259cff624a51a63c1d4847ee3`（2026-10-28），只取用到的部件的 `walk.png`，目录结构与原仓库 `spritesheets/` 相同。

每个文件的作者、许可证和上游链接见同目录 `CREDITS.csv`（从原仓库 CREDITS.csv 摘出，未删改）。一个文件列了多个许可证时，本项目按其中的 OGA-BY 3.0、CC-BY 4.0、CC-BY 3.0、CC0 或 CC-BY-SA 3.0 使用，不用 GPL。

游戏的美术生成器对这些图做的改动（改动结果在游戏的运行时资源里，本目录存原图）：
- 衣服、头发、皮肤转成灰阶，运行时按玩家选的颜色染色；
- 眼睛从头部图层分出来，虹膜换成 LPC 自带的棕色眼睛色板；
- 按「下、左、右、上」重排方向；
- 原仓库里有 14 张是调色板 PNG，复制时转成了 RGBA，像素不变。

改作仍按原许可证发布（CC-BY-SA 3.0 的部件及其改作按 CC-BY-SA 3.0），不在本项目保留权利的范围内。
