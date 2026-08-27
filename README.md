<div align="center">

# ⚔️ 几何围猎

### Rogue Arena

**带上武器与器灵，在不断异变的地下城里杀出自己的流派。**

一款由我制作、可以自行部署的中文网页肉鸽动作射击游戏。

<p>
  <img alt="Python 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white">
  <img alt="HTML5 Canvas" src="https://img.shields.io/badge/HTML5-Canvas-E34F26?logo=html5&logoColor=white">
  <img alt="No npm build" src="https://img.shields.io/badge/npm_构建-不需要-CB3837?logo=npm&logoColor=white">
  <img alt="Self hosted" src="https://img.shields.io/badge/部署-自托管-2E8B57?logo=docker&logoColor=white">
  <a href="LICENSE.md"><img alt="PolyForm Noncommercial" src="https://img.shields.io/badge/许可-PolyForm_Noncommercial-6A5ACD"></a>
</p>

`双武器流派` · `器灵伙伴` · `多生态 Boss` · `华山论剑` · `排行榜` · `可选 AI 村民`

</div>

---

## 写在前面

我想做的，不是一款只靠数值越滚越大、最后满屏特效自动清场的肉鸽游戏。

在《几何围猎》里，**走位、瞄准、弹药、格挡和出手时机始终有意义**。构筑会改变你的战斗方式，但不会替你战斗；技能能救场，却不能掩盖失误；每个 Boss 都应该像一场考试，检验你是否真正理解了手里的武器。

所以我把枪盾、太刀、器灵、英雄伙伴、生态地形和首领机制都做成了真实参与战斗的系统。弹坑会挡住子弹，伙伴会受伤和休整，召唤物有自己的生命与碰撞，海妖甚至会伪装成等待营救的公主。

> **普攻与走位决定下限，构筑决定风格，技能锦上添花，首领负责检验掌握程度。**

项目采用单页 HTML5 Canvas 前端和纯 Python 标准库后端，没有 npm 构建步骤，也不依赖 Web 框架或外部数据库。下载、启动、创建账号，就可以拥有一套完全由自己管理的游戏服务。

## ✨ 游戏亮点

| | 你会在游戏里遇到什么 |
|---|---|
| ⚔️ **两套完整武装** | 枪盾流强调射速、弹匣与格挡；赤霞太刀强调连段、蓄力、架刀与弹反 |
| 🧚 **三种器灵** | 霜语、幽蕈、燧心并非装饰，它们有实体飞剑、属性、技能和自己的台词 |
| 🧩 **自由构筑** | 火力、穿透、射速、机动、生存、弹仓、冷却、器灵与伙伴可以持续叠加 |
| 👑 **多生态 Boss** | 星骸巨像、德古拉、海盗船长、末影龙、海神等首领会改变战场规则 |
| 🏔️ **双模式挑战** | 在无尽围猎里经营一场长远征，或在华山论剑中连续挑战高压 Boss |
| 🏰 **完整自托管** | 邀请制账号、排行榜、永久成长、管理后台和数值配置都保存在自己的服务上 |

### 一局远征是怎样的？

```text
选择武器与器灵
      ↓
进入战场，走位、格挡、管理弹药
      ↓
升级并组合自己的局内构筑
      ↓
迎战改变地形与规则的阶段首领
      ↓
休整、营救伙伴、探索事件、补充物资
      ↓
带着新的力量进入更危险的下一关
```

游戏会在浏览器本地记住上次选择的模式、难度、武器、器灵、斗篷颜色和护符样式。

## 🎮 战斗系统

### 两种模式

- **无尽围猎**：怪群、远程兵、精英、补给、环境事件和阶段首领循环推进。击败 Boss 后不会立刻切走，而是直接在原战场进入安全休整，营救伙伴、探索遗迹并为下一关做准备。
- **华山论剑**：纯 Boss 高难挑战。以 5 级开局，先选择一项加护，再迎战不断增强的首领组合。每轮胜利都能获得英雄或提升英雄阶位，正式首领还会授予跨局永久生效的赐福。

### 两套主武器流派

| 枪盾流 · 远征盾牌 | 太刀流 · 赤霞双武装 |
|---|---|
| 自动射击，通过射速和弹匣压力换取火力 | 太刀不会自动挥砍，每一次出刀都由玩家决定 |
| 点击敌人持续集火，可成长出穿透、多发、追踪、霰弹和激光 | 短按依次打出横斩、突刺、交叉重斩，长按追加蓄力裂空劈 |
| 自动完美格挡提供容错，也可以主动举盾进入“坚如磐石” | 支持架刀、弹反、拔刀反击和 Boss 决斗倍率 |
| `4` / `5` 调整射速 | `4` 主刀，`5` 切换副手手枪与护体罡气 |

两套武器不是简单换皮。太刀的近战弹匣和远程弹匣独立恢复，枪盾则围绕持续火力与防御节奏展开；它们还会与全部主动技能产生各自的联动。

### 器灵、能力与英雄

- **器灵**：霜语使用寒冰剑，幽蕈使用毒液剑，燧心使用火焰剑。三位器灵都有可见的实体飞剑和独立战斗属性。
- **主动能力**：翠幕屏障、巨像之力、引力涡流、追踪掩体弹、追猎激光环、混沌形态和星骸化身会随进程逐步解锁。
- **御剑体系**：御剑飞行、万剑归宗与飞剑循环既是进攻手段，也承担统一净化机制。
- **英雄伙伴**：天使、骑士、公主、女巫和国王拥有不同支援职责，会受伤、休整、复归，也会在战场上与你对话。

### 首领不只是“血更多”

我不希望 Boss 只是普通怪的放大版，因此首领会通过独立招式、召唤物和场地变化制造压力：

- **星骸巨像**会改变地形，留下同时阻挡敌我弹道的弹坑；
- **德古拉**使用高速位移、蝙蝠、血系弹幕和治疗链；
- **海盗船长**把战场变成黑潮海区，船毁后还会亲自加入战斗；
- **暮沼女巫、夜幕刺客、末影龙、无头骑士**分别强调区域控制、背袭突刺、黑洞烈焰与人马分离；
- **哭泣天使、大守护者、沙漠之神、海神**构成独立的神职首领体系；
- **阴毒医师**用毒层、恢复压制和实体猎蛛逼迫玩家选择净化时机；
- **深渊海妖**会伪装成待救公主，在本该安全的休整阶段发动伏击。

所有高伤害招式都必须有可读预警。Boss 技能召唤出的生物拥有真实生命、碰撞、移动和攻击，不会用一团纯特效冒充单位。

### 四档难度

| 难度 | 适合谁 | 战场变化 |
|---|---|---|
| 入门 | 第一次接触游戏 | 降低怪物压力，先熟悉移动、格挡和补给 |
| 简单 | 想体验完整流程 | 默认的标准地下城体验 |
| 困难 | 已经熟悉构筑 | 更高威胁、更多精英和更高得分倍率 |
| 噩梦 | 想挑战极限 | 极高密度，高级敌人更早出现，得分倍率最高 |

难度不会替玩家跳过正常成长过程，排行榜也会记录每一局所使用的难度。

## 🕹️ 操作方式

| 操作 | 键位 / 方式 |
|---|---|
| 移动 | `WASD` / 方向键；移动端使用左下方向键 |
| 瞄准与锁敌 | 鼠标移动、点击敌人；移动端点击目标 |
| 枪盾射速 | `4` 降低、`5` 提高 |
| 太刀双武装 | `4` 主刀、`5` 副枪 |
| 副武器 / 主刀攻击 | `空格`；太刀长按可蓄力裂空 |
| 主动能力 | `1`、`2`、`3`、`Q`、`E`、`F`、`R`，按等级或模式解锁 |
| 事件互动 | 靠近后按 `G` 或点击 |
| 随身商店 | `B` |
| 暂停 | `Esc` / `P` |

## 🚀 快速开始

### 使用 Docker Compose（推荐）

需要 Docker Engine 和 Docker Compose v2。

```bash
git clone https://github.com/188zjl/rogue-arena.git
cd rogue-arena
cp .env.example .env
```

打开 `.env`，把 `SESSION_SECRET` 改成至少 48 个字符的随机值。村民 AI 的三项配置可以全部留空，不影响游戏主体。

```bash
mkdir -p data
docker compose up -d --build
docker compose exec rogue-arena python manage_users.py add admin --role admin
```

启动后访问：<http://127.0.0.1:18088>

Windows PowerShell 可以使用下面的命令复制环境文件：

```powershell
Copy-Item .env.example .env
```

Linux 宿主机如果遇到数据目录写入权限错误：

```bash
sudo chown -R 10001:10001 data
```

### 直接使用 Python

项目要求 Python 3.11 或更高版本，没有第三方 Python 依赖。

<details>
<summary><strong>Windows PowerShell</strong></summary>

```powershell
$env:SESSION_SECRET = python -c "import secrets; print(secrets.token_urlsafe(48))"
$env:DATA_DIR = Join-Path $PWD 'data'
python manage_users.py add admin --role admin
python app.py
```

</details>

<details>
<summary><strong>Linux / macOS</strong></summary>

```bash
export SESSION_SECRET="$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DATA_DIR="$PWD/data"
python3 manage_users.py add admin --role admin
python3 app.py
```

</details>

管理员密码通过交互输入，不会进入命令历史。第一次运行时，服务会自动创建空白数据文件。

## 🏰 自托管能力

这不只是一个本地 HTML 小游戏。后端还提供了一套轻量、完整的自托管系统：

- 邀请制账号登录与限次邀请码注册；
- 今日、全量和华山论剑排行榜；
- Boss 赐福、教程状态、个人记录与永久成长；
- 管理员创建、停用、启用和重置玩家账号；
- 管理员生成随机凭证、创建邀请码并控制可注册次数；
- 在线调整怪物、Boss、玩家、补给和成长参数；
- 可选的“村民”AI 知识助手，只回答本游戏机制问题；
- 桌面 60 FPS、移动端约 35 FPS 的自适应渲染预算和弹幕聚合降噪。

管理员登录后可以从游戏首页进入 `/admin`。命令行也可以直接管理账号：

```bash
python manage_users.py add admin --role admin
python manage_users.py add PLAYER_NAME
python manage_users.py reset PLAYER_NAME
python manage_users.py status PLAYER_NAME disable
python manage_users.py status PLAYER_NAME enable
python manage_users.py list
```

## 🤖 可选村民 AI

村民问答默认关闭。只有同时配置下面三项时才会启用：

```dotenv
VILLAGER_API_BASE=https://example.com/v1
VILLAGER_API_KEY=your_api_key_here
VILLAGER_MODEL=your_model_name
```

接口使用 OpenAI Chat Completions 兼容格式。服务端会向你配置的模型提供方发送玩家当前问题、最多 6 条近期村民对话，以及 [GAME_KNOWLEDGE.md](GAME_KNOWLEDGE.md) 与 [DESIGN.md](DESIGN.md) 中的游戏知识。

API Key 只从服务端环境变量读取，不会发送到浏览器，也不会通过 `/api/me` 或村民响应返回。如果不需要 AI，保持三项为空即可；账号、战斗、排行榜和管理面板不会受到影响。

> 接入前，请确认你信任相应模型服务，并按照服务提供方的隐私政策处理玩家问题。

## 🔧 配置与技术资料

为了让首页保持好读，完整配置放在下面的折叠区里。

<details>
<summary><strong>环境变量</strong></summary>

| 变量 | 默认值 | 用途 |
|---|---:|---|
| `SESSION_SECRET` | 启动时随机生成 | 会话签名密钥；生产环境必须固定设置，建议至少 48 个随机字符 |
| `HOST` | `127.0.0.1` | 直接运行 Python 时的监听地址 |
| `PORT` | `18088` | 直接运行 Python 时的监听端口 |
| `DATA_DIR` | `./data` | JSON 持久化目录 |
| `COOKIE_SECURE` | `0` | HTTPS 反代后设为 `1`，为会话 Cookie 增加 `Secure` |
| `TRUST_PROXY` | `0` | 仅在可信反向代理后设为 `1`，用于读取真实客户端 IP |
| `BIND_ADDRESS` | `127.0.0.1` | Compose 发布到宿主机的地址 |
| `HOST_PORT` | `18088` | Compose 发布到宿主机的端口 |
| `VILLAGER_API_BASE` | 空 | 可选 OpenAI Chat Completions 兼容接口 |
| `VILLAGER_API_KEY` | 空 | 可选村民模型服务密钥，只在服务端读取 |
| `VILLAGER_MODEL` | 空 | 可选模型名称 |
| `VILLAGER_TIMEOUT` | `28` | 村民请求超时，限制在 5–60 秒 |

`.env` 只会被 Docker Compose 自动读取。直接运行 Python 时，需要在当前终端显式设置环境变量。

</details>

<details>
<summary><strong>数据与隐私</strong></summary>

运行数据默认保存在 `data/`：

```text
data/
├── users.json          # 账号、PBKDF2 密码哈希、角色与永久成长
├── invite_codes.json   # 邀请码与使用次数
├── scores.json         # 排行榜成绩
└── game_config.json    # 管理员调整后的游戏数值
```

公开仓库不包含真实账号、密码哈希、邀请码、排行榜、生产参数、服务器地址、部署日志、Cookie 或 API Key。Git 会忽略 `.env`、`data/*.json`、临时数据、备份、本机部署文件和未确认再分发许可的素材。

公开 Git 历史由经过审计的净化版本重新建立，避免个人化服务地址、模型名或旧运行数据残留在可访问提交中。

</details>

<details>
<summary><strong>安全与生产部署</strong></summary>

- 密码使用 `PBKDF2-HMAC-SHA256`、独立随机盐和 310,000 次迭代，不保存明文密码。
- 会话使用 HMAC 签名；Cookie 启用 `HttpOnly` 与 `SameSite=Strict`，HTTPS 环境可以额外启用 `Secure`。
- 管理接口会在服务端检查管理员角色；登录失败和村民问答按客户端地址限速。
- Docker 镜像使用非 root 用户，并启用只读根文件系统、`no-new-privileges`、能力集清空和资源限制。
- 公网部署必须使用 HTTPS 反向代理，并设置 `COOKIE_SECURE=1`。
- 只有应用确实位于可信反向代理之后时才设置 `TRUST_PROXY=1`。
- 应用端口默认只绑定 `127.0.0.1`；跨主机反代时，应使用防火墙仅允许反向代理来源。
- 定期备份 `DATA_DIR`，限制 `.env` 和数据目录的文件权限，并实际测试恢复流程。

安全问题请按照 [SECURITY.md](SECURITY.md) 私密报告，不要在公开 Issue 中粘贴凭证或运行数据。

</details>

<details>
<summary><strong>主要 HTTP 接口</strong></summary>

| 方法与路径 | 用途 |
|---|---|
| `GET /health` | 匿名健康检查 |
| `GET /` | 游戏入口，未登录时跳转 `/login` |
| `GET /api/me` | 当前会话与永久成长 |
| `GET /api/leaderboard` | 今日、全量与华山论剑排行榜 |
| `GET /api/game-config` | 登录后的活动游戏参数 |
| `POST /api/register` | 使用有效邀请码注册 |
| `POST /api/score` | 提交本局成绩 |
| `POST /api/boss-blessing` | 保存正式首领赐福等级 |
| `POST /api/villager` | 可选村民知识问答 |
| `GET /admin` | 管理员页面 |
| `/api/admin/*` | 账号、邀请码与游戏参数管理 |

</details>

<details>
<summary><strong>项目结构</strong></summary>

```text
.
├── app.py                 # HTTP 服务、鉴权、数据、排行榜与可选村民代理
├── windows2.html          # Canvas 游戏本体、UI、输入与战斗逻辑
├── login.html             # 登录与邀请码注册
├── admin.html             # 管理员控制台
├── manage_users.py        # 交互式账号管理命令
├── DESIGN.md              # 长期设计哲学、平衡原则与内容边界
├── GAME_KNOWLEDGE.md      # 玩家机制知识与村民 AI 知识库
├── assets/music/          # CC0 音乐与可选自备音乐目录
├── Dockerfile
└── docker-compose.yml
```

</details>

## 🧪 开发与验证

提交前至少运行：

```bash
python -m py_compile app.py manage_users.py
docker compose config
```

启动后建议确认：

1. `/health` 返回 `{"status":"ok"}`；
2. 未登录访问 `/` 会跳转到 `/login`；
3. 管理员可以创建玩家或邀请码；
4. 新玩家可以进入战场并提交一局成绩；
5. 未配置村民模型时，游戏主体正常运行，`/api/villager` 明确返回未配置状态。

如果你想了解我为玩法设定的长期原则，可以阅读 [DESIGN.md](DESIGN.md)；如果你想查某个已经实现的机制，可以阅读 [GAME_KNOWLEDGE.md](GAME_KNOWLEDGE.md)。

## 🎵 音乐与素材

仓库内的 4 首 `cc0_*.mp3` 来自 OpenGameArt.org，以 CC0 1.0 方式分发。曲名、作者和来源记录在 [assets/music/CC0_SOURCES.md](assets/music/CC0_SOURCES.md)。

开发过程中使用过但不具备公开再分发许可的音乐不会进入仓库。你也可以按照 [assets/music/README.md](assets/music/README.md) 放入自己有权使用的场景音乐。代码许可证不会自动覆盖第三方素材，新增素材时请保留原作者、来源和许可证。

## 🤝 一起完善它

这是我持续打磨的一款游戏。如果你遇到玩法问题、数值异常或浏览器兼容问题，欢迎提交 Issue；如果你愿意修复 Bug、改善手感或贡献原创内容，也欢迎发起 Pull Request。

提交反馈时，请尽量包含复现方式和浏览器信息，但不要公开粘贴真实密码、邀请码、会话 Cookie、`.env`、API Key 或运行数据。涉及安全问题时，请改用 [SECURITY.md](SECURITY.md) 中的私密报告方式。

## 📜 许可证与使用边界

本仓库公开源代码，但使用 [PolyForm Noncommercial License 1.0.0](LICENSE.md)。它属于 **source-available / 源码可用**，不是 OSI 定义的开源许可证。

- 可以用于个人学习、研究、实验、非商业修改和非商业分享；
- 不允许收费游玩、广告或赞助变现、转售、商业托管、商业发行、商业产品集成，以及其他以商业获利为目的的使用；
- 再分发源码或修改版本时，必须保留 `LICENSE.md` 和 [NOTICE.md](NOTICE.md)；
- 如果用途可能涉及商业利益，请先停止使用，除非另行取得授权。

---

<div align="center">

**如果你也喜欢需要亲手走位、格挡和做出选择的肉鸽游戏，欢迎来地下城走一趟。**

Made with ⚔️ by [188zjl](https://github.com/188zjl)

</div>
