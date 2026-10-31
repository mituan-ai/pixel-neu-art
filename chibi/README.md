# chibi/：Q 版角色部件

游戏里的人物由这里的底模和发型合成：一帧 24×32，脚底在第 30 行，按 1 倍显示（全身约 26 px）。衣服、鞋和短发类发型由主项目的生成器按底模轮廓画，不在这里。

| 文件 | 内容 | 作者 | 许可证 | 来源 |
|---|---|---|---|---|
| `base-male.png` | 男体型底模（原名 `SWEN_adult_m_thin`） | Svetlana Kushnariova (Cabbit)，Jordan Irwin (AntumDeluge) 改作 | CC0 1.0 | https://opengameart.org/content/human-bases-cabbit-rework （`human_20220627.zip`），原作 https://opengameart.org/content/cabbit-bases-collection |
| `base-female.png` | 女体型底模（原名 `SWEN_adult_f_thin_torsoA_armsA`） | 同上 | CC0 1.0 | 同上 |
| `hair/*.png` | 七种发型：中长发、马尾、侧马尾、麻花辫、侧编辫、卷发、爆炸头 | diamonddmgirl | CC0 1.0 | https://opengameart.org/content/hair-for-24x32-bases （`24x32 hair.zip` 里的 `* walk.png`） |

CC0 不要求署名，这里照样写明，方便追溯。

## 规格

- 底模：3 列（迈步、站立、迈步）× 4 行（下、左、右、上），72×128。
- 发型：同样 3 列，但行序是原包的 上、右、下、左，生成器里换算，文件保持原样，方便和原包对照。
- 按原色交；染色由游戏完成（生成器把肤色、发色转成灰阶）。
- 新发型要和 `base-male.png` 的头对齐：同一帧、同一位置。
