# PackMachine101 — 食品托盒包装机市场分析与外贸培训项目

面向食品托盒包装（Tray Sealer）领域的知识与协作平台，围绕生鲜与预制菜市场的包装技术与整线方案，持续收集竞品参数与客户反馈，支持设计、销售与外贸同事开展培训与客户沟通，并为未来开源共建打下基础。

## 为什么存在
- 缩短国内食品机械与国际的技术与经验差距，形成可复用的知识库。
- 让销售与外贸能够快速理解客户语言与关注点，提升沟通效率。
- 为设计与工艺提供结构化数据与模板，支持方案配置与验证。
- 通过开源协作，推动国内食品包装行业整体进步。

## 项目内容
- 四大分类站点文档：
  - 市场（Market）：客户场景、品类入口、案例卡片与FAQ。
  - 产品（Product）：整线架构、TS350映射、竞品总览与讲义。
  - 词汇（Glossary）：包装术语、包装形式科普与技术速成。
  - 行动手册（Playbooks）：需求采集模板、测试与验收清单、问答脚本与速成讲义。
- 竞品库：TRAVE平台、MULTIVAC T700等机型的能力与参考链接。
- TS350映射：针对国内场景的规格、工艺、换型与差异化要点。
- 模板与清单：站内化页面用于发布，仓库根目录保留原始模板文件。

## 目录结构
- `docs/` 站点文档（按四大分类组织）
  - `market/` 客户场景与渠道诉求、品类入口、案例卡片、FAQ
  - `product/` 整线架构、TS350映射、竞品总览与讲义
  - `glossary/` 术语词汇、包装技术速成、包装形式科普
  - `playbooks/` 行动手册（需求采集、验收清单、问答脚本、速成讲义）
- `data/` 结构化数据（YAML/JSON），如竞品参数与参考链接
- `templates/` 原始模板（竞品档案、客户需求、验收清单）
- `playbooks/` 仓库根目录下的现场勘查与沟通清单
- `assets/` 图片与图示占位

## 快速开始
- 克隆仓库：
  ```bash
  git clone git@github.com:John-Qu/FPM101.git
  cd FPM101
  ```
- 浏览站点：
  - GitHub Pages：`https://John-Qu.github.io/FPM101/`
  - 市场：`docs/market/customer-scenarios.md`、`docs/market/faq.md`
  - 产品：`docs/product/system-architecture.md`、`docs/product/ts350-mapping.md`、`docs/product/competitors.md`
  - 词汇：`docs/glossary/packaging-basics.md`、`docs/glossary/packaging-forms.md`
  - 行动手册：`docs/playbooks/customer-requirements.md`、`docs/playbooks/validation-checklist.md`、`docs/playbooks/qa.md`、`docs/playbooks/packaging-quickstart.md`
- 使用模板与数据：
  - 复制 `templates/competitor.md` 作为新竞品档案的起点
  - 在 `data/competitors/*.yml` 录入结构化参数（含来源链接）
  - 站内化页面用于站点发布；原始模板位于 `templates/` 目录

## 数据约定
- 竞品数据以 YAML 存放于 `data/competitors/`，字段示例：
    - `brand`, `series`, `model`, `packaging`, `lanes`, `throughput_trays_per_min`
    - `residual_o2_target`, `leak_rate_target`, `tool_change_time_min`
    - `materials`, `controls`, `utilities`, `maintenance`, `references`
- 每条数据需附权威来源链接与采集时间；不明参数暂以 `tbd` 占位。

## 培训材料使用
- 讲义：`docs/product/competitors-lecture.md`
- 客户问答：`docs/market/faq.md` 与 `docs/playbooks/qa.md`
- 案例卡片：`docs/market/casecards.md`
- 现场演练与勘查：仓库根目录 `playbooks/customer_scoping.md` 与 `playbooks/site_survey.md`

## 参与方式
- 提交信息与改动：
    - 新建分支并提交 PR，补充 `docs/` 或 `data/` 内容；引用来源必填。
    - Issue 模式：提出新增词条、补充竞品参数、修正错误或新增案例。
- 贡献规范：
    - 使用模板与既有目录结构；保持术语一致与中英文对照。
    - 数据变更附来源链接与采集日期；客户敏感信息需脱敏。
    - 提交信息以“事实+来源”为准，避免未经验证的推测。

## 隐私与合规
- 不公开客户隐私与商业敏感信息；必要时统一脱敏与审核。
- 材料与参数遵循食品接触与安全合规要求；严禁误导性宣传。

## 路线图
- 近期：完善 TS350 参数与选件、补充更多竞品档案与案例。
- 中期：接入脚本生成对比表与图表、搭建静态文档站点与多语言视图。
- 远期：开源协作与行业共建，建立可验证测试协议与基准数据集。

## 参考资料
- G.Mondini TRAVE 平台概述：`https://www.gmondini.com/solution/trave`
- G.Mondini 平台与包装技术：`https://www.gmondini.com/`
- Harpak-ULMA 对 TRAVE 的介绍与创新：`https://www.harpak-ulma.com/g-mondini-trave-tray-sealer/`
- MULTIVAC 自动托盒封口机与 T700：`https://my.multivac.com/en/solutions/packaging-solutions/traysealers/automatic-high-output-traysealers/`
- MULTIVAC T700 美区页：`https://us.multivac.com/en/solutions/products/categories/product/traysealer/automatic-traysealers/t-700/`

## 许可
- 内容与代码许可待确定。建议：内容使用 `CC BY-SA 4.0`，代码使用 `Apache-2.0`。

---
如需将内容渲染为网站或生成自动化对比表，请提出需求，我将补充站点配置与数据生成脚本，并配置发布流程（如 GitHub Pages）。