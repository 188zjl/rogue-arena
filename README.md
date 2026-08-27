# 几何围猎 / Rogue Arena

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776ab.svg)](https://www.python.org/)
[![Canvas](https://img.shields.io/badge/Frontend-HTML5_Canvas-e34f26.svg)](https://developer.mozilla.org/docs/Web/API/Canvas_API)
[![Source available](https://img.shields.io/badge/source-available-4f8f70.svg)](#许可证与使用边界)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/license-PolyForm_Noncommercial-6a5acd.svg)](LICENSE.md)

一款可以自行部署的中文网页肉鸽动作射击游戏。玩家带着器灵和伙伴深入持续异变的地下城，在怪群、首领、生态地形与遗迹事件之间走位、格挡、管理弹药、构筑流派，并不断刷新远征记录。

> **核心原则：普攻与走位决定下限，构筑决定风格，技能锦上添花，首领负责检验玩家是否真正掌握了战斗。**

项目采用单页 Canvas 前端和纯 Python 标准库后端，没有 npm 构建步骤，也不依赖 Web 框架或外部数据库。账号、邀请码、排行榜、永久成长和管理员数值配置均由自托管服务保存。

## 游戏内容

### 两种挑战模式

- **无尽围猎**：普通怪、远程兵、精英、补给、环境事件与阶段首领循环推进。Boss 胜利后会在原战场进入安全休整，可营救伙伴、探索事件、购买补给并准备下一关。
- **华山论剑**：纯 Boss 高难挑战。玩家以 5 级开局，先选择一项加护，再迎战随轮次增长的首领组合。每轮过关都会获得英雄或提升英雄阶位；正式首领会授予可跨局、可重复升级的永久赐福。

### 四档难度

| 难度 | 定位 |
|---|---|
| 入门 | 降低怪物压力，适合第一次熟悉移动、格挡和补给 |
| 简单 | 标准地下城体验，也是默认难度 |
| 困难 | 更高威胁等级、更多精英和更高得分倍率 |
| 噩梦 | 极高密度、提前出现高级敌人，并提供最高得分倍率 |

难度主要影响出怪频率、场上容量、怪物威胁等级、精英概率与得分倍率，不会替玩家跳过正常成长过程。排行榜会记录每局难度。

### 两套主武器流派

- **远征盾牌 / 枪盾流**
  - 自动射击，`4` 降低射速、`5` 提高射速，以弹匣压力换取火力。
  - 点击敌人持续集火；普通攻击会随等级获得穿透、多发、短程追踪、霰弹与激光等成长。
  - 自动完美格挡提供容错；短按空格主动格挡，长按进入“坚如磐石”。
- **赤霞双武装 / 太刀流**
  - `4` 切换太刀主武器，`5` 切换副手手枪与护体罡气。
  - 太刀不自动挥砍：短按空格依次打出横斩、突刺和交叉重斩，长按追加蓄力裂空劈。
  - 近战弹匣与远程弹匣独立恢复，鼓励在贴身决斗与远程补伤之间主动切换。
  - 支持架刀、弹反、拔刀反击、Boss 决斗倍率，以及与全部主动技能的专属联动。

### 器灵、构筑与伙伴

- **三种器灵**：霜语（寒冰剑）、幽蕈（毒液剑）、燧心（火焰剑）都有可见的实体飞剑、战斗属性与角色台词。
- **主动能力**：翠幕屏障、巨像之力、引力涡流、追踪掩体弹、追猎激光环、混沌形态和星骸化身会逐步解锁。
- **御剑体系**：御剑飞行、万剑归宗和飞剑循环既是进攻技能，也是统一净化机制的一部分。
- **局内升级**：火力、穿透、射速、机动、生存、弹仓、冷却、器灵和伙伴构成可叠加的远征构筑。
- **英雄伙伴**：天使、骑士、公主、女巫与国王拥有不同支援职责，会真实受伤、休整、复归并参与场上对话。

### 首领与生态战场

游戏不是简单放大普通怪数值，而是让首领通过独立攻击方式、召唤物和场地变化形成压力：

- 星骸巨像改变地形并留下阻挡双方的弹坑；
- 德古拉使用高速位移、蝙蝠、血系弹幕和治疗链；
- 海盗船长把战场变成黑潮海区，船毁后亲自加入战斗；
- 暮沼女巫、夜幕刺客、末影龙、无头骑士分别强调区域控制、突刺背袭、黑洞烈焰与人马分离；
- 哭泣天使、大守护者、沙漠之神和海神属于独立神职首领体系；
- 阴毒医师通过毒层、恢复压制和实体猎蛛挑战净化时机；
- 深渊海妖会伪装成待救公主，在休整阶段触发特殊伏击。

高伤害招式必须有可读预警；神职、海洋、沙漠和普通 Boss 阵营遵守生态互斥与协同规则。Boss 技能召唤出的生物都是具有生命、碰撞、移动和攻击的真实实体，不使用纯特效冒充单位。

### 自托管系统

- 邀请制账号登录与限次邀请码注册；
- 今日、全量、华山论剑分榜；
- 管理员创建、停用、启用和重置玩家账号；
- 管理员生成随机凭证、创建邀请码并控制可注册次数；
- 管理员在线调整怪物、Boss、玩家、补给与成长参数；
- Boss 赐福、教程状态、排行榜和个人记录持久化；
- 可选“村民”AI 知识助手，只回答本游戏机制问题；
- 桌面 60 FPS、移动端约 35 FPS 的自适应渲染预算与弹幕聚合降噪。

## 操作说明

| 操作 | 键位 / 方式 |
|---|---|
| 移动 | `WASD` / 方向键；移动端使用左下方向键 |
| 瞄准与锁敌 | 鼠标移动、点击敌人；移动端点击目标 |
| 枪盾射速 | `4` 降低、`5` 提高 |
| 太刀双武装 | `4` 主刀、`5` 副枪 |
| 副武器 / 主刀攻击 | `空格`；太刀长按可蓄力裂空 |
| 主动能力 | `1`、`2`、`3`、`Q`、`E`、`F`、`R`（按等级或模式解锁） |
| 事件互动 | 靠近后按 `G` 或点击 |
| 随身商店 | `B` |
| 暂停 | `Esc` / `P` |

游戏会在浏览器本地记住上次选择的模式、难度、武器、器灵、斗篷颜色和护符样式。

## 快速开始

### Docker Compose（推荐）

要求：Docker Engine 与 Docker Compose v2。

```bash
git clone https://github.com/188zjl/rogue-arena.git
cd rogue-arena
cp .env.example .env
```

将 `.env` 中的 `SESSION_SECRET` 替换为至少 48 个字符的随机值。村民 AI 的三项配置可以留空，不影响游戏主体。

```bash
mkdir -p data
docker compose up -d --build
docker compose exec rogue-arena python manage_users.py add admin --role admin
```

Linux 宿主机若遇到数据目录写入权限错误：

```bash
sudo chown -R 10001:10001 data
```

Windows PowerShell 复制环境文件可使用：

```powershell
Copy-Item .env.example .env
```

启动后打开：<http://127.0.0.1:18088>

### 直接运行 Python

要求 Python 3.11 或更高版本；项目没有第三方 Python 依赖。

PowerShell：

```powershell
$env:SESSION_SECRET = python -c "import secrets; print(secrets.token_urlsafe(48))"
$env:DATA_DIR = Join-Path $PWD 'data'
python manage_users.py add admin --role admin
python app.py
```

Linux / macOS：

```bash
export SESSION_SECRET="$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DATA_DIR="$PWD/data"
python3 manage_users.py add admin --role admin
python3 app.py
```

管理员密码通过交互输入，不会出现在命令历史中。首次运行会自动创建空白数据文件。

## 环境变量

| 变量 | 默认值 | 用途 |
|---|---:|---|
| `SESSION_SECRET` | 启动时随机生成 | 会话签名密钥；生产环境必须固定设置，建议至少 48 个随机字符 |
| `HOST` | `127.0.0.1` | 直接运行 Python 时的监听地址 |
| `PORT` | `18088` | 直接运行 Python 时的监听端口 |
| `DATA_DIR` | `./data` | JSON 持久化目录 |
| `COOKIE_SECURE` | `0` | HTTPS 反代后设为 `1`，给会话 Cookie 增加 `Secure` |
| `TRUST_PROXY` | `0` | 仅在可信反向代理后设为 `1`，用于读取真实客户端 IP |
| `BIND_ADDRESS` | `127.0.0.1` | Compose 发布到宿主机的地址 |
| `HOST_PORT` | `18088` | Compose 发布到宿主机的端口 |
| `VILLAGER_API_BASE` | 空 | 可选 OpenAI Chat Completions 兼容接口，例如 `https://example.com/v1` |
| `VILLAGER_API_KEY` | 空 | 可选村民模型服务密钥，只在服务端环境变量中读取 |
| `VILLAGER_MODEL` | 空 | 可选模型名称 |
| `VILLAGER_TIMEOUT` | `28` | 村民模型请求超时，限制在 5–60 秒 |

`.env` 只会被 Docker Compose 自动读取；直接运行 Python 时请在当前终端显式设置环境变量。

## 可选村民 AI 助手

村民功能默认关闭。只有同时设置 `VILLAGER_API_BASE`、`VILLAGER_API_KEY` 和 `VILLAGER_MODEL` 才会启用。接口使用 OpenAI Chat Completions 兼容格式，服务端会把以下内容发送给你配置的模型提供方：

- 玩家当前问题；
- 最多 6 条近期村民对话；
- [GAME_KNOWLEDGE.md](GAME_KNOWLEDGE.md) 和 [DESIGN.md](DESIGN.md) 中的游戏知识。

API Key 不会发送到浏览器，也不会通过 `/api/me` 或村民响应返回。请只接入你信任的模型服务，并按提供方隐私政策处理玩家问题。若不需要 AI 助手，保持三项配置为空即可，账号、战斗、排行榜和管理面板不受影响。

## 账号与管理命令

```bash
python manage_users.py add admin --role admin
python manage_users.py add PLAYER_NAME
python manage_users.py reset PLAYER_NAME
python manage_users.py status PLAYER_NAME disable
python manage_users.py status PLAYER_NAME enable
python manage_users.py list
```

管理员登录后可以从游戏首页进入 `/admin` 管理账号、邀请码和游戏参数。

## 数据与隐私

运行数据默认位于 `data/`：

```text
data/
├── users.json          # 账号、PBKDF2 密码哈希、角色与永久成长
├── invite_codes.json   # 邀请码及使用次数
├── scores.json         # 排行榜成绩
└── game_config.json    # 管理员调整后的游戏数值
```

公开仓库不包含真实账号、密码哈希、邀请码、排行榜、生产参数、服务器地址、部署日志、Cookie 或 API Key。以下内容均被 Git 忽略：

- `.env` 与其他本地环境配置；
- `data/*.json`、临时数据和备份；
- 本机部署脚本、日志、截图与代理工作文件；
- 未确认公开再分发许可的音乐、图片和其他素材。

公开版的 Git 历史从经过审计的净化版本重新建立，避免个人化服务地址、模型名或旧运行数据残留在可访问提交中。

## 安全设计与生产部署

- 密码使用 `PBKDF2-HMAC-SHA256`、独立随机盐和 310,000 次迭代存储，不保存明文密码。
- 会话由 HMAC 签名；Cookie 使用 `HttpOnly` 与 `SameSite=Strict`，HTTPS 环境可启用 `Secure`。
- 管理接口在服务端检查管理员角色；登录失败和村民问答按客户端地址限速。
- Docker 镜像以非 root 用户运行，启用只读根文件系统、`no-new-privileges`、能力集清空和资源限制。
- 公网部署必须使用 HTTPS 反向代理并设置 `COOKIE_SECURE=1`。
- 只有应用确实位于可信反向代理之后时才设置 `TRUST_PROXY=1`。
- 应用端口默认仅绑定 `127.0.0.1`；跨主机反代时应使用防火墙只允许反向代理来源。
- 定期备份 `DATA_DIR`，限制 `.env` 与数据目录的文件权限，并实际测试恢复流程。

安全问题请按 [SECURITY.md](SECURITY.md) 私密报告，不要在公开 Issue 中粘贴凭证或运行数据。

## 主要接口

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

## 项目结构

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

## 音乐与素材

仓库内 4 首 `cc0_*.mp3` 来自 OpenGameArt.org，按 CC0 1.0 分发；曲名、作者与来源说明见 [assets/music/CC0_SOURCES.md](assets/music/CC0_SOURCES.md)。

原开发环境使用过但不具备公开再分发授权的音乐不会进入仓库。你可以按 [assets/music/README.md](assets/music/README.md) 放入自己有权使用和分发的场景音乐。代码许可不自动覆盖第三方素材；新增素材时请保留其原始作者、来源和许可证。

## 开发与验证

提交前至少运行：

```bash
python -m py_compile app.py manage_users.py
docker compose config
```

启动后建议检查：

1. `/health` 返回 `{"status":"ok"}`；
2. 未登录访问 `/` 会跳转 `/login`；
3. 管理员可以创建玩家或邀请码；
4. 新玩家登录后能进入战场并提交一局成绩；
5. 未配置村民模型时，游戏主体正常运行，`/api/villager` 明确返回未配置状态。

长期玩法方向、平衡原则和新增机制准入问题见 [DESIGN.md](DESIGN.md)。已实现机制的玩家可见知识见 [GAME_KNOWLEDGE.md](GAME_KNOWLEDGE.md)。

## 许可证与使用边界

本仓库公开源代码，但采用 [PolyForm Noncommercial License 1.0.0](LICENSE.md)，属于 **source-available / 源码可用**，不是 OSI 定义的开源许可证。

- 允许个人学习、研究、实验、非商业修改与非商业分享；
- 禁止收费游玩、广告或赞助变现、转售、商业托管、商业发行、商业产品集成，以及其他预期商业获利的用途；
- 再分发源码或修改版本时必须保留 `LICENSE.md` 与 [NOTICE.md](NOTICE.md)；
- 如用途可能涉及商业利益，请勿使用本仓库代码，除非另行取得授权。

欢迎通过 Issue 报告玩法问题或提出非敏感建议，通过 Pull Request 提交修复与原创内容。请勿在 Issue、日志或截图中发布真实密码、邀请码、会话 Cookie、`.env`、API Key 或运行数据。
