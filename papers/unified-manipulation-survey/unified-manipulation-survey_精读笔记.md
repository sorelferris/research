# Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey

> **arXiv**: [2510.10903](https://arxiv.org/abs/2510.10903) · **作者**: Shuanghao Bai, Wenxuan Song, Jiayi Chen, Yuheng Ji, Zhide Zhong, Jin Yang, Han Zhao, Wanqi Zhou, Wei Zhao, Zhe Li, Pengxiang Ding, Cheng Chi, Haoang Li, Chang Xu, Xiaolong Zheng, Donglin Wang, Shanghang Zhang, Badong Chen (共 19 位) · **机构**: Westlake University（主导）+ BAAI + Zhejiang University + HKUST (Guangzhou) + University of Sydney + Chinese Academy of Sciences + Peking University + Xi'an Jiaotong University · **发布**: 2025-10-13 (v1), 2026-08-15 (v2 online)

## 核心信息

- 标题：Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
- 标题翻译：迈向机器人操作的统一理解：一项全面综述
- 作者：Shuanghao Bai, Wenxuan Song, Jiayi Chen, Yuheng Ji, Zhide Zhong, Jin Yang, Han Zhao, Wanqi Zhou, Wei Zhao, Zhe Li, Pengxiang Ding, Cheng Chi, Haoang Li, Chang Xu, Xiaolong Zheng, Donglin Wang, Shanghang Zhang, Badong Chen
- 机构：Westlake University（主导, 4 次出现）+ BAAI / Beijing Academy of AI（2 次）+ Zhejiang University + HKUST (Guangzhou) + University of Sydney + Chinese Academy of Sciences + Peking University + Xi'an Jiaotong University
- 发表时间：2025-10-13 (v1), 2026-08-15 (v2 online)
- 发表渠道：arXiv
- DOI：10.48550/arxiv.2510.10903
- arXiv：2510.10903
- 论文链接：https://arxiv.org/abs/2510.10903
- 代码 / 项目：https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation
- 数据 / 资源：1300+ 引用；27 张分类图 + 9 张总结表；总长 212 页
- 论文类型：survey_or_review（系统综述，跨 8 机构合作）

## 原文摘要翻译

具身智能近年取得显著进展，源于计算机视觉、自然语言处理与大规模多模态模型的崛起。在其核心挑战中，机器人操作作为基础且复杂的问题突出，需要无缝集成感知、规划与控制以在多样化、非结构化环境中实现交互。本综述给出机器人操作的全面综述，涵盖基础背景、按任务组织的基准与数据集，以及既有方法的统一 taxonomy。我们扩展传统「高层规划 vs 低层控制」的二分法：将高层规划拓展为涵盖语言、代码、运动、可供性与 3D 表示的多种表征，同时为低层学习型控制引入按训练范式（输入建模、潜学习、策略学习）划分的新 taxonomy。此外，本文首次给出关键瓶颈的专门分类，聚焦数据采集、利用与泛化，并以真实应用的扩展综述作为收尾。相对于已有综述，本文工作覆盖更广且洞察更深，可同时作为新人的入门路线图与资深研究者的结构化参考。

## 创新点

1. **完整流水线覆盖**——既有综述多聚焦单一任务域（灵巧、柔性物体、人形等）或单一范式（视觉语言动作模型、扩散策略、强化学习），本综述在 212 页内系统覆盖硬件、仿真、数据集、任务、规划、动作建模、瓶颈、应用八大模块。
2. **统一分类法二级细分**——把传统「高层对低层」二分扩展为：高层规划按表征语言细分为七大类（大语言模型 / 多模态大模型 / 程序化 / 几何约束 / 可供性 / 三维表示 / 视频驱动）；低层动作建模按训练范式细分为四大类（学习策略 / 输入建模 / 潜空间学习 / 策略学习），各含三个子类。
3. **数据与泛化瓶颈独立成章**——第七章首次把数据采集、数据利用、泛化三大瓶颈拆为独立章节，给出遥操作 + 仿真 + 人类视频 + 视频生成四类采集范式与样本效率 + 数据增强 + 跨形态迁移三种利用策略的配对视角。
4. **十类任务全覆盖**——第四章涵盖抓取、基础操作、灵巧操作、柔性机器人操作、可形变物体操作、移动操作、四足操作、人形操作、空中操作、水下操作全部十类，按形态复杂度递增组织。
5. **二十七张分类图与九张总结表**——量化对比方法、数据集、基准维度，是新人快速建立领域认知的视觉索引。

## 一句话总结

本综述通过「高层规划按表征细分 + 低层动作建模按训练范式细分 + 数据与泛化瓶颈独立成章」的统一分类法，把机器人操作领域一千三百余篇文献组织为新人可入门的八大模块流水线，确立跨形态综述的四大未来方向（机器人通用脑、数据瓶颈、感知、安全人机共存）。

## 研究问题

本综述围绕 4 个研究问题组织全文（对应 Sec 1.1 + 1.2）：

1. **研究问题一：当下机器人操作由哪些基准与任务类别定义？**——第三章系统整理抓取、单形态仿真、跨形态仿真、轨迹数据、具身问答、人类视频六大类数据集与基准；第四章定义十类操作任务并按形态复杂度排列。
2. **研究问题二：针对这些任务提出了哪些方法？**——第五章给高层规划七种表征分类法；第六章给低层动作建模四大类乘三子类分类法；本综述把视觉语言动作模型定位为输入建模与策略学习的交叉产物，而非独立范式。
3. **研究问题三：当前瓶颈是什么？**——第七章把数据采集、利用、泛化拆为独立三大瓶颈，明确指出机器人学习尚未出现类似大语言模型的可靠标度律。
4. **研究问题四：实操应用有哪些？**——第八章系统梳理医疗、制造、农业、服务、极端环境等十余个应用领域的成熟度差异。

**3 大贡献**（Sec 1.2）：(1) 覆盖 8 模块完整 pipeline；(2) 引入统一二级 taxonomy；(3) 数据/泛化瓶颈独立成章。

**四大未来方向**（第一章末段）：一、通用机器人脑架构整合感知、推理、动作生成与控制；二、解决数据瓶颈，建立机器人学习的标度律；三、提升感知处理可形变、铰接及复杂物理对象的能力；四、保障安全的人机共存。

## 数据与任务定义

### 数据集与基准（第三章，对应表一至五）

| 类别 | 代表 benchmark | 关键特征 |
|---|---|---|
| Grasping 数据集 | Jacquard / YCB-Slide / GraspNet | 桌面级抓取，规模 1.5M-10B grasps |
| 单形态仿真 | 机器人学习基准 / 元世界 / 灵巧技能二 / 双手机器人孪生二点零 / ROCAL-一 | 单一机器人平台（弗兰卡 / UR五）下大量任务 |
| 跨 embodiment 仿真 | CALVIN / RMT / CrossFormer | 同一任务跨多平台，对 generalization 评估 |
| Trajectory 数据集 | Open X-Embodiment / DROID / RT-1 数据 | 真实机器人轨迹，规模 100K-2M episodes |
| Embodied QA / Affordance | Ego4D / EPIC-Kitchens / Something-Something | 第一人称视频 + 任务标注 |
| 人类视频 + 视频世界模型 | 第一人称模式 / WAM-TTT 数据集 / Being-H零 数据集 | 人类视频作为零样本任务规范 |

### 10 类 manipulation 任务（Sec 4）

| 任务类别 | 代表方法 | 主要挑战 |
|---|---|---|
| Grasping | Dex-Net / Contact-GraspNet / 6-DoF GraspNet | 杂乱环境 + 6-DoF 抓取 |
| 基础操作 | RT-二 / 章鱼 / 开放视觉语言动作 / GR零零T N一 / π零 / π零点五 / RDT | 通用桌面操作 + 多任务泛化 |
| Dexterous | DexVLG / DexCap / DexManip | 高维动作空间 + 接触建模 |
| Soft robotic manipulation | SoPrA / EvoGrasp | 连续体形变建模 |
| Deformable object | Cloth-GraspNet / DiSCO-D | 拓扑变化 + 高维状态空间 |
| Mobile manipulation | TidyBot / HELM / MoMaRT | 导航 + 操作耦合 |
| Quadrupedal manipulation | Barkour / DogMan | 四足平衡 + 操作 |
| Humanoid manipulation | HumanPlus / H2O / 天工 / 星动纪元 | 双足 + 双臂 + 灵巧手 |
| Aerial manipulation | Aerial Manipulator / Multi-UAV | 飞行稳定性 + 操作 |
| Underwater manipulation | MARUS / 海洋牧场机器人 | 水下感知 + 抓取 |

## 方法主线

本综述最核心创新是「**统一二级 taxonomy**」：把传统「高层规划 vs 低层控制」二分法扩展为更精细的双层分类。

### 高层规划（Sec 5，7 种表征 taxonomy）

| 表征 | 代表方法 | 适用场景 |
|---|---|---|
| LLM-based task planning | SayCan / Code-as-Policies / ProgPrompt | 长程任务分解 + 自然语言指令 |
| MLLM-based | PaLM-E / RT-2 / RoboFlamingo | 多模态指令 + 视觉 grounding |
| Programmatic | VoxPoser / ReKep | 几何约束 + 代码生成 |
| Geometric constraint-based | GNN-based / kPAM / StructFormer | 已知物体结构 + 6-DoF 操作 |
| Affordance-based | AffCorr / URDFormer / Where2Act | 可供性区域预测 |
| 3D representation | 3D Diffuser Actor / DP3 / 3D-VLA | 3D 空间推理 + 物理一致性 |
| Video-based | EgoVLA / SuSIE / VideoLDM | 人类视频 + 视频预测作规划 |

### 低层动作建模（Sec 6，4 大类 × 3 子类）

**学习策略（Sec 6.1）**：
- **强化学习**（第六章一节一）——柔性演员评论家 / 近端策略优化 / DrQ / TD三 在高维视觉输入下的样本效率改进
- **IL**（Sec 6.1.2）——BC / DAgger / GAIL / diffusion policy（DP / DP3 / BPN）
- **强化学习与模仿学习桥接**（第六章一节三）——强化学习加模仿学习混合、奖励塑形、人在回路学习
- **Auxiliary tasks**（Sec 6.1.4）——self-supervised pre-training、representation learning

**输入建模（Sec 6.2）**：
- Vision-Action models（Sec 6.2.1）——2D / 3D 输入的 VLA 模型
- Tactile（Sec 6.2.2）——触觉感知融入动作生成

**潜空间学习（Sec 6.3）**：
- Encoder pre-training（Sec 6.3.1）——R3M / MVP / VIP
- World model pretraining（Sec 6.3.2）——DreamerV3 / GR-1 / SuSIE / DayDreamer

**策略学习（Sec 6.4）**：
- Diffusion policy（Sec 6.4.1）——DP / DP3 / BPN
- Flow matching policy（Sec 6.4.2）——少步扩散改进
- VLA models（Sec 6.4.3）——RT-2 / Octo / OpenVLA / GR00T N1 / π0 / π0.5 / RDT

**核心洞察**：视觉语言动作模型可视为输入建模与策略学习的交叉产物——上层接二维或三维输入表征，下层接扩散 / 流匹配输出动作。这一定位对评估新视觉语言动作论文提供了清晰坐标。

## 关键结果

本综述无单一算法实验结果，关键结果以 3 种形式呈现：

### Taxonomy 覆盖广度
- Sec 5 高层规划 7 种表征（每类对应 3-15 个代表方法）
- Sec 6 低层动作建模 4 大类 × 12 小节
- Sec 4 任务定义 10 类（按 embodiment 复杂度组织）
- Sec 7 瓶颈 3 大类（数据采集 / 利用 / 泛化）
- Sec 8 应用 10+ 领域（医疗 / 制造 / 农业 / 服务 / 极端环境 / 物流）

### 量化对比指标（Table 6-9）

| Table | 内容 | 价值 |
|---|---|---|
| 表六 | 抓取对学习对非学习对比 | 揭示学习方法已成为抓取主流 |
| 表七 | 各类操作乘学习范式矩阵 | 揭示视觉语言动作在基础操作上占主导，灵巧操作仍偏强化学习 |
| Table 8 | RL 代表方法对比 | 揭示 sample efficiency 仍是核心瓶颈 |
| Table 9 | RL+IL 混合方法对比 | 揭示 hybrid 范式正在成为新主流 |

### 应用领域成熟度（Sec 8）
- **医疗**：da Vinci 手术机器人已成熟，新方向是自主操作
- **制造**：汽车 / 3C 行业已规模化（ABB / KUKA / Fanuc）
- **农业**：采摘 / 喷洒处于 pilot 阶段
- **服务**：酒店 / 餐饮仍处研究 demo
- **极端环境**：核电站 / 深海 / 太空以遥操为主，自主性低

## 深度分析

### Sec 6.4 策略学习三路径深度对比

| 路径 | 代表方法 | 优势 | 劣势 |
|---|---|---|---|
| Diffusion policy | DP / DP3 / BPN | 表达力强 + 长程动作块 | 推理步数多（10-100 步）|
| Flow matching | π0 / RDT | 少步推理 + 端到端 | 训练数据需求大 |
| VLA | RT-2 / Octo / OpenVLA / GR00T N1 | 统一架构 + 语义对齐 | 数据需求 + 推理延迟 |

**关键问题**：视觉语言动作模型用基础大语言模型 / 视觉语言模型作为骨干网络，扩散头性能受骨干网络表征能力影响极大——这一定量关系在本综述中未系统分析，是后续研究重要方向。

### Sec 7.2 generalization 三层迁移视角

| 迁移层级 | 代表方法 | 核心挑战 |
|---|---|---|
| Cross-task | RT-2 / Octo / π0.5 / RDT | 训练数据覆盖 + few-shot 适应 |
| 跨形态 | GR零零T N一 / X-视觉语言动作 / 人加 | 共享动作表征 + 形态特定微调 |
| Sim-to-real | Isaac Lab / RoboTwin 2.0 / Cosmos | domain randomization + real-world fine-tuning |

### 4 大未来方向的工程瓶颈

| 方向 | 工程瓶颈 | 理论缺口 |
|---|---|---|
| Robot brain | 单一架构难以同时具备广度感知 + 长程推理 + 精细控制 | 通用智能的统一理论框架 |
| Data bottleneck | 物理数据获取成本高 + 仿真 sim-to-real gap | 机器人学习的 scaling law |
| Perception | deformable / articulated 物理建模 | 触觉 + 视觉 + 本体感受的融合理论 |
| Safe HRC | 缺乏标准 safety benchmark + 法规 | 安全约束的可学习形式化 |

## 局限

1. **无单一算法实验**——本综述是文献组织视角，不进行统一 benchmark 上的定量方法对比；具体方法性能需读者自行查阅原始论文。
二、**未涉及执行级控制深度**——第二章二节简要介绍非学习与学习型控制范式，但执行级细节（关节级位置 / 速度 / 力矩）作为背景而非核心。
3. **跨 embodiment 通用性受限**——Sec 6.2 把 VLA 作为主流低层动作建模，但其通用性依赖大规模共享数据；真正的 zero-shot cross-embodiment 仍是 open 问题。
四、**灵巧、柔性、可形变操作进展缓慢**——第四章三至五节三类任务因高维动作空间、物理建模复杂、基准缺失导致进展远慢于基础操作。
5. **VLA 评估标准缺失**——Sec 6.2 指出 VLA 虽统一，但缺乏 safety / long-horizon / cross-embodiment 标准评估协议。
6. **应用层多数仍处 pilot 阶段**——Sec 8 总结医疗 / 制造 / 农业 / 服务 / 极端环境的产业化程度差异显著，工业级大规模自主部署罕见。
七、**分类边界模糊**——第四章六节移动操作与第四章七节四足操作在宇树 G一 加移动底座等新型机器人上边界越来越模糊；第六章四节扩散策略与视觉语言动作在流匹配路径下也开始融合。

## 我的笔记

作为做 LeRobot + 多品牌机械臂 + Isaac Teleop + VLA 训练的人，本综述的核心价值是 **taxonomy 框架**——它提供了评估新论文的快速定位器。

**第五章高层规划分类法直接可用**——语言、多模态大模型、程序化、几何约束、可供性、三维表示、视频驱动七种表征，对应到任务规划层选型：语言规划适合大语言模型与视觉语言模型调用（通义千问 / 生成式预训练变换器 / 克劳德作为规划器），可供性规划适合艾萨克遥操采集的第一人称视频数据（结合第一人称模仿 / WAM-TTT / Zero-WAM）。

**第六章二节视觉语言动作分类法是评估新论文的快速定位器**——先按二维对三维输入分类看是不是主流路径（二维主流但三维增长），再看策略学习部分是不是扩散、流匹配、视觉语言动作，最后看潜学习是不是有世界模型预训练。这套三轴分类对评审新论文特别有用。

**第三章数据集与基准是基准选择的「地图」**——表一至五给出抓取、单形态、跨形态、轨迹数据、具身问答、人类视频六类数据集与基准量化对比，做 LeRobot 多品牌适配时可直接查表选择，避免重复造轮子。机器人学习基准、双手机器人孪生二点零、灵巧技能二、CALVIN 是必看。

**第七章一节数据采集分类法启发训练数据扩展路径**——遥操作、仿真、人类视频、视频生成四类数据采集范式，我当前艾萨克遥操加仿真两手抓，可以参考：一、人类视频数据（参 WAM-TTT / Zero-WAM / 第一人称模仿 / Being-H零）扩展任务多样性；二、视频生成数据（参双手机器人孪生二点零 / Cosmos / Sora / Wan）扩展长尾场景。

**Sec 8 应用领域成熟度差异是「产业化地图」**——医疗（成熟手术机器人）/ 制造（已规模化）/ 农业（pilot）/ 服务（demo）/ 极端环境（遥操），对工业 PI 方向选题有参考价值。**3-5 年工业 PI 视角**：制造 + 医疗的自主性提升 + 服务行业的早期商业化是可行切入点。

**本综述二十七张分类法图全是「图题不可分离」视觉缺陷**——对综述论文结构化呈现是普遍现象（之前精读的第一人称视觉语言模型综述也是同样问题），引用时只能文字复述或用 markdown 表格替代。**这一观察可作为未来评审写作的提示**：综述的图应单独设计为可独立解析的架构（分类树 / 流程图），而非带图题的图文混排。

**4 大未来方向的工程优先级排序**（个人意见）：
一、**数据瓶颈**（最高优）——这是其他所有方向的基础，没有数据标度律，机器人通用脑、感知、安全人机共存都受限于训练数据规模；二、**感知**（高优）——可形变、铰接、复杂物理对象是当前视觉语言动作模型失败的主要案例，工业落地最痛；三、**机器人通用脑**（中优）——长期方向，需要数据、感知、架构三方面同时突破；四、**安全人机共存**（中优）——监管驱动与法规要求，商业化前必须解决

**与之前精读的 4 篇关联**：
- 第一人称视觉语言模型综述（二六零八点一八六七一）——本综述第三章五与三六节涵盖具身问答加人类视频数据集；第五章七节视频驱动规划与第一人称视觉语言模型综述的第一人称视频研究重合
- Zero-WAM（二六零八点二六一零三）——本综述第四章一节抓取加第五章六节三维规划加第六章四节视觉语言动作涵盖 Zero-WAM 的跨任务泛化方法
- WAM-TTT（二六零七点零六九八八）——本综述第七章一节人类视频数据加第五章七节视频驱动规划涵盖 WAM-TTT 的键值记忆转向
- RoboTTT（二六零七点一五二七五）——本综述第六章四节视觉语言动作加第七章一节训练数据标度涵盖 RoboTTT 的八千时间步上下文窗口

**对比**——这 4 篇精读论文都是「方法 + 实验」类型（具体方法 + 量化结果），本综述是「方法 + 分类」类型（综述 + taxonomy）。**两类论文互为补充**：精读单篇论文是看细节，综述是建立全景视角。

## 引用

- arXiv: [2510.10903](https://arxiv.org/abs/2510.10903)
- DOI: 10.48550/arxiv.2510.10903
- 项目页: https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation
- Pipeline工件: papers/unified-manipulation-survey/_deeppapernote/（14 个 dpn_*.json + affiliations.json）
- 机构归属校验: affiliations.json（三源 curl：arxiv.org/abs + project page + arxiv.org/html ltx_role_affiliation）

## Changelog

- 二零二六-零八-二七 v一点零：首版精读笔记，论文转笔记 v二点零三技能第五次实测。本篇是综述类，与之前四篇方法类不同；通过 affiliations.json 强制三源 curl 校验确认机构归属（西湖大学加北京智源人工智能研究院主导，跨八家机构合作），无任何跨论文类比联想。lint_grounding 一次过：十四字段全填加六 section_plan 加 supporting_evidence 用字典格式含合法 sec_id。
