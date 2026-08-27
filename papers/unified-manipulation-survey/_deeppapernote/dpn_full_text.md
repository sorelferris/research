# A Comprehensive Survey on Robot Manipulation

## sec:preamble preamble
_Pages 1-1_

A Comprehensive Survey on Robot Manipulation
V2: 2026-08-15
Towards a Unified Understanding of Robot
Manipulation: A Comprehensive Survey
Shuanghao Bai1∗†
Wenxuan Song2∗
Jiayi Chen2∗
Yuheng Ji3∗
Zhide Zhong2∗
Jin Yang1∗
Han
Zhao4,5∗
Wanqi Zhou1∗
Wei Zhao4,5∗
Zhe Li6∗
Pengxiang Ding4,5
Cheng Chi7
Haoang Li2
Chang
Xu6
Xiaolong Zheng3
Donglin Wang4
Shanghang Zhang7,8
Badong Chen1
1 Xi’an Jiaotong University, 2 Hong Kong University of Science and Technology (Guangzhou), 3 Chinese Academy of Sciences,
4 Westlake University, 5 Zhejiang University, 6 University of Sydney, 7 BAAI, 8 Peking University
† Project Lead
∗Core Contributors
Corresponding Authors
# chenbd@mail.xjtu.edu.cn
§ Awesome-Robotics-Manipulation
Abstract | Embodied intelligence has witnessed remarkable progress in recent years, driven by advances in
computer vision, natural language processing, and the rise of large-scale multimodal models. Among its core
challenges, robot manipulation stands out as a fundamental yet intricate problem, requiring the seamless
integration of perception, planning, and control to enable interaction within diverse and unstructured environ-
ments. This survey presents a comprehensive overview of robotic manipulation, encompassing foundational
background, task-organized benchmarks and datasets, and a unified taxonomy of existing methods. We extend
the classical division between high-level planning and low-level action modeling by broadening high-level
planning to include language, code, motion, affordance, and 3D representations, while introducing a new
taxonomy of low-level learning-based action modeling grounded in training paradigms such as input modeling,
latent learning, and policy learning. Furthermore, we provide the first dedicated taxonomy of key bottlenecks,
focusing on data collection, utilization, and generalization, and conclude with an extensive review of real-world
applications. Compared with prior surveys, our work offers both a broader scope and deeper insight, serving as
an accessible roadmap for newcomers and a structured reference for experienced researchers.
Task Type
§ 4
Grasping
Basic
Manipulation
Mobile
Manipulation
Quadrupedal
Manipulation
Humanoid
Manipulation
Dexterous
Manipulation
Deformable Object
Manipulation
Soft Robotic
Manipulation
Language
Vision
Touch
Audio
Input Modeling
§ 6.2
What and how to input
How to obtain and learn latent
How to decode latent to action
Latent Learning
§ 6.3
Policy Learning
§ 6.4
Learning Paradigms
§ 6.1
Reinforcement Learning
Imitation Learning
w/ Auxiliary Tasks
encode and fuse
decode
Diffusion
Autoregressive
VA, VLA, TLA, …
Pretrained Latent &
Latent Action Learning
control
Simulators, Benchmarks
and Datasets § 3
Environment
Actor
High-level
Planning § 5
Thinking
Low-level
Action
Modeling
Robot Type
§ 2.1
Control Paradigms
Application
§ 8
Industry
Agriculture
Art
Household
AI4Science
Sports
simple tasks
with more complex hands, objects
with complex mobile platforms

## sec:datasets Datasets
_Pages 1-1_

Action
Learning-based
§ 6
Bottlenecks § 7

## sec:data Data
_Pages 1-2_

§ 7.1
Generalization
§ 7.2
Agent
§ 7.3
Human-Robot
Collaboration § 7.4
Video
Code
Task
Plan
3D repres-
entations
Affordance
High-level Planning § 5
Geometric
Constraint
Figure 1 | Overview of the survey. We first provide a broad introduction to existing benchmarks,
datasets, and manipulation tasks, followed by an extensive review of representative methods with a
particular focus on learning-based action modeling. We then discuss two fundamental challenges,
namely data and generalization, and conclude with an overview of their diverse applications.
arXiv:2510.10903v2 [cs.RO] 15 Aug 2026
Contents

## sec:introduction Introduction
_Pages 2-2_

1.1
Survey Scope and Key Research Questions . . . . . . . . . . . . . . . . . . . . . . . .
1.2
Comparison with Previous Surveys and Contributions . . . . . . . . . . . . . . . . . .

## sec:background Background
_Pages 2-2_

2.1
Hardware Platforms for Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2
Low-Level Action Modeling: Non-Learning and Learning-Based Paradigms
. . . . . .
2.2.1
Non-Learning-Based Action Modeling . . . . . . . . . . . . . . . . . . . . . . .
2.2.2
Learning-Based Action Modeling
. . . . . . . . . . . . . . . . . . . . . . . . .
2.3
Robotics Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4

## sec:evaluation Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
_Pages 2-4_

Simulators, Benchmarks and Datasets
3.1
Grasping Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2
Single-Embodiment Manipulation Simulators and Benchmarks . . . . . . . . . . . . .
3.3
Cross-Embodiment Manipulation Simulators and Benchmarks . . . . . . . . . . . . .
3.4
Trajectory Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5
Embodied QA and Affordance Datasets . . . . . . . . . . . . . . . . . . . . . . . . . .
3.6
Human Video Datasets and Video-World-Model Benchmarks . . . . . . . . . . . . . .
Manipulation Tasks
4.1
Grasping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2
Basic Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3
Dexterous Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4
Soft Robotic Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5
Deformable Object Manipulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6
Mobile Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7
Quadrupedal Manipulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8
Humanoid Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9
Aerial Manipulation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10 Underwater Manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
High-level Planning
5.1
LLM-Based Task Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2
MLLM-based Task Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3
Programmatic Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4
Geometric Constraint-based Planning . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.5
Affordance-Based Planning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.6
3D Representation-Based Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
5.7
Video-Based Planning
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Low-level Learning-based Action Modeling
6.1
Learning Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.1
Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.2
Imitation Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3
Bridging Reinforcement and Imitation Learning . . . . . . . . . . . . . . . . .
6.1.4
Learning with Auxiliary Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2
Input Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.1
Vision-Action Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2
Vision-Language-Action Models . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3
Tactile-based Action Models . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.4
Extra Modalities as Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3
Latent Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1
Pretrained Latent Learning
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.2
Latent Action Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4
Policy Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.1
MLP-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.2
Transformer-based Policy
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.3
Diffusion Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.4
Flow Matching Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.5
SSM-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.6
SNN-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.7
Frequency-based Policy
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.8
Action Tokenization and Structured Action Representation . . . . . . . . . . .
6.4.9
Drift-based Policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Approaches to the Key Bottlenecks
7.1
Data Collection and Utilization
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1.1
Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1.2
Data Utilization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2
Generalization
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.1
Environment Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.2
Task Generalization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.2.3
Cross-Embodiment Generalization
. . . . . . . . . . . . . . . . . . . . . . . .
7.3
Agent
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.4
Human–Robot Interaction and Collaboration . . . . . . . . . . . . . . . . . . . . . . .
Applications
8.1
Household Assistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.2
Agriculture
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
8.3
Industry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.4
AI4Science . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.5
Art . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8.6
Sports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Prospective Future Research Directions
9.1
Building a General-Purpose and Self-Evolving Robot Brain . . . . . . . . . . . . . . .
9.2
Scaling Robot Intelligence Beyond Robot Data . . . . . . . . . . . . . . . . . . . . . .
9.3
Multimodal and Contact-Rich Physical Interaction . . . . . . . . . . . . . . . . . . . .
9.4
Safety, Recovery, and Collaborative Autonomy . . . . . . . . . . . . . . . . . . . . . .

## sec:conclusion 10 Conclusion
_Pages 4-5_

Author Contributions
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey

## sec:introduction-2 1. Introduction
_Pages 5-7_

In recent years, embodied intelligence has attracted increasing attention, largely driven by advances
in computer vision and natural language processing, particularly the success of large-scale models.
These developments have not only demonstrated remarkable machine intelligence but also offered a
glimpse into the potential of artificial general intelligence (AGI). Building on this progress, large-scale
language and multimodal models [1–3] have accelerated the development and deployment of robotic
systems by enhancing perceptual and semantic understanding, enabling operation in unstructured
environments, and supporting natural-language task specification. Their zero-shot and few-shot
generalization capabilities improve the adaptability of robotic systems, while multimodal interaction
enhances usability and reduces deployment barriers in real-world scenarios.
Robot manipulation is a core and extensively studied problem in embodied intelligence, referring
to a robot’s ability to perceive its environment, plan task execution, generate appropriate actions,
and control its effectors to physically interact with and modify the environment, such as by grasping,
moving, or using objects. Its development spans classical rule-based and non-learning methods [4–7]
from the late twentieth century through the 2010s, followed by deep learning-based approaches [8,
9], the widespread adoption of imitation learning (IL) and reinforcement learning (RL) [10, 11],
and, more recently, the integration of large language and vision-language models into IL and RL
frameworks [12, 13]. In this survey, non-learning methods are primarily introduced as methodological
background, while the main discussion focuses on data-driven and learning-based approaches.
1.1. Survey Scope and Key Research Questions
In this survey, we aim to provide newcomers with a concise roadmap to the development, tasks, and
methods of robot manipulation, while offering experienced researchers a structured reference and a
broader perspective on the field. To this end, we organize the survey around the following research
questions:
1. What benchmarks and task categories define robot manipulation today? We review the
current landscape of benchmarks in Section 3 and organize representative manipulation problems
into major task categories in Section 4.
2. What methods have been proposed to address these manipulation tasks? Beyond basic
manipulation, Section 4 reviews representative approaches for dexterous, deformable-object, mobile,
quadrupedal, and humanoid manipulation. For these categories, we briefly introduce classical
non-learning methods and place greater emphasis on learning-based approaches, including RL, IL,
VLA models, and strategy-augmented methods, while highlighting the distinct methodological and
embodiment-specific challenges of each domain.
Basic manipulation, in contrast, represents the most extensively studied setting and is supported by
a substantially richer body of literature. We therefore provide a dedicated analysis in Sections 5 and 6,
distinguishing between high-level planning methods that produce task-level plans or intermediate
planning artifacts and low-level action-modeling methods that generate executable robot actions
from observations and task specifications. Actuation-level control, which converts these actions into
joint-level position, velocity, or torque commands, is introduced separately as part of the foundational
background. Although this taxonomy is developed primarily in the context of basic manipulation, its
underlying distinction between planning, action generation, and physical execution is also applicable
to other manipulation settings.
3. What are the current bottlenecks in robot manipulation? We identify data collection and
utilization, together with generalization, as two central challenges. Section 7.1 reviews the evolution
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
of robot-data collection and examines strategies for improving the efficiency and effectiveness of
data utilization during training. Section 7.2 analyzes the major forms of generalization in robot
manipulation and summarizes the corresponding methodological strategies.
4. What are the practical applications of manipulation techniques beyond research? We
survey how advances in robot manipulation are being deployed across a wide range of real-world
application domains in Section 8.
1.2. Comparison with Previous Surveys and Contributions
First, compared with prior surveys that are limited in scope, our work provides a comprehen-
sive and systematic overview of robot manipulation. Existing surveys typically adopt narrower
perspectives. Some focus on particular task domains, such as dexterous manipulation [14, 15],
deformable-object manipulation [16], mobile manipulation [17], or humanoid manipulation [18].
Others emphasize methodological paradigms that recur across different tasks, including vision-
language-action models [19–22], diffusion models [23], and generative approaches [24]. A further
group concentrates on specific methodological concepts, such as language-conditioned learning [25]
or object-centric representations [26]. Several broader embodied-intelligence surveys cover a wide
range of topics but treat manipulation only as one subsection, providing insufficient depth for a
systematic understanding of the field [27, 28].
Second, our survey introduces a unified taxonomy that covers the robot-manipulation
pipeline more extensively than existing categorizations. The resulting organization provides an
accessible blueprint for newcomers while offering experienced researchers a structured perspective
on the relationships among different problem formulations and methodological paradigms.
Specifically, we provide a comprehensive background in Section 2, covering hardware embodi-
ments, actuation-level control paradigms, and foundational robotic models. We introduce benchmarks
and datasets organized by manipulation-task category in Section 3, present a systematic overview
of representative manipulation tasks, and develop a refined methodological taxonomy in Sections 5
and 6. While prior surveys often distinguish broadly between high-level planning and low-level
control, we refine this division by separating high-level planning, low-level action modeling, and
actuation-level control according to the system interface and the form of the model output. We
broaden high-level planning in Section 5 to encompass planning representations expressed through
language, code, motion, affordances, and 3D scene structures. For low-level action modeling in
Section 6, we propose a taxonomy grounded in training paradigms and further organize existing
methods according to learning strategy, input modeling, latent learning, and policy learning.
In addition, we provide a detailed analysis of current bottlenecks in robot manipulation in Section 7
and introduce a dedicated taxonomy covering data collection, data utilization, and generalization.
Finally, Section 8 presents a broader and more systematic review of real-world applications than those
provided in previous surveys.
Finally, based on these contributions and recent developments in the field, we identify
emerging research trends and outline four promising directions for future work. The first
concerns the development of a genuine robot brain, namely a general-purpose architecture that
integrates broad perception, reasoning, action-generation, and control capabilities. The second
addresses the data bottleneck, as current robot learning has not yet exhibited a reliable scaling law
comparable to those observed in language and vision, largely because of the high cost of physical
data acquisition and the limitations of simulation. The third concerns perception, particularly the
need for richer multimodal sensing and more reliable interaction with deformable, articulated, and
otherwise physically complex objects. The fourth emphasizes safe human–robot coexistence, which
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Hello Stretch
Franka Panda
UR5
Kinova Gen3
Google Robot
xArm
WidowX
Robotiq 2f-85
Shadow Hand
D’Kitty and D’Claw
RBO Hand 3
SpiRobs
COBOT Magic
ALOHA
ABB YuMi
Unitree Go2
Boston Dynamics Spot
Unitree G1
Single Arm
Bimanual Arms
Soft Hands
Allegro Hand
Dexterous Hands
Parallel-Jaw Gripper
Mobile Robots
Quadruped Robots
Figure 02
Humanoid Robots
hand
+ arm
+ mobile platform
Complexity
Unitree Dex3
Inspire Hand
Linker L20 Hand
Wuji Hand
OnRobot 2FG7
Franka Hand
UMI
qb SoftHand
Galaxea R1 Lite
AgiBot A2
Galaxea R1 Pro
Tienkung3.0
PR2
Walker S2
Galbot S1
Booster K1
Alphabot2
Figure 2 | Overview of hardware platforms.
remains essential for the large-scale deployment of robotic systems in real-world environments.

## sec:background-2 2. Background
_Pages 7-13_

In this section, we first introduce the hardware types commonly used in robotic manipulation (Sec-
tion 2.1). We then outline the main categories of control strategies, namely non-learning-based and
learning-based approaches (Section 2.2). Next, we review the robotic models widely adopted for
learning-based control (Section 2.3) and discuss the evaluation protocols used to assess the robotic
models within these frameworks (Section 2.4).
2.1. Hardware Platforms for Manipulation
Before introducing manipulation tasks and their corresponding methodologies, it is important to
first understand the hardware systems that enable these operations. Robotic manipulation can be
achieved through various embodiments composed of fundamental components such as hands, arms,
and mobile platforms. Different combinations of these components define specific embodiments and
their functional capabilities. For example, pairing a parallel-jaw gripper with a Franka Panda arm
enables basic manipulation tasks such as pick-and-place or insertion, while integrating a Unitree G1
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
humanoid platform with a dexterous hand allows for humanoid-level manipulation that demands
greater dexterity and coordination. We summarize the commonly used robotic hardware types in
current research in Figure 2.
Parallel-Jaw Grippers. Parallel-jaw grippers are among the most widely adopted end-effectors in
robotic manipulation because their low-dimensional actuation, repeatable contact geometry, and
reliable force transmission simplify control, demonstration collection, and policy learning. Repre-
sentative commercial platforms include the Robotiq 2F-851, OnRobot 2FG72, and Franka Hand3.
Research-oriented designs further extend this basic morphology, including DexWrist [29], which
augments a gripper with additional wrist dexterity, and UMI [30], which integrates a portable gripper
and visual sensing interface for scalable real-world demonstration collection. Although these grippers
provide limited in-hand dexterity, their compact action spaces and robust grasping behavior make
them effective for pick-and-place, insertion, and large-scale imitation-learning experiments.
Dexterous Hands. Dexterous hands employ multiple articulated fingers and higher-dimensional
actuation to support contact-rich manipulation beyond simple opening and closing. Representative
multi-finger end-effectors include the Robotiq 3-Finger Adaptive Robot Gripper4, Allegro Hand5,
Shadow Dexterous Hand6, Unitree Dex3-17, D’Claw and D’Kitty from the ROBEL platform [31], Inspire
Hand8, Linker Hand L209, and Wuji Hand10, together with other learning-oriented designs [32, 33].
Their articulated structures enable object reorientation, in-hand manipulation, tool use, and coordi-
nated multi-contact interaction. However, the increased number of controllable joints also enlarges
the action space and places substantially greater demands on sensing, calibration, demonstration
quality, and closed-loop policy learning.
Soft Hands. Soft hands exploit material compliance, underactuated transmission, or deformable
actuation to conform passively to object geometry. Representative platforms include the RBO Hand
3 [34], Festo BionicSoftHand11, SpiRobs [35], and qb SoftHand12. In contrast to rigid dexterous hands,
these systems partially transfer the burden of contact adaptation from explicit control to mechanical
compliance, improving grasp robustness and interaction safety under geometric uncertainty. This
adaptability is obtained at the cost of less precise kinematic modeling and more difficult estimation of
contact states and deformation-dependent dynamics.
Single Arm. Fixed-base single-arm manipulators remain the predominant platforms for learning-
based manipulation because they provide accurate and repeatable motion within a well-defined
workspace. Commonly used systems include the KUKA LBR iiwa13, Franka Emika Panda [36]14,
UR5 and UR1015, Kinova Gen316, xArm6 and xArm717, and WidowX18. These platforms typically
provide six or seven degrees of freedom and are widely employed for behavior cloning, reinforcement
learning, visuomotor control, and sim-to-real evaluation. More recently, low-cost and reproducible
systems supported by open-source ecosystems such as LeRobot19 have lowered the barrier to physical
experimentation and facilitated standardized data collection across research groups.
Bimanual Arms. Bimanual systems extend the workspace and contact capabilities of single-arm
platforms by coordinating two manipulators. Representative systems include dual Franka Panda
configurations20, ALOHA [37], and ABB YuMi21. They support tasks such as bilateral assembly, object
handover, deformable-object manipulation, container opening, and coordinated tool use. Nevertheless,
bimanual manipulation introduces additional challenges associated with temporal synchronization,
inter-arm collision avoidance, assignment of complementary roles, and learning coupled actions
whose effectiveness depends on the coordinated behavior of both arms.
Mobile Manipulators. Mobile manipulators combine one or more arms with a movable base, thereby
extending manipulation beyond the bounded workspace of a fixed-base robot. Representative plat-
forms include COBOT Magic22, Hello Robot Stretch 323, the Google mobile manipulation platform24,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Galaxea R1 Lite25, PR226, and TIAGo27. By coupling navigation, base positioning, torso adjustment,
and arm motion, these platforms can perform object fetching, household assistance, long-horizon
rearrangement, and human–robot interaction across extended environments. Their operational range
also introduces partial observability, accumulated localization error, dynamic obstacles, and the need
to coordinate manipulation and locomotion within a unified decision process.
Quadruped Robots. Quadruped platforms provide agile locomotion over uneven terrain and can be
equipped with articulated arms or specialized end-effectors to support mobile manipulation. Represen-
tative systems include Unitree Go2, B1, and Aliengo28, together with Boston Dynamics Spot29. Their
legged morphology enables operation in environments that are inaccessible to conventional wheeled
platforms, including stairs, rough terrain, and infrastructure-inspection settings. Manipulation on
quadrupeds nevertheless requires tight coupling among locomotion, body stabilization, arm motion,
and contact-force regulation, particularly when manipulation forces disturb the support configuration
of the robot.
Humanoid Robots. Humanoid and anthropomorphic whole-body platforms are designed to operate
in spaces, use tools, and interact with objects originally configured for humans. Representative
systems include Tesla Optimus Gen 230, Boston Dynamics Atlas31, Figure 0232, 1X NEO33, Unitree
G134, AgiBot A235, Tiangong 3.036, UBTECH Walker S237, Booster K138, AlphaBot 239, Galbot S140,
and Galaxea R1 Pro41. This category increasingly encompasses both bipedal humanoids and wheeled
anthropomorphic systems that retain a human-scale torso and manipulation workspace. Compared
with arm-centered platforms, these embodiments expand the action space to include locomotion,
balance, torso motion, whole-body contact, and coordinated use of multiple limbs. They therefore
provide a promising substrate for general-purpose embodied intelligence while introducing substantial
challenges in data efficiency, safety, state estimation, hierarchical control, and reproducible evaluation.
2.2. Low-Level Action Modeling: Non-Learning and Learning-Based Paradigms
In this survey, low-level action modeling broadly refers to methods that transform task goals, environ-
ment states, or observations into executable robot paths, trajectories, actions, or action sequences.
This definition is based on the exposed system interface rather than the internal computational mech-
anism. Accordingly, low-level actions may be constructed analytically, obtained through sampling
or optimization, or learned from data. They are subsequently translated into joint-level position,
velocity, force, or torque commands by actuation-level controllers.
Similar to how humans may follow explicit rules, such as stopping at a red light, or acquire
adaptive skills through repeated practice, such as learning to ride a bicycle, low-level robot actions
can be generated through either classical non-learning methods or data-driven learning approaches.
Non-learning methods offer interpretability, predictable behavior, and explicit constraint handling in
well-defined settings, whereas learning-based methods provide greater adaptability and generalization
in complex or uncertain environments.
2.2.1. Non-Learning-Based Action Modeling
Non-learning-based action modeling generates executable paths, trajectories, or control sequences
using analytical construction, search, optimization, and model-based control without learning the
underlying observation-to-action mapping from data. We include these methods as foundational
counterparts to learning-based action models and because they are frequently combined with learned
perception, planning, or policy modules. However, they are not the primary focus of the methodological
taxonomy developed in this survey.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Interpolation-Based Planning. Classical manipulators often employ interpolation-based plan-
ning [38, 39], in which smooth joint-space trajectories are generated, typically offline, by fitting
polynomial curves, such as cubic splines, between predefined start and goal states. These methods
are computationally lightweight and straightforward to deploy, making them prevalent in repetitive
and well-structured industrial tasks. However, their dependence on predefined boundary conditions
provides limited adaptability to dynamic or uncertain environments, constraining their applicability
in unstructured settings.
Sampling-Based Planning. Sampling-based planners [40–43] construct feasible paths by sampling
configuration space and incrementally building a graph or tree of collision-free states, rather than
explicitly representing free space or solving a large global optimization problem. Canonical algorithms
include Rapidly-exploring Random Trees (RRT) [41, 43] and Probabilistic Roadmaps (PRM) [42],
together with asymptotically optimal variants such as RRT*. These methods scale effectively to
high-dimensional configuration spaces, but the resulting paths may be suboptimal or non-smooth and
therefore often require subsequent smoothing, time parameterization, and trajectory tracking.
Optimization-Based Planning. Optimization-based planners formulate low-level action generation
as a constrained optimization problem over paths, trajectories, or control sequences. They minimize
task-specific objectives while enforcing constraints related to robot kinematics, dynamics, collision
avoidance, smoothness, and task completion.
Offline optimization-based planners solve the trajectory-generation problem before execution by
optimizing the complete motion as a batch. Representative methods include CHOMP (Covariant
Hamiltonian Optimization for Motion Planning) [44], TrajOpt (Trajectory Optimization) [45], and
STOMP (Stochastic Trajectory Optimization for Motion Planning) [7]. These approaches can produce
smooth and collision-free trajectories, but they often require substantial computation and cannot
directly adapt to unexpected changes encountered during execution.
Online optimization-based planners, such as Model Predictive Control (MPC) [46, 47], repeatedly
solve a finite-horizon optimization problem using the current state as the initial condition. MPC
leverages a predictive model to estimate future states and generate executable control actions in
a receding-horizon manner. This repeated re-optimization enables adaptation to disturbances and
dynamic environments. In the taxonomy adopted here, MPC is included as a low-level action-modeling
method because its exposed output is a finite sequence of executable actions or control inputs, whereas
the downstream servo loop that realizes these commands is treated as actuation-level control.
2.2.2. Learning-Based Action Modeling
Learning-based action modeling aims to learn a policy that maps environment observations, robot
states, and optional task specifications to executable actions or action sequences. Depending on the
source of supervision and the interaction setting, representative paradigms include reinforcement
learning and imitation learning.
Sequential decision-making for learning-based action modeling is commonly formulated as a
Markov Decision Process (MDP), which provides a formal framework for modeling interactions
between a robot and its environment under uncertainty. An MDP is defined as a five-tuple:
M = ⟨S, A, P, R, 𝛾⟩,
(1)
where
• S denotes the state space containing all possible environment and robot states;
• A denotes the action space containing the executable actions available to the robot;
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
• P(𝑠′ | 𝑠, 𝑎) denotes the transition probability of reaching state 𝑠′ after executing action 𝑎in state
• R : S×A →ℝdenotes the reward function specifying the expected immediate reward obtained
by executing action 𝑎in state 𝑠;
• 𝛾∈[0, 1] denotes the discount factor that balances short-term and long-term rewards.
This formulation provides a unified basis for learning policies that map states or observations to
executable actions and underlies a wide range of robot-learning approaches, including reinforcement
learning and imitation learning.
Reinforcement Learning (RL). The objective of reinforcement learning is to learn an optimal policy
𝜋∗: S →A that maximizes the expected cumulative discounted reward, also referred to as the
return [48]:
𝜋∗= arg max
" ∞
𝑡=0
𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡)
𝑎𝑡∼𝜋(· | 𝑠𝑡).
(2)
This objective provides the theoretical foundation for a broad family of algorithms, including Q-
learning [49, 50], policy-gradient methods [51, 52], and actor-critic approaches [53, 54]. According
to how interaction data are obtained, RL methods can be categorized into offline RL [55, 56], which
learns entirely from a fixed pre-collected dataset; online RL [54, 57], which continually interacts
with the environment to collect new experience; and offline-to-online RL [58, 59], which initializes
learning from offline data and subsequently improves the policy through online interaction.
Imitation Learning (IL). Imitation learning acquires action policies from expert demonstrations
and is commonly divided into Behavior Cloning (BC), Inverse Reinforcement Learning (IRL), and
Generative Adversarial Imitation Learning (GAIL).
BC formulates action modeling as supervised learning from expert state-action pairs, without
requiring an explicitly specified reward function [60, 61]. Let 𝑠𝑡denote the system state at timestep 𝑡,
which may include the robot proprioceptive state, visual observations, language instructions, and
observation histories. A policy 𝜋maps these inputs to an action or action sequence. Given an expert
demonstration dataset D𝑒, the optimization objective can be written as:
𝜋∗= arg min
𝜋𝔼(𝑠𝑡,ˆ𝑎𝑡)∼D𝑒[L (𝜋(𝑠𝑡), ˆ𝑎𝑡)] ,
(3)
where ˆ𝑎𝑡denotes the expert action label. In conventional BC, L is typically instantiated as cross-
entropy loss for discrete action spaces and as mean squared error or 𝐿1 loss for continuous action
spaces.
IRL seeks to recover a reward function that explains the expert’s behavior rather than directly
imitating expert actions. By inferring the objective underlying expert demonstrations, the learned
policy may generalize more effectively to unseen states and related tasks [62, 63]. IRL assumes that
the expert behaves approximately optimally with respect to an unknown reward function 𝑅(𝑠, 𝑎).
Given expert demonstrations D𝑒, the objective is to identify a reward function 𝑅∗under which the
expert policy 𝜋𝑒achieves a higher expected return than alternative policies:
𝑅∗= arg max
𝔼𝜋𝑒
" ∞
𝑡=0
𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡)
−𝔼𝜋
" ∞
𝑡=0
𝛾𝑡𝑅(𝑠𝑡, 𝑎𝑡)
(4)
where 𝜋denotes a policy induced by the learned reward and 𝛾∈[0, 1) is the discount factor. After
estimating 𝑅∗, a reinforcement-learning algorithm is employed to obtain a policy 𝜋∗that maximizes
the expected return under the inferred reward. This separation between reward inference and policy
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
optimization enables the model to capture objectives implicit in expert behavior rather than merely
reproducing individual demonstrated actions.
GAIL formulates imitation learning as distribution matching between the discounted state-action
occupancy measures induced by the learner and the expert, thereby avoiding explicit recovery of a
task reward. The discounted occupancy measure induced by a policy 𝜋is defined as:
𝜌𝜋(𝑠, 𝑎) = (1 −𝛾)
𝑡=0
𝛾𝑡𝑃(𝑠𝑡= 𝑠, 𝑎𝑡= 𝑎| 𝜋, P) ,
(5)
where 𝛾∈[0, 1) is the discount factor, P denotes the MDP transition kernel P(𝑠′ | 𝑠, 𝑎), and the
prefactor (1 −𝛾) normalizes the occupancy measure over the infinite horizon. A standard adversarial
objective is:
min
max
𝐷:S×A→(0,1)
𝔼(𝑠,𝑎)∼𝜌𝐸[log 𝐷(𝑠, 𝑎)] + 𝔼(𝑠,𝑎)∼𝜌𝜋[log (1 −𝐷(𝑠, 𝑎))]
−𝜆H (𝜋),
(6)
where 𝐷is a discriminator over state-action pairs, 𝜌𝜋and 𝜌𝐸denote the learner and expert occupancy
measures, respectively, H (𝜋) = 𝔼(𝑠,𝑎)∼𝜌𝜋[−log 𝜋(𝑎| 𝑠)] is the policy entropy, and 𝜆≥0 controls
the strength of entropy regularization. At the optimal discriminator, this objective corresponds to
minimizing a divergence between 𝜌𝐸and 𝜌𝜋. In practice, the policy is updated through policy-gradient
optimization using a discriminator-induced pseudo-reward, without requiring an externally specified
task reward.
2.3. Robotics Models
Vision Models. To perceive the environment, robotic models typically incorporate vision models to
extract informative visual features. Common choices for visual encoders include models trained purely
on visual data, such as the ResNet family [64], Vision Transformers (ViT) [65], and self-supervised
models like DINO [66]. For 3D perception tasks, point cloud-based encoders such as PointNet [67]
and PointTransformer [68] are widely used. Additionally, vision-language pre-trained encoders, such
as the image encoders of CLIP [69] or SigLIP [70], are employed to obtain semantically enriched
representations that align visual observations with linguistic inputs. Some models leverage additional
visual information, including object detection results (such as bounding boxes) [71] and visual
tracking outputs [72], to improve perception and support downstream tasks more effectively.
Language Models. In recent years, especially since around 2020, language has emerged as a more
natural and human-friendly modality, leading to a growing integration of language models into
robotics. To understand human instructions, language embedding models are commonly employed
for extracting textual features, such as BERT [73] and the language encoder of CLIP. With the
leap from autoregressive models like GPT-2 [74] to GPT-3 [1], large language models (LLMs) have
demonstrated remarkable advances in text understanding and generalization. To further leverage
the powerful generalization capabilities of LLMs [2, 75], many recent robotic models adopt LLMs as
backbones, where textual inputs are processed through tokenization.
Text-conditioned Vision Models and Vision-Language Models (VLMs). Robotic models also adopt
VLMs such as LLaVA [3], PaLM-E [76], and Prism [77] as backbones, building upon their architectures
to enhance multimodal understanding and control. In addition, some works leverage text-conditioned
image editing [78] and video generation models [79] to guide action generation through visual
imagination and goal specification.
Vision-Action Models and Vision-Language-Action Models. Early approaches relied on visual
servoing for control [6] and gradually incorporated RL or IL methods that map states or images to
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
actions [80, 81], giving rise to vision–action (VA) models. Over time, VA architectures have evolved
from simple MLPs to more advanced diffusion-based frameworks [81], accompanied by diverse policy
designs. The concept of VLA models was introduced by RT-2 [12]. In the narrow sense, VLAs refer to
models that are fine-tuned from foundation VLMs using robotic trajectory data, enabling them to
take human instructions and visual observations as input and directly generate robot actions in an
end-to-end manner. In a broader sense, any model that takes both visual and language inputs and
outputs robot actions through an end-to-end pipeline can be considered a VLA model.

## sec:evaluation-2 2.4. Evaluation
_Pages 13-14_

Evaluation Metrics. The most commonly used metric for evaluating robotic performance is the success
rate, which measures whether a given task is completed successfully. For long-horizon tasks [82],
this has been extended to metrics such as average success length, which captures the average number
of consecutive tasks completed within a sequence of up to 𝑛tasks. Beyond success-based measures,
efficiency metrics such as task completion time and action frequency are also employed to assess how
quickly and effectively a robot accomplishes a task. In RL settings, return is also widely used as an
overall measure of performance.
Model Selection. Evaluation strategies vary depending on the experimental setting. A common
approach is to evaluate the model every 𝑘epochs and select the checkpoint with the highest success rate.
Alternatively, for more stable comparisons, one can average the results of the top-𝑛checkpoints from
the final training phase. These strategies are frequently employed in single-task settings. In contrast,
multi-task settings often adopt a simpler approach by reporting performance at the final training
epoch or step, which enables more straightforward and consistent cross-task comparisons. Another
widely used strategy is to select the checkpoint that achieves the highest validation performance for
subsequent testing.
3. Simulators, Benchmarks and Datasets
Simulators, Benchmarks, and Datasets provide the empirical foundation for advancing robotic ma-
nipulation, enabling standardized evaluation, reproducibility, and fair comparison across methods.
They are crucial for assessing generalization, robustness, and scalability in data-driven models. This
section reviews key resources across six major areas: grasping datasets that support perception–pose
learning, single-embodiment manipulation simulators and benchmarks that focus on a specific
robotic embodiment, cross-embodiment simulators and benchmarks that evaluate generaliza-
tion across different morphologies, trajectory datasets that capture multimodal robot interaction
sequences, human video datasets and video-world-model benchmarks that provide large-scale
human interaction data and evaluate predictive visual modeling for embodied control, and embodied
QA and affordance datasets that connect perception with semantic and functional understanding.
3.1. Grasping Datasets
This subsection primarily focuses on grasp detection and generation tasks, where the goal is to predict
viable grasp configurations directly from sensory inputs. While some works explore grasping as a
downstream outcome of broader manipulation objectives, our discussion is centered on methods that
explicitly target grasp prediction rather than those that infer grasps from manipulation trajectories
or task goals. Data annotations are typically categorized into two formats: rectangle-based and
6-DoF-based. The rectangle-based format labels each grasp using a 5-dimensional grasp rectangle
representation, defined by the center position (𝑥, 𝑦), the gripper’s width and height, and the orientation
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Cornell
GraspNet-1Billion
Graspanything
Graspanything++
Give me the eraser.
MetaWorld1
RLbench1
CALVIN1
Robomimic1
Maniskill3
VIMA-Bench1
ARNOLD1
LIBERO1
COLOSSEUM1
SimplerEnv1
GenSim21
VLABench1
RoboEval2
SoftGym3
BEHAVIOR-1K4
HomeRobot4
BiGym5
HumanoidGen5
Robosuite
RoboCasa
Graspanything-6D
Grasping Datasets
VIKI-Bench
Cross-Embodiment Manipulation Simulators and Benchmarks
Single-Embodiment Manipulation Simulators and Benchmarks
RoboTwin2.02
Dex1B
Figure 3 | Overview of simulators and benchmarks. 1Basic Manipulation with Single Arm, 2Basic Ma-
nipulation with Bimanual Arms, 3Deformable Object Manipulation, 4Mobile Manipulation, 5Humanoid
Manipulation.
Table 1 | Summary of grasping datasets.

## sec:dataset Dataset
_Pages 14-17_

Venue
Grasp Type
Scene
#Objects
Domain
Size
Visual Modality
w/ Language
Cornell [83]
ICRA 2011
rect.
single object
real
1035 images, 8019 grasps
RGB-D
Jacquard [84]
IROS 2018
rect.
single object
11k
sim
54k images, 1.1M grasps
RGB-D
GraspNet [85]
CVPR 2020
6-DoF
cluttered
real
97,280 images, ∼1.2B grasps
RGB-D
ACRONYM [86]
ICRA 2021
6-DoF
multi-object
sim
17.7M grasps
RGB-D
Regrad [87]
RA-L 2022
rect. & 6-DoF
multi-object
50K
sim
1.02K images, 100M grasps
RGB-D
MetaGraspNet [88]
CASE 2022
6-DoF
cluttered
sim + real
217k (sim) + 2.3k (real) images
RGB-D
Dexgraspnet [89]
ICRA 2023
dexterous
single-object
sim
1.32M grasps
MetaGraspNet-V2 [90]
TASE 2023
6-DoF
cluttered
sim + real
296k (sim) + 3.2k (real) images
RGB-D
Grasp-Anything [91]
ICRA 2024
rect.
multi-object
syn
1M images, ∼600M grasps
RGB
Grasp-Anything++ [92]
CVPR 2024
rect.
multi-object
syn
1M images, 10M grasps
RGB
Grasp-Anything-6D [93]
ECCV 2024
6-DoF
multi-object
syn
1M images, 200M grasps
RGB-D
Dex1B [94]
RSS 2025
dexterous
single object
sim
1B grasps
GraspClutter6D [95]
RA-L 2025
6-DoF
cluttered
real
52K images, 9.3B grasps
RGB-D
RealVLG-11B [96]
CVPR 2026
rect.
single to cluttered
∼800
real
165K images, 11B grasps
RGB
angle relative to the horizontal axis. In contrast, the 6-DoF format directly annotates the end-effector’s
six-degree-of-freedom pose, including position (𝑥, 𝑦, 𝑧), orientation (e.g., Euler angles or quaternions),
and may also include additional information such as the approach direction and a grasp quality score.
We provide a comprehensive summary of existing grasping datasets in Table 1.
Grasping datasets have undergone significant evolution along several dimensions, each contributing
to the advancement of the field. First, annotation has shifted from manual labeling to model-based
automation, greatly reducing human effort and enabling scalable data generation. Second, the amount
of annotated data has increased from small to large-scale datasets, allowing for more robust and
data-driven learning. Third, grasp representations have evolved from simple 2D rectangles [83, 84,
87, 91, 92, 96] to full 6-DoF [85, 86, 88, 90, 93] and dexterous hand [89, 94, 97, 98] poses, enabling
a more accurate modeling of the complexity inherent in real-world grasping. Fourth, task settings
have expanded from single-object scenarios to multi-object and cluttered environments, offering more
realistic and challenging conditions. Lastly, the input modalities have progressed from purely vision-
based inputs to language-conditioned instructions, facilitating more flexible and semantically rich
manipulation. These changes collectively support the development of generalizable and intelligent
grasping systems.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 2 | Summary of robot manipulation simulators and benchmarks. All benchmarks provide
proprioceptive or pose observations by default, and most include additional modalities.
Name
Venue/Year
Simulator
#Objects
#Tasks
#Demos
Observation
Robot Type
Mani. Type
MetaWorld [99]
CoRL 2019
MuJoCo
Pose
Sawyer
Ba, Uni
Franka Kitchen [100]
CoRL 2020
MuJoCo
Pose
Franka Panda
Ba, Uni
RLBench [101]
RA-L 2020
CoppeliaSim
RGB, D, S
Franka Panda
Ba, Uni
Robomimic [102]
CoRL 2021
MuJoCo
RGB, D
Franka Panda
Ba, Uni
Maniskill [103]
NeurIPS 2021
SAPIEN
100+
30K+
RGB, D, S
Franka Panda
Ba, Uni
CALVIN [82]
RA-L 2022
Pybullet
40M
RGB, D
Franka Panda
Ba, Uni
VLMbench [104]
NeurIPS 2022
CoppeliaSim/[101]
6K+
RGB, D, S
Franka Panda
Ba, Uni
Maniskill2 [105]
ICLR 2023
SAPIEN
30K+
RGB, D, S
Franka Panda
Ba, Mo, Uni, Bi
VIMA-Bench [106]
ICML 2023
Pybullet/Ravens
100+
600K+
RGB, D, S
UR5
Ba, Uni
ARNOLD [107]
ICCV 2023
Isaac Sim
10K+
RGB, D, S
Franka Panda
Ba, Uni
LIBERO [108]
NeurIPS 2023
MuJoCo/[109]
6.5K
RGB, D
Franka Panda
Ba, Uni
COLOSSEUM [110]
RSS 2024
CoppeliaSim/[101]
RGB, D
Franka Panda
Ba, Uni
SimplerEnv [111]
CoRL 2024
SAPIEN
140K+
RGB, D
Google Robot, WidowX
Ba, Uni
GenSim2 [112]
CoRL 2024
SAPIEN
RGB, D
Franka Panda
Ba, Uni
GemBench [113]
ICRA 2025
CoppeliaSim
20+
RGB, D
Franka Panda
Ba, Uni
RoboTwin [114]
CVPR 2025
SAPIEN/[115]
10+
RGB, D, S
Aloha-AgileX
Ba, Bi
GENMANIP [116]
CVPR 2025
Isaac Sim
10K
200K
RGB, D, S
Franka Panda
Ba, Uni
VLABench [117]
ICCV 2025
MuJoCo
2000+
RGB, D
Franka Panda
Ba, Uni
AGNOSTOS [118]
NeurIPS 2025
CoppeliaSim/[101]
3.6K
RGB, D, S
Franka Panda
Ba, Uni
RoboTwin 2 [119]
SAPIEN/[115]
100K
RGB, D, S
Aloha, UR5, Franka, ARX-X5
Ba, Uni, Bi
ROBOEVAL [120]
3K+
RGB, D
Franka Panda
Ba, Bi
INT-ACT [121]
SAPIEN/[111]
60K+
RGB, D
Franka Panda
Ba, Uni
RoboDojo [122]
Isaac Sim
5.3K
RGB
ARX X5, Piper, Piper X
Ba, Bi
TacSL [123]
T-RO 2025
Isaac Gym
RGB, D, T
Franka Panda
Ba, Uni
ManiFeel [124]
Isaac Gym/[123]
RGB, D, T
Franka Panda
Ba, Uni
[11]
RSS 2018
MuJoCo
RGB, D, T
ADROIT Hand
Dex, Uni
TriFinger [125]
CoRL 2021
PyBullet
RGB
3-DoF Hand
Dex, Uni
PlasticineLab [126]
ICLR 2021
Taichi + DiffTaichi
RGB, D, P
Rigid End-Effector
SoftGym [127]
CoRL 2021
NVIDIA FleX
RGB, D, P
Sawyer, Franka
De, Uni
DaXBench [128]
ICLR 2023
DaX
RGB, D, P
DLO-Lab [129]
ICML 2026
Genesis/Taichi
RGB, V
Robot Arm(s) + Parallel Gripper
De, Uni, Bi
ManipulaTHOR [130]
CVPR 2021
Unity/AI2-THOR
2.6K+
RGB, D, N
Kinova Gen3 on Mobile Base
Mo, Uni
HomeRobot [131]
CoRL 2023
AI Habitat
RGB, D
Hello Robot Stretch
Mo, Uni
BEHAVIOR-1K [132]
CoRL 2023
OmniGibson
RGB, D
Mobile Manipulator
Mo, Uni
ODYSSEY [133]
AAAI 2026
Isaac Sim
100+
RGB, D, LiDAR
Unitree Go2 + ARX5
Mo, Quad, Uni
BiGym [134]
CoRL 2024
MuJoCo
10+
RGB, D
Unitree H1
Hu, Bi
HumanoidBench [135]
RSS 2024
MuJoCo
RGB, LiDAR
Unitree H1 + Shadow-Hand
Hu, Bi, Dex
HumanoidGen [136]
NeurIPS 2025
SAPIEN
RGB, D
Unitree
Hu, Bi, Dex
SIMPLE [137]
MuJoCo + Isaac Sim
1.5K+
RGB
Unitree G1
Hu, Bi, Dex
D = depth, S = segmentation, T = tactile sensing, P = particle-based state representations, N = normals
Ba = basic, De = deformable object, Dex = dexterous, Mo = mobile, Quad = quadrupedal, Hu = humanoid manipulation
Uni = single arm, Bi = bimanual arms
3.2. Single-Embodiment Manipulation Simulators and Benchmarks
Single-embodiment manipulation benchmarks focus on a specific type of robotic platform, typically
represented by single-arm manipulators or humanoids equipped with manipulators. For consistency
in categorization, we group single-arm and dual-arm systems under the same embodiment type.
Building on the task taxonomy introduced in Section 4, we provide a comprehensive overview of
existing single-embodiment manipulation simulators and benchmarks in Table 2.
Basic Manipulation Benchmarks. These benchmarks primarily target relatively constrained tabletop
tasks performed by single- or dual-arm manipulators, including pick-and-place, sorting, pushing,
insertion, opening, closing, and pouring. Early benchmarks largely focused on learning task-specific
trajectories through reinforcement learning or imitation learning [99, 100]. More recent efforts have
progressively expanded the evaluation scope toward more demanding settings, including long-horizon
tasks that require sequential execution of multiple manipulation stages [82, 117, 138], language-
conditioned trajectory generation [104, 106, 108], generalization under visual distractions [110, 113,
139] or unseen tasks [121], and robustness to environmental or execution perturbations [140, 141].
Other benchmarks seek to establish fairer and more standardized evaluation protocols for VLA
models [111, 117], while recent platforms increasingly extend evaluation from single-arm settings to
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
more capable bimanual manipulation [114, 119, 142]. In parallel, growing attention has been devoted
to tactile sensing for policy learning and evaluation in contact-rich manipulation tasks [123, 124, 143].
Dexterous Manipulation Benchmarks. Dexterous manipulation benchmarks have progressed from
evaluating individual algorithms and hardware platforms toward broader assessment across tasks
and embodiments. Early work combined deep reinforcement learning with demonstrations to im-
prove high-dimensional skill acquisition [11], while TriFinger provided a reproducible hardware
testbed [125]. More recent benchmarks expand this scope: DexJoCo [144] evaluates task-oriented
dexterous manipulation under diverse settings, whereas DexVerse [145] emphasizes multi-task and
multi-embodiment generalization. Together, they support more systematic evaluation of dexterous
manipulation policies.
Deformable Object Manipulation Benchmarks. Benchmarks for deformable object manipulation
provide environments for evaluating robotic systems on non-rigid materials such as cloth, ropes, fluids,
and elastic objects [126, 127]. DaXBench [128] broadens task and object coverage through differen-
tiable physics, while DLO-Lab [129] focuses on deformable linear objects with material properties,
contact interactions, and topological complexity. RGBench [146] emphasizes physically accurate
garment simulation and systematic measurement of the sim-to-real gap, whereas MoDeSuite [147]
extends deformable-object evaluation to mobile manipulation requiring coordinated base and arm
motion. Together, these benchmarks support more systematic comparison of planning and learning
methods across physical properties, object categories, embodiments, and sim-to-real settings.
Mobile Manipulation Benchmarks. Mobile manipulation benchmarks evaluate systems that integrate
locomotion and manipulation [130–132]. Typical tasks involve coordinating a mobile base (wheeled
or legged) with an onboard manipulator to transport objects, navigate to target locations, and interact
within cluttered or spatially extended environments. These benchmarks are critical for studying
perception, planning, and control challenges faced by embodied agents operating in dynamic and
unstructured settings.
Quadrupedal Manipulation Benchmarks. Wang et al. introduced ODYSSEY [133], a benchmark and
framework for open-world quadruped robots that unifies exploration and manipulation in long-horizon
tasks. By integrating vision-language planning with whole-body control, ODYSSEY addresses key
challenges in instruction decomposition, locomotion–manipulation coordination, and generalization
across diverse open-world scenarios, with validation in both simulation and the real world.
Humanoid Manipulation Benchmarks. Humanoid manipulation benchmarks evaluate whole-body
coordination, dexterity, and stability in tasks involving upper-body manipulation and legged lo-
comotion [134–136]. Recent benchmarks further expand this scope: SIMPLE [137] provides a
scalable simulation testbed for diverse loco-manipulation tasks and policy architectures, while Hu-
manoidArena [148] emphasizes egocentric hierarchical learning and transfer across motion-tracking
controllers. Complementary frameworks such as OASIS [149] and GRAIL [150] improve scalable sim-
to-real learning through simulated teleoperation, reconstructed assets, domain randomization, and
video-generated interaction priors. Together, these efforts support more comprehensive evaluation
and data generation for generalizable humanoid loco-manipulation.
3.3. Cross-Embodiment Manipulation Simulators and Benchmarks
Cross-embodiment manipulation benchmarks support a diverse range of robotic platforms, including
single-arm, dual-arm, mobile, quadrupedal, and humanoid robots. These settings are designed to
evaluate whether a single model can consistently perform similar tasks across robots with varying
morphologies, degrees of freedom, and control constraints. Some benchmarks integrate multiple
embodiment-specific benchmarks, each with different simulator backends and without a unified
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 3 | Summary of cross-embodiment robotic manipulation benchmarks. S denotes segmentation,
T tactile sensing, A audio, L LiDAR, and F force/contact information.
Name
Venue/Year
Simulator
#Objects
#Tasks
#Demos
Observation
#Robots
Manip. Type
RoboSuite [109]
MuJoCo
9 tasks
RGB, D
Ba, Mo, Hu, Quad, Uni, Bi, Dex
CortexBench [151]
NeurIPS 2023
Multiple
17 tasks
850+
RGB, D
Ba, Mo, Uni
RoboHive [152]
NeurIPS 2023
Multiple
17 tasks
850+
RGB, D
10+
Ba, Mo, Quad, Hu, Uni, Bi, Dex
ORBIT/Isaac Lab [154]
RA-L 2023
Isaac Sim
5 types
RGB, D, S
Ba, Mo, Hu, Uni, Bi, Dex
RoboCasa [155]
RSS 2024
MuJoCo/[109]
100 tasks
100K+
RGB, D
Ba, Mo, Hu, Quad, Uni, Bi, Dex
Genesis [156]
Genesis Engine
RGB, D, T, A
Ba, Mo, Hu, Uni, Bi, Dex
ManiSkill3 [115]
RSS 2025
SAPIEN
10K+
12 types
1M frames
RGB, D, S
20+
Ba, Mo, Hu, Uni, Bi, Dex
RoboVerse [153]
RSS 2025
MetaSim
5.5K
276 tasks
500K
RGB, D
Ba, Mo, Hu, Uni, Bi, Dex
AgentWorld [157]
CoRL 2025
Isaac Sim
1000+
RGB, D
Mo, Hu, Uni, Bi, Dex
VIKI-Bench [158]
NeurIPS 2025
[115, 155]
23,737 tasks
RGB, D
Ba, Mo, Hu, Uni, Bi, Dex
GS-Playground [159]
RSS 2026
GS-Playground
3 types
RGB, D, L, F
Ba, Mo, Hu, Quad, Uni
Table 4 | Summary of trajectory datasets.

## sec:dataset-2 Dataset
_Pages 17-18_

Venue/Year
Domain
#Demos
#Verbs
Robot Type
Observation
MIME [160]
CoRL 2018
real
8.3k
Baxter Robot
RGB, D
BridgeData [161]
real
7.2k
WidowX250
RGB, D
BC-Z [162]
CoRL 2021
real
26k
Google Robot
RGB
RT-1 [163]
RSS 2023
real
130k
Google Robot
RGB, D
RH20T [164]
RSSW 2023
real
110k
Flexiv, UR5, Franka
RGB, D, T
BridgeData V2 [165]
CoRL 2023
real
60.1k
WidowX 250
RGB, D
RoboSet [166]
ICRA 2024
real
98.5k
Franka Panda
RGB, D
Open X-Embodiment [167]
ICRA 2024
real
1.4M
22 Embodiments
RGB, D
DROID [168]
RSS 2024
real
76k
Franka Panda
RGB, D
AgiBot World Dataset [169]
IROS 2025
real
1M+
Agibot
RGB, D, T
ARIO [170]
real + sim
AgileX, UR5, Cloud Ginger XR-1
RGB, D, T, A
RoboMind [171]
RSS 2025
real
107k
Franka Panda, Tien Kung, AgileX, UR5
RGB, D
RoboFAC [172]
sim (SAPIEN/ManiSkill)
9.44k
Franka Panda
RGB, D
RoboCOIN [173]
real
180K+
15 Dual-Arm/Humanoid Embodiments
RGB, D
Humanoid Everyday [174]
ICRA 2026
real
10.3k
Unitree G1, H1
RGB, D, L, T
interface [151]. Others consolidate various simulator backends and provide a unified API for consistent
interaction [152, 153]. Additionally, there are benchmarks that rely on a single simulator backend,
within which different embodiments are supported through carefully designed environments [109,
115, 154–157]. We present a comprehensive overview of existing cross-embodiment simulators and
benchmarks in Table 3.
3.4. Trajectory Datasets
Trajectory datasets are structured collections of time-ordered data that capture the sequential states,
actions, and sensory observations of an agent interacting with an environment. In the context of
robotics and embodied AI, these datasets typically include robot joint states, end-effector poses, control
inputs, and multimodal observations (e.g., RGB images, depth maps, force-torque readings) collected
during the execution of specific tasks. In addition to trajectory datasets included in benchmarks, some
works focus on building dedicated datasets that vary in scale, quality, and diversity. These datasets
range from small collections to large-scale repositories with millions of samples, and from low-fidelity
teleoperated data to high-quality expert demonstrations. They also differ in embodiment types,
control modes, and data sources such as human teleoperation, scripted agents, or learned policies.
Many high-quality datasets include semantic labels, task definitions, and multimodal observations,
making them valuable for learning general manipulation policies across tasks and robot types. We
provide a comprehensive summary of existing trajectory datasets in Table 4.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 5 | Summary of embodied QA and affordance datasets.

## sec:dataset-3 Dataset
_Pages 18-20_

Venue
Domain
Size
Visual Perception
Tasks
Spatial Reasoning
Tasks
Functional and
Commonsense
Reasoning Tasks
OpenEQA [175]
CVPR 2024
real
1.6K
Object, Attribute and
Object State
Recognition
Object Localization,
Spatial Reasoning
Functional Reasoning,
World Knowledge
ManipVQA [176]
IROS 2024
real + sim
84K
Physically Grounded
Understanding
Object Detection
ManipBench [177]
CoRL 2025
real + sim
12K+
Keypoint Selection,
Trajectory
Understanding
Fabric Manipulation,
Tool & Drawer Contact
RefSpatial [178]
NeurIPS 2025
real
20M
Object Location,
Orientation and
Topological Reasoning
Robo2VLM [179]
NeurIPS 2025
real
684K+
Scene Understanding,
Multiple View
Object State, Spatial
Relationship
Goal-conditioned
Reasoning, Interaction
Reasoning
PAC Bench [180]
NeurIPS 2025
real + sim
30K+
Properties
Constraints
Affordance
PointArena [181]
real
Pointing
Pointing
3.5. Embodied QA and Affordance Datasets
While EQA and affordance understanding both require visual-semantic and spatial reasoning, EQA
emphasizes high-level question answering based on environmental context, whereas affordance
understanding targets low-level functional interaction with objects, such as grasping or tool use.
These datasets empower robotic models with the ability to perceive and understand the physical
world, and we categorize their capabilities into three core task types. First, Visual Perception
Tasks focus on the static recognition of visual information, enabling robots to identify what an
object is, what color or material it has, and what state it is in (e.g., open or closed). This includes
object recognition, attribute recognition, object state recognition [175], and keypoint selection to
determine actionable locations for manipulation [177]. Second, Spatial Reasoning Tasks involve
understanding object positions, spatial relationships, and reachability. They encompass 2D/3D object
detection [176], object localization [175], and reasoning about spatial relations between the robot and
its environment [178, 179], such as determining the relative direction between a gripper and a target
object. Finally, Functional and Commonsense Reasoning Tasks address the robot’s understanding of
affordances [180] and functional uses [175] of objects—for instance, recognizing that a dish wand
is used for cleaning utensils or that a knife should be grasped by its handle. These tasks bridge
perception with actionable, context-aware behavior grounded in physical interaction knowledge.
Table 5 offers detailed descriptions of representative datasets.
3.6. Human Video Datasets and Video-World-Model Benchmarks
Given the scarcity of robot trajectories, increasing attention has turned to human egocentric videos
as a scalable complementary data source that captures diverse hand-object interactions and offers
valuable priors for learning robot manipulation. Ego4D [182] established a large-scale founda-
tion for first-person activity understanding, while Ego-Exo4D [183] extended this setting with
synchronized egocentric and exocentric views and rich multimodal annotations. More manipulation-
oriented datasets have increasingly incorporated supervision that is directly relevant to robot learning.
EgoDex [184] provides large-scale dexterous manipulation videos with detailed 3D hand trajectories,
and EgoVerse [185] emphasizes diverse human demonstrations and systematic human-to-robot trans-
fer across tasks, scenes, and robot embodiments. Hoi! [186] further connects human and robotic
interaction data through cross-view visual observations, force, torque, and tactile sensing. Collectively,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 6 | Comparison between non-learning and learning-based methods for grasping and manipula-
tion. Here, grasping specifically refers to grasp detection and generation.
Mani. Type
Control Type
Pose Generation
Trajectory Generation
Generalization
Interpretability
& Stability
Grasping
Non-learning
Analytical: geometric rules,
force-closure analysis
IK + motion planning
Low
High
Learning
Learned from data
IK + motion planning
High
Low
Manipulation
Non-learning
Task-specific or predefined
goal pose
IK + motion planning
Low
High
Learning
Learned implicitly via RL
or IL
Learned policies via RL or
High
Low
these datasets shift human video from generic activity understanding toward scalable supervision for
manipulation, although embodiment mismatch, incomplete action labels, and uncertain recovery of
contact dynamics remain important limitations.
In parallel, recent benchmarks have begun evaluating whether video world models capture
interaction dynamics that can support robot execution, rather than assessing generated videos
solely through perceptual quality. Dream.exe [187] converts generated manipulation videos into
robot trajectories and evaluates their execution in simulation, while RoboWM-Bench [188] extends
embodiment-grounded evaluation to both human-hand and robotic manipulation videos. WoW-
World-Eval [189] further introduces an embodied Turing test that evaluates perception, planning,
prediction, generalization, and execution through complementary automatic, human-preference,
and action-execution metrics. Together, these benchmarks shift world-model evaluation from visual
realism toward physical consistency, long-horizon reasoning, and embodied executability.
4. Manipulation Tasks
Early grasping methods primarily focused on identifying stable grasp configurations through geometric
analysis, force closure conditions, or task-specific heuristics. Candidate grasp poses were analytically
generated from object geometry, contact normals, or predefined grasp templates, and then executed
using inverse kinematics (IK) and motion planning. Building on such established grasps, early
approaches to dexterous, deformable, mobile, quadrupedal, and humanoid manipulation typically
assumed a known target pose or a task-specific goal. The emphasis was on optimizing motion
trajectories or control commands to achieve these goals under physical and kinematic constraints,
rather than learning end-to-end action generation from raw sensory input as in modern RL or IL
methods. The comparison is summarized in Table 6.
Among these, basic manipulation is by far the most extensively studied, supported by a rich body
of literature that enables fine-grained categorization of methods. We therefore dedicate Sections 5
and 6 to a detailed discussion of high-level planning and low-level learning-based action modeling
in the context of basic manipulation, while for other task categories we summarize representative
methods within their respective subsections.
4.1. Grasping
In the narrow sense considered in this work, grasping specifically refers to the tasks of grasp detection
and grasp generation. These tasks involve identifying feasible grasp configurations from sensor inputs
such as images or point clouds, allowing robotic end-effectors to securely pick up objects. The primary
focus is on predicting the position and orientation of the gripper to ensure stable and reliable grasps,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
(b) Multimodal Feature Fusion
(c) High-level Planner-Guided
Modular Pipeline
(d) End-to-end Foundation Model
(a) Vision-only-based Methods
Pick up the
lemon/pan
Grasp Foundation Model
Mapping or
Generative Model
Image
Encoder
Text
Encoder
Fusion
Decoder
Grasp

## sec:model Model
_Pages 20-67_

High-level
Planner
Planning & Grounding
filter
Figure 4 | Comparison of different grasping methods. (a) Vision-only approaches, which map visual
inputs to grasp poses using CNNs or spatial transformers, or generate poses via VAEs or diffusion
models. With the introduction of language, three main categories emerge: (b) fusion of language
and visual features through mechanisms such as cross-attention; (c) generation of multiple grasp
candidates using pretrained grasp models, followed by selection with high-level planners (e.g., LLMs,
VLMs, or 3D representations); and (d) end-to-end fine-tuning of grasp foundation models on large-
scale grasping datasets. Figure adapted from [199].
even in the presence of diverse object shapes, varying poses, and cluttered environments.
Non-Learning-Based Grasp. Early methods generate grasp poses by explicitly analyzing object
geometry [190], performing contact-driven force analysis [191], or applying task-specific rules [192],
in combination with the gripper model. However, due to their limited generalization ability in handling
complex shapes, occlusions, and unseen objects, these approaches have gradually been replaced by
data-driven, learning-based methods, as discussed below. The taxonomy of learning-based grasping
approaches is illustrated in Figure 4.
Rectangle-based Grasp. Grasping rectangles were first introduced by Jiang et al. [83]. While they are
visually similar to bounding boxes, their representational semantics are fundamentally different. A
grasping rectangle is defined as a 5-dimensional representation, as previously described in Section 3.1.
Subsequent methods have progressively incorporated deep learning techniques, ranging from basic
convolutional neural networks (CNNs) [193–195] to more advanced architectures such as ResNet [71],
GR-ConvNet [196] and Transformer [197], and further to CLIP-based models that integrate textual
information through feature fusion methods [198]. More recently, diffusion models have also been
employed [92]. Over time, the models have evolved from simple to complex, and the modalities have
shifted from unimodal to increasingly multimodal.
6-DoF Grasp. Two-dimensional rectangle-based representations, which typically assume parallel-jaw
grippers executing top-down grasps, are limited to 2 or 3 degrees of freedom (DoF). This restricts the
gripper’s orientation and reduces applicability in unstructured or complex environments. To address
these limitations, researchers have proposed 6-DoF grasp representations [200] that define a grasp as
a 6-dimensional pose in 3D space. This formulation enables the robot to grasp objects from arbitrary
orientations, improving flexibility and robustness. The 6-DoF representation is especially beneficial in
cluttered scenes, non-planar object poses, and scenarios involving complex geometries.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Apart from a few early 2D-based approaches [201], the majority of recent methods adopt 3D
representations. In particular, methods based on point cloud inputs have explored a wide range
of architectures, ranging from mapping convolutional networks [202] and transformer-based mod-
els [203], to generative autoencoders [200], variational autoencoders [204, 205], and UNet-style
frameworks [206]. To improve efficiency, various methods have been proposed, including applying in-
stance segmentation or heatmap to focus on task-relevant manipulation regions [207, 208], reducing
the grasp search space by representing grasp poses with contact points on the object surface [209],
incorporating graph neural networks for geometric reasoning on point cloud data [210], and adopting
an economic supervision paradigm that selects key annotations and leverages focal representation
to reduce training cost and improve performance [211]. Some works further address structural
distortions commonly found in real-world point cloud data by introducing completion or denoising
modules to convert the input into a clean and consistent style [212, 213]. Several methods also
address the SE(3)-equivariance problem [214, 215] by modeling grasp generation as a continuous
normalizing flow over SE(3) with equivariant vector fields, or by predicting per-point grasp quality
over the orientation sphere using spherical harmonic basis functions. Meanwhile, several methods
also leverage 3D representations such as SDF [216–218], NeRF [219, 220], and 3DGS [221–223] to
extract geometric features or to sample grasp points for downstream prediction.
Language-driven Grasp. In recent years, language-driven grasping has gained increasing attention,
aiming to achieve object-specific and instruction-guided manipulation. Existing approaches can be
broadly categorized into three groups. The first adopts multimodal feature fusion [224, 225], where
textual and visual modalities are jointly encoded, often via cross-attention mechanisms. The second
leverages existing grasp models to generate large numbers of grasp candidates, followed by ranking or
scoring with LLMs or VLMs to select the most confident grasps. For instance, LLMs can generate task-
specific descriptions [226], while VLMs are used for visual grounding to compute grasp confidence
scores [227, 228]. Representative methods include VL-Grasp, which employs VLMs to attend to
the target object and generate grasps [229]; OWG, which leverages VLM-based semantic priors for
planning under occlusion [230]; and Reasoning-Grasping, which integrates visual-linguistic inference
for improved object-level understanding [231]. Other efforts adapt MLLMs for environment-aware
error correction [232], or learn object-centric attributes to enable rapid grasp adaptation across
tasks [233]. Affordance-driven approaches also ground grasp generation in language and vision
cues [234–236]. The third line of work directly fine-tunes MLLMs on grasp foundation models with
large-scale grasp datasets [199, 237].
Challenges. Firstly, the aforementioned grasp detection and generation methods were originally de-
signed for 2-DoF parallel-jaw grippers. However, with the increasing use of dexterous hands, research
has shifted toward dexterous grasping, which requires complex annotations such as hand joint angles
and contact force maps. To handle the high dimensionality of this task, various generative approaches,
including diffusion-based models, have been proposed [238–240]. Some approaches represent grasp
configurations via contact points or maps [241], or leverage interaction-based representations such
as D(R, O) [242] to infer grasps from geometric relationships. Second, traditional grasping strategies
typically rely on a single end-effector, such as suction or parallel grippers, which limits adaptability
to diverse object geometries. To address this, several works have explored bimanual grasping using
dual-arm or dual-gripper configurations [243, 244]. Lastly, grasping transparent objects remains a
significant challenge, as depth sensors often fail to detect or localize such materials accurately. Recent
efforts address this limitation by incorporating alternative modalities, such as LiDAR [245] or 3D
reconstruction [246–248], to infer the geometry of transparent or reflective objects.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 7 | Representative methods across manipulation types and learning paradigms.
Mani. Type
RL+IL
VLA
Basic
See Table 8
See Figure 15
See Table 9
See Figure 17
Dexterous
PDDM [249],
[11], [250]
DexHandDiff [251],
CordViP [252]
REBOOT [253],
ViViDex [254]
OFA [255], LBM [256]
Soft Robotics
[257], [258]
Soft DAgger [259],
KineSoft [260]
SS-ILKC [261]
Deformable Object
[262]
DeformerNet [263],
DexDeform [264]
DMfD [265]
𝜒0 [266]
Mobile
[267],
MoMa [268]
MOMA-Force [269], Skill
Transformer [270]
[271]
MoManipVLA [272]
Quadrupedal
VBC [273],
GAMMA [274]
Human2LocoMan [275]
[276], WildLMa [277]
QUAR-VLA [278],
GeRM [279]
Humanoid
[280],
FLAM [281]
OmniH2O [282], iDP3 [283]
[284]
GR00T N1 [285],
Humanoid-VLA [286]
4.2. Basic Manipulation
Basic manipulation refers to relatively simple tabletop tasks performed by single- or dual-arm ma-
nipulators, such as pick-and-place, sorting, pushing, inserting, opening, closing, and pouring. Most
current research remains focused on this category, as illustrated in Figure 12 and further discussed in
Sections 5–6, where the majority of methods and benchmarks are developed around object-centric
interactions in structured environments. While these sections classify approaches within the scope of
basic manipulation, the proposed taxonomy is general in nature and can be readily extended to other
categories of manipulation tasks.
4.3. Dexterous Manipulation
Dexterous manipulation refers to the capability of robotic systems equipped with multi-fingered or
anthropomorphic hands to achieve precise and coordinated object control through complex contact
interactions. It involves in-hand reorientation, fine force modulation, and multi-point contact, enabling
actions such as twisting, grasping, and rotating, as illustrated in Figure 5. This capability is critical for
tasks requiring high precision and adaptability, such as tool use, assembly, and manipulation of small
or irregular objects. Human hand models typically include 20–25 DoF, with each finger modeled by 4
DoF, the thumb by 4–5 DoF, and additional DoF from the palm and wrist for enhanced realism [287].
Rotate
Spin & Roll
Pour
Open
Grasp
Insert
Figure 5 | Tasks in dexterous manipulation, fig-
ure adapted from [249, 250, 288–290].
Non-Learning-Based Methods. Early work on
dexterous manipulation predominantly employed
non-learning approaches, including optimization-
and control-based techniques such as heuristic
search and constrained optimization [291]. These
methods typically assume access to known dy-
namics and object models, and focus on trajectory
planning under physical constraints.
Learning-Based Methods. With the advent of
RL, both model-based and model-free paradigms
have been applied to dexterous manipulation.
Model-based methods such as PDDM [249] ex-
ploit learned dynamics for efficient planning and
control, while model-free approaches directly op-
timize policies through interaction [11], sometimes combined with few-shot imitation to accelerate
adaptation to real hands [250]. More recently, human-in-the-loop frameworks such as HIL-SERL [292]
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
integrate demonstrations, online corrections, and reinforcement learning for sample-efficient acquisi-
tion of precise skills on physical robots. DexScrew [293] further addresses imperfect simulation by
first learning transferable finger-motion primitives with RL in simplified environments, then using
these primitives to collect real multisensory demonstrations for tactile-conditioned behavior cloning.
IL has gained attention for its data efficiency, exemplified by DexMV [294], which employs
kinematic retargeting from human videos to robot hands. Extensions incorporate auxiliary supervision
such as contact prediction [251, 252] and inverse dynamics modeling [295], improving generalization
and action consistency. SAT [296] instead represents an action chunk as a variable-length sequence
of joint-wise trajectories and incorporates joint-level functional and kinematic priors, enabling 3D
dexterous policy learning across heterogeneous hand embodiments. Hybrid IL–RL approaches combine
these strengths, typically using IL for policy initialization followed by RL refinement [297, 298].
DexMV [294] instead translates human videos into robot demonstrations for imitation learning,
whereas ViViDex [254] first performs RL in a privileged state space and subsequently distills the
resulting policy through IL.
Recent VLA models expand task and embodiment generalization. DexGraspVLA [299] integrates
semantic reasoning with diffusion-based policies for grasping in cluttered scenes, while OFA [255],
LBM [256], and Being-H0 [300] leverage multimodal prompts or human videos to generate dexterous
motions and follow language instructions. UniDex [301] transforms egocentric human videos into
robot-centric trajectories and introduces a function-aligned action space to support unified control
across heterogeneous dexterous hands. Dexora [302] extends VLA modeling to high-dimensional dual-
arm and dual-hand manipulation, combining embodiment-matched simulated and real demonstrations
with quality-aware training to reduce the influence of noisy teleoperation data.
Human guidance provides another supervision source: Chen et al. [303] use object and wrist
trajectories from videos to guide RL, and Mandi et al. [304] introduce functional retargeting to
transition from demonstrations to autonomous control. Affordance reasoning further supports grasp-
specific strategies [305, 306], guiding object selection under semantic constraints. Finally, recent
works emphasize robustness and autonomy. Task decomposition reduces complexity by structuring
subtasks [307], while recovery mechanisms such as REBOOT [253] introduce IL-trained reset policies
to handle failures in long-horizon settings.
Challenges. Beyond high-dimensional control and contact dynamics, dexterous manipulation faces
broader challenges. First, many real-world tasks are long-horizon and compositional, requiring
sequential execution of fine-grained skills. Chen et al. [289] address this by decomposing tasks into
discrete skills trained with RL and linking them via a high-level policy. Second, sim-to-real transfer
remains a bottleneck due to discrepancies in perception, dynamics, and actuation. CyberDemo [290]
mitigates this through data augmentation, improving robustness under domain shift. Third, accurate
perception is difficult in cluttered or partially observed scenes, where occlusion hampers object
tracking. DexPoint [288] leverages point cloud completion to recover missing geometry and enhance
spatial awareness.
4.4. Soft Robotic Manipulation
Soft manipulators, built with compliant materials or structures, are well-suited for human–robot
collaboration, operation in uncertain environments, and safe, adaptive grasping, as illustrated in
Figure 6. They overcome the limitations of rigid manipulators when handling delicate or deformable
objects [308]. To this end, a wide range of designs have been developed to support diverse applica-
tions [34, 35, 309–311].
Non-Learning-Based Methods. For soft manipulator control, analytical kinematic models based on
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
the constant-curvature assumption map shape parameters to end-effector poses via virtual rigid-link
chains and Denavit–Hartenberg transformations [312]. Similarly, three-dimensional continuum
manipulators can be approximated as rigid-jointed robots, with computed-torque control achieving
closed-loop dynamics [313]. Other approaches employ model predictive control with Koopman
operators [314, 315], or rely on accurate Lagrangian models combined with adaptive dynamic sliding
mode control to enhance robustness [316]. Hybrid schemes also integrate learning into non-learning
frameworks: forward dynamics can be approximated with machine learning and combined with
trajectory optimization for open-loop control [317], while feedback-driven strategies exploit learned
models to stabilize and restore system states [310].
Pick & Insert
Unscrew
Move
Grasp
Flick Lid
Grasp Fabric
Figure 6 | Tasks in soft robotic manipulation,
figure adapted from [35, 260, 318].
Learning-based Methods. RL and IL have
been widely applied to soft manipulator control.
Model-free RL avoids explicit physical modeling by
training policies in simulation for closed-loop end-
point control [318]. Forward dynamics learned
with recurrent networks can be integrated into
trajectory optimization to generate samples and
train predictive controllers [257], while LSTM-
based dynamics models enable feedback policy
learning [319]. Domain randomization combined
with incremental offline training has improved
task-space accuracy and adaptability [258], and
wavelet-based dynamics approximations paired
with LSTM and TD3 controllers further enhance
generalization under variability [320]. IL approaches include Soft DAgger [259], which employs
dynamic behavior mapping for online expert-like action generation, and KineSoft [260], which inte-
grates kinesthetic teaching with diffusion-based policy learning. Hybrid methods also emerge, such as
SS-ILKC [261], which combines multi-objective RL with adversarial IL to learn goal-directed control
strategies in sensor space, supported by sim-to-real pre-calibration for zero-shot transfer.
Challenges. Soft-hand-based manipulation faces several challenges, including modeling highly
nonlinear and underactuated dynamics, achieving precise force and pose control with deformable or
fragile objects, ensuring robustness under environmental uncertainty and sensor noise, and lowering
the cost and complexity of data collection and teleoperation for policy training. To improve sample
efficiency, Soft DAgger [259] enables online imitation learning from limited demonstrations through
dynamic behavior mapping. To reduce hardware complexity in teleoperation, Liu et al. [311] propose
a flexible bimodal sensory interface that combines vision-based perception with wearable sensors,
enabling intuitive and low-cost control without bulky equipment.
4.5. Deformable Object Manipulation
Deformable object manipulation (DOM) requires robots to perceive and control non-rigid objects
whose shapes vary under applied forces. Unlike rigid-body manipulation, it demands reasoning
over high-dimensional, continuous state spaces, coping with uncertain deformation dynamics, and
interpreting subtle visual or tactile cues. As illustrated in Figure 7, tasks such as cloth folding, rope
and cable tying, and food handling involve diverse deformations—including tension, compression,
and bending—making DOM a complex yet crucial challenge in robotic manipulation [16, 321, 322].
Non-Learning-Based Methods. Traditional approaches to DOM, such as path planning [323]
and model-based control [324], often rely on simplified physical models or analytical solutions.
However, these methods typically struggle with generalization and real-time adaptability in complex
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
environments, leading to a shift toward data-driven techniques such as RL, IL, and hybrid learning-
control frameworks.
Shape the Plasticine
Open the Bag
Folding Clothes
Untie the
Knotted Cable
Figure 7 | Tasks in deformable object manipula-
tion, figure adapted from [325–328].
Learning-based Methods. Jan et al. [262] pro-
pose a deep RL method based on a modified DDPG
algorithm that learns from visual and robot state
inputs and achieves zero-shot sim-to-real transfer
via domain randomization. In contrast, IL meth-
ods exploit demonstrations: DexDeform [264] ex-
tracts latent skills from human demonstrations
and fine-tunes them with limited robot data, De-
fGoalNet [329] predicts goal configurations from
few-shot demonstrations conditioned on state and
context, and MPD [330] generates movement
primitives with diffusion models. To combine both
paradigms, DMfD [265] incorporates expert data
into RL through advantage-weighted BC loss, expert-initialized replay buffers, and reset-to-state
initialization, achieving efficient policy optimization.
Beyond learning paradigms, DOM has explored diverse strategies spanning geometric modeling,
affordance prediction, and structure-aware perception. DeformGS [331] represents deformable objects
with canonical Gaussians and learns a time-conditioned deformation field for temporally consistent 3D
pose tracking. Affordance-based approaches include DeformerNet [263], which predicts end-effector
displacements from partial point clouds, Foresightful Affordance [332], which integrates dense per-
pixel affordances with long-horizon value estimation, and APS-Net [328], which ranks standardized
folding and flattening trajectories guided by affordance heatmaps. Language-conditioned affordance
prediction has also been explored [333]. Finally, estimating object-specific physical properties has
emerged as a complementary direction [334, 335]. GenDOM [335] learns a parameter-conditioned
policy and leverages a single human demonstration with differentiable simulation to infer unseen
object properties, enabling generalization to novel deformable instances.
Challenges. Deformable objects lack a fixed pose, and key deformation regions are often occluded
during manipulation. To improve visibility and perception, recent work jointly optimizes camera and
manipulator motion, guided by structure-of-interest cues [327]. Deformation dynamics also exhibit
delayed responses, complicating real-time control; this is addressed by encoding states into latent
spaces and predicting their dynamics. For example, DeformNet [336] encodes object geometry with
PointNet and a conditional NeRF, and models temporal evolution with a recurrent state-space model
for latent-level MPC. An even greater challenge is modeling topological changes. DoughNet [337]
extends latent-space modeling to jointly capture geometric and topological variations from point
clouds, enabling long-horizon planning with CEM for tool selection and manipulation.
4.6. Mobile Manipulation
Mobile manipulation is a robotic paradigm that combines navigation and manipulation capabilities
within a single system. It allows robots to physically interact with objects beyond a fixed workspace
by actively navigating the environment. This integration poses significant challenges in perception,
planning, and control, as it requires coordinating whole-body motion, handling long-horizon tasks, and
dealing with dynamic, partially observable scenes. Several studies have focused on designing robots
specifically for mobile manipulation [37, 338, 339]. As illustrated in Figure 8, mobile manipulation is
critical for real-world applications such as household assistance, warehouse automation, and service
robotics [17].
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Non-Learning-Based Methods. Traditionally, mobile manipulation is decomposed into two separate
problems: navigation and manipulation. Navigation is typically handled by classic path planners, such
as grid-based methods (e.g., Dijkstra) and sampling-based planners (e.g., RRT). Manipulation is often
addressed using grasp models, motion primitives, or trajectory planning based on point clouds. Some
control methods perform joint optimization of navigation and manipulation. For example, Berenson
et al. [340] optimize full-body configurations and grasp poses simultaneously, then plan motions via
sampling. Chitta et al. [341] coordinate base-arm planning with ROS-based navigation and point
cloud grasping. Others embed manipulation goals directly into MPC cost functions [342].
Load Laundry
Open Fridge
Cook Shrimp
Wipe Countertop
Take out Trash
Clean the room
Push Chairs
Open Cabinet
Drawer
Rotate Tap
Open washer
Figure 8 | Tasks in mobile manipulation, figure
adapted from [37, 269, 343, 344].
Learning-based Methods. These methods have
emerged to learn policies for whole-body control.
For RL, Wang et al. [345] use RGB-D inputs to
estimate object pose and train a policy that jointly
predicts base velocity, arm trajectories, and grip-
per actions. HarmonicMM [346] extends this by
integrating visual and pose information into a
unified RL framework, while Wu et al. [267] pro-
pose spatial Q-value learning at the map level for
navigation guidance. To improve reward signals,
Honerkamp et al. [347] design dense rewards
based on end-effector reachability, and Causal
MoMa [268] introduces causality-aware model-
ing of control–reward relations to stabilize policy
optimization. For IL, MOMA-Force [269] learns
motion and force policies from visual-force demonstrations, while HoMeR [344] decomposes tasks
into global keypose prediction and local refinement to map end-effector targets to whole-body actions.
Wang et al. [348] leverage SAM2-based perception for object-centric IL, and Skill Transformer [270]
treats manipulation as a skill prediction problem, learning both skill categories and corresponding
low-level actions. Hybrid methods combine IL with RL to enhance generalization. For example, Xiong
et al. [271] initialize policies via behavior cloning and refine them through online RL to handle unseen
articulated objects.
Beyond learning paradigms, recent work integrates high-level reasoning and multimodal rep-
resentations. VLA-based methods such as MoManipVLA [272] process multimodal instructions to
predict end-effector waypoints while delegating base motion to a trajectory optimizer. LLM-driven
frameworks, including MoMa-LLM [349] and SayPlan [350], combine open-vocabulary language,
scene graphs, and reasoning for object search and high-level task planning. Complementary efforts in
3D scene modeling guide manipulation through active perception: ActPerMoMa [351] optimizes view-
point selection and grasp reachability via incremental TSDF mapping, while TaMMa [352] employs
sparse Gaussian localization and depth completion to generate accurate target poses.
Challenges. In addition to perception–action coordination, dynamic obstacles, and long-horizon
decision-making, mobile manipulation faces several additional challenges. A first challenge is enabling
effective human–robot collaboration. Ciocarlie et al. [353] developed an assistive system that combines
user interfaces, shared control, and autonomy to transform a PR2 robot into an in-home assistant.
Extending this line of work, Robi Butler [354] introduces a closed-loop household control framework
that supports multimodal interaction, where high-level planners such as LLMs and VLMs enable
natural language and gesture-based commands for intuitive and remote collaboration. A second
challenge is real-time manipulation during navigation, where robots must coordinate mobility and
manipulation under environmental constraints. Whole-body motion control frameworks [355, 356]
address this problem by enabling reactive planning and execution for on-the-move manipulation.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
4.7. Quadrupedal Manipulation
Quadrupedal manipulation is an emerging paradigm that combines the agile mobility of quadruped
robots with the ability to physically interact with objects. Unlike traditional manipulators or mobile
bases, quadrupeds can traverse complex and unstructured terrains while maintaining dynamic stability,
making them particularly suitable for applications such as search and rescue, field robotics, and
autonomous exploration. Representative tasks are illustrated in Figure 9. Manipulation can be
realized through several embodiments: whole-body loco-manipulation [278, 279, 357–360]; leg-as-
manipulator designs that repurpose one or more legs for interaction [276, 361, 362]; back-mounted
arms [273, 274, 363–374]; and grippers integrated into front legs for simultaneous locomotion and
manipulation [375]. Each embodiment introduces unique challenges in whole-body coordination,
dynamic control, and perception-driven planning.
Pick & Place
Write
Press Button
Press Switch
Push
Wave Ribbon
Figure 9 | Tasks in quadrupedal manipulation,
figure adapted from [133, 362, 370, 371, 374].
Non-Learning-Based Methods.
Recent ad-
vances in quadrupedal manipulation have ex-
plored diverse control strategies, ranging from
model-based optimization to learning-based ap-
proaches. Optimization-based methods provide
interpretable and physically grounded control
with strong task generalization.
For example,
Arcari et al. [365] combine MPC with Bayesian
multi-task error learning for real-time dynamics
adaptation. Wolfslag et al. [363] incorporate SUF
stability metrics and contact constraints into a
quadratic programming framework for robust,
support-leg-aware planning, a concept further extended by RoLoMa [366] to improve trajectory robust-
ness. LocoMan [375] demonstrates a hardware–control co-design approach, equipping quadrupeds
with lightweight front-leg manipulators and employing unified WBC to achieve agile locomotion and
precise manipulation.
Learning-based Methods. In the realm of RL, recent research has focused on developing structured
and informative control representations. Jeon et al. [357] introduce a hierarchical RL framework that
encodes interaction experience, robot morphology, and action history into latent representations to
facilitate effective policy learning. Fu et al. [364] decouple leg and arm rewards in the policy-gradient
formulation to enhance coordination between locomotion and manipulation, while Zhi et al. [373]
present a unified force-position controller that estimates forces from perception instead of sensors. Hou
et al. [374] incorporate explicit arm kinematics and feasibility-based rewards to promote physically
plausible behaviors. Two-stage training schemes have also been explored: RoboDuet [372] sequen-
tially trains locomotion and arm policies with reward adaptation for coordination. GAMMA [274]
improves grasp precision by conditioning policies on grasp poses, while Wang et al. [371] propose
GORM, a metric for grasp reachability under varying base poses, to guide base movement for effective
grasping. Teacher-student frameworks further advance base-arm coordination, as in VBC [273] and
Jiang et al. [370], where visual or pose-tracking guidance is distilled into student policies. SLIM [376]
extends this paradigm to long-horizon pick-and-place by progressively expanding a privileged teacher
across task stages and distilling it into an egocentric visuomotor policy through RL. Other works
combine hierarchical and hybrid designs, such as HiLMa-Res [358], which uses high-level RL to
control Bézier parameters and base motion while relying on hybrid CPG-Bézier controllers for leg
movements, and Pedipulate [362], which demonstrates end-to-end RL for single-foot manipulation.
HeLoM [377] further develops hierarchical whole-body RL for hexapod robots, using a high-level
planner to specify pushing commands and foreleg targets and a low-level controller to coordinate
locomotion, balance, and forceful object interaction.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
In the IL domain, Human2LocoMan [275] enables cross-embodiment transfer from XR-driven
human demonstrations using a modular Transformer policy, effectively transferring human manipula-
tion skills to quadrupeds. Hybrid IL–RL frameworks further improve efficiency and generalization.
He et al. [276] employ BC to train a high-level planner for grasp trajectories, while a low-level RL
controller coordinates locomotion and single-leg manipulation. WildLMa [277] builds an IL-based
skill library from VR demonstrations and sequences these skills under LLM guidance.
VLA-based frameworks have also emerged for high-level semantic reasoning. QUAR-VLA [278]
pioneers the application of VLA models to quadrupeds, while GeRM [279] and MoRE [360] inte-
grate mixture-of-experts architectures with offline RL to learn generalist visuomotor policies and
Q-functions with enhanced generalization and decision quality. QUART-Online [378] advances this
line by introducing action-chunk discretization and semantic alignment training, enabling latency-free
inference for quadrupedal VLA tasks.
Finally, advances in 3D semantic perception and high-level planning extend quadrupedal capabil-
ities. GeFF [368] performs real-time NeRF-based reconstruction with semantic relevance fields to
guide locomotion, while manipulation is executed via learned grasp models. At the task level, LLMs
have been combined with policy libraries: Ouyang et al. [359] propose a hierarchical framework
where LLMs parse long-horizon, multi-skill instructions into structured subgoals executed by RL-based
skills, bridging symbolic reasoning and continuous control.
Challenges. In addition to common challenges such as balance–manipulation coupling, terrain
adaptability, and perception delays, real-world deployment remains difficult due to the sim-to-real gap
caused by modeling inaccuracies and sensor noise. To mitigate this, fully autonomous RL pipelines
have been developed. Mendonca et al. [369] propose a framework that integrates on-policy data
collection with continuous training, while ASC [367] addresses long-horizon tasks by decomposing
them into modular skills trained via RL, coordinating them through a skill-switching policy jointly
trained with IL and RL, and introducing a corrective policy to improve robustness during deployment.
Long-horizon task execution itself poses another significant challenge. Cheng et al. [361] propose a
stage-wise RL framework that independently learns locomotion and single-leg manipulation skills,
which are later composed via a behavior tree to accomplish temporally extended tasks.
4.8. Humanoid Manipulation
(a) Manipulation
(b) Navi-Manipulation
Pick
Pick & Place
Play Piano
Water Plants
(c) Loco-Manipulation
Box Loco-
Manipulation
Play Ping Pong
Squat & Pick
& Place
Figure
Tasks in humanoid manipu-
lation, categorized into manipulation [280,
283, 379], navi-manipulation [380], and loco-
manipulation [379, 381, 382].
Humanoid manipulation involves robotic plat-
forms with human-like morphology, typically com-
prising a torso, two arms, and either simplified
2-DoF grippers or fully dexterous hands, with loco-
motion provided by a mobile base or bipedal legs.
Designed for object interaction in human-centered
environments, these systems aim to replicate or
extend human manipulation capabilities through
tasks such as grasping, lifting, tool use, and co-
ordinated bimanual operation, as illustrated in
Figure 10. Although humanoid morphology of-
fers natural compatibility with tools, workspaces,
and infrastructures designed for humans, it also
introduces substantial challenges in balance main-
tenance, whole-body coordination, and fine motor
control, making humanoid manipulation a central
topic in robotics and embodied intelligence.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Non-Learning-Based Methods. Early humanoid
control primarily relied on traditional approaches such as rule-based and analytical controllers [383,
384]. Some works also explored the integration of learning-based models into control frameworks.
For example, OKAMI [385] leverages 3D human pose estimation from a single human video to infer
joint positions and derive executable actions for humanoid robots via inverse kinematics.
Learning-Based Methods. Recent humanoid manipulation research has shifted from hand-engineered
control stacks toward learning-based systems spanning RL, IL, hybrid RL–IL, VLA, and world-action-
model paradigms [18]. In RL, FLAM [281] uses a pretrained human-motion model to score pose
stability as an auxiliary reward, while Xie et al. [280] combine diffusion-based motion generation
with RL for whole-body manipulation. OmniRetarget [386] further preserves robot–object and
robot–environment interactions when retargeting human demonstrations into kinematic references
for RL. In IL, TRILL [387] maps RGB observations to pose commands, OmniH2O [282] unifies
goals from language, vision, motion capture, and VR, and iDP3 [283] adapts diffusion policies to
egocentric whole-body control. Other methods leverage large-scale egocentric demonstrations [381],
tactile feedback [388], or data augmentation from a single demonstration [389]. MimicDroid [390]
meta-trains an in-context policy from human play videos for few-shot adaptation. Hybrid RL–IL
methods combine efficient supervision with feasible execution, as in André et al. [284], who train a
mid-level trajectory generator with IL and a low-level whole-body tracker with RL.
VLA methods jointly ground language and visual observations in coordinated locomotion and
manipulation. HumanVLA [391] separately encodes images and language, while GR00T N1 [285]
fuses visual and tokenized language features through a VLM and predicts actions with a diffusion
head. Humanoid-VLA [286] aligns language and action representations via cross-attention. Traj-
Booster [382] uses dual-arm end-effector trajectories to transfer wheeled-humanoid demonstrations to
bipedal whole-body control. WholeBodyVLA [392] learns latent representations from action-free ego-
centric videos and decodes them into arm and locomotion commands. Ψ0 [393] adopts staged training
with egocentric videos and humanoid trajectories, while HEX [394] leverages humanoid-aligned
states and expert-routed proprioceptive prediction for cross-embodiment learning. OpenHLM [395]
further studies teleoperation interfaces, action-space design, and heterogeneous co-training for
whole-body-native VLAs. Beyond conventional VLAs, MotionWAM [396] incorporates intermediate
denoising features from a video world model and predicts unified whole-body motion tokens spanning
locomotion, torso motion, height regulation, foot interaction, and hand manipulation. This direction
seeks to combine visual dynamics priors with real-time whole-body action generation.
Challenges. In addition to challenges such as multimodal perception, balance–manipulation coupling,
and high degrees of freedom, humanoid manipulation also struggles with enabling multi-agent
collaboration. For instance, CooHOI [397] exploits object dynamics as an implicit communication
channel to achieve coordinated manipulation across multiple agents. To further address the sim-to-real
gap, Lin et al. [398] introduce a generalizable reward formulation and a decoupled RL architecture,
which improve sample efficiency through staged training.
4.9. Aerial Manipulation
Aerial manipulation combines the mobility of unmanned aerial vehicles with robotic end-effectors,
such as grippers or articulated arms, to enable physical interaction beyond the reach of ground-based
platforms. Representative tasks include aerial grasping, object transportation, pick-and-place, tool
use, surface interaction, and infrastructure maintenance. Unlike fixed-base manipulation, aerial
manipulation must coordinate flight and manipulation while maintaining stability under arm motion,
contact forces, and payload changes. Its floating-base dynamics, limited onboard sensing and
computation, and strict payload constraints therefore create distinctive challenges for perception,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
planning, and action modeling.
Pick and Place
Writing
Pick
Figure 11 | Tasks in aerial manipulation, figure
adapted from [399–401].
Non-Learning-Based Methods. Early aerial ma-
nipulation systems primarily relied on analytical
modeling, motion planning, and model-based con-
trol. Pounds et al. [402] studied hovering capture
and load stability during aerial grasping, while
Kim et al. [403] modeled a quadrotor and a 2-DoF
arm as a coupled system and designed an adap-
tive sliding-mode controller for autonomous object
transportation. Orsag et al. [404] further orga-
nized aerial manipulation according to momen-
tary, loose, and strong environmental coupling,
demonstrating tasks such as pick-and-place, inser-
tion, and valve operation. More recent systems extend these foundations toward greater workspace
and robustness. Lee et al. [405] combine geometric robust control with optimization-based whole-
body planning, allowing an omnidirectional aerial manipulator to operate at arbitrary poses in SE(3).
FlyAware [406] instead addresses payload-dependent dynamics through vision-based pre-grasp inertia
estimation and post-grasp adaptive control.
Learning-Based Methods. Learning-based aerial manipulation has gradually expanded from task-
specific RL and demonstration-based learning toward general-purpose VLA systems. In RL, Dimmig
and Kobilarov [407] jointly learn a world model and interaction policy for non-prehensile aerial
manipulation under unknown object dynamics. Swooper [408] adopts a two-stage deep RL strategy
that first learns flight control and subsequently coordinates high-speed flight with active gripper
control using a unified lightweight policy. Demonstration-based approaches reduce the cost and risk
of direct interaction during policy acquisition. Zito and Ferrante [409] learn transferable contact
distributions from a single demonstration to identify attachment points on unseen payloads. Flying
Hand [401] introduces an end-effector-centric interface that combines whole-body model predictive
control with intuitive teleoperation, enabling imitation policies to learn diverse tasks including writing,
insertion, pick-and-place, and tool interaction.
VLA models seek to unify semantic understanding, long-horizon reasoning, flight, and manip-
ulation. AIR-VLA [400] establishes an aerial-manipulation benchmark and multimodal dataset
covering spatial understanding, base motion, manipulator control, and multi-stage task execution.
AirVLA [399] investigates the transfer of a manipulation-pretrained 𝜋0 model to aerial pick-and-place,
using synthetic navigation data and payload-aware guidance to address data scarcity and the mis-
match between fixed-base and aerial dynamics. AIR-VLA+ [410] separates UAV movement from arm
manipulation through cascaded action decoders and an asymmetric mixture-of-experts architecture,
reducing interference between coarse platform motion and precise end-effector control.
Challenges. Aerial manipulation remains constrained by strong coupling between flight and arm mo-
tion, time-varying payload dynamics, limited sensing and onboard computation, and the destabilizing
effects of physical contact. Learning-based methods additionally face scarce demonstrations, costly and
potentially unsafe exploration, and substantial sim-to-real discrepancies in aerodynamics and contact
behavior. For VLA systems, a central challenge is coordinating semantically driven platform movement
with precise manipulation despite their different action scales and dynamics. Future progress will re-
quire safer data collection, more accurate payload and contact estimation, embodiment-aware action
representations, and tighter integration of high-level reasoning with real-time stability guarantees.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
4.10. Underwater Manipulation
Underwater manipulation involves robotic platforms equipped with one or more arms or grippers
to physically interact with submerged objects, structures, and environments. Representative tasks
include object retrieval, valve operation, sampling, inspection, maintenance, and archaeological
intervention. Compared with terrestrial manipulation, underwater systems must account for coupled
vehicle–manipulator dynamics, buoyancy, hydrodynamic drag, external currents, degraded visibility,
and limited communication bandwidth. These factors complicate perception, contact regulation, and
coordinated motion while placing stringent requirements on operational reliability and safety.
Non-Learning-Based Methods. Traditional underwater manipulation primarily relies on model-
based control, task-priority optimization, and human teleoperation. The TRIDENT framework [411]
coordinates a floating vehicle and redundant manipulator through an extended task-priority controller,
enabling dexterous grasping while satisfying operational constraints such as joint limits and target
visibility. Ocean One [412, 413] combines a whole-body controller for manipulation, posture, and
constraint regulation with visual and haptic interfaces, allowing a human operator to supervise
deep-sea dexterous manipulation without directly controlling every joint. DexROV [414] addresses
long-distance underwater teleoperation under communication latency through predictive simulation,
force-feedback interfaces, and shared autonomy. More recently, MR-UBi [415] integrates bilateral
control with a mixed-reality reaction-torque indicator, providing visual and haptic feedback to improve
contact-force regulation during underwater grasping and pick-and-place operations.
Learning-Based Methods. Learning-based underwater manipulation remains less explored than
its terrestrial counterpart, but recent work has begun to address model uncertainty, demonstration
scarcity, and challenging visual conditions. In RL, Carlucho et al. [416] introduce an actor–critic con-
troller that directly predicts joint torques for an underwater manipulator while respecting position and
torque constraints, reducing dependence on an accurate hydrodynamic model. In IL, AquaBot [417]
first learns from human teleoperation through behavior cloning and subsequently improves the policy
using autonomous real-world trials, supporting tasks such as grasping, sorting, and object retrieval.
Bi-AQUA [418] learns from bilateral-control demonstrations and introduces lighting-aware feature
modulation and transformer conditioning to maintain manipulation performance under varying under-
water illumination. UMI-Underwater [419] further reduces reliance on underwater teleoperation by
autonomously collecting underwater grasp demonstrations and transferring knowledge from on-land
human demonstrations through a depth-based affordance representation. An affordance-conditioned
diffusion policy then generates robot actions that remain robust to changes in lighting, color, and
background appearance. Together, these methods indicate a shift from manually operated systems
toward autonomous and data-scalable underwater manipulation.
Challenges. Underwater manipulation remains constrained by uncertain hydrodynamics, strong
coupling between vehicle and manipulator motion, limited visibility, communication latency, and
the difficulty of regulating contact forces in moving fluids. Learning-based approaches additionally
face scarce real-world demonstrations, costly and risky data collection, limited simulation fidelity,
and substantial distribution shifts across water conditions, lighting, payloads, and deployment sites.
Future progress will require tighter integration of model-based control with learned policies, scalable
self-supervised data collection, robust multimodal perception using vision, sonar, proprioception, and
force sensing, and safety-aware adaptation under changing environmental dynamics.
5. High-level Planning
High-level planning in robot manipulation provides structured guidance for low-level execution by
determining what actions to perform, in which order, and which aspects of the environment are
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Decision
Layer
Motion
Generation Layer
Actuation
Control Layer
High-level Planning (§5)
• Task Plan (§5.1 & §5.2)
• Code (§5.3)
• Geometric Objective and Constraint (§5.4)
• Affordance (§5.5)
• 3D Representations (§5.6)
Output: Structured Artifacts (e.g., symbolic plan, program,
constraint set, affordance prior, structured 3D world, video)
Low-Level Action Modeling
Classical Non-Learning
• Sampling-based Planning
• Trajectory Optimization
• Model Predictive Control …
Output: Trajectory
Actuation-Level Control
• Joint-space Control (Position, Velocity, Torque)
• Interaction Control (Impedance, Admittance)
Output: Motor torques
Learning-Based (§6)
• Input Modeling (§6.2)
• Latent Learning (§6.3)
• Policy Learning (§6.4)
Output: Actions
Language / Perception
(or other modalities)
Instantiated as target
pose / constraint
Instantiated as
input/latent
Robot Dynamics
• Video (§5.7)
Figure 12 | Method taxonomy for basic manipulation, extensible to other manipulation tasks. It
comprises High-Level Planning, Low-Level Action Modeling, and Actuation-Level Control. High-level
modules produce planning artifacts that guide downstream action generation, while low-level methods
operate on these artifacts or raw multimodal observations. Solid arrows indicate the survey’s primary
focus: High-Level Planning and Learning-Based Low-Level Action Modeling.
relevant. LLMs and MLLMs are increasingly used for task planning, programmatic planning, and
geometric constraint-based planning, supporting task decomposition, skill sequencing, executable
program generation, and spatially grounded reasoning. In parallel, affordance-based planning
and 3D representation-based planning provide actionable intermediate representations, such as
functional regions, contact cues, geometric relations, and structured scene states. More recently,
video-based planning extends this paradigm by representing future task evolution through generated
visual trajectories or predictive world models, enabling prospective reasoning over action outcomes and
plan refinement. Together, these approaches establish high-level planning as a flexible guidance layer
that integrates semantic reasoning, spatial grounding, scene understanding, and future prediction
to support reliable execution across diverse manipulation tasks. We summarize this taxonomy in
Figure 13 and provide a visualization in Figure 14.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
High-level Planner (§ 5)
LLM-based Task
Planning 5.1
Grounded & Closed-Loop
Planning
SayCan [420], Grounded Decoding [421], Inner
Monologue [422], LLM-Planner [423], Polaris [424]
Feasibility-Aware Planning
LLM+P [425], LLM3 [426], REFLECT [427]
Preference & Collaborative
Planning
APRICOT [428], MALMM [429], RoCo [430]
MLLM-based Task
Planning 5.2
General-Purpose MLLM
Reasoning
PaLM-E [76], VILA [431], PG-InstructBLIP [432], EVLP [433],
EmbodiedGPT [434]
Spatial Reasoning &
Grounding
SpatialVLM [435], SpatialBot [436], RoboSpatial [437],
EmbodiedVSR [438], SoFar [439], RoboRefer [178]
Reward & Progress Reasoning
Robo-Dopamine [440], RoboReward [441], Robometer [442],
ProcVLM [443]
Failure Reasoning & Recovery
AHA [444], Code-as-Monitor [445], I-FailSense [446],
Rewind-IL [447], AgentChord [448]
Robot-Specialized Embodied
Reasoning
RoboBrain [449], RoboBrain 2.0 [450], RynnBrain [451],
FSD [452], Embodied-R1 [453], Gemini Robotics [454]
Programmatic
Planning 5.3
Language-to-Program
Code as Policies [455], ProgPrompt [456], ChatGPT for
Robotics [457]
Demonstration-to-Program
Instruct2Act [458], Demo2Code [459], SHOWTELL [460],
Statler [461]
Grounded & Verifiable
Programs
InterPreT [462], Reliable CaP [463], HyCodePolicy [464]
Geometric
Constraint-Based
Planning 5.4
Spatial Objectives
VoxPoser [465], IKER [466]
Relational & Keypoint
Constraints
CoPa [467], ReKep [468], GeoManip [469]
Functional Constraints
CoDex [470]
Affordance-Based
Planning 5.5
Geometric Affordance
Ditto [471], GAPartNet [472], CPM [473], RoboPCA [474]
Visual Affordance
Transporter Networks [475], VAPO [476], RAAP [477]
Semantic Affordance
Affordance-Based Imitation Learning [478], SAGE [479]
Multimodal Affordance
CLIPort [480], ManipLLM [481], MOKA [482], A3VLM [483],
RoboPoint [484], UniAff [485], BiPreManip [486]
3D Representation-
Based Planning 5.6
Point-Cloud Representations
Point-Cloud Planning [487], PA3FF [488]
Implicit & Descriptor Fields
NDF [489], R-NDF [490], F3RM [491], 𝐷3Fields [492],
PA3FF [488]
Gaussian-Splatting
Representations
Splat-MOVER [493], Physically Embodied GS [494],
MSGField [495], RoboSplat [496]
Generative & Structured 3D
Representations
Imagination Policy [497], RoboEXP [498]
Figure 13 | Taxonomy of high-level planning approaches, organized into major planning paradigms,
including LLM- and MLLM-based task planning, programmatic planning, and geometric constraint-
based planning, together with supporting capabilities in affordance learning and 3D representations.
5.1. LLM-Based Task Planning
Early work followed a symbolic planning and grounding paradigm, in which neural networks mapped
demonstrations and observations to symbolic states and goals represented by predicate truth val-
ues [499]. LLMs have subsequently extended this paradigm by providing semantic knowledge,
instruction decomposition, and open-vocabulary reasoning, while frequently retaining symbolic repre-
sentations or predefined robot skills for grounding and execution. SayCan [420] is an early influential
example that combines language-model-based task relevance with learned affordance scores estimat-
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
ing skill executability, thereby selecting actions that are both semantically appropriate and physically
feasible. Grounded Decoding [421] further integrates language and grounded model likelihoods
during sequence decoding. However, these methods primarily perform planning without incorporating
execution feedback. Inner Monologue [422] addresses this limitation by feeding task-success signals,
scene descriptions, and human feedback back into the LLM reasoning process, enabling closed-loop
plan revision in unstructured environments. Related feedback-driven replanning is also explored in
LLM-Planner [423].
Another line of work improves the logical and physical feasibility of LLM-generated plans. LLM+P
[425] translates natural-language problems into PDDL representations and delegates plan search to
a classical planner, combining the semantic flexibility of LLMs with the correctness guarantees of
symbolic planning. LLM3 [426] more directly connects task and motion planning by using motion-
planning failures to revise action sequences and continuous parameters, reducing repeated exploration
of geometrically infeasible plans. REFLECT [427] similarly diagnoses unsuccessful interactions and
uses the resulting failure information to generate corrective plans. These methods shift LLM-based
planning from unconstrained language generation toward iterative planning grounded in symbolic
validity, motion feasibility, and execution outcomes.
Recent studies further incorporate user preferences, safety requirements, and broader interaction
structures. APRICOT [428] combines LLM-based active preference learning with constraint-aware
task planning, querying users to resolve ambiguous preferences while adapting plans to geometric
limitations. MALMM [429] employs multiple LLM agents to improve planning and decision-making,
while Polaris [424] combines LLM reasoning with Syn2Real visual grounding for open-ended tabletop
manipulation. RoCo [430] extends LLM-based planning to multi-robot collaboration and introduces
RoCoBench for evaluating collaborative manipulation tasks.
5.2. MLLM-based Task Planning
Text-only LLMs require visual observations and other sensory inputs to be processed by separate
perception modules before reasoning. In contrast, MLLMs [3, 77, 500] jointly process visual and
linguistic information, enabling tighter integration of perception, reasoning, planning, and execution
monitoring. We therefore view MLLM-based task planning as a closed-loop process that encompasses
plan generation, spatial grounding, progress evaluation, failure diagnosis, and corrective reasoning.
General-Purpose MLLM Reasoning. Early studies adapt general-purpose MLLMs to robotic decision-
making. PaLM-E [76] incorporates continuous embodied observations into a pretrained language
model, enabling visually grounded sequential decision-making, while VILA [431] directly lever-
ages GPT-4V for visual grounding and manipulation planning without task-specific fine-tuning. PG-
InstructBLIP [432] instead fine-tunes InstructBLIP [501] on physical concepts to strengthen physical
reasoning. EmbodiedGPT [434] introduces embodied chain-of-thought reasoning [502], and Zhang
et al. [503] further incorporate fine-grained reward guidance. Matcha [504] enables interactive
multimodal perception, whereas EVLP [433] jointly generates linguistic subplans and visual sub-
goals. Socratic Models [505] and Socratic Planner [506] further coordinate specialized perception,
reasoning, and control modules through language.
Spatial Reasoning and Grounding. Spatial reasoning supplies the geometric and relational in-
formation required to ground high-level instructions into manipulation plans. SpatialVLM [435],
SpatialBot [436], and RoboSpatial [437] improve metric, directional, and 3D scene understand-
ing, while EmbodiedVSR [438] organizes evolving relations through dynamic scene graphs. For
manipulation-specific grounding, SoFar [439] represents object poses and action directions using
language-grounded functional orientations, and RoboRefer [178] combines depth-aware perception
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
with multi-step spatial referring. These methods provide intermediate representations, including
orientations, referring regions, scene graphs, affordances, and geometric relations, that constrain
downstream action generation.
Reward and Progress Reasoning. MLLMs can also serve as critics that evaluate execution progress
and provide feedback for replanning or policy improvement. Robo-Dopamine [440] models fine-
grained manipulation progress, RoboReward [441] learns general-purpose vision–language rewards
from diverse robot trajectories, and Robometer [442] combines within-trajectory progress estimation
with cross-trajectory comparison. ProcVLM [443] further grounds dense rewards in procedural
stages and visual state transitions. Together, these methods extend multimodal reasoning from plan
generation to execution evaluation.
Failure Reasoning and Recovery. Failure reasoning closes the planning loop by detecting deviations,
diagnosing their causes, and selecting corrective actions. AHA [444] detects manipulation failures and
produces natural-language explanations for plan revision, while Code-as-Monitor [445] translates task
constraints into executable visual programs for reactive and proactive monitoring. I-FailSense [446]
targets failure detection across robots and tasks, and self-refining VLMs [507] improve failure
recognition and reasoning through iterative feedback. Rewind-IL [447] leverages detected failures
for recovery learning, whereas AgentChord [448] incorporates anticipated failure branches and
corrective transitions into task graphs. These approaches extend one-shot planning toward closed-
loop monitoring, diagnosis, recovery, and replanning.
Robot-Specialized Embodied Reasoning. Recent work increasingly trains MLLMs specifically for
robotic perception and reasoning. RoboBrain [449] learns from robot-centric annotations spanning
task plans, affordances, and end-effector trajectories, while RoboBrain 2.0 [450] extends these
capabilities to spatial–temporal reasoning and closed-loop interaction. RynnEC [508] emphasizes
region-centric visual representations, and RynnBrain [451] further integrates embodied reasoning
within a unified foundation model. FSD [452] connects spatial reasoning to manipulation through
affordance regions and visual traces, whereas Embodied-R1 [453] uses pointing as an intermediate
interface between multimodal reasoning and action generation. Other embodied models, including
ERA [509], GenieReasoner [510], PhysBrain [511], HY-Embodied [512], and ACE-Brain [513], further
integrate task reasoning, spatial grounding, affordance prediction, and action-related representations.
Overall, this trend shifts MLLMs from external planners toward embodied foundation models that
support planning, grounding, evaluation, and closed-loop adaptation within a unified framework.
5.3. Programmatic Planning
Programmatic planning represents robot plans as executable programs that connect high-level seman-
tic reasoning with perception, motion primitives, and control APIs. Early work maps natural-language
instructions to robot programs [514], while Code as Policies [455] prompts LLMs with perception and
control APIs to synthesize executable policies. ProgPrompt [456] similarly generates situated robot
programs with explicit action and state structures, and Vemprala et al. [457] establish a reusable
framework for integrating ChatGPT with robotic APIs. Subsequent methods broaden the available
supervision and program representations. Instruct2Act [458] integrates visual foundation models
for multimodal instruction following, Demo2Code [459] abstracts demonstrations into reusable pro-
grammatic skills, and SHOWTELL [460] generates policy code directly from visual demonstrations.
Statler [461] further maintains an explicit world state to support longer-horizon reasoning.
Recent work increasingly focuses on grounding, verification, and adaptation of generated pro-
grams. InterPreT [462] learns executable predicates from language feedback and compiles them
with learned symbolic operators into PDDL domains for generalizable planning. Towards Reliable
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Programmatic Planning
Geometric Constraint-
based Planning
Representations
(t = 0) Instruction: Cook a potato and put it into the recycle bin.
LLM Planner: Plan → navigate to potato → pick up → … → place in recycle bin.
(t = 5) Observation: Potato not found; fridge observed.
LLM Planner: Replan → navigate to fridge → open → pick up potato → close → … →
place in recycle bin.
(t = 20) Observation: Recycle bin not found; garbage can observed.
LLM Planner: Replan → navigate to
garbage can → place potato.
Visual Planning
Affordance
MLLM-based Task Planning
Text / Code Planning
Video:
LLM-based Task Planning
Figure 14 | Overview of the taxonomy of high-level planners, highlighting six core components:
LLM-based task planning, MLLM-based task planning, code generation, motion planning, affordance
learning, and 3D scene representations. Figure adapted from [423, 434, 455, 465, 471, 491].
Code-as-Policies [463] combines symbolic verification with interactive environment exploration to
validate task-relevant conditions before execution. HyCodePolicy [464] closes the programming loop
by integrating geometric grounding, visual monitoring, failure diagnosis, and iterative code repair.
More recently, Functional Cache Grafting [515] retrieves and composes validated function-level code
structures, reducing redundant generation while improving policy robustness. Overall, program-
matic planning is evolving from one-shot language-to-code generation toward grounded, verifiable,
self-correcting, and reusable executable representations.
5.4. Geometric Constraint-based Planning
Geometric objectives and constraints provide an intermediate representation between semantic task
reasoning and motion execution. Rather than directly mapping observations to robot actions, these
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
approaches translate language and perception into spatial costs, keypoint relations, target poses, or
geometric constraints that can be optimized by downstream planners. VoxPoser [465] composes
language-conditioned 3D value maps as spatial objectives for model-based trajectory generation.
CoPa [467] identifies task-relevant object parts and their spatial relations to derive target end-effector
poses, while ReKep [468] represents manipulation tasks as sequences of optimizable relational
constraints over semantic 3D keypoints. GeoManip [469] further treats stage-specific geometric
constraints as a general interface between semantic reasoning and trajectory optimization.
Recent work extends this paradigm toward adaptive objectives and more complex physical inter-
actions. IKER [466] uses VLMs to generate and iteratively refine keypoint-based reward functions
from language and RGB-D observations, enabling geometric task specification for downstream policy
learning. CoDex [470] similarly infers semantic constraints for dexterous functional manipulation
and uses constrained optimization to generate physically feasible grasp candidates before policy
refinement. Collectively, these methods separate semantic task interpretation from numerical motion
generation through explicit, optimizable geometric representations, improving the modularity and
physical grounding of manipulation planning.
5.5. Affordance-Based Planning
Affordance-based planning represents manipulation tasks through action-oriented properties that
specify where and how an agent can interact with objects or environments. Originating from
Gibson’s notion of affordance [516], this perspective provides an intermediate abstraction between
semantic understanding and motion generation. Rather than directly predicting complete trajectories,
affordance-based methods identify functional parts, interaction regions, keypoints, contact poses,
action directions, or kinematic constraints that guide downstream execution. We organize these
methods by their dominant information source and representation into geometric, visual, semantic,
and multimodal affordances, while noting that recent approaches increasingly combine these cues.
Geometric Affordance. Geometric affordances derive interaction possibilities primarily from object
shape, articulation, and kinematic structure. Early methods infer parts, joints, and motion constraints
directly from 3D observations [471, 472, 517]. Ditto [471], for example, reconstructs articulation
models from physical interaction, while GAPartNet [472] introduces cross-category generalizable
actionable parts that support skill transfer across object instances. CPM [473] further represents
manipulation through compositional geometric relations between functional parts. For articulated ob-
jects, Kinematic-aware Prompting [518] converts joints and contact locations into a unified kinematic
description and prompts an LLM to generate 3D manipulation waypoints, explicitly connecting object
kinematics with low-level action generation. ScrewSplat [519] instead reconstructs object geometry,
movable parts, and screw axes directly from RGB observations, providing an explicit kinematic model
that can subsequently support text-guided manipulation. More recently, RoboPCA [474] jointly
predicts task-conditioned contact regions and end-effector poses from RGB-D observations, coupling
where to interact with how the interaction should be geometrically realized.
Visual Affordance. Visual affordances infer interaction opportunities directly from images, commonly
representing them as pixels, regions, keypoints, or action-conditioned heatmaps. Transporter Net-
works [475] establish a spatially equivariant formulation for pick-and-place by predicting image-space
action locations, while VAPO [476] learns visual affordances from unstructured interaction data.
KITE [520] grounds language instructions into 2D image keypoints and conditions downstream
manipulation skills on these keypoints, enabling fine-grained object- and part-level interaction across
scene variations. UAD [521] reduces the dependence on manually annotated affordances by distilling
complementary knowledge from pretrained vision and vision–language models into a lightweight
task-conditioned affordance predictor. Recent work further improves transfer beyond fixed training
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
categories. RAAP [477] combines retrieval with cross-image alignment, decoupling contact localiza-
tion from post-contact action direction to transfer affordances across unseen objects. Together, these
methods turn visual grounding and correspondence into actionable intermediate representations for
manipulation.
Semantic Affordance. Semantic affordances associate object identity, functional parts, and task
concepts with possible interactions. Early affordance-based imitation learning [478] showed that
semantic properties can provide transferable priors for mapping observations to manipulation be-
haviors. More recent methods shift from category-level semantics toward functional and part-level
representations. SAGE [479] bridges semantic parts with Generalizable Actionable Parts, combining
instruction interpretation with part-level motion knowledge to construct executable policies. PartIn-
struct [522] further highlights the importance of such fine-grained grounding through a benchmark
in which instructions explicitly refer to object parts and their task-dependent roles, exposing the
difficulty of jointly grounding part semantics and predicting manipulation actions in 3D space. This
distinction between semantic identity and physical functionality is especially important for articulated
and multi-part objects, where similarly named parts may exhibit different kinematics and afford
different interactions.
Multimodal Affordance. Foundation models increasingly combine language, vision, geometry, demon-
strations, and interaction feedback to infer richer affordance representations. CLIPort [480] couples
a semantic “what” pathway with a spatial “where” pathway for language-conditioned manipulation.
ManipLLM [481] further reasons about object categories, affordance priors, contact points, and
end-effector directions within an embodied MLLM. MOKA [482] uses marked visual prompts to elicit
point-based affordances from pretrained VLMs, providing a compact interface between semantic
reasoning and robot motion, while RoboPoint [484] predicts spatial affordance points from language
and images. PIVOT [523] similarly turns continuous spatial decisions into iterative visual selection by
overlaying candidate actions, locations, or trajectories onto images and repeatedly querying a VLM to
refine them, enabling actionable spatial reasoning without task-specific fine-tuning.
Retrieval provides another route to generalizable affordance reasoning. RAM [524] constructs an
affordance memory from heterogeneous robot, human–object interaction, and custom demonstrations,
retrieves task-relevant examples from language instructions, and transfers the retrieved 2D affordance
into an executable 3D affordance in the target scene. For articulated manipulation, A3VLM [483]
learns robot-agnostic articulation and action affordances that can be instantiated through downstream
motion primitives, whereas UniAff [485] jointly models affordance understanding and object-centric
3D motion constraints for both articulated objects and tools. AIC MLLM [525] further closes the
interaction loop by using visual and textual feedback from failed interactions to correct predicted
SE(3) contact poses, showing how affordance-related geometric decisions can be refined through
physical experience. BiPreManip [486] uses affordance prediction prospectively, reasoning about
the desired final interaction to plan preparatory actions for coordinated bimanual manipulation.
These developments shift affordances from passive interaction descriptors toward explicit planning
interfaces that connect multimodal task reasoning, geometric grounding, interaction feedback, and
executable robot behavior.
5.6. 3D Representation-Based Planning
3D representation-based planning uses structured scene representations to bridge perception and ac-
tion by exposing planning-relevant geometry, semantics, relations, or goal states. Rather than directly
mapping observations to control signals, these methods support manipulation through intermediate
representations such as point-cloud transformations, continuous descriptor fields, editable Gaussian
scenes, imagined goal geometries, or action-conditioned scene graphs. We focus on representations
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
that explicitly support goal specification, correspondence, search, or downstream motion generation.
Point-Cloud Representations. Point clouds provide an explicit geometric state space for manipulation
planning. Saha et al. [487] formulate multi-object rearrangement as A* search directly over point-
cloud transformations, avoiding discrete symbolic state and action representations. Related methods
use point clouds to encode functional parts or geometric targets for manipulation. For example,
PA3FF [488] learns a continuous part-aware 3D feature field from point-cloud inputs, providing
functional-part representations that support correspondence and downstream policy learning.
Implicit and Descriptor Fields. Implicit fields provide continuous, geometry-aware representa-
tions for pose correspondence and language-conditioned manipulation. NDF [489] learns SE(3)-
equivariant descriptors for pose transfer, while R-NDF [490] extends them to relational rearrangement.
F3RM [491] distills 2D foundation-model features into 3D fields for few-shot language-guided grasp-
ing and placing. 𝐷3Fields [492] further models dynamic semantic and instance-aware descriptors for
zero-shot rearrangement, while PA3FF [488] incorporates functional part structure to improve robust
articulated-object generalization.
Gaussian-Splatting Scene Representations. Gaussian Splatting provides an explicit and editable
3D scene representation combining geometry, appearance, and semantics. Splat-MOVER [493]
embeds semantic and affordance features into 3DGS and generates grasp candidates for multi-
stage open-vocabulary manipulation. Physically Embodied Gaussian Splatting [494] couples visual
Gaussians with particle-based physical states for predictive and correctable scene modeling, while
MSGField [495] augments Gaussian primitives with semantic and motion attributes for dynamic
manipulation. RoboSplat [496] instead exploits scene editability to synthesize diverse demonstrations
and improve downstream policy generalization.
Generative and Structured 3D Representations. Beyond reconstructing the current scene, 3D rep-
resentations can encode desired future states and action-relevant structure. Imagination Policy [497]
generates target point clouds and recovers keyframe actions through rigid registration, formulating
action inference as goal-state generation. RoboEXP [498] incrementally builds action-conditioned
scene graphs through interaction, combining geometry, semantics, and relational structure for down-
stream manipulation. These approaches extend 3D representations from static perception toward
explicit goal and interaction representations for planning.
5.7. Video-Based Planning
Video-based planning represents task evolution through predicted visual futures, providing a temporal
interface between task understanding and robot execution. Unlike static goals or geometric constraints,
videos encode object motion, interaction outcomes, and intermediate task states. Recent world models
further condition future prediction on language or robot actions, enabling visual rollouts to support
action extraction, model-based planning, and planner optimization. We focus on methods where
predicted futures directly contribute to plan representation, action selection, or planner learning.
Generative Video Planning. One line of work treats generated future observations as visual plans.
Large Video Planner [526] learns from large-scale human and task videos to produce zero-shot
video plans that are converted into robot actions. RIGVid [527] generates manipulation videos
from language and initial observations, filters them with a VLM, and recovers object trajectories
through 6-DoF pose tracking. Geometry-aware 4D Video Generation [528] improves cross-view
geometric consistency in generated RGB-D videos, while GEM-4D [529] adds dense 4D correspondence
supervision and inverse dynamics for trajectory recovery. These methods use video as an explicit
spatiotemporal plan that can be translated into robot motion.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Predictive World-Model Planning. A second direction predicts the consequences of candidate actions
for action selection. SAMPO [530] performs action-conditioned video prediction for model-based
control. Grounded World Model [531] predicts outcomes in a vision–language-aligned latent space
and scores them against task instructions, enabling language-conditioned model-predictive control.
Here, the world model functions as a predictive dynamics model within the planning loop.
World-Model-Guided Planner Learning. World models can also provide simulated interaction for
improving planners with fewer physical rollouts. DreamPlan [532] uses imagined rollouts from an
action-conditioned video world model to construct preferences for reinforcement fine-tuning of a VLM
planner. RoboEvolve [533] co-evolves a VLM planner and video simulator using simulated successes
and near-miss failures. GE-Sim 2.0 [534] further supports closed-loop simulation by predicting
visual and proprioceptive evolution and providing rollout-level supervision for policy learning. These
approaches position world models as learned environments for planner refinement.
6. Low-level Learning-based Action Modeling
Low-level action modeling focuses on how robots transform perception and task context into executable
actions, trajectories, or action sequences, providing the interface between high-level planning and
physical execution. While high-level planning determines what to do and in what order, such as task
decomposition, skill sequencing, or goal reasoning, low-level action modeling determines how planned
intent is instantiated into concrete manipulation behaviors through learned visuomotor mappings.
The two are complementary: high-level planners provide structured intent and semantic constraints,
whereas low-level action models translate them, or directly map multimodal observations, into action
representations that can be executed by controllers. Within this framework, learning paradigms
such as imitation learning and reinforcement learning define how action models are optimized. We
further decompose learning-based low-level action modeling into three interdependent components:
input modeling, which determines what sensory and contextual information is used and how it is
encoded; latent learning, which studies compact and transferable internal representations; and policy
learning, which determines how these representations are decoded into executable actions. Together,
this taxonomy provides a unified view of learning-based action generation by connecting perception,
representation, and policy optimization between high-level reasoning and actuation-level control.
6.1. Learning Strategy
6.1.1. Reinforcement Learning
In robotic manipulation, reinforcement learning (RL) has emerged as a central paradigm for acquiring
complex skills. By leveraging high-dimensional perceptual inputs (e.g., vision or proprioception)
and reward signals as feedback, RL enables agents to learn control policies through trial-and-error
interaction with the environment. This section reviews RL methods for robotic manipulation from
both theoretical and application perspectives. We categorize existing approaches into two main
classes: model-free and model-based algorithms, depending on whether the agent exploits an explicit
or learned dynamics model to guide the learning process. Representative methods across these
categories are summarized in Table 8.
i) Model-Free Methods
In robotic manipulation, model-free RL learns policies or value functions directly from interaction
data without explicitly modeling environment dynamics. Its flexibility makes it suitable for high-
dimensional and contact-rich manipulation, but typically at the cost of substantial interaction data
and limited sample efficiency. Recent work therefore increasingly combines RL with offline data,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 8 | Representative RL methods for manipulation tasks.
Category
Subcategory
Representative Methods
Model-Free RL
Pre-Training
QT-Opt [535], PTR [536], V-PTR [537]
Fine-Tuning
Residual RL [538], RLDG [539], V-GPS [540], PA-RL [541]
VLA-RL
iRe-VLA [542], RIPT [543], VLA-RL [544], ConRFT [545]
Model-Based RL
Imagination Trajectory Generation
Dreamer [546], MWM [547]
Planning
GPS [548], TD-MPC [549]
Differentiable RL
SAPO [550], SAM-RL [551], DiffTORI [552]
pre-trained policies, learned rewards, and imitation priors to improve scalability and real-world
applicability. We categorize these methods into three groups.
RL in Pre-Training. RL pre-training aims to acquire reusable policies, value functions, rewards,
or exploration behaviors before downstream adaptation. QT-Opt [535] demonstrates scalable self-
supervised RL for vision-based manipulation, while PTR [536] and Q-Transformer [553] show how
offline RL and value learning can support rapid adaptation from large robot datasets. V-PTR [537]
further incorporates human videos into value pre-training. Beyond offline supervision, PEAC [554]
performs reward-free cross-embodiment pre-training to learn task-agnostic and embodiment-aware
knowledge, while TaskExp [555] uses multi-task pre-training with decision and perceptual objectives
to improve generalization. ROBOFUME [556] and ReWiND [557] extend pre-training to learned
rewards and multi-task policies, and DEAS [558] improves long-horizon offline value learning over
action sequences. Together, these methods broaden RL pre-training from policy and value initialization
toward reward learning, unsupervised skill acquisition, and generalizable multi-task control.
RL in Fine-Tuning. RL fine-tuning improves pre-trained policies through task-specific interaction
while preserving prior capabilities and training stability. Residual methods [538, 559] and Policy
Decorator [560] refine frozen base policies through corrective actions, while RLDG [539] distills
RL-improved trajectories back into a generalist policy. Value-guided approaches such as V-GPS [540]
and PA-RL [541] improve action selection without directly modifying the base policy, and batch
online RL [561] alternates autonomous data collection with offline updates. For expressive generative
policies, EXPO [562] stabilizes online RL by learning a lightweight value-guided edit policy around
an imitation-trained base policy, while Behavioral Mode Discovery [563] regularizes fine-tuning to
prevent mode collapse. These approaches highlight a shift toward policy-agnostic, value-guided, and
distribution-preserving RL post-training.
RL for VLA Models. VLA, as a special class of generalist models, has attracted significant research
attention in the field, with numerous studies focusing on designing efficient reinforcement learning
post-training schemes for VLA models [542–545, 564–568]. iRe-VLA [542] proposed a robust post-
training pipeline that iteratively executes online RL for efficient exploration and IL on both expert
and collected online data. RIPT [543] introduces a simple and critic-free VLA-RL framework that
extends the Leave-One-Out PPO (LOOP [569]) algorithm to estimate advantage functions for each
sampled trajectory, allowing significant performance improvements over supervised fine-tuning with
minimal demonstrations through online RL. ConRFT [545] proposes a comprehensive post-training
pipeline that employs a unified consistency-based training objective that combines RL and IL in both
the offline and online phases.
ii) Model-Based Methods
In robotic manipulation, model-based methods exploit explicit or learned environment dynamics
to facilitate policy learning and action optimization. By predicting future states and rewards, they
enable planning, imagination-based policy learning, and improved sample efficiency. However, their
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
effectiveness depends on model fidelity, which remains challenging in high-dimensional and contact-
rich manipulation. We categorize these methods into three groups.
Imagination Trajectory Generation. The classical Dyna framework [570] uses learned dynamics to
generate additional transitions for policy learning. Modern approaches increasingly perform such
imagination in compact latent spaces. The Dreamer series [546, 571, 572] learns latent dynamics from
observations and optimizes policies through imagined rollouts, forming the basis of many subsequent
visual MBRL methods [547, 573–575]. DayDreamer [574] extends latent imagination to real physical
robots, while MWM [547] improves visual world modeling through masked representation learning.
Recent work further improves the data sources and representations used for imagination. Ve-
oRL [576] learns an interactive world model from unlabeled videos and uses predicted long-term
behaviors to guide offline RL. GWM [577] predicts action-conditioned future scenes using 3D Gaussian
representations, enabling scalable world-model learning for robotic manipulation. MIST-WM [578]
instead couples active exploration with structured world-model learning to discover compact task-
sufficient latent states, improving sample efficiency and generalization across tasks. These approaches
extend imagination-based RL from generic latent prediction toward richer data sources, explicit 3D
structure, and task-relevant dynamics.
Planning. Model-based RL can also exploit learned dynamics for online action optimization. The GPS
series [8, 548, 579–581] uses locally fitted dynamics and trajectory optimization to generate super-
vision for policy learning. TD-MPC [549] and TD-MPC2 [582] jointly learn latent dynamics, value
functions, and policies, and optimize action sequences through model-predictive control. VLAPS [583]
combines VLA-derived action priors with model-based MCTS, enabling test-time search over candidate
action sequences. More recently, MBDPO [584] integrates search and policy improvement by formu-
lating optimization over imagined world-model trajectories as diffusion policy optimization. Together,
these methods shift model-based planning from local trajectory optimization toward scalable latent
search and policy refinement.
Differentiable RL. Differentiable RL exploits differentiable dynamics and rewards to optimize actions
or policy parameters directly through model gradients. Although real-world dynamics are generally
not differentiable, this capability can be provided by differentiable simulators or learned dynamics
models. SAPO [550] leverages analytic simulation gradients for efficient policy optimization in
dexterous manipulation. SAM-RL [551] combines differentiable physics and rendering to jointly
adapt simulation parameters and learn manipulation policies. DiffTORI [552] further integrates
differentiable trajectory optimization with actor-critic learning, using model gradients to refine
policy-generated trajectories.
6.1.2. Imitation Learning
In 1999, Schaal et al. [585] proposed imitation learning (IL) as a key pathway for enabling robots to
acquire efficient motor skills, visuomotor coordination, and modular control. Since then, IL has evolved
into a central paradigm for learning complex manipulation behaviors, with its algorithms, recent
developments, and challenges comprehensively reviewed in [586]. Compared with RL, IL avoids
costly reward design and extensive environment interaction. Early studies were largely grounded in
control-theoretic formulations with limited perception–action integration, while subsequent work
progressively adopted deep architectures such as ResNets and Transformers, large-scale visual and
multimodal pretraining, and more recently large language and vision models. Current advances
emphasize multimodal fusion, robust and efficient policy learning, scalable data utilization, and
generative modeling.
Looking forward, promising directions include foundation-model-driven IL that integrates VLA
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Imitation Learning Methods (§ 6.1.2)
Imitation from Action
Action-level IL
BC from Action
[587], Data Scaling Laws [588], BC-Z [162], Most of
VA/VLA/TVLA, Diffusion Policies, etc
BC from Pose
PoseInsert [589], ZeroMimic [590], RiEMann [591]
MP-based IL
DMP [592, 593], ProMP [594], HSMM [595], Language
Movement Primitives [596], FODMP [597]
Search-based IL
[598], [599], [600], Guided TAMP Imitation [601],
SAILOR [602]
Optimization-based IL
[603], [604], LeTO [605], NODE-IL [606], SCDS [607]
Reward-based IL
Inverse Reinforcement
Learning
Inverse KKT [608], SPRINQL [609], Masked IRL [610],
Constrained Demonstrators [611]
Adversarial Imitation
Learning
GAIL [612], Option-GAIL [613], LAPAL [614],
DRAIL [615], OLLIE [616], C-LAIfO [617]
Representation Learning for IL
Latent Learning for IL
[618], [619], [620], Riemannian IL [621], TRAIL [622],
MCNN [623], BC-IB [61], Latent Policy Barrier [624]
In-Context Imitation
Learning
[625], ICRT [626], Instant Policy [627], Robust Instant
Policy [628], HiST-AT [629], ICLR [630]
Interactive IL
TIPS [631], IWR [632], Sirius [633], LILAC [634],
Lazy [635], Thrift [636], CHG-DAgger [637],
FlowDAgger [638], Set-Supervised DP [639],
ARMADA [640]
Robustness and Efficiency
Robustness
DART [641], [642], [643], Counter-BC [644], ADC [645],
CCIL [646], CREST [647], RAIL [648], FAIL-Detect [649]
Efficiency
[650], TEDA [651], SRIL [652], DemoSpeedup [653],
SAIL [654]
Imitation from Observation
Reward or Occupancy Recovery
from Observation
[655], [656], DIFO [657], DILO [658]
State or Representation
Alignment and Matching
[659], [660], SILO [661], VGS-IL [662], WHIRL [663],
ZeST [664], NIFT [665], VIP [666], LIV [667]
Model- and Physics-Grounded
LfO
[668], Diff-LfD [669]
Behavior Cloning from
Observation
Sensorimotor Primitives [670], Point Policy [671]
Observation-to-Action
Reconstruction and Retargeting
[672], MimicFunc [673], Do as I Do [674],
EgoInfinity [675]
Command-, Goal-, and
Planning-Based LfO
Learning Actions from Human Demonstration Video [676],
Motion Reasoning [677], Cago [678]
Figure 15 | A structured taxonomy of imitation learning methods organized by the source of supervi-
sion, including imitation from action and imitation from observation.
models and LLMs with robotics, causal IL based on counterfactual reasoning, generalization and
transfer across tasks and embodiments, safe and reliable deployment, and more efficient human–robot
interaction with reduced dependence on continuous human feedback. In this subsection, we primarily
focus on state-based and visual imitation learning, as summarized in Figure 15. Language-related
approaches are discussed separately in Section 6.2.2.
i) Imitation from Action
Imitation Learning from Action assumes access to expert demonstrations in the form of state–action
pairs, where both the sensory states (e.g., robot configurations and environment observations) and
the corresponding expert control commands (e.g., end-effector actions and poses) are available.
Action-level IL. Action-level IL focuses on directly learning control policies from expert demonstrations
at the action or trajectory level. Rather than inferring high-level goals or task abstractions, these
methods map observed states to executable actions, poses, or motion primitives, thereby emphasizing
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
precise motor control, trajectory generation, and stability in manipulation.
• Behavior Cloning (BC). BC from Action learns a direct mapping from states to low-level
control commands based on expert state–action pairs. Early studies relied on non-parametric or
regression-based methods [679], later expanding into hierarchical architectures [587, 680, 681],
multimodal generalization [682], stability-constrained training [648, 683], cross-embodiment trans-
fer, human–robot collaboration [684], and the integration of structural priors [685–688]. More
recently, efficient Transformer-based multi-task policies have improved scalability and reusability
under limited data conditions [689]. Additional studies investigate fine-tuning strategies for model
components [690], architectural comparisons [691], and scaling laws [588], while others propose
end-to-end frameworks encompassing data collection, training, and deployment [692, 693]. Overall,
BC from action has evolved beyond supervised imitation into a paradigm emphasizing efficiency,
robustness, structural priors, and adaptability, with growing emphasis on language-integrated inter-
action that advances action-level supervision toward general-purpose manipulation.
BC from Pose abstracts away low-level control by predicting end-effector poses in SE(3), leaving
tracking to IK or force controllers. This geometry-aware formulation improves precision, transferability,
and robustness. Representative works include PoseInsert [589], which leverages relative SE(3) as a
core representation to learn pose-guided policies for sub-millimeter insertion, optionally fusing RGB-D
cues; ZeroMimic [590], which distills skills from in-the-wild human videos into deployable, image-
goal–conditioned policies via pose and geometry alignment; and RiEMann [591], which develops an
SE(3)-equivariant pipeline to predict 6-DoF target poses in real time without explicit segmentation.
Collectively, these approaches highlight the strengths of pose-level cloning for high-precision tasks
and generalization across scenes and embodiments.
• MP-based IL. Movement primitives (MPs) encode demonstrations as parameterized trajectories
or dynamical systems, providing compact and adaptable skill representations. Dynamic Movement
Primitives (DMPs) introduced stable attractor systems for reproducing and adapting demonstrated
motions [592, 593], while Probabilistic Movement Primitives (ProMPs) model trajectory distributions
for uncertainty handling and skill blending [594]. Hidden Semi-Markov Models (HSMMs) further
capture temporal variability through skill segmentation and sequencing [595]. MPs have also been
integrated with task constraints for safe and flexible execution [694], hybrid force/motion primitives
for compliant manipulation [695], and dynamical systems for visual servoing [696]. Recent work
connects MPs with foundation and generative models. Language Movement Primitives [596] grounds
VLM reasoning into DMP parameters for language-conditioned manipulation, while FODMP [597]
combines ProDMP trajectory representations with one-step diffusion to generate temporally structured
motions efficiently. Overall, MP-based IL has evolved from trajectory reproduction toward probabilistic,
constraint-aware, multimodal, and generative skill representations.
• Search-based IL. Search-based IL treats imitation as planning or search over trajectories,
policies, or outcomes rather than direct action regression. Early work formulated imitation as a search
for optimal strategies [598], followed by Learning to Search approaches using functional-gradient
optimization [599]. Planner-in-the-loop methods further combine imitation with structured search.
Guided Imitation of Task and Motion Planning [601] distills TAMP-generated subgoals and trajectories
into hierarchical policies, while partially learned policies in turn accelerate subsequent planning. More
recently, SAILOR [602] learns a world model and reward model from demonstrations and performs
test-time search toward expert outcomes, enabling recovery from states outside the demonstration
distribution. These methods shift imitation from reproducing expert actions toward learning how to
search for expert-like outcomes, improving robustness to covariate shift and long-horizon errors.
• Optimization-based IL. Optimization-based IL integrates imitation objectives with trajectory
optimization, constraint satisfaction, or differentiable planning. Early methods incorporate task
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
constraints into policy learning [603] and optimize demonstrated skills under temporal-logic speci-
fications [604]. More recent approaches integrate optimization more tightly with policy learning.
LeTO [605] embeds differentiable trajectory optimization into end-to-end visuomotor learning, while
NODE-IL [606] uses continuous-time Neural ODE dynamics for long-horizon multi-skill manipula-
tion. Contractive dynamical imitation policies [607] further impose contractive dynamics to improve
stability and recovery under out-of-distribution perturbations. Overall, this line has evolved from
constraint-aware trajectory optimization toward differentiable and stability-aware policy learning.
Reward-based IL. Reward-based IL infers reward or cost functions from demonstrations and op-
timizes policies under the learned objectives. Unlike behavior cloning, which directly fits expert
actions, reward-based methods model the underlying objectives that explain demonstrated behavior,
potentially improving generalization and adaptation beyond the demonstration distribution.
• Inverse Reinforcement Learning (IRL). IRL seeks a reward or cost under which expert
trajectories are approximately optimal and derives a policy through planning or RL. Inverse KKT [608]
formulates manipulation IRL as inverse optimal control, recovering task costs and active constraints
from demonstrations through KKT conditions. SPRINQL [609] instead learns an inverse soft Q-function
from mixed-quality offline demonstrations, emphasizing expert data without adversarial training or
online interaction. A divergence-minimization perspective [697] further unifies BC, GAIL, AIRL, and
related methods through occupancy-distribution matching. Recent work addresses ambiguity and
limitations in demonstrations. Masked IRL [610] combines demonstrations with language and uses
LLMs to identify task-relevant state factors, reducing reward ambiguity and spurious correlations.
Learning from constrained demonstrators [611] infers state-based progress rewards from restricted
demonstrations, allowing subsequent optimization to surpass the demonstrated behavior. These
developments extend IRL toward language-guided reward disambiguation, imperfect demonstrations,
and interactive model-based learning.
• Adversarial Imitation Learning (AIL). AIL learns imitation objectives by discriminating
expert behavior from agent-generated trajectories, with GAIL [612] establishing the occupancy-
matching paradigm. Subsequent work improves visual representation and robustness through latent
world models and contrastive learning [617, 698]. Reward modeling has also been strengthened
through diffusion-based discriminators and preference supervision [615, 699]. Efficiency is improved
through offline-to-online learning [616], discriminator-guided model-based imitation [700], and
trajectory augmentation and correction [701]. Structured policies further address long-horizon and
high-dimensional control through hierarchical options and latent action spaces [613, 614], while
auxiliary-task exploration, actor-critic formulations, and empirical studies improve exploration and
training stability [702–704].
Representation Learning for IL. Representation learning for IL extracts task-relevant, structured,
and transferable representations from demonstrations to improve policy efficiency, robustness, and
adaptation. Rather than directly fitting observation–action mappings, these methods shape latent
spaces, temporal representations, or demonstration-conditioned contexts that capture the factors
underlying expert behavior.
• Latent Learning for IL. Latent representation learning seeks compact task-relevant embed-
dings while suppressing nuisance information that can impair imitation. Task-relevant adversarial
IL [622] restricts representations to behaviorally relevant information, while information-bottleneck
behavior cloning [61] explicitly compresses perceptual inputs into task-sufficient latents to reduce
representational redundancy. Geometry-aware formulations further model demonstrations on Rie-
mannian manifolds [621], while temporal and memory-based approaches capture dependencies
beyond individual observations [623, 705, 706]. More recently, Latent Policy Barrier [624] treats
the latent distribution of expert demonstrations as an implicit in-distribution region and optimizes
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
predicted future latents to remain within this region, improving robustness to covariate shift. Together,
these methods extend latent learning from compact representation toward geometry-, memory-, and
distribution-aware policy representations.
• In-Context Imitation Learning (ICIL). ICIL conditions a pre-trained policy on demonstrations
at inference time, enabling adaptation to new tasks without parameter updates. Early approaches
represent demonstrations through visual sequences, relational graphs, or sensorimotor tokens [625–
627, 707]. Robust Instant Policy [628] further aggregates candidate trajectories with a Student’s-𝑡
formulation to reduce sensitivity to outliers. Recent work increasingly focuses on richer context
representations and scalable training. HiST-AT [629] learns hierarchical spatiotemporal action
tokens that capture both action structure and temporal progression, while ICLR [630] augments
demonstrations with visual reasoning traces of anticipated robot motion. These developments shift
ICIL from direct demonstration conditioning toward structured action tokenization, intermediate
visual reasoning, and scalable context learning.
Interactive Imitation Learning (IIL). IIL improves imitation policies through corrective feedback
collected during policy execution, mitigating distribution shift while reducing the need for complete
expert demonstrations. Early approaches primarily rely on human teleoperation, shared control, or
language feedback to correct policy failures [632, 634, 708–712]. Language-based methods further
enable intuitive online correction, while LLM-based teachers provide corrective or evaluative feedback
with reduced human supervision [713].
Recent work increasingly adapts generative policies from sparse interventions. FlowDAgger [638]
maps human corrective actions into the latent noise space of frozen flow- or diffusion-based policies
and learns a latent policy for adaptation. Set-Supervised Diffusion Policy [639] exploits paired erro-
neous and corrected action chunks, using positive and negative supervision to improve diffusion-policy
learning. For dexterous manipulation, Hand-in-the-Loop [714] smoothly blends human corrections
with autonomous execution to avoid discontinuities during hand–arm takeover. LazyDAgger and
ThriftyDAgger [635, 636] reduce unnecessary queries through switching- and risk-aware intervention
strategies, while Sirius [633] integrates human intervention with continual learning during deploy-
ment. Model-based runtime monitoring [715] anticipates failures and triggers corrective interaction,
while ARMADA [640] combines failure detection with shared control for scalable real-world adapta-
tion. Overall, IIL is evolving from continuous human correction toward selective intervention and
lightweight adaptation of generative and foundation policies.
Robustness and Efficiency. Robustness and efficiency in IL address two critical requirements for de-
ploying manipulation policies in real-world environments: reliability under uncertainty and scalability
under resource constraints. Robustness focuses on ensuring safe and stable execution in the presence
of imperfect data, sensor noise, and distribution shifts, while efficiency emphasizes accelerating
learning and inference to achieve real-time performance and practical deployment.
• Robustness. Recent work on robust and safe imitation learning for manipulation consolidates
three threads. First, robustness to imperfect data is advanced along three lines. Methods either
clean and reweight demonstrations via counterfactual consistency and uncertainty-aware handling of
label conflicts [642, 644], augment and stress-test policies through adversarial human-in-the-loop
collection [645], continuity-based corrective augmentation [646], and Bayesian or classical noise
injection [641, 643], or exploit causal interventions [647] to isolate task-relevant state variables.
Second, safety and constraints are enforced via reachability-based safety filters that wrap IL policies
and provably reduce collisions without sacrificing task success [648]. Third, failure handling under
distribution shift combines object-centric inverse-policy recovery to drive states back toward the
training manifold and failure detection without failure data via sequential OOD tests with uncertainty
quantification and conformal guarantees [649, 716]. Collectively, these advances move IL toward
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
data-efficient, safety-aware, and deployment-ready manipulation.
• Efficiency. A recent line of work pushes imitation learning for manipulation toward faster exe-
cution and practical deployment. Current techniques chiefly accelerate training and inference through
accelerated or resampled demonstrations, model slimming via parameter reduction, quantization,
pruning and distillation, action scheduling, and asynchronous parallelism, thereby improving both
throughput and latency [650–654].
ii) Imitation from Observation
Imitation Learning from Observation (LfO) assumes access to expert demonstrations as state or
visual trajectories without corresponding robot action labels. Compared with imitation from action,
the central challenge is therefore to bridge the missing action supervision between observed behavior
and executable robot control. Existing approaches address this gap in different ways, including
recovering learning objectives, aligning observation spaces, exploiting physical models, learning
policies from reconstructed supervision, retargeting observed motions into robot trajectories, or
inferring task goals and commands.
Reward or Occupancy Recovery from Observation. This line infers rewards, utilities, or occupancy-
matching objectives directly from observation-only demonstrations and subsequently optimizes policies
through RL or planning. Representative approaches include observation-only IRL with automatic
discount scheduling [655], human-video reward learning for manipulation [656], and diffusion-based
adversarial LfO [657]. DILO [658] instead derives a dual occupancy-matching objective that learns
a multi-step utility from offline interaction data, avoiding explicit inverse dynamics or adversarial
discriminators. Rather than reconstructing expert actions, these methods transform observed behavior
into an optimization objective that guides subsequent policy learning.
State or Representation Alignment and Matching. A second strand reduces the discrepancy between
demonstrations and robot execution by aligning states or latent representations across viewpoints,
domains, and embodiments [659–663, 717]. VIP and LIV [666, 667] learn transferable visual repre-
sentations and progress-aware objectives from videos, while ZeST [664] leverages foundation-model
representations for zero-shot task specification. NIFT [665] represents human–object interactions
through transferable interaction fields, while selective and ergodic matching methods determine which
aspects of demonstrated behavior should be reproduced [661, 717]. These methods do not necessarily
reconstruct explicit expert actions, but instead establish shared task-relevant representations in which
observed human and robot behaviors can be compared or matched.
Model- and Physics-Grounded LfO. Model- and physics-grounded methods exploit environment
dynamics, contact models, or differentiable simulation to constrain the mapping from observed state
evolution to executable behavior. Imitation Learning as State Matching [668] optimizes control
by differentiating through physical dynamics to match demonstrated state trajectories, while Diff-
LfD [669] combines differentiable physics and rendering to recover physically consistent manipulation
behavior from visual demonstrations. Such physical grounding is particularly useful when similar
visual trajectories may arise from substantially different actions, contacts, or underlying dynamics.
Behavior Cloning from Observation. A more direct family of LfO methods ultimately learns
executable policies from observation-only demonstrations, despite the absence of original robot action
labels. Instead of treating the observed trajectory only as a reward or goal, these approaches infer
task-relevant action supervision, intermediate control targets, or robot-aligned representations and
use them to learn observation-to-action policies. Liang et al. [670] learn both low-level sensorimotor
primitives and high-level manipulation policies directly from raw human demonstration videos, jointly
recovering intermediate subgoals and sequential task structure without manually annotated actions
or subtask boundaries. Point Policy [671] similarly learns robot policies exclusively from offline
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
human videos by representing both human observations and robot actions through semantically
meaningful 3D keypoints, thereby translating human hand motion into morphology-agnostic robot-
space supervision. These methods extend the behavior-cloning paradigm from directly provided
expert actions to action supervision inferred or structured from observation-only demonstrations.
Observation-to-Action Reconstruction and Retargeting. Another family focuses primarily on
reconstructing executable robot trajectories from observed human behavior rather than directly
learning a policy within the reconstruction procedure. Bharadhwaj et al. [672] extract agent-agnostic
action representations from passive human videos and transform predicted human hand trajectories
into robot-executable motions for zero-shot manipulation. MimicFunc [673] introduces function-
centric correspondences for tool manipulation, constructing a local function frame from keypoints
in a single RGB-D human demonstration and transferring its motion to geometrically different but
functionally equivalent tools. More recent pipelines explicitly reconstruct 3D or 4D hand–object
interactions before retargeting them to robotic embodiments. Do as I Do [674] recovers hand–
object interactions from monocular human videos and retargets them into executable trajectories
for dexterous robotic hands, while EgoInfinity [675] lifts in-the-wild videos into metric 4D hand–
object representations and compiles recovered human motions into robot trajectories across diverse
embodiments. The resulting robot-space trajectories can either be executed directly or serve as
automatically generated demonstrations for subsequent behavior cloning, making reconstruction and
retargeting an important bridge between passive human video and policy learning.
Command-, Goal-, and Planning-Based LfO. A complementary direction abstracts away the demon-
strator’s exact motion and instead recovers semantic commands, symbolic goals, or intermediate states
that specify what the robot should accomplish. Yang et al. [676] formulate human-video imitation
as video-to-command learning, combining manipulation-oriented visual understanding with video
captioning to infer semantic commands that are subsequently grounded into robot execution. Motion
Reasoning [677] instead infers symbolic task goals from third-person demonstrations and combines
task and motion reasoning to distinguish intended task effects from incidental state changes, allowing
the recovered goal to be replanned in a different environment. Cago [678] uses demonstrated states
as goal supervision and selects intermediate goals according to the learner’s current capabilities,
constructing an adaptive curriculum for long-horizon policy learning. By preserving task intent
rather than reproducing embodiment-specific actions, these approaches are particularly suitable when
human and robot motions differ substantially but the desired task outcome remains shared.
6.1.3. Bridging Reinforcement and Imitation Learning
Reinforcement learning (RL) and imitation learning (IL) provide complementary supervision for
robotic manipulation: IL offers efficient learning from demonstrations, while RL enables autonomous
exploration and improvement beyond demonstrated behavior. Their integration has evolved from
sequential pre-training and fine-tuning toward shared formulations, learned rewards, interleaved
optimization, and human-guided adaptation. We organize these approaches into seven categories, as
summarized in Table 9.
Methods Supporting RL and IL. Some methods provide shared formulations or components applicable
to both RL and IL. Dual RL [718] establishes a unified optimization perspective that connects several
reinforcement and imitation learning objectives through common dual formulations. Other techniques,
such as frame mining, provide reusable data-processing mechanisms that benefit both paradigms.
These approaches expose methodological commonalities between RL and IL without prescribing a
specific direction of knowledge transfer.
IL Pre-training + RL Fine-tuning. A dominant paradigm initializes policies from demonstrations
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Table 9 | Representative methods combining RL and IL for manipulation tasks.
Category
Representative Methods
Methods Supporting RL and IL
Frame Mining [718], Dual RL [725]
IL Pre-training + RL Fine-tuning
[719], SkiLD [720], FERM [721], Q-attention [722], CSIL [723],
PLANRL [724],
Sketch-to-Skill [726],
TMRL [727],
RL-100 [728],
ZPRL [729], [730]
RL Pre-training + IL Fine-tuning
MoPA-PD [731], [732]
Reward Shaping from IL
MaxEnt IOC [733], [734], [735], LbW [736], [737], [738], Robo-
CLIP [739], IRIS [740], ORIL [741], [742], ResiP [559], ORCA [743],
Concept2Robot [744]
Joint RL–IL Optimization
[745], AW-Opt [746], [747], IN-RIL [748], TSIL [749]
Human-in-the-Loop RL
HIL-SERL [292], SiLRI [750]
In-Context RL
DCRL [751]
and subsequently uses RL to improve performance beyond the demonstrated distribution. Earlier
approaches combine imitation-derived skills, action priors, or value objectives with RL refinement [719–
724]. Recent work increasingly targets generative and large robot policies. TMRL modulates diffusion
timesteps during pre-training to preserve exploration capacity for subsequent RL, while Q2RL extracts
Q-values from behavior-cloned policies to bootstrap on-robot RL. RL-100 further combines imitation
initialization with offline and online RL for scalable real-world manipulation, and latent-steering
approaches constrain RL refinement to compact policy representations. Overall, this direction shifts
IL from a final policy-learning objective toward an initialization for autonomous post-training.
RL Pre-training + IL Fine-tuning. The reverse direction first obtains strong behaviors through RL,
planning, or privileged supervision and subsequently transfers them into deployable policies through
imitation. Motion-planner-augmented policies can be distilled into visual control policies [731], while
kickstarting and offline RL can generate informative experience that is later transferred to downstream
policies [732]. This paradigm is particularly useful when powerful training-time teachers rely on
privileged states, planners, or expensive interaction that cannot be retained during deployment.
Reward and Goal Shaping from IL. Demonstrations can also guide RL without directly supervising
actions by defining rewards, values, or goal-progress signals. Early approaches infer objectives through
inverse optimal control or demonstration ranking [733, 734]. Other methods derive perceptual or
semantic rewards through representation similarity, temporal progress, or goal proximity [735–
737, 752]. More recent approaches use optimal transport and foundation-model representations
to convert demonstrations or videos into dense objectives [738, 739], while temporally misaligned
demonstrations can still provide useful reward signals for RL refinement [743]. These methods allow
imitation information to supervise reinforcement learning without requiring direct action matching.
Joint RL–IL Optimization. Rather than separating imitation and reinforcement into different stages,
joint approaches combine their objectives throughout training. Demonstration losses can regularize RL
updates or be alternated with reinforcement objectives to improve sample efficiency and stability [745–
748]. Recent interleaved methods explicitly alternate RL and IL updates to reduce conflicts between
their optimization signals, while temporal self-imitation converts successful trajectories discovered
by RL into new imitation targets. This bidirectional interaction allows autonomous experience and
demonstration supervision to improve each other during training.
Human-in-the-Loop RL. Human interventions bridge imitation and reinforcement learning by pro-
viding corrections during autonomous exploration. HIL-SERL [292] combines intervention data with
real-world RL for precise manipulation while reducing exploration risk. Recent methods further
handle imperfect interventions by weighting suboptimal corrections. Human feedback thus provides
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
both demonstrations and safer exploration guidance.
In-Context RL. In-context RL uses demonstrations as contextual information rather than explicit
imitation targets. Demonstration-conditioned RL [751] conditions policies on example trajectories
while optimizing task return, enabling adaptation to new behaviors from only a few demonstrations.
This formulation separates demonstration conditioning from imitation loss and provides an alternative
route for combining few-shot imitation with reinforcement-based optimization.
Overall, RL–IL integration has moved beyond sequential training. Demonstrations can initialize
policies, provide rewards or goals, regularize optimization, guide human-supervised exploration, or
serve as contextual inputs. Conversely, RL experience can refine demonstrated behaviors and provide
improved supervision for imitation, making RL and IL increasingly complementary within a unified
policy-learning pipeline.
6.1.4. Learning with Auxiliary Tasks
Learning with auxiliary tasks refers to training paradigms that enhance policy learning by introducing
additional self-supervised or weakly supervised objectives beyond the primary manipulation goal.
These auxiliary objectives encourage the model to capture structured representations of the environ-
ment, actions, and goals, thereby improving sample efficiency, generalization, and robustness. As
illustrated in Figure 16, we summarize the most commonly used auxiliary tasks in current robotic
learning frameworks.
i) World Model
World models (WMs) have become a central paradigm in robotic manipulation, supporting
predictive planning, policy generalization, and data-efficient control. Formally, a WM learns an
internal representation of environment dynamics, typically parameterizing the conditional distribution
𝑝𝜃(𝑠𝑡+1 | 𝑠𝑡, 𝑎𝑡), where 𝑠𝑡∈𝑆denotes the state (or observation) at time 𝑡and 𝑎𝑡∈𝐴the agent’s action.
By modeling such transitions, WMs enable agents to anticipate the outcomes of actions and perform
rollouts in latent space, thereby reducing reliance on costly real-world interaction. This capability is
especially critical in robotic manipulation, where physical contact, safety constraints, and limited
data render direct trial-and-error learning impractical. Beyond the following research directions,
WM-related approaches also overlap with the model-based RL methods discussed in Section 6.1.1.
Generative Visual WMs. Generative visual world models learn to represent environment dynamics
by synthesizing future visual observations conditioned on past states and actions. By treating video
or image generators as interactive environments, such models enable rollouts in visual or latent space
that can be queried for planning and policy learning. Recent advances span video–action diffusion
pretraining on large robotic datasets [753, 754], transforming generic video diffusion into interactive
predictive models [755], leveraging world models for trajectory generation in one-shot imitation [756],
and compositional imagination for skill generalization [757]. VLMPC further demonstrates how
action-conditioned video prediction can be integrated with vision–language constraints and model-
predictive control to enable closed-loop manipulation [758]. Structured WMs from human videos also
highlight how large-scale visual modeling can support manipulation via transfer and representation
learning [759]. Collectively, these works establish generative visual WMs as a promising route toward
scalable, data-driven predictive control.
3D-Structured or Physics-Grounded WMs. Beyond pixel-based prediction, these methods incorpo-
rate explicit spatial structures or physical priors, such as 3D Gaussians, occupancy fields, point clouds,
and particle-based representations, to improve geometric and physical consistency. Gaussian-based
approaches include Physically Embodied Gaussian Splatting [494], ManiGaussian [760], ManiGaus-
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
sian++ [761], and GWM [577]. ORV [762] instead uses 4D semantic occupancy to provide geometric
and semantic guidance for action-conditioned video generation, improving temporal and multi-view
consistency as well as sim-to-real transfer. Other approaches model dynamics through 3D point clouds,
continuous fields, or flow-based representations, including ParticleFormer [763], GAF [764], and
3DFlowAction [765]. Collectively, these methods introduce explicit spatial or physical structure into
predictive modeling to produce more reliable and control-relevant future states.
Policy Learning with WMs. World models not only serve as predictive environments but also provide
structured interfaces for policy learning and long-horizon control. A key direction lies in offline-to-
online adaptation, where methods such as MOTO and FOWM pretrain on large offline datasets and
then finetune policies in the real world [766, 767]. Diffusion-policy adaptation has also been integrated
into world models, as in DiWA, enabling efficient policy transfer across tasks [768]. Robustness to
language variation and viewpoint shifts is pursued in works such as LUMOS and ReViWo [769, 770].
Another line of research focuses on generalist pretraining or multi-stage learning pipelines that couple
reward, policy, and world model optimization [771–775]. Beyond architecture, several methods
exploit the latent dynamics of world models: Coupled distillation approaches design stable online
imitation rewards directly in the latent space [776], while WoMAP explicitly models 𝑝(𝑧𝑡+1 | 𝑧𝑡, 𝑎𝑡)
and a reward predictor, using rollouts with MPC to guide latent-space action selection [777]. Residual
Plan further refines this by searching for corrective residuals within latent rollouts [602]. Together,
these approaches demonstrate how structured WM interfaces can transform policy learning from raw
trial-and-error into efficient, robust, and generalizable control.
Systemization and Deployment. Beyond single-robot settings, recent efforts focus on scaling world
models to fleet- and platform-level deployments, making them more practical and accessible in
real-world robotics. Sirius-Fleet demonstrates multi-task fleet learning with shared visual world
models across distributed robots [778], highlighting collaborative scalability. Cosmos proposes a
foundation platform for physical AI, integrating modular world models to support diverse robotic
systems [779]. Similarly, Genie Envisioner introduces a unified world foundation platform for robotic
manipulation, aiming at standardized pretraining and deployment pipelines [780]. Together, these
system-level initiatives emphasize robustness, interoperability, and scalability, pushing WMs beyond
isolated benchmarks toward large-scale embodied AI platforms.
ii) Image or Video Prediction
Pure image or video prediction methods for robotics synthesize future visual signals or goal
imagery without learning explicit action-conditioned forward dynamics. At deployment, generators
may serve as control surrogates by providing visual plans, subgoals, or trajectories that controllers or
inverse dynamics can follow, or as data and representation engines for pretraining, augmentation,
and evaluation. Recent work includes video-as-policy and latent video planning [431, 781, 782],
foundation-model pretraining with generative video [783–785], human-to-robot transfer through
generated demonstrations [681, 786–788], policy or inverse-dynamics learning 𝑝(𝑎𝑡| 𝑠𝑡, 𝑠𝑡+ 1)
from predictive visual representations [789–791], controllable editing and goal imagery for data
and goal synthesis [792, 793], visual planning for robust control with goal-expressive plans and
subgoal filtering [794–797], self-improving or interpolation-based video supervision [798, 799], and
mining implicit dynamics in diffusion generators to support manipulation [800]. Collectively, these
approaches use generative models as visual surrogates or data engines rather than explicit world
models, yet they improve generalization and sample efficiency by providing structured goals, broad
visual coverage, and reusable predictive representations.
iii) Vision-Grounded Goal Extraction
Vision-grounded goal extraction refers to deriving task-relevant information directly from visual
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Waypoint
Optical Flow
Vision-Grounded Goal Extraction
World Model
Image or Video Prediction
w/ modeling of action
w/o modeling of action
Generative
Visual WMs
Image Prediction
Video Prediction
3D WMs
Contrastive Learning
Reconstruction
3D Generative Reconstruction
2D Masked Reconstruction
Text-Grounded Goal Extraction
Detection
Segmentation
Keypoint
Heatmap
Key-Patch
Gaze
Visual Track
Visual Trace
Figure 16 | Overview of the taxonomy of methods for learning with auxiliary tasks, highlighting
six core components: world models [759, 760], image or video prediction [790, 792], contrastive
learning [801, 802], masking reconstruction [803, 804], text-grounded goal extraction [434, 805],
and vision-grounded goal extraction [806–814].
inputs to support manipulation tasks. Examples include object detection and segmentation, visual
tracking, and optical flow, all of which provide structured cues that guide the robot’s actions.
Detection and Segmentation. These methods transform raw pixels into goal-bearing symbols,
such as sparse object proposals that indicate what or where to act, and dense masks that capture
precise geometry. Proposal-centric policies [815, 816] leverage pre-trained object proposals and
transformer reasoning to focus control on task-relevant entities. Segmentation-centric approaches
ground actions with language-conditioned masks or incorporate fine-grained semantic cues through
diffusion, enabling precise localization of task-critical regions even in cluttered scenes [817, 818]. For
open-world generalization, open-vocabulary detectors (e.g., Grounding-DINO [819]) and promptable
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
segmenters (e.g., SAM [820]) provide zero- or few-shot category grounding, which can be seamlessly
integrated into policy learning pipelines.
Gaze. Human gaze, either measured or predicted, serves as a compact attention prior with little
supervision that tells policies what to look at and when. First, foveated perception crops or reweights
features around fixations to enable high precision control and better sample efficiency in manip-
ulation [807, 821]. Second, gaze acts as a robustness and few-shot prior, suppressing distractors
and improving generalization under limited demonstrations [822, 823]. When eye trackers are
unavailable, video-based gaze prediction can supply similar priors during learning or inference [824].
Beyond attention shaping, gaze also structures behavior, revealing subtask boundaries and reusable
skill bottlenecks that facilitate modular policies [825, 826]. Related hand and eye action spaces offer
spatial invariance that complements gaze-driven attention [827]. Recent systems further integrate
gaze with foveated and vision transformers, scaling these benefits to cluttered scenes with improved
data and compute efficiency [807, 828].
Keypoint. Keypoint-based goal extraction encodes task-relevant landmarks in image or 3D space
into compact, object-relative representations that policies can consume directly. Compared with raw
pixels, keypoints provide geometric structure, interpretability, and improved generalization across
viewpoints and scenes. Recent work falls into several directions: supervised or semantic keypoints that
align with task semantics and affordances, enabling data-efficient manipulation and even bimanual
settings [829–831]; automatic discovery or task-driven selection that chooses a small set of informative
landmarks for robust policy learning [832]; large model-guided abstraction that infers object-relative
frames and stable anchors from language and vision [808]; tokenizing actions through keypoint
sequences to enable in-context imitation and rapid adaptation [833]; and hierarchical or open-world
frameworks that use keypoints as an interface for composing reusable skills [834]. Knowledge-guided
pipelines further stabilize keypoint definitions under distribution shifts by injecting priors about parts,
constraints, and contact patterns [835]. In practice, keypoints serve as inputs, conditioning variables,
or attention anchors for predicting poses, waypoints, and action parameters, offering a clean bridge
from perception to control.
Key-Patch. CALAMARI [809] formulates action as contact itself by predicting language-conditioned
contact formation maps in the image plane, so the policy decides where on a surface to make contact
rather than selecting a single point. The architecture factorizes perception and control at the natural
boundary of contact. A multimodal spatial action module aligns per-pixel action predictions with
observations, and a low-level controller then optimizes motion to maintain contact while avoiding
penetration. By leveraging visual language pretraining for spatial features, CALAMARI improves
grounding and sim-to-real transfer and demonstrates strong performance on contact-rich tasks such
as sweeping, wiping, and erasing, providing a clean key-patch interface from instruction to control.
Keypose. Keypose-based goal extraction selects a small set of SE(3) anchor states that summarize task
progress and provide precise geometric targets for control. Compared with pixel features or sparse
keypoints, keyposes carry subgoal semantics, mark completion events, and reduce compounding error
in multi-stage manipulation. Two representative directions illustrate this interface. KOI accelerates
online imitation by deriving hybrid key states from demonstrations, where semantic key states from
a vision language pipeline describe what to do and motion key states from optical flow describe
how to do it, yielding task-aware rewards that improve exploration efficiency in simulation and
real-world settings [836]. BiKC targets bimanual manipulation with a hierarchical policy in which
a high-level keypose predictor segments stages and conditions a low-level consistency model that
generates trajectories with fast inference and improved success and efficiency [810].
Waypoint. Waypoint-based goal extraction summarizes manipulation into a short sequence of
executable subgoals in task space, typically a handful of SE(3) poses that bridge perception and
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
control. By decoupling “what to achieve” from “how to move,” waypoints reduce covariate shift, ease
long-horizon planning, and provide a stable interface to motion controllers and consistency policies.
Two representative lines illustrate this interface. AWE learns to predict object-centric pick and place
waypoints directly from demonstrations, then delegates time parameterization and smoothing to
a low-level controller, yielding strong sample efficiency and robustness in cluttered scenes [811].
VIEW further systematizes the perception to waypoint pipeline with object relative frames and
consistency regularization so that the predicted subgoals remain geometrically coherent across views
and instances, improving generalization while retaining simple downstream control [837].
Visual Trace. Visual trace methods encode human intent as drawable primitives, such as sketches,
contours, and reticles, aligned with the scene and used as lightweight goal representations. Compared
with keypoints or waypoints, traces provide richer semantic guidance at low annotation cost and can
support both training and inference. Sketch-guided methods map freehand drawings to object-relative
motion plans for controllable trajectory following [812], while minimal visual cues use simple reticles
or marks to guide attention and spatial priors in clutter without modifying the policy backbone [838].
Visual Track. Visual track methods encode identity-consistent trajectories of scene points across time
and use them as an action or guidance space that bridges perception and control with low supervision
cost. Tracks can directly serve as actions for cross-embodiment transfer from human videos, with
2D motion tracks predicted from multiple views and then lifted to 6-DoF robot trajectories, yielding
strong few-shot performance in the real world [839]. Web videos can supervise track prediction to
produce an open-loop plan that is subsequently refined by a residual closed-loop policy, improving
generalization to novel objects and scenes [840]. Pre-training a trajectory model to predict future
paths of arbitrary points further supplies dense correspondence priors that boost visuomotor learning
with minimal action labels and enable transfer across morphologies [813]. Diffusion-generated
trajectories can guide policy optimization at the sequence level, reducing compounding error in
long-horizon tasks [841]. Complementary work prescribes a small set of semantically meaningful
points and propagates them through data with off-the-shelf vision models, creating stable anchors
that improve out-of-distribution generalization and can be tracked to condition policies [842].
Flow. Flow-based goal extraction treats motion fields as the interface between perception and control,
specifying how objects should move rather than only where they are. Under this lens, it is useful
to separate four flavors. Optical flow uses dense 2D correspondences from videos without action
labels to supervise policies or provide priors for planning and control, exemplified by the action-
from-video pipeline [843, 844]. Action flow encodes policy- or task-conditioned motion fields in
time and space, which can be fused with memory or generated by diffusion to coordinate multi-arm
behaviors and improve precision, as in ActionSink [845] and VLM-SFD [846]. Object-centric flow
defines motion on manipulated objects or parts, enabling cross-embodiment transfer and even reward
shaping [814, 847, 848], for example, Im2Flow2Act’s object-flow interface [814] and GenFlowRL’s
generative object-centric flow [848]. 3D flow lifts signals to scene flow, voxels, or point clouds
and often augments them with semantics, serving as pose-aware priors or world-model latents;
representative systems include G3Flow [849], 3DFlowAction [765], and ManiTrend [850], while
VIP [851] uses sparse point flows during pre-training and ToolFlowNet [852] predicts per-point tool
flow to ground contact-rich skills.
iii) Text-Grounded Goal Extraction
Recent advances in text-grounded goal extraction highlight the shift from simple language condi-
tioning toward explicitly parsing instructions into actionable goals, recovery strategies, or reasoning
steps. RACER introduces rich language-guided recovery policies that allow imitation learning agents
to adapt when failures occur, demonstrating how natural language can serve as a corrective signal
rather than only a task specifier [805]. EmbodiedGPT extends this idea to large-scale pretraining by
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
incorporating embodied chain-of-thought, enabling policies to follow multi-step reasoning trajectories
derived from textual instructions [434]. Along similar lines, CoTPC formulates chain-of-thought
predictive control, translating instructions into structured predictive sub-goals that can be optimized
in control loops [853]. Complementing these reasoning-oriented approaches, OCI leverages object-
centric instruction augmentation to link linguistic references more directly to specific entities in the
environment, thereby reducing ambiguity and improving manipulation precision [854]. Together,
these works demonstrate that grounding language into structured goals—whether through recovery
cues, reasoning chains, or object-level references—substantially improves robustness, generalization,
and interpretability in robotic manipulation.
iv) Contrastive Learning
The integration of contrastive learning into robotic manipulation can be organized into five
categories. First, universal representation learning employs large-scale contrastive pretraining on
internet or egocentric videos to obtain transferable embeddings that accelerate downstream robot
learning. R3M demonstrates how time-contrastive objectives yield general-purpose features for con-
trol and language grounding [801]. Second, language-conditioned alignment applies contrastive
objectives to couple visual states, natural language instructions, and robot actions. This line includes
BC-Z [162] and HULC [855], which align multimodal representations for zero-shot task general-
ization and robust imitation over unstructured datasets. Third, video-to-action alignment maps
human demonstration videos to robot policies via cross-modal contrastive learning. Vid2Robot [856]
leverages cross-attention transformers with video-conditioned contrastive losses to bridge video-to-
robot execution. Fourth, contrastive imitation learning directly integrates contrastive losses into
imitation pipelines, supervising alignment of embeddings with action trajectories or policy heads.
Σ-agent [802] exemplifies this by combining contrastive imitation with multi-task, language-guided
manipulation. Finally, action-sequence contrastive supervision contrasts correct and incorrect ac-
tion trajectories to shape representations tailored for policy optimization, as in CLASS [857]. This
five-category taxonomy disentangles overlapping use cases—representation pretraining, multimodal
alignment, video-conditioned imitation, contrastive IL, and trajectory-level supervision—providing a
clear structure for surveying contrastive methods in manipulation.
v) Reconstruction
Reconstruction has emerged as a powerful self-supervised pretraining strategy for robot manipu-
lation, encompassing both masked modeling and generative reconstruction paradigms. The central
idea is to recover or predict missing or novel observations such as masked pixels, tokens, or 3D
representations from partial inputs. By compelling the model to infer the underlying structure of the
environment and action space, reconstruction-based pretraining promotes the learning of rich and
structured representations. These representations can then be transferred to downstream imitation or
reinforcement learning tasks, improving sample efficiency, robustness, and cross-task generalization.
Existing works can be broadly categorized into two groups: (1) 2D masked reconstruction, which
focuses on reconstructing intentionally occluded or masked inputs, and (2) 3D reconstruction, which
encompasses both 3D masked reconstruction and generative reconstruction approaches that predict
unseen views, 3D feature fields, or future observations.
2D Masked Reconstruction. Early methods focused on reconstructing masked pixels or spatiotemporal
tokens from egocentric robot data. MVP introduced masked visual pretraining for real-world robotic
control, showing strong transfer across manipulation tasks [858]. STP extended this to spatiotemporal
predictive pretraining for motor control [859], while sensorimotor pretraining methods coupled visual
masking with proprioceptive prediction to learn multimodal embeddings [860]. MUTEX [861] and
Voltron [804] further demonstrated how masked reconstruction can be combined with multimodal
task specifications and language grounding.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
3D Reconstruction. Beyond pixel masking, 3D reconstruction approaches leverage multiview images,
point clouds, or implicit feature fields to learn spatially consistent representations, often in SE(3)-
equivariant forms [760, 803, 862–870]. 3D-MVP performed masked multiview pretraining for
robust manipulation policies [866], while SPA introduced spatial-awareness masking to enhance
embodied representations [865]. Lift3D demonstrated how to “lift” 2D pretrained models into
3D spaces [867], and CL3R combined 3D reconstruction with contrastive learning for enhanced
manipulation features [869]. Perceiver-actor models such as PerAct [871], M2T2 [872], and RVT-
2 [873] integrate masked pretraining into transformer-based architectures for multi-task pick-and-
place. Recent generative 3D methods extend this trend: GNFactor [803] employs neural feature fields
for volumetric reconstruction, while NeRF-style formulations explore corrective augmentation and
novel-view synthesis for manipulation [874].
Reconstruction thus serves as a unifying self-supervised scaffold across modalities. 2D masked
methods emphasize scalable pretraining from large-scale egocentric video and multimodal signals,
while 3D reconstruction approaches—whether masked or generative—focus on spatial consistency,
equivariance, and viewpoint robustness. Together, these methods establish reconstruction-based
pretraining as a key enabler of sample-efficient and generalizable manipulation policies.
6.2. Input Modeling
Input modeling defines how robots perceive and represent the world through various sensory modal-
ities, determining what inputs are used and how they are processed before being fed into control
or policy models. It encompasses the selection and encoding of multimodal observations—such as
vision, language, touch, force, or audio—and the transformation of these raw signals into structured
representations suitable for learning and decision-making. Effective input modeling ensures that
sensory data are aligned, fused, and abstracted in a way that preserves essential spatial, temporal,
and semantic information, thereby enabling robust perception, reasoning, and control across diverse
manipulation tasks.
6.2.1. Vision-Action Models
2D Vision as Input. The development of Vision Action Models largely relies on 2D visual observa-
tions [80, 81, 875–881], often captured by multi-view RGB cameras. Representative architectures
include convolutional, Transformer-based, and diffusion-based policies. Vi-PRoM [80] employs
ResNet-50 [64] to extract visual features for manipulation, while HDP [875] introduces hierarchical
policy learning for efficient visuomotor control. HPT [876] uses a Transformer backbone to align
vision and proprioception across embodiments. Diffusion Policy [81] represents a major shift by
modeling visuomotor control as conditional denoising, while Consistency Policy [879] substantially
accelerates diffusion-based action generation through consistency distillation. Beyond policy architec-
tures, recent work highlights the importance of visual sensing itself: Rethinking Camera Choice [882]
systematically studies fisheye cameras and shows how field of view and visual diversity affect spatial
localization and generalization. Despite their effectiveness, 2D visual-action models lack explicit 3D
grounding, motivating 3D-aware policies that directly align actions with scene geometry.
3D Vision as Input. An increasing number of vision–action models incorporate explicit 3D observations
of the physical environment [873, 883–892]. By leveraging multi-view transformations, RVT [883]
and RVT-2 [873] explicitly enhance task execution efficiency and generalization, thereby improving
performance in real-world applications. GenDP [884] significantly improves success rates on unseen
instances and enables category-level generalization by addressing the generalization limitations of
diffusion policies through 3D semantic fields derived from multi-view RGBD observations. DP3 [885]
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
conditions the diffusion model on 3D point-cloud representations and robot states, enabling efficient
execution of complex manipulation tasks with the Allegro Hand. 3D-FDP [886] leverages scene-
level 3D flow as a structured intermediate representation to capture fine-grained local motion cues.
However, while these models provide 3D-aware capabilities lacking in 2D Vision-Action models, their
absence of textual semantic information ultimately limits their generalization and robustness in the
real world.
6.2.2. Vision-Language-Action Models
Recent progress in Vision–Language–Action (VLA) models has created a unified paradigm for map-
ping multimodal perception into executable robotic behaviors. Compared with earlier vision-only or
language-conditioned controllers, VLAs integrate semantic grounding, spatial reasoning, and sequen-
tial action generation within a single architecture. To provide a systematic overview, we summarize the
landscape in a taxonomy (Figure 17) that organizes existing work by input modality (2D and 3D) and
by methodological orientation, distinguishing model-oriented approaches (architectural innovations)
from model-agnostic ones (inference, training, or efficiency enhancements). This taxonomy clarifies
technical differences, shared design trade-offs, and the evolution of VLAs toward scalable, robust,
and general-purpose robotic intelligence.
i) 2D Vision as Input
Most VLAs rely on 2D images from RGB cameras, sometimes with multi-view setups, as the
primary perceptual stream. Within this setting, a diverse set of methods has emerged, which can
be broadly divided into model-oriented approaches that redesign the policy architecture itself, and
model-agnostic strategies that improve inference or training without altering the core model.
Model-oriented Approaches. Model-oriented approaches focus on advancing the architecture and
internal structure of VLA models to improve their representation learning, reasoning ability, and task
adaptability. Instead of modifying training schemes or inference strategies, these methods emphasize
redesigning the policy backbone, integrating multimodal modules, and structuring control hierarchies
to better align perception, reasoning, and action.
• Non-LLM-based VLA. Early approaches directly mapped visual observations and language
instructions to robot actions without relying on large language-model backbones. RT-1 [163] pio-
neered scalable Transformer-based action prediction from large robot datasets, while VIMA [106] and
HULC [855] extended language-conditioned control toward multimodal prompts and unstructured
demonstrations. More recent methods improve scalability and action modeling. Octo [894] trains
a generalist Transformer policy on large-scale cross-embodiment robot data and supports efficient
adaptation to new robots and action spaces, while MDT [895] combines multimodal goal condition-
ing with diffusion-based action generation under sparse language annotations. Dita [899] further
scales Diffusion Transformers to directly model continuous action sequences across heterogeneous
embodiments. Collectively, these methods demonstrate that scalable multimodal policy learning can
achieve broad manipulation capabilities without large language backbones, while motivating stronger
semantic priors for open-world generalization.
• LLM/VLM-based VLA. With the rise of LLMs and VLMs, robotic policies increasingly leverage
web-scale semantic priors for action generation. RT-2 [12] co-trains vision-language and robot data
with tokenized actions, enabling improved generalization to novel objects and instructions and emer-
gent semantic reasoning. RoboFlamingo [905] adapts pretrained VLMs to manipulation through
lightweight fine-tuning and an explicit policy head, while OpenVLA [13] scales open-source VLA train-
ing across diverse robot demonstrations. 𝜋0 [907] and 𝜋0.5 [908] further introduce flow-matching
action generation and large-scale cross-embodiment training. Recent work increasingly focuses on
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Vision-Language-Action Models (§ 6.2.2)
2D Vision as Input
Model-oriented
Non-LLM-based VLA
RT-1 [163], VIMA [106], HULC [855], HULC++ [893], Octo [894], MDT [895],
BAKU [896], MResT [897], LISA [898], Dita [899], OTTER [900], RoboGround [901],
Bi-LAT [902], GR-1 [783], TwinVLA [903], STEER [904]
LLM/VLM-based VLA
RT-2 [12], RoboFlamingo [905], OpenVLA [13], OpenVLA-OFT [906], 𝜋0 [907],
𝜋0.5 [908], CogACT [909], RoboVLMs [910], RoboMamba [911], Magma [912],
Diffusion-VLA [913], DexVLA [914], ChatVLA [915], HybridVLA [916],
InstructVLA [917], X-VLA [918], UD-VLA [919], GR-3 [920], Interleave-VLA [921]
Latent Learning for VLA
QueST [922], UniVLA [923], VQ-VLA [924], villa-X [925], MemoryVLA [926],
ViPRA [927], LARA [928], LDA-1B [929], From Pixels to Tokens [930],
LaRA-VLA [931], Fast-ThinkAct [932], Chain of World [933], JALA [934],
VLA-JEPA [935]
Hierarchical VLA
RT-H [936], PIVOT-R [937], Hi Robot [938], HiBerNAC [939], H-GAR [940],
MemER [941]
Dual-/Multi-system VLA
LCB [942], DP-VLA [943], HiRT [944], RoboDual [945], Fast-in-Slow [946],
Hume [567], OpenHelix [947], RationalVLA [948], TriVLA [949], G0 [950],
Libra-VLA [951]
Model-agnostic
Training-time
Optimization
Knowledge Insulation [952], RETAIN [953], FAN [954], T-MEE [955], MAPS [956],
RICL [957], CronusVLA [958], [959], MoIRA [960]
Inference-time
Optimization
VOTE [961], RoboMonkey [962], AR-VRM [963], Mechanistic Steering [964],
VLA-Reasoner [965], TapSampling [966], CO-RFT [967], [968], [969]
Reinforcement Learning
and Post-training
V-GPS [540], iRe-VLA [542], ConRFT [545], RLDG [539], ThinkAct [970],
VLA-RL [544], RIPT-VLA [543], SimpleVLA-RL [971], RL4VLA [564],
ManipLVM-R1 [972], [973], [974], DyGRO-VLA [975], VLA-RFT [976]
Learning with Auxiliary
Tasks
ECoT [977], CoT-VLA [978], TraceVLA [979], Seer [791], UP-VLA [980], MOO [981],
DreamVLA [982], ReconVLA [983], Emma-X [984], RAD [985], VLA-OS [986],
OneTwoVLA [987], ACoT-VLA [988], RoboInter [989], HiF-VLA [990], A0 [991],
Action-Sketcher [992], CrayonRobo [993], ControlVLA [994], LLARVA [995]
Efficiency
TinyVLA [996], NoRA [997], SmolVLA [998], Flower [999], VLA-Adapter [1000],
[1001], Evo-1 [1002], DeeR-VLA [1003], EfficientVLA [1004], MoLe-VLA [1005],
CogVLA [1006], SP-VLA [1007], VLA-Cache [1008], QVLA [1009], QuantVLA [1010],
[1011], Spec-VLA [1012], BEAST [1013], PD-VLA [1014], Fast-dVLA [1015],
BlockVLA [1016] RTC [1017], REMAC [1018], TTF-VLA [1019], CEED-VLA [1020]
Robustness
SAFE [1021], FAIL-Detect [649], RACER [805], BYOVLA [1022], RobustVLA [1023],
StableVLA [1024], BadVLA [1025], Phantom Menace [1026], [1027], [1028]
Generalization
LongVLA [1029], LoHoVLA [1030], BehaviorVLA [1031], [1032], [1033],
FOCA [1034], AtomicVLA [1035], [1036], BagelVLA [1037], PALM [1038], Spatial
Memory [1039]
3D Vision as Input
Model-oriented
3D Embedding and
Fusion
SpatialVLA [1040], 3D-CAVLA [1041], GeoVLA [1042], FP3 [1043], VoxAct-B [1044],
VIHE [1045], OG-VLA [1046], RoboMM [1047], PointACT [1048], PointVLA [1049]
Spatial Alignment and
Guidance
BridgeVLA [1050], FALCON [1051]
Multi-view and Active
Perception
Learning to See and Act [1052], Cortical Policy [1053]
3D/4D Reasoning and
Prediction
evo-0 [1054], 3D-VLA [1055], ConsisVLA-4D [1056], PhysMani [1057],
GraphCoT-VLA [1058], ChainedDiffuser [1059],
Model-agnostic
Training-time
Optimization
Spatial Forcing [1060], GeoPredict [1061]
Inference-time
Optimization
Affordance Field Intervention [1062], DepthCache [1063]
Figure 17 | A structured taxonomy of VLA models organized by input modality (2D vs. 3D) and
methodological orientation (model-oriented architectures vs. model-agnostic strategies).
coupling semantic reasoning with expressive action models. DiffusionVLA [913] combines autoregres-
sive VLM reasoning with diffusion-based action generation, while DexVLA [914] introduces a large
diffusion action expert for cross-embodiment and dexterous control. Together, these developments
shift VLA research from simply transferring semantic priors toward tighter integration of reasoning,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
generalization, and continuous motor generation.
• Latent Learning for VLA. Latent learning introduces compact intermediate representations be-
tween multimodal perception and action generation, supporting action abstraction, internal reasoning,
and predictive modeling. Early approaches primarily focus on action representation: QueST [922]
learns quantized temporal skill abstractions for continuous control, while VQ-VLA [924] scales vector-
quantized action tokenization over large trajectory datasets. UniVLA [923] further learns task-centric
latent actions from videos, enabling pre-training across embodiments and viewpoints. Recent work
extends latent learning beyond action compression toward internal reasoning. Latent Reasoning
VLA [931] internalizes multimodal reasoning and future prediction into continuous latent states,
while Fast-ThinkAct [932] distills explicit reasoning into compact latent plans for efficient action
generation. Chain of World [933] further combines latent motion representations with world-model
prediction, allowing temporal dynamics to guide downstream actions. Overall, latent learning is
evolving from compact action representations toward unified latent spaces for action abstraction, rea-
soning, and future prediction, with the key challenge of preserving task relevance, physical grounding,
and alignment with executable actions.
• Hierarchical VLA. Long-horizon and compositional tasks motivate hierarchical designs that
decompose control into intermediate instructions, primitives, waypoints, or skills. Hi Robot [938]
separates high-level VLM reasoning from low-level VLA execution, enabling open-ended instruction
following and interactive task refinement. RT-H [936] introduces hierarchical action abstractions,
while PIVOT-R [937] combines primitive parsing, waypoint prediction, and low-level action decod-
ing through an asynchronous hierarchical executor. Such structures improve interpretability and
long-horizon execution, but introduce challenges in learning reliable intermediate abstractions and
preventing high-level errors from propagating downstream.
• Dual- and Multi-System VLA. Inspired by dual-process cognition, these architectures decouple
slow semantic reasoning from fast visuomotor execution. LCB [942] introduces a learnable latent
action code to communicate high-level LLM intent to low-level policies beyond explicit language
interfaces. DP-VLA [943] and HiRT [944] further decouple execution frequencies, using slowly
updated VLM representations to guide lightweight policies that react to real-time observations.
OpenHelix [947] systematically studies this interface and shows the importance of policy pre-training,
projector pre-alignment, and multimodal supervision, while revealing that high-level latent tokens
may otherwise encode instruction semantics more strongly than dynamic visual changes. Fast-in-
Slow [946] instead embeds the fast action module within the slow VLM through partial parameter
sharing and joint co-training. Libra-VLA [951] explicitly communicates discrete macro-intents to
a continuous action refiner through asynchronous coarse-to-fine execution. Beyond dual systems,
TriVLA [949] adds a video-based dynamics module to couple semantic perception, future prediction,
and real-time control. These developments shift structured VLAs from simple frequency separation
toward tighter reasoning–action communication and predictive multi-system coordination.
Model-agnostic Strategies. Model-agnostic strategies aim to enhance the performance, reliability,
and efficiency of VLA models without modifying their underlying architecture. Rather than redesigning
model structures, these approaches operate at the inference, training, or auxiliary supervision level to
improve decision quality, generalization, and deployment practicality.
• Training-Time Optimization. Training-time strategies improve VLA adaptation through op-
timization objectives or parameter-update schemes without redesigning the policy architecture.
Knowledge Insulation [952] mitigates interference between newly initialized action modules and pre-
trained VLM representations through gradient insulation and multimodal co-training. RETAIN [953]
merges pretrained and task-finetuned parameters to preserve generalist capabilities during adapta-
tion, while FAN-guided finetuning [954] exploits feasible action neighborhoods to improve sample
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
efficiency and generalization. T-MEE [955] instead reshapes trajectory-level action error distributions
through minimum error entropy, improving robustness to few-shot, noisy, and imbalanced training
data. Together, these methods improve VLA training through knowledge preservation, structured
action supervision, and robust optimization.
• Inference-Time Optimization. Inference-time methods improve VLA execution without mod-
ifying the underlying policy architecture. VOTE [961] and RoboMonkey [962] generate multiple
action candidates and improve selection through ensemble voting or learned verification. More recent
methods explore stronger test-time scaling mechanisms. TapSampling [966] samples actions in
a learned latent space and selects them using a task-progress verifier, while verifier-free test-time
sampling [968] exploits the model’s internal distributional confidence to rank candidates without an
external verifier. Adaptive Action Chunking [969] instead dynamically adjusts the execution horizon
according to action uncertainty, balancing temporal consistency and responsiveness. Together, these
approaches shift VLA inference from single-shot prediction toward adaptive sampling, verification,
and execution.
• Reinforcement Learning and Post-training. RL-based post-training improves pretrained
VLAs through reward-driven interaction, enabling policies to move beyond imitation and adapt to
deployment distributions. SimpleVLA-RL [971] demonstrates scalable online RL with sparse outcome
rewards, while ConRFT [545] combines offline and online reinforced fine-tuning for sample-efficient
real-world adaptation. iRe-VLA [542] alternates RL and supervised learning to stabilize online VLA
optimization, whereas adaptive offline RL [974] balances advantage signals and gradient variance
for flow-based policies. Recent studies further examine broader roles of RL: empirical analysis [564]
shows that RL primarily improves semantic generalization and execution robustness, while residual-RL-
based self-improvement [973] uses RL to discover failure-recovery behaviors and distills the resulting
trajectories back into a generalist policy. Together, these developments shift VLA post-training from
simple task-specific fine-tuning toward scalable online adaptation, robust offline optimization, and
self-improving data generation.
• Learning with Auxiliary Tasks. Auxiliary objectives enrich VLA learning with intermediate
reasoning, structured representations, and predictive supervision beyond action imitation. ECoT [977]
and CoT-VLA [978] introduce embodied and visual chain-of-thought supervision, while ACoT-VLA
grounds intermediate reasoning in action generation. Visual intermediate representations are ex-
plored by TraceVLA [979], whereas RoboInter learns broader robotic intermediate representations to
improve perception–action grounding. Predictive objectives provide temporal supervision: Seer [791]
learns future-aware inverse dynamics, and HiF-VLA incorporates hindsight and foresight through
motion representations. Reconstruction- and world-aware objectives such as DreamVLA [982] and
ReconVLA [983] further improve representation learning. Overall, auxiliary tasks are evolving from
explicit reasoning traces toward multimodal intermediate representations and predictive supervision
that better connect perception, reasoning, and action.
• Efficiency. Recent work improves VLA efficiency across model size, computation, representation,
and execution. Compact policies such as TinyVLA [996], FLOWER [999], and Evo-1 [1002] reduce
model complexity while retaining competitive manipulation performance. At the computation level,
DeeR-VLA [1003] dynamically allocates inference depth, EfficientVLA [1004] performs training-free
acceleration and compression, and VLA-Cache [1008] exploits temporal redundancy through adaptive
token caching. Quantization methods such as QVLA [1009] and QuantVLA [1010] further reduce
memory and computation through VLA-specific low-precision inference. Action-side compression
provides another route: BEAST [1013] encodes trajectories with compact B-spline representations
to reduce autoregressive decoding steps. Finally, RTC [1017] enables asynchronous execution of
action-chunking flow policies to mitigate inference-induced control latency. Together, these methods
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
extend VLA efficiency from model compression toward joint optimization of computation, memory,
action representation, and real-time execution.
• Robustness. Robustness has become a central requirement for reliable VLA deployment under
distribution shifts, execution failures, and adversarial disturbances. RobustVLA [1023] systemati-
cally studies perturbations across actions, observations, instructions, and environments, and jointly
improves input and output robustness through consistency and robust optimization. For visual dis-
turbances, BYOVLA [1022] performs test-time observation intervention, while StableVLA [1024]
suppresses unseen visual corruptions through information-bottleneck-based feature filtering. Failure
awareness provides another line of defense: SAFE [1021] learns task-general failure signals from VLA
representations, whereas FAIL-Detect [649] performs uncertainty-aware sequential OOD detection
without requiring failure demonstrations; RACER [805] further enables language-guided failure recov-
ery. Security-oriented studies expose complementary vulnerabilities, with BadVLA [1025] revealing
persistent backdoor attacks and Phantom Menace [1026] analyzing and mitigating physical sensor
attacks. Together, these works broaden VLA robustness from visual resilience toward multimodal
perturbation tolerance, failure awareness and recovery, and adversarial security.
• Generalization. Generalization remains a central challenge for VLAs across task horizon,
embodiment, environment, and data regimes. Long-VLA [1029] improves long-horizon execution
through phase-aware modeling, while BehaviorVLA [1031] learns temporally coherent behavior
representations robust to distribution shifts. Cross-embodiment approaches such as XL-VLA [1032]
introduce shared latent action spaces across heterogeneous robot hands. Beyond embodiment transfer,
sim-to-real methods [1033] increase environmental diversity by translating simulated trajectories into
realistic training videos, whereas FOCA [1034] targets few-shot adaptation through future-oriented
conditioning. AtomicVLA [1035] supports continual skill acquisition through extensible atomic skill
experts, while long-tail learning [1036] addresses data-scarce tasks. Together, these studies broaden
VLA generalization from unseen objects and scenes toward new embodiments, longer task horizons,
limited-data adaptation, and expanding skill distributions.
Together, the 2D VLA landscape illustrates a clear trajectory: starting from direct end-to-end
policies, evolving into architectures that leverage semantic priors from LLMs/VLMs, and further into
modular, hierarchical, or multi-system designs. Complemented by model-agnostic techniques for
optimization, reinforcement, and robustness, these developments collectively point toward a new
generation of VLAs that balance efficiency, interpretability, and scalability.
ii) 3D Vision as Input
Compared with 2D inputs, 3D representations provide richer spatial grounding for contact-rich
manipulation and long-horizon planning. However, because most VLM backbones are pre-trained
on 2D image–text data, they lack intrinsic 3D understanding. This has motivated research into how
VLAs can incorporate explicit 3D perception, which can be broadly divided into Model-oriented
approaches that redesign architectures to integrate 3D information, and Model-agnostic strategies
that introduce auxiliary mechanisms without altering the backbone.
Model-oriented Approaches. Model-oriented approaches explicitly augment the representation or
policy architecture with geometry-aware components. Rather than relying solely on planar image
features, these methods introduce point-cloud, depth, voxel, multi-view, or geometry-foundation
representations to improve spatial grounding and action prediction.
• 3D Embedding and Fusion. A primary direction is to integrate explicit 3D observations
with pretrained 2D vision–language representations. SpatialVLA [1040] introduces geometry-aware
position encodings and adaptive action grids to inject spatial structure into VLA prediction, while
VoxAct-B [1044] and VIHE [1045] exploit voxelized or virtual-view representations for fine-grained 3D
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
manipulation. Other methods explore complementary geometric representations: 3D-CAVLA [1041]
incorporates depth and 3D context, GeoVLA [1042] introduces point-based geometric features,
OG-VLA [1046] converts 3D observations into orthographic views, and FP3 [1043] investigates large-
scale 3D policy learning. More recently, PointACT [1048] directly couples hierarchical point-cloud
representations with action decoding through multi-scale point–action interaction, allowing action
tokens to exploit both local geometric details and global scene structure. Together, these approaches
demonstrate different ways of coupling explicit 3D geometry with pretrained semantic representations
for spatially grounded control.
• Spatial Alignment and Guidance. A complementary direction focuses on aligning geo-
metric and semantic representations rather than directly replacing image features with 3D inputs.
BridgeVLA [1050] projects 3D observations into multiple 2D views and formulates action prediction
as spatial heatmaps, thereby aligning both perception and action prediction with representations
readily processed by pretrained vision models. FALCON [1051] instead extracts spatial priors from
spatial foundation models and injects the resulting spatial tokens into an enhanced action pathway,
preserving the pretrained vision–language representation while strengthening geometric reasoning.
These approaches reflect a shift from directly encoding geometric observations toward explicitly
bridging pretrained semantic features and transferable spatial priors.
• Multi-view and Active Perception. Multiple viewpoints provide another mechanism for
reducing occlusion and depth ambiguity. Learning to See and Act [1052] reconstructs scenes and
selects task-relevant virtual viewpoints, allowing the policy to acquire informative observations rather
than relying on fixed cameras. Cortical Policy [1053] models complementary static and dynamic
visual streams and exploits cross-view geometric correspondence to strengthen spatial reasoning while
preserving motion-sensitive information for control. Such methods extend 3D perception from passive
multi-view fusion toward task-conditioned viewpoint selection and cross-view reasoning, particularly
useful under occlusion, viewpoint variation, and dynamic interaction.
• 3D/4D Reasoning and Prediction. Beyond static geometric representations, another line
models spatial structures and their evolution over time. 3D-VLA [1055] is an early representative
that combines language-conditioned 3D generation with action prediction, casting VLA learning as
a generative 3D world-modeling problem. ConsisVLA-4D [1056] extends spatial modeling toward
spatiotemporal consistency by reasoning across views, objects, and temporally evolving scene states.
For dynamic-object manipulation, PhysMani [1057] couples a physics-principled 3D Gaussian world
model with a future-aware policy to predict physically grounded scene dynamics before action
generation. GraphCoT-VLA [1058] complements predictive world modeling with structured spatial
reasoning, representing 3D relations as graphs and connecting intermediate reasoning states to
downstream action generation. Together, these methods extend 3D VLAs from static geometric
perception toward structured reasoning and temporally coherent prediction of geometry, motion, and
interaction outcomes.
Model-agnostic Strategies. Model-agnostic strategies preserve the underlying VLA architecture
to a greater extent and instead use 3D information as auxiliary supervision or external guidance.
Compared with model-oriented 3D VLAs, this direction remains less extensively explored, but recent
work has begun to reveal how geometric information can improve existing policies without making
explicit 3D processing an indispensable component of the deployed backbone.
• Training-time Optimization. Training-time strategies transfer geometric knowledge into a
VLA primarily through additional supervision. Spatial Forcing [1060] aligns intermediate VLA visual
representations with geometric features produced by pretrained 3D foundation models, encouraging
spatially informative representations without requiring explicit depth or point-cloud inputs during
inference. GeoPredict [1061] instead introduces predictive supervision over multi-step 3D robot
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
keypoints and future 3D Gaussian geometry; these geometric predictors are used during training,
whereas deployment avoids explicit 3D decoding. The two approaches therefore inject 3D information
at different levels—representation alignment and predictive supervision, respectively—while retaining
relatively lightweight inference.
• Inference-time Optimization. A smaller but emerging line exploits geometric information at in-
ference time without retraining the underlying VLA policy. Affordance Field Intervention (AFI) [1062]
introduces an external 3D spatial affordance field as an on-demand plug-in to detect unfavorable
behaviors, guide rollback and waypoint search, and score candidate trajectories during execution.
DepthCache [1063] instead uses depth as a structural prior for training-free visual-token merging,
preserving geometrically important near-field regions while compressing redundant background
tokens. These studies suggest that 3D information can serve not only as a perception modality but
also as an external signal for runtime correction and inference efficiency. Nevertheless, compared
with the mature inference-time optimization literature for 2D VLAs, systematic studies of sampling,
verification, caching, and lightweight spatial guidance remain relatively limited in 3D settings.
Across both 2D and 3D modalities, VLA research shows converging trends. Model-oriented
approaches aim to strengthen representational capacity by incorporating LLM and VLM priors, latent
structures, and hierarchical reasoning in 2D, and by leveraging embeddings, alignment mechanisms,
and world models in 3D. Complementing these, model-agnostic strategies emphasize improving
inference robustness and efficiency with minimal retraining. Looking ahead, key directions include
the standardization of 3D representations in VLAs, the development of hybrid frameworks that
integrate reactive control with deliberative planning through safety-aware dual systems, and co-
training across 2D and 3D modalities to couple large-scale priors with spatial grounding. Together,
these advances move beyond scaling backbone models toward architectures that explicitly integrate
perception, memory, planning, and control, evaluated under long-horizon, cross-embodiment, and
real-world deployment challenges.
6.2.3. Tactile-based Action Models
Tactile sensing provides direct information about contact, force, slip, compliance, and other physical
properties that are difficult to infer reliably from vision alone. Such feedback is particularly important
for contact-rich and partially observable manipulation, where small geometric or force errors can
lead to task failure. Recent tactile-based action models have therefore evolved from task-specific
tactile feedback integration toward pretrained tactile representations, visuo-tactile policy learning,
language-grounded touch understanding, and tactile-augmented generalist policies.
Tactile Representation and Latent Learning. Representation learning provides reusable tactile
features that can be transferred across tasks and policies. T-DEX [1064] learns self-supervised tactile
representations from robotic play to support dexterous manipulation, while Sparsh [1065] scales
self-supervised pretraining to learn generalizable representations from vision-based tactile sensing.
CLTP [1066] introduces contrastive language–tactile pretraining to align tactile geometry with
natural language for 3D contact understanding. Moving toward interaction-aware representations,
exUMI [1067] proposes action-aware Tactile Predictive Pretraining that learns contact dynamics by
predicting future tactile observations conditioned on robot actions and visual context. Tactile Beyond
Pixels [1068] extends tactile representation learning beyond image-based signals by jointly modeling
sensory cues such as force, motion, and sound. Together, these works show a progression from generic
self-supervised tactile encoding toward action-conditioned and multisensory representations that
directly capture physical interaction dynamics.
Tactile-Action Models. Tactile-action models directly condition manipulation policies or control
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Tactile-based Action Models § 6.2.3
Tactile Representation and
Latent Learning
T-DEX [1064], Sparsh [1065], CLTP [1066], exUMI [1067],
Tactile Beyond Pixels [1068]
Tactile-Action Models
Seq2Seq Imitation [1069], RoboPack [1070], MimicTouch [1071],
Feel the Force [1072], SimShear [1073]
Tactile-Vision-Action Models
RotateIt [1074], [1075], VTTB [1076], VITaL [1077], VT-Refine [1078],
Reactive Diffusion Policy [1079], ViTaS [1080], ViTacGen [1081],
ViTacFormer [1082], GelFusion [1083]
Tactile-Language Grounding
Octopi [1084], TLA [1085]
Tactile-Vision-Language-Action Models
FuSe [1086], VLA-Touch [1087], Tactile-VLA [1088], OmniVTLA [1089],
VTLA [1090], T-Rex [1091], FTP-1 [1092]
Figure 18 | A structured overview of tactile-based action models.
models on tactile feedback without necessarily relying on vision–language reasoning. Seq2Seq
Imitation [1069] formulates tactile feedback as a sequential input for imitation learning under partial
observability. RoboPack [1070] instead incorporates tactile observations into learned dynamics
models for model-predictive control, enabling precise dense-packing behaviors. MimicTouch [1071]
transfers multimodal human tactile demonstrations to contact-rich robotic manipulation, while Feel
the Force [1072] captures human contact forces with tactile gloves to train transferable force-aware
manipulation policies. SimShear [1073] further addresses sim-to-real tactile control by synthesizing
shear-aware tactile observations and transferring tactile servoing policies to real contact-sensitive
tasks. These methods illustrate how tactile feedback can support not only reactive control but also
dynamics prediction, human-to-robot transfer, and sim-to-real policy learning.
Tactile-Vision-Action Models. Combining vision and touch enables policies to exploit complementary
global and local information, with vision providing scene-level context and tactile sensing resolving
fine-grained contact states. RotateIt [1074] combines visual and tactile observations to generalize
in-hand object rotation, while Multimodal-SeeThrough [1075] uses a transparent visuotactile sensor
together with force-matched demonstrations for imitation learning. VTTB [1076] integrates visual
and tactile feedback for adaptive robot-assisted bed bathing, and VITaL [1077] introduces visuo-tactile
pretraining to improve both tactile-based and vision-only manipulation policies. Reactive Diffusion
Policy [1079] adopts a slow–fast visual-tactile diffusion architecture to improve responsiveness
during contact-rich manipulation. More recent work explores stronger multimodal training and
transfer: VT-Refine [1078] combines real visuo-tactile demonstrations with tactile simulation and
reinforcement-learning fine-tuning for precise bimanual assembly; ViTaS [1080] uses soft-fusion
contrastive learning to model both the alignment and complementarity between vision and touch; and
ViTacGen [1081] generates standardized tactile representations from visual observations, allowing
tactile-informed policies to operate even when high-resolution tactile sensors are unavailable during
deployment. Overall, visuo-tactile policies are shifting from direct modality concatenation toward
structured fusion, predictive tactile generation, and simulation-assisted policy improvement.
Tactile-Language Grounding. Language provides a shared semantic space for interpreting tactile
observations and connecting physical properties with task intent. Octopi [1084] develops a large
tactile-language model for reasoning about object properties such as hardness and material charac-
teristics from touch. TLA [1085] extends tactile-language alignment toward action generation by
learning mappings among tactile sequences, language instructions, and manipulation actions. These
approaches establish tactile-language grounding as an interface between low-level contact signals
and higher-level semantic reasoning.
Tactile-Vision-Action Models. Combining vision and touch enables policies to exploit comple-
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
mentary global scene context and local contact information. RotateIt [1074] combines visual and
tactile observations for generalized in-hand rotation, while Multimodal-SeeThrough [1075] uses
visuotactile sensing with force-matched demonstrations for imitation learning. Funk et al. [1093]
further demonstrate the importance of tactile feedback for fast contact-rich manipulation through
robotic match lighting. VTTB [1076] integrates vision and touch for adaptive bed bathing, whereas
VITaL [1077] introduces visuo-tactile pretraining for manipulation. Touch Begins Where Vision
Ends [1094] combines VLM-based object localization with a reusable local visuo-tactile policy to
generalize contact-rich skills across scenes. Reactive Diffusion Policy [1079] adopts a slow–fast visual-
tactile diffusion architecture for responsive control. More recent methods improve multimodal fusion
and transfer: VT-Refine [1078] combines real demonstrations, tactile simulation, and RL fine-tuning;
ViTaS [1080] models vision–touch alignment and complementarity through contrastive learning; and
ViTacGen [1081] generates standardized tactile representations from vision. Overall, visuo-tactile
policies are progressing from direct sensory fusion toward structured multimodal learning, reusable
local control, and simulation-assisted transfer.
6.2.4. Extra Modalities as Input
Beyond vision, language, and tactile sensing, additional physical modalities such as force, audio,
infrared, and radar provide complementary information that is difficult to infer reliably from im-
ages alone. These signals are particularly useful for contact-rich manipulation, partially observable
interactions, and environments in which visual observations are ambiguous or degraded. Existing
approaches have progressed from incorporating individual sensing channels into task-specific control
policies toward integrating heterogeneous physical feedback into generalist VLA models.
Force. Force and torque provide direct measurements of physical interaction and have long been used
to improve manipulation in contact-sensitive tasks. Early work focused on imitation learning from
demonstrations that capture motion and force. AR-Haptic [1095] learns positional and force profiles
from kinesthetic and haptic demonstrations, while Bilateral [1096] employs bilateral control to record
position and force simultaneously for precise manipulation imitation. Feeling the Force [1097] jointly
models pose and contact force from human demonstrations to discover latent interaction stages in
multi-step bottle-opening tasks, highlighting the value of force for revealing physical state changes that
may be visually ambiguous. Wang et al. [1098] further combine trajectory and force demonstrations
for contact-sensitive assembly, and ImmersiveDemo [1099] shows that immersive demonstrations
with force feedback can provide informative supervision for imitation learning.
More recent work shifts from demonstration-level force supervision toward closed-loop force-
aware policy learning. FoAR [1100] introduces a force-aware reactive policy that combines visual
observations with real-time force feedback to adapt manipulation behaviors during contact. TA-
VLA [1101] systematically studies how torque signals should be incorporated into VLA architectures,
highlighting the importance of where and how physical feedback is integrated into action generation.
ForceVLA [1102] further introduces a force-aware mixture-of-experts mechanism that combines
vision–language representations with real-time force sensing for physically grounded contact-rich
manipulation. In contrast to methods that require force sensing during deployment, FD-VLA [1103]
distills force information from force-supervised training into latent force representations inferred
from vision and robot states, enabling force-aware action generation without relying on physical force
sensors at inference time. These developments illustrate a progression from explicit force imitation
toward force-conditioned VLA architectures and the transfer of physical interaction knowledge into
deployable latent representations.
Audio. Audio provides an additional source of information about interaction events that may be
visually occluded or difficult to detect from images alone. Play It By Ear [1104] attaches a microphone
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
to the robot gripper and uses contact sounds during imitation learning, allowing policies to recognize
interaction events that are hidden from visual observations. See, Hear, and Feel [1105] jointly models
visual, tactile, and auditory signals through multimodal attention, where sound provides immediate
evidence of events such as contact or liquid pouring. MUTEX [861] extends the role of audio from
environmental feedback to task specification by learning a unified manipulation policy conditioned
on heterogeneous inputs, including speech instructions and spoken goal descriptions.
Recent approaches increasingly exploit audio at larger scales and integrate it more tightly with
manipulation policies. ManiWAV [1106] learns from in-the-wild audio–visual demonstrations and uses
contact sounds together with vision to improve contact-rich manipulation. MS-Bot [1107] introduces
stage-guided multisensory fusion that dynamically adjusts the contribution of visual, tactile, and
auditory signals according to the current manipulation stage. VLAS [1108] directly incorporates
speech instructions into a VLA model through speech–text alignment, enabling spoken commands to
condition downstream robot actions. More recently, ELLSA [1109] unifies visual perception, speech
understanding, language generation, and robot action within an end-to-end framework, supporting
concurrent listening, seeing, speaking, and acting during embodied interaction. Together, these works
show that audio is evolving from a supplementary contact cue toward a general interface for both
physical-event perception and natural human–robot interaction.
Other Physical Sensors. Beyond force and audio, emerging work has begun to integrate heteroge-
neous physical sensing into generalist robot policies. OmniVLA [1110] develops a unified multi-sensor
VLA framework that incorporates signals from infrared cameras, mmWave radar, and microphone
arrays. Rather than designing an independent policy for each sensor, it maps heterogeneous obser-
vations into spatially grounded representations that can be incorporated into an RGB-pretrained
VLA through lightweight modality-specific components. Such approaches broaden VLA perception
beyond conventional visual inputs and suggest a path toward policies that can selectively exploit
sensing modalities according to environmental and task requirements. Related directions include
thermal perception [1110], event cameras [1111], and physiological sensing [1112], although these
modalities remain substantially less explored than force and audio for general-purpose manipulation.
6.3. Latent Learning
Latent learning investigates how robots acquire and leverage compact, structured, and transferable rep-
resentations that bridge perception and control. It focuses on discovering intermediate representations
that capture task-relevant semantics, dynamics, and affordances, thereby improving generalization
and sample efficiency. Existing approaches can be broadly categorized into two complementary direc-
tions. Pretrained latent learning aims to learn general-purpose visual or multimodal representations
through large-scale pre-training, typically using self-supervised or multimodal objectives to distill
task-relevant structure from human egocentric videos or robotic demonstrations. These pretrained
encoders provide robust perceptual embeddings that serve as transferable inputs for downstream
control across diverse tasks and embodiments. Latent action learning, in contrast, goes beyond
representation acquisition to explore how latent spaces can be effectively utilized for control. It
jointly models latent representations and their temporal or causal mappings to actions, often through
quantized tokens, continuous latent dynamics, or implicit world models. In this paradigm, the latent
space not only encodes environmental and task information but also serves as an internal interface
for reasoning, planning, and action generation, offering a unified perspective on representation and
policy learning. We summarize these two paradigms in Figure 19.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Human Egocentric

## sec:datasets-2 Datasets
_Pages 67-67_

General Datasets
Robotic Datasets
Pretrained Robotic
Encoder
Policy
System 2
(High-level)
System 1
(Low-level)
Latent Feature
VQ Encoder
VQ Decoder
Policy
Transformer IDM
Transformer FDM
Encoder
Diffusion
Encoder
Koopman
Operator
IDM
DiT Layer
Policy
DiT Layer
Place pepsi
can upright.
Transformer Encoder
Transformer Decoder
VLA

## sec:model-2 Model/
_Pages 67-67_

Policy
Pretrained Latent
Learning
Discretization
and Vector
Quantization
Latent in Dual System
Latent of
Dynamics
Diffusion-based

## sec:methods Methods
_Pages 67-67_

Koopman
Operator

## sec:methods-2 Methods
_Pages 67-80_

Implicit
World
Modeling
Instruction-
conditioned
Policies
Discretized Latent
Continuous Latent
Latent Action Learning
Figure 19 | Overview of Latent Learning. Left Top: Robotic encoders are pretrained on general
datasets, human egocentric datasets, and robotic datasets to produce latents for policies. Left Bottom:
In the dual system, system 2 outputs latent to guide system 1 to generate action. Right: Latent action
learning is conducted through discretized (yellow) or continuous latents (pink).
6.3.1. Pretrained Latent Learning
Learning encoder-grounded and generalizable visual representations, often referred to as robotic
representations, is essential for real-world visuomotor control. Pre-training such representations on
large domain-relevant data has emerged as an effective strategy for robot learning, inspired by the suc-
cess of representation pre-training in computer vision [1113] and natural language processing [73].
Depending on the source of pre-training data, existing robotic representations can be broadly catego-
rized into three groups: those learned from general-purpose visual datasets (e.g., ImageNet [1114]),
human egocentric datasets (e.g., Ego4D [182]), and robot interaction datasets (e.g., BridgeV2 [165]).
Across these regimes, representation learning has progressively moved from static semantic features
toward task-adaptive, interaction-aware, and dynamics-aware latent representations.
Training on General Datasets. General-purpose image and video datasets provide broad visual
priors that can be adapted to robotic control. Parisi et al. [1115] aggregate features from multiple
layers of a MoCo-v2 encoder to construct a pre-trained visual representation for control, showing that
appropriately adapted visual features can rival hand-crafted state inputs. Theia [1116] further distills
complementary knowledge from multiple vision foundation models into a compact representation
specialized for robot learning, while VER [1117] extends this idea toward task-adaptive representation
selection by distilling multiple visual experts and learning a lightweight router to activate task-relevant
features. Beyond static semantics, Token Bottleneck (ToBo) [1118] compresses the current scene
into a compact latent token and predicts subsequent observations, encouraging the representation
to preserve both scene content and temporal dynamics. Generalizable Imitation Learning Through
Pre-Trained Representations [1119] instead exploits patch-level features from self-supervised vision
transformers to extract stable semantic keypoints, improving policy generalization across unseen
object appearances, geometries, and categories.
Training on Human Egocentric Datasets. Human egocentric videos provide large-scale observations
of object interaction without the cost of robot data collection. MVP [858] applies masked visual
pre-training to egocentric imagery and transfers the frozen encoder to downstream control, while
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
VC-1 [151] scales masked pre-training to more than 4,000 hours of egocentric video and ImageNet
data to establish a general visual backbone for embodied intelligence. R3M [801] combines temporal
contrastive learning and video–language alignment on Ego4D, and Voltron [804] jointly learns
language-conditioned visual reconstruction and visually grounded language generation to capture
both perceptual and semantic information. Vi-PRoM [80] further combines contrastive self-supervision
and supervised human–object interaction learning. More interaction-oriented approaches explicitly
model manipulation structure: MPI [1120] predicts intermediate interaction states and active objects,
HRP [1121] transfers affordance priors such as hand locations and contact regions from human
videos, and VIP [666] formulates representation learning as goal-conditioned value pre-training.
Ag2Manip [1122] further addresses the human–robot embodiment gap by learning agent-agnostic
visual and action representations that suppress embodiment-specific cues. Together, these methods
move egocentric pre-training from generic visual reconstruction toward interaction-aware, affordance-
aware, and embodiment-invariant representations.
Training on Robotic Datasets. Robot datasets provide direct supervision over observations, actions,
proprioception, and interaction dynamics, allowing representations to be aligned more closely with
downstream control. RPT [1123] pre-trains transformers by masking and reconstructing visual
observations, proprioceptive states, and actions from large-scale robot trajectories, while Premier-
TACO [1124] improves temporal action contrastive learning through more effective negative sampling
for few-shot policy adaptation. MCR [1125] introduces manipulation centricity to quantify the align-
ment between visual representations and manipulation performance and learns manipulation-centric
features from large-scale robot data. Recent methods increasingly model how actions transform the
environment: LaVA-Man [1126] learns language-guided visual-action representations by predicting
manipulation-induced visual changes, whereas DynaRend [1127] combines masked reconstruction,
future prediction, and differentiable volumetric rendering to jointly encode 3D geometry, semantics,
and temporal dynamics. Complementing these methods, CVESC [1128] shows that the ability of a
visual representation to recover latent environment structure, including object configuration, geom-
etry, and physical state, strongly correlates with downstream control performance. Overall, these
results suggest that pretrained robotic representations are evolving from broadly transferable visual
features toward latent representations that explicitly preserve task-relevant physical state, interaction
structure, and action-conditioned dynamics.
6.3.2. Latent Action Learning
Recent advances in latent action learning have introduced diverse paradigms that connect video
representation, world modeling, and policy generation, allowing robots to acquire reusable action
abstractions beyond explicit action supervision. In addition to the latent representations discussed in
Section 6.1.2 and intermediate latent structures in dual-/multi-system VLAs in Section 6.2.2, latent
actions provide an explicit interface between observations and executable robot controls. Existing
methods instantiate latent actions primarily as discrete tokens, continuous vectors, or hierarchical
structures that combine reusable skill abstractions with continuous parameterization. The following
sections review these major formulations.
i) Discretization and Vector Quantization
Discrete latent action methods map continuous behaviors into a finite vocabulary of reusable action
or motion tokens, simplifying action modeling and enabling large-scale pre-training from data without
explicit robot controls. ILPO [1129] pioneered learning latent action variables from observation-
only demonstrations, while LAPO [1130] reconstructs latent action structure from unlabeled videos
through a latent inverse dynamics model. Behavior Generation with Latent Actions [1131] applies
vector quantization to continuous control for efficient generative behavior modeling, and Discrete
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Policy [1132] learns disentangled discrete action codes for multi-task manipulation. STAR [1133]
further introduces rotation-augmented vector quantization to learn diverse and orientation-robust skill
abstractions, whereas MOTO [1134] treats latent motion tokens as a bridging language between large-
scale video pre-training and downstream robot manipulation. LAPA [1135] learns latent actions by
modeling transitions between current and future visual observations and subsequently trains a vision-
language model to predict these latent actions before grounding them to executable robot controls
using action-labeled data. DreamGen [1136] further scales this video-driven learning paradigm by
generating diverse synthetic robot trajectories with video world models and recovering corresponding
robot actions through inverse dynamics, thereby expanding the supervision available for downstream
policy learning.
ii) Continuous Latent Action Representations
Continuous latent action representations encode behaviors as vectors in a continuous space,
preserving fine-grained variations in motion and supporting interpolation across related behaviors.
Compared with discrete action tokens, continuous latent spaces are particularly suitable for model-
ing smooth dynamics, cross-embodiment correspondence, and predictive structures that condition
downstream action generation.
Latent Dynamics Representations. One line of work learns latent variables that capture changes in
observations or motion dynamics and subsequently uses them to guide control. MimicPlay [1137]
learns long-horizon manipulation from human play by constructing latent plans conditioned on visual
goals. CLAM [1138] learns continuous latent actions from unlabeled demonstrations and grounds
them to executable motor commands using limited action supervision. CoMo [1139] further scales
continuous latent motion learning to internet videos, extracting motion-centric representations that
can serve as pseudo-actions across substantial domain and embodiment differences. These approaches
exploit continuous representations to separate transferable motion structure from embodiment-specific
low-level controls.
Implicit World Modeling. Another direction derives action-relevant latent representations from
predictive world models. VPP [790] adapts a video foundation model for language-conditioned future
prediction and aggregates its intermediate representations through a Video-Former to condition
a diffusion policy. FLARE [1140] learns action-relevant representations through implicit future
prediction, allowing predictive latent features to improve policy generalization without explicitly
generating future observations during deployment. Genie Envisioner [780] further aligns intermediate
latent features of a video diffusion model with representations inside an action diffusion policy,
transferring predictive structures from video generation to robot control. These methods indicate
that useful action representations can emerge from predicting how the physical scene evolves, even
when the world model itself is not explicitly decoded at policy inference time.
Diffusion-based Methods. Continuous latent representations can also provide structured spaces
in which diffusion policies generate robot behaviors. LAD [1141] learns a shared latent action
space and trains diffusion policies within this space to facilitate cross-embodiment manipulation
transfer. KOAP [1142] combines diffusion-based planning with Koopman controllers, allowing a small
set of learned latent actions to be composed into stable long-horizon behaviors. LaDi-WM [1143]
instead trains a latent diffusion world model to predict semantic and geometric dynamics, which are
subsequently used as conditioning information for diffusion-based action generation.
Koopman Operator Methods. Koopman-based approaches seek latent spaces in which nonlinear
manipulation dynamics become easier to model through approximately linear evolution. KoDex [1144]
investigates Koopman operator representations for dexterous manipulation and demonstrates their
utility for learning structured manipulation dynamics. KOROL [1145] further learns interpretable
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
object-centric latent features whose evolution can be rolled out using a Koopman operator, providing
visualizable predictions that support downstream manipulation.
Goal- or Instruction-conditioned Representations. Latent spaces can additionally provide interfaces
between high-level task specifications and low-level behavior. Procedure Cloning [1146] learns
intermediate procedural representations that capture the sequence of decisions underlying long-
horizon demonstrations. GRIF [1147] constructs a shared goal representation that aligns language
instructions with visual goal observations using partially labeled data, while IGOR [1148] represents
image goals as atomic control units that bridge high-level foundation models and downstream robot
controllers. UniVLA [923] learns task-centric latent actions without action supervision from videos
spanning different embodiments and viewpoints and subsequently trains a VLA to predict these
latent action tokens for downstream control. Oishi et al. [1149] further learn disentangled latent
behavioral characteristics, allowing qualitative task modifiers to selectively adjust motion attributes
during execution.
iii) Hierarchical and Parameterized Latent Skills
Recent work moves beyond flat discrete or continuous representations toward structured latent
spaces that explicitly capture the hierarchy and compositionality of manipulation skills. HiMa-
Con [1150] discovers hierarchical manipulation concepts from unlabeled multimodal trajectories
through cross-modal correlation learning and multi-horizon prediction, organizing interaction pat-
terns across temporal scales from short-term behaviors to longer-horizon subgoals. DEPS [1151]
instead learns parameterized skills through a hierarchical latent policy consisting of a discrete skill
selector, a continuous skill parameter, and a low-level action policy. Such hybrid representations
preserve reusable discrete skill identities while capturing task-specific variations through continu-
ous parameters. Together, these methods suggest that latent action learning is evolving from flat
action compression toward structured skill representations that model temporal hierarchy, behav-
ioral variation, and compositionality, thereby providing more scalable interfaces between large-scale
observational data and executable robot control.
6.4. Policy Learning
Policy learning defines how a robot transforms internal representations, such as latent features or
encoded observations, into executable actions that interact with the physical world. It focuses on
decoding perceptual and latent information into control outputs (for example, end-effector poses)
through learned mappings rather than manually designed rules. In essence, policy learning establishes
the computational mechanism that connects perception and decision-making with motor execution.
We summarize these methods in Figure 20.
6.4.1. MLP-based Policy
MLP-based policies [151, 801, 1123, 1152] provide a simple and efficient baseline for visuomotor
control by directly mapping encoded observations or latent representations to robot actions. Such
architectures are computationally lightweight and particularly effective when coupled with strong
pretrained encoders, but their limited temporal modeling capacity makes performance strongly
dependent on the quality of the input representation.
6.4.2. Transformer-based Policy
Transformer-based policies exploit attention to model dependencies among observations, actions, goals,
and language over time. Self-attention captures long-range temporal structure, while cross-attention
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
allows action generation to selectively retrieve task-relevant perceptual or linguistic information.
These properties make Transformers particularly suitable for action chunking, autoregressive control,
multimodal conditioning, and long-horizon manipulation.
ACT-based Policy. The Action Chunking Transformer (ACT) [1153] predicts short action sequences
using a CVAE-based Transformer, reducing compounding errors and enabling fine-grained bimanual
manipulation with low-cost hardware. RoboAgent [166] extends action chunking to multi-task ma-
nipulation through semantic augmentation, while Bi-ACT [1154] incorporates bilateral position–force
information for contact-sensitive imitation. BAKU [896] develops an efficient multi-task Transformer
capable of fusing heterogeneous observations and decoding chunked actions, and InterACT [1155]
explicitly models inter-arm dependencies through hierarchical attention for coordinated bimanual
manipulation. Haptic-ACT [1156] combines action chunking with immersive haptic demonstrations,
whereas Bi-LAT [902] further introduces language conditioning to control both motion and contact
force. Chain-of-Action [1158] formulates trajectory generation as autoregressive action reasoning,
while Q-chunking [1159] incorporates action chunks into reinforcement learning to improve explo-
ration in sparse-reward settings. These developments extend action chunking from short-horizon
imitation toward multimodal, interactive, and decision-aware sequence control.
Autoregressive Policy. Autoregressive policies explicitly factorize robot trajectories into sequential
predictions. Act3D [887] constructs an adaptive-resolution 3D feature field and uses coarse-to-fine
attention for end-effector prediction, while ICRT [626] treats demonstrations as in-context prompts
and autoregressively predicts actions for few-shot imitation. CARP [877] learns multi-scale action
embeddings and predicts trajectories through coarse-to-fine autoregressive refinement, whereas Dense
Policy [1160] introduces bidirectional autoregressive action generation using a BERT-style encoder.
Robotic View Transformer [883] predicts 3D manipulation locations through multi-view reprojection,
and 3D-MVP [866] pretrains a multi-view 3D Transformer through masked reconstruction before
adapting its features to action generation. Together, these approaches demonstrate that autoregressive
policies can model action dependencies at multiple temporal and spatial resolutions rather than
predicting individual motor commands independently.
6.4.3. Diffusion Policy
Diffusion Policy (DP) [81] formulates visuomotor control as conditional denoising in action space,
enabling expressive modeling of multimodal demonstrations while supporting receding-horizon
execution. Its success has motivated extensions along several directions, including 3D perception,
model scaling, acceleration, expert specialization, geometric structure, predictive modeling, and
reinforcement-learning adaptation.
3D DP. Three-dimensional diffusion policies incorporate explicit geometric structure to improve spatial
grounding and manipulation generalization. DP3 [885] conditions diffusion policies on compact point-
cloud representations and demonstrates strong data efficiency across complex manipulation tasks.
3D Diffuser Actor [888] lifts multi-view visual features into 3D scene representations and performs
diffusion-based prediction of end-effector keyposes and trajectories using 3D relative-position atten-
tion. iDP3 [283] extends 3D diffusion policies toward egocentric deployment, while G3Flow [849]
maintains dynamic object-centric 3D semantic features during manipulation. CordViP [252] explicitly
models hand–object spatial correspondences, DP4 [1161] incorporates 3D spatial and 4D temporal
information through dynamic Gaussian representations, and H3DP [1162] hierarchically organizes
depth, multi-scale visual features, and coarse-to-fine action generation.
Scaling and Foundation DP. Diffusion policies have also progressed from task-specific models toward
large-scale generalist policies. ScaleDP [1163] redesigns conditioning and attention mechanisms to
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Policy Learning (§ 6.4)
MLP-based Policy
§ 6.4.1
R3M [801], VC-1 [151], RPT [1123], DyWA [1152]
Transformer-based
Policy § 6.4.2
ACT-based Policy
ACT [1153], RoboAgent [166], Bi-ACT [1154],
BAKU [896], InterACT [1155], Haptic-ACT [1156],
ALOHA Unleashed [1157], Bi-LAT [902],
Chain-of-Action [1158], Q-chunking [1159]
Autoregressive
Policy
Act3D [887], ICRT [626], CARP [877], Dense
Policy [1160], HAT [381], RVT [883]
Diffusion Policy § 6.4.3
3D DP
DP3 [885], 3D Diffuser Actor [888], iDP3 [283],
G3Flow [849], DP4 [1161], H3DP [1162]
Scaling and
Foundation DP
ScaleDP [1163], RDT-1B [1164]
Accelerated DP
OneDP [1165], Consistency Policy [879], ManiCM [890]
MoE DP
SDP [1166], MoDE [1167]
Geometry- and
Equivariance-aware
EquiBot [1168], EDP [1169]
DP with Video
Prediction
UniPi [1170], UVA [1171], UWM [753]
DP with Other
Techniques
HDP [875], DPPO [1172], Latent Diffusion
Planning [1173], MBA [1174], RDP [1079], Past-Token
Prediction [1175], DP-Attacker [1176]
Flow Matching Policy
§ 6.4.4
General FM Policy
AdaFlow [1177], X-IL [1178], FLOWER [999], Streaming
Flow Policy [1179], RTC [1017], H-RDT [1180],
VFP [1181], GenFlowRL [848], ManiFlow [1182]
Efficient and
One-step FM
MP1 [1183], Action-to-Action FM [1184]
3D FM Policy
PointFlowMatch [1185], FlowPolicy [1186], Affordance
FM [1187], FlowRAM [1188], 3D FlowMatch Actor [891]
SSM-based Policy
§ 6.4.5
MaIL [1189], RoboMamba [911], FlowRAM [1188],
MTIL [1190], Mamba as Motion Encoder [1191]
SNN-based Policy
§ 6.4.6
SDP [1192], STMDP [1193], Multimodal SNN [1194],
Fully Spiking A2C [1195]
Frequency-based
Policy § 6.4.7
Fourier Transporter [1196], FreqPolicy [1197], Wavelet
Policy [1198], ManipForce [1199]
Action Tokenization
and Action
Representation § 6.4.8
Action Tokenization
and Compression
FAST [1200], [1201], [1202]
Trajectory
Parameterization
ABPolicy [1203]
Drift-based Policy
§ 6.4.9
DBPO [1204], Implicit Drifting Policy [1205]
Figure 20 | A structured overview of policy learning for visuomotor control, organized by modeling
paradigm.
scale diffusion Transformers from relatively small policies toward billion-parameter models, demon-
strating systematic performance gains with increasing capacity. RDT-1B [1164] develops a billion-scale
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
diffusion foundation policy for bimanual manipulation and introduces a unified action representation
to learn transferable behaviors from heterogeneous multi-robot datasets. These works suggest that
scaling laws and heterogeneous data aggregation, previously central to foundation vision and language
models, are increasingly relevant to low-level robot policies.
Accelerated DP. Because iterative denoising introduces substantial control latency, several approaches
seek to reduce the number of policy evaluations. OneDP [1165] distills an iterative diffusion policy
into one-step generation, while Consistency Policy [879] learns self-consistent predictions across
diffusion times to enable fast sampling with limited degradation. ManiCM [890] applies consistency
modeling to 3D manipulation and achieves approximately one-step action generation while main-
taining competitive manipulation performance. These approaches shift computation from iterative
inference toward training-time distillation or consistency constraints.
MoE DP. Mixture-of-Experts architectures improve the capacity and specialization of diffusion policies.
SDP [1166] sparsely activates task-specific experts to enable multi-task learning without proportionally
increasing computation, while MoDE [1167] introduces noise-conditioned routing among expert
denoisers. More recently, skill-oriented MoE diffusion policies explicitly interpret expert specialization
as reusable manipulation abstractions, coupling temporally stable routing with selective expert
activation to support compositional and few-shot skill learning.
Geometry- and Equivariance-aware DP. Another direction incorporates the geometry of robot actions
directly into policy design. EquiBot [1168] introduces SIM(3)-equivariant diffusion for data-efficient
generalization under scale, rotation, and translation changes, while EDP [1169] exploits SO(2)/SE(3)
symmetry for 6-DoF manipulation. More recently, Lie-manifold diffusion formulations model pose
generation directly on SE(3) rather than treating rotations and translations as unconstrained Euclidean
vectors, predicting updates in the tangent space and mapping them back to valid poses through
geometric operators. Such methods reduce representation mismatch between generative objectives
and the underlying kinematic structure of robot actions.
DP with Video Prediction. Predictive visual modeling provides another source of structure for
diffusion policies. UniPi [1170] formulates planning as language-conditioned video generation and
subsequently extracts actions from imagined task execution. UVA [1171] jointly models video predic-
tion and action generation through shared latent representations, while UWM [753] combines video
and action diffusion within a unified framework and can exploit both action-labeled demonstrations
and action-free videos. These methods use future visual evolution as an intermediate representation
that constrains downstream action generation.
DP with Other Techniques. Diffusion policies have further been combined with hierarchical planning,
reinforcement learning, latent prediction, tactile sensing, and task-specific structural priors. HDP [875]
separates high-level keypose generation from low-level trajectory diffusion, while DPPO [1172] applies
policy-gradient fine-tuning to pretrained diffusion policies. Latent Diffusion Planning [1173] predicts
future states in a learned latent space and decodes them into executable controls with inverse dynamics,
allowing action-free and suboptimal trajectories to contribute to policy learning. MBA [1174] first
predicts object motion and subsequently conditions robot action diffusion on the inferred motion,
whereas RDP [1079] combines a low-frequency diffusion planner with high-frequency tactile feedback
for contact-rich manipulation. YOTO [1206] synthesizes demonstrations from human videos and
trains a specialized bimanual diffusion policy for long-horizon coordination.
Recent analysis has also questioned which ingredients are responsible for the strong performance
of diffusion policies. Much Ado About Noising [1207] shows that their advantages cannot be ex-
plained solely by the ability to represent multimodal action distributions; noise injection and iterative
supervised refinement can themselves induce useful regularization toward plausible action manifolds.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
This perspective suggests that future policies may retain the optimization benefits of diffusion-style
training while simplifying the generative process used at inference.
6.4.4. Flow Matching Policy
Flow-matching policies model action generation as continuous transport between an initial distribution
and demonstrated robot trajectories. Compared with conventional diffusion objectives, flow matching
directly learns a velocity field and often permits straighter generation paths, fewer inference steps,
and smoother trajectory synthesis. Recent work explores both general visuomotor flow policies and
geometry-aware 3D variants.
General Flow-Matching Policy. X-IL [1178] systematically studies architectural and representation
choices across diffusion and flow-matching imitation policies. AdaFlow [1177] introduces variance-
adaptive flow integration, dynamically adjusting the number of ODE steps according to uncertainty.
FLOWER [999] develops a compact vision-language-action flow policy with strong multi-task manip-
ulation performance, while Streaming Flow Policy [1179] directly interprets action trajectories as
continuous flow trajectories and incrementally generates actions during execution. Real-Time Action
Chunking [1017] overlaps action generation with execution through action inpainting, improving
continuity between consecutive chunks. H-RDT [1180] combines human-video pre-training with
flow-matching fine-tuning for bimanual manipulation, and VFP [1181] introduces variational flow
matching to improve multimodal trajectory generation. GenFlowRL [848] uses generated object-
centric motion flows as reward signals for reinforcement learning, whereas VITA [1208] learns a
direct vision-to-action flow mapping with a lightweight architecture. ManiFlow [1182] combines flow
matching with consistency-style training to straighten generative trajectories and reduce sampling
cost. Action-to-Action Flow Matching [1184] further replaces an uninformed noise source with
representations of previously executed actions, exploiting temporal continuity to shorten the transport
path toward future actions.
3D Flow-Matching Policy. FlowPolicy [1186] introduces consistency flow matching conditioned on 3D
point clouds for efficient manipulation, while PointFlowMatch [1185] directly conditions continuous
flow trajectories on point-cloud and proprioceptive observations. FlowRAM [1188] couples flow
matching with region-aware RGB-D representations and Mamba-based temporal modeling, improving
generalization under occlusion and spatial variation. MP1 [1183] applies MeanFlow to point-cloud-
conditioned manipulation and compresses trajectory generation to a single network evaluation. 3D
FlowMatch Actor [891] combines pretrained 3D representations with flow matching to unify single-
and dual-arm control, while Affordance-based Flow Matching [1187] conditions flow generation on
task-relevant spatial affordances. Together, these approaches show that flow matching can combine
efficient generative control with increasingly structured spatial representations.
6.4.5. SSM-based Policy
State-space-model policies use architectures such as Mamba to efficiently encode long observation and
action histories while retaining approximately linear sequence complexity. MaIL [1189] demonstrates
that Mamba can replace conventional sequence models in imitation learning and provide strong long-
horizon control. RoboMamba [911] combines vision, language, and robot states in a multimodal state-
space architecture, while FlowRAM [1188] integrates region-aware Mamba representations with flow-
based action generation. MTIL [1190] explicitly encodes the complete interaction history to improve
temporally dependent manipulation. More recently, SUREFlow [1209] combines Mamba-based
sequence modeling with uncertainty-aware residual flow matching, selectively refining unreliable
components of generated actions while retaining efficient long-context processing.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
6.4.6. SNN-based Policy
Spiking neural network (SNN) policies explore event-driven computation for energy-efficient and
precise robot control. SDP [1192] develops a spiking diffusion policy with learnable channel-wise
membrane thresholds, allowing spiking activity to adapt across modalities. STMDP [1193] combines
spiking computation with Transformer-based diffusion control to retain generative trajectory modeling
while introducing event-driven dynamics. Multimodal Spiking Neural Network [1194] incorporates
multiple sensing channels for manipulation in high-dimensional action spaces, while Fully Spik-
ing Actor-Critic [1195] extends spiking architectures to continuous-control reinforcement learning.
Although these methods demonstrate the feasibility of neuromorphic policy learning, SNN-based
manipulation remains substantially less mature than Transformer- and generative-policy paradigms.
6.4.7. Frequency-based Policy
Frequency-based policies exploit spectral representations of actions or observations to capture long-
horizon structure and separate dynamics occurring at different temporal scales. Fourier Trans-
porter [1196] uses Fourier-domain representations to construct bi-equivariant manipulation policies
in 3D. FreqPolicy [1197] constrains flow-based action generation through frequency consistency, while
a complementary frequency-autoregressive formulation represents continuous action trajectories
through spectral tokens. Wavelet Policy [1198] uses hierarchical wavelet decomposition to capture
both coarse long-horizon behavior and fine-grained local motion. ManipForce [1199] further extends
frequency-aware modeling to contact-rich manipulation by jointly processing asynchronous visual
observations and high-frequency force–torque feedback. These approaches suggest that explicitly
separating temporal frequency components can provide useful inductive biases for long-horizon and
contact-sensitive control.
6.4.8. Action Tokenization and Structured Action Representation
In addition to the policy architecture itself, recent work increasingly studies how dense continuous
robot trajectories should be represented before prediction. Compact action representations can reduce
sequence length, remove temporal redundancy, impose trajectory smoothness, and provide more
efficient interfaces for autoregressive or generative policies. FAST [1200] transforms high-frequency
action chunks into the frequency domain and combines quantization with byte-pair encoding to obtain
compact discrete action tokens, substantially reducing the sequence length required by autoregressive
VLA policies. Learning High-Frequency Continuous Action Chunks in Latent Space [1201] instead
learns a continuous latent representation of dense high-frequency action chunks and introduces
reuse-and-refinement across consecutive predictions to maintain smooth execution. ABPolicy [1203]
represents trajectories using B-spline control points and performs flow-based generation in this
compact parameter space, naturally enforcing intra-chunk smoothness while reducing redundancy.
These methods highlight action representation as an independent design dimension: rather than only
improving the network that predicts actions, policies can benefit from choosing structured coordinates
in which action sequences are easier to model.
6.4.9. Drift-based Policy
Drift-based policies have recently emerged as an alternative route to efficient generative control.
Unlike diffusion and flow-matching policies that typically construct actions through iterative denoising
or numerical integration, drifting methods attempt to internalize iterative trajectory refinement
into the training objective and directly generate actions in a single policy evaluation. Drift-Based
Policy [1204] learns a native one-step generative policy through fixed-point drifting, while its policy-
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
optimization extension enables reinforcement-learning refinement without abandoning one-step
deployment. Implicit Drifting Policy [1205] further avoids explicitly estimating the drifting vector
field and instead exploits the local geometry of expert demonstrations to constrain predictions toward
plausible conditional action manifolds. Although still an emerging research direction, drifting provides
a conceptually distinct path toward real-time multimodal control by replacing iterative inference with
training-time geometric refinement.
7. Approaches to the Key Bottlenecks
Despite the remarkable progress of robot manipulation, achieving general-purpose deployment in
unstructured real-world environments remains constrained by both fundamental learning bottlenecks
and system-level challenges. At the learning level, data and generalization remain central: the
quality, diversity, and utilization of data determine the scalability of imitation and reinforcement
learning, while generalization governs whether learned skills can transfer across unseen environments,
novel tasks, and diverse embodiments. Beyond these foundations, real-world deployment increasingly
requires higher-level capabilities for coordinating complex behaviors and interacting with humans.
Agentic systems provide mechanisms for planning, tool orchestration, memory, verification, and
continual adaptation, whereas human–robot interaction and collaboration enable robots to infer
human intent, incorporate feedback, share autonomy, and coordinate safely with users. Accordingly,
this section discusses these four complementary directions—data, generalization, agents, and human–
robot collaboration—that jointly shape the scalability, adaptability, and practical deployment of
modern robot manipulation systems.
7.1. Data Collection and Utilization
Data serves as the cornerstone of learning-based and data-driven approaches in embodied intelligence,
as its quality, diversity, and scale fundamentally determine the effectiveness and generalization of
learned policies. Unlike conventional machine learning, robot learning depends on data that jointly
capture perception, action, physical interaction, and embodiment-specific dynamics, making data
simultaneously a critical resource and a principal bottleneck. This section focuses on two complemen-
tary dimensions. Data collection concerns how new demonstrations and interaction experiences are
acquired or generated, encompassing human teleoperation, human-in-the-loop refinement, synthetic
and automatic generation, and crowdsourced acquisition. Data utilization concerns how collected
data are selected, retrieved, relabeled, augmented, expanded, and reweighted to improve learning
efficiency and robustness. Together, these two dimensions form the data foundation for scaling robot
learning toward increasingly generalizable real-world manipulation. We summarize representative
data collection paradigms in Figure 21 and illustrate their specific forms in Figure 22.
7.1.1. Data Collection
Data collection for robot learning spans multiple paradigms that differ in cost, scalability, embodiment
alignment, data fidelity, and reliance on humans. Broadly, existing approaches can be grouped into
four categories. First, human teleoperation systems acquire direct supervision through interfaces
ranging from replica arms and wearable devices to XR and robot-free systems. Second, human-in-
the-loop methods reduce human effort by allowing operators to selectively intervene in or correct
autonomous policy execution. Third, synthetic and automatic data generation amplifies limited
human supervision through simulation, demonstration transformation, foundation models, optimiza-
tion, or autonomous policy rollouts. Finally, crowdsourcing frameworks distribute data acquisition
across large groups of contributors, lowering access barriers and broadening data coverage.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
i) Human Teleoperation
Human teleoperation remains the most direct and widely used paradigm for collecting high-quality
robot demonstrations. Existing systems differ primarily in interface cost, embodiment alignment,
sensing fidelity, portability, and operator burden, ranging from direct robot teleoperation to robot-free
systems that capture human manipulation trajectories for subsequent transfer to robotic embodiments.
Cost–Effective and Scalable Teleoperation. Several systems [30, 1210–1213] reduce hardware
and deployment requirements to support scalable demonstration collection. Young et al. [1210] use
inexpensive reacher–grabber tools to collect visual demonstrations that can be transferred to robot
manipulation. AnyTeleop [1211] develops a modular vision-based teleoperation framework applicable
across robot arms, dexterous hands, and camera configurations, while GELLO [1212] introduces a
low-cost replica-arm interface that provides intuitive embodiment-aligned control. UMI [30] further
decouples demonstration collection from access to the target robot by using a portable manipulation
interface to acquire in-the-wild robot-compatible trajectories. OPEN TEACH [1213] instead uses
consumer VR hardware and hand tracking to provide a broadly accessible teleoperation interface
across different robot morphologies.
Feedback–Rich Teleoperation for Contact and Dexterity. For contact-rich manipulation, data col-
lection systems increasingly augment kinematic trajectories with force, tactile, or haptic information.
M2R [1214] introduces a master-to-robot interface with force or torque sensing to capture physical
interaction information without expensive bilateral hardware. ALPHA-BiACT [1215] combines bilat-
eral position and force control to collect richer demonstrations for uni- and bimanual manipulation,
while Bunny-VisionPro [1216] couples real-time VR hand tracking with low-cost haptic interfaces for
dexterous teleoperation. FreeTacMan [1217] further develops a robot-free wearable interface with
visuo-tactile grippers and optical pose tracking, jointly recording visual, tactile, and kinematic signals
from human manipulation for contact-rich robot learning. These systems complement conventional
motion demonstrations with direct interaction signals that are particularly important for insertion,
compliant manipulation, and fine contact control.
Egocentric and XR Interfaces Aligning Viewpoints. XR and egocentric interfaces provide intuitive
human control while reducing discrepancies between human and robot observations. Zhang et
al. [1218] use consumer VR controllers to place operators directly in the robot observation–action
loop, while EgoMimic [1219] leverages egocentric wearable observations and human motion for
viewpoint-aligned imitation learning. ARCap [1220] provides augmented-reality feedback that guides
users toward robot-feasible demonstrations, lowering the expertise required for high-quality data
collection. Active perception can further improve demonstration quality when manipulation is
affected by occlusion; AV-ALOHA [1221], for example, incorporates an auxiliary controllable camera
to maintain task-relevant visual observations during bimanual manipulation.
Embodiment-Aligned and Dexterous Demonstration Interfaces. A complementary line explicitly
addresses kinematic and morphological mismatches between human operators and target robots.
AirExo [1222] introduces a low-cost dual-arm exoskeleton that provides embodiment-aligned demon-
strations while remaining portable for in-the-wild collection. DexCap [1223] develops a portable
motion-capture system that jointly records wrist and finger motion together with 3D environmental
observations, supporting dexterous policy learning from human demonstrations. DexUMI [1224]
further combines wearable human-hand interaction capture with a transfer pipeline for dexterous
manipulation, while Tilde [1225] uses a paired TeleHand–DeltaHand design for precise in-hand
teleoperation. TeleMoMa [1226] extends teleoperation to whole-body mobile manipulation through
a modular multimodal interface. More recently, TypeTele [1227] moves beyond direct human-to-
robot pose retargeting by introducing reusable dexterous manipulation types and an MLLM-assisted
retrieval mechanism, allowing operators to exploit robot-specific hand capabilities that are difficult to
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
DATA (§ 7.1)
Collection (§ 7.1.1)
Human Teleoperation
Cost-Effective and Scalable
Teleoperation
Young et al. [1210], AnyTeleop [1211], GELLO [1212],
UMI [30], OPEN TEACH [1213]
Feedback-Rich Teleoperation
for Contact and Dexterity
M2R [1214], ALPHA-BiACT [1215],
Bunny-VisionPro [1216], FreeTacMan [1217]
Egocentric and XR Interfaces
Aligning Viewpoints
Zhang et al. [1218], EgoMimic [1219], ARCap [1220],
AV-ALOHA [1221]
Embodiment-Aligned and
Dexterous Demonstration
Interfaces
AirExo [1222], DexCap [1223], DexUMI [1224],
Tilde [1225], TeleMoMa [1226], TypeTele [1227]
Human-in-the-Loop
Enhancement
IntervenGen [1228], CR-DAgger [1229]
Synthetic and
Automatic Data
Generation
Foundation-Model-Guided
Generation
Scaling Up and Distilling Down [1230],
Manipulate-Anything [1231], SOAR [1232]
Demonstration Transformation
and Synthesis
MimicGen [1233], DexMimicGen [1234],
SkillMimicGen [1235], DemoGen [1236],
Lucid-XR [1237]
Physics- and Constraint-Aware
Generation
Physics-Driven Data Generation [1238], CP-Gen [1239],
MoMaGen [1240]
Autonomous and
Self-Improving Generation
RoboCat [1241], DexFlyWheel [1242]
Crowdsourcing-based
Data Collection
Chung et al. [1243], RoboTurk [1244], David et
al. [1245], MART [1246], AR2-D2 [1247],
EgoZero [1248], COBALT [1249]
Utilization (§ 7.1.2)
Data Selection
EAD [1250], EIL [1251], DC-IL [1252], UVP [1253],
L2D [1254], ILID [1255], Re-Mix [1256],
MimicLabs [1257], CUPID [1258]
Data Retrieval
VINN [1259], SAILOR [1260], Behavior Retrieval [1261],
Di Palo & Johns [1262], DINOBot [1263], RAEA [1264],
GSR [1265], FlowRetrieval [1266], STRAP [1267],
COLLAGE [1268]
Data Augmentation
Language, Goal, and Trajectory
Relabeling
DIAL [1269], SPRINT [1270], NILS [1271],
DAAG [1272], S2I [1273], GoalGAIL [1274],
OILCA [1275]
Physics- and
Geometry-Consistent
Augmentation
Mitrano & Berenson [1276], Wang et al. [1277],
SEIL [1278]
Generative Visual, Viewpoint,
and Embodiment
Augmentation
GenAug [1279], RoVi-Aug [1280], RoboPearls [1281],
ROSIE [1282], DMD [1283], VISTA [1284], DABI [1285]
Data Expansion
Synthesis and Imagined
Rollouts
Generative Predecessor Models [1286], SAFARI [1287],
TASTE-Rob [1288], Self-Imitation by Planning [1289],
Category-Level Manipulation [1290]
Reuse and Corrective
Expansion
Scalable Multi-Task IL [1291], JUICER [1292],
Diff-DAgger [1293]
Data Reweighting
Beliaev et al. [1294], FABCO [1295], PLARE [1296]
Figure 21 | A structured taxonomy of data collection and utilization in robot learning.
express through direct human-hand imitation. Overall, teleoperation systems are evolving from direct
trajectory recording toward portable, multimodal, and embodiment-aware interfaces that jointly
improve scalability and demonstration fidelity.
ii) Human-in-the-Loop Enhancement
Human-in-the-loop methods reduce the need for operators to demonstrate complete trajectories by
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
allowing an autonomous policy to execute most of the task while humans selectively provide guidance
or correction around difficult states and failure modes. IntervenGen [1228] uses a small number of
human interventions as seeds and automatically generates additional corrective trajectories around
encountered failure states, expanding the state-space coverage of intervention data without requiring
proportional human effort. CR-DAgger [1229] further targets contact-rich manipulation through a
compliant intervention interface that allows operators to provide continuous delta-action corrections
without interrupting policy execution and uses the resulting correction signals to learn a force-aware
residual policy. These approaches shift human supervision from exhaustive demonstration toward
targeted intervention, concentrating human effort on states where autonomous policies are most
prone to failure.
iii) Synthetic and Automatic Data Generation
Human demonstrations remain expensive and inherently limited in coverage. Synthetic and
automatic approaches amplify a small amount of supervision into substantially larger and more
diverse datasets through foundation-model guidance, demonstration transformation, simulation,
constrained optimization, and autonomous policy improvement.
Foundation-Model-Guided Generation. Foundation models can provide semantic task specifications
and planning priors for generating robot experiences. Scaling Up and Distilling Down [1230] uses
language-guided task generation and planning to acquire diverse robot skills and subsequently distills
the resulting experience into a multitask visuomotor policy. Manipulate-Anything [1231] leverages
vision–language models to autonomously generate and correct real-world robot behaviors without
relying on privileged task information or manually specified skill libraries. SOAR [1232] similarly uses
foundation models to support improvement of instruction-following skills, illustrating how semantic
reasoning can increasingly replace manually designed task-generation pipelines.
Demonstration Transformation and Synthesis. Another major direction transforms a small number
of source demonstrations into new trajectories under varied task configurations. MimicGen [1233]
decomposes source demonstrations and adapts their object-relative segments to novel scene configura-
tions, enabling large-scale generation from limited human supervision. DexMimicGen [1234] extends
this strategy to coordinated bimanual and dexterous manipulation, while SkillMimicGen [1235]
organizes generation around reusable manipulation skills. DemoGen [1236] further combines trajec-
tory adaptation with 3D point-cloud editing to transform both actions and observations, enabling
synthetic demonstration generation from extremely limited source data. Lucid-XR [1237] comple-
ments trajectory-level transformation with an XR-based synthetic data engine that combines on-device
physics simulation, human-to-robot retargeting, and physics-guided video generation to amplify
virtual interactions into diverse visuomotor training data.
Physics- and Constraint-Aware Generation. Pure geometric transformation does not necessarily
preserve robot kinematics, contact dynamics, collision constraints, or task feasibility. Physics-Driven
Data Generation [1238] addresses this by combining embodiment-flexible human demonstrations
with kinematic retargeting and trajectory optimization, producing physically consistent contact-
rich trajectories across robot embodiments and physical parameters. CP-Gen [1239] represents
manipulation skills through keypoint-trajectory constraints and generates demonstrations under novel
object poses and geometries while preserving task-relevant geometric relations. MoMaGen [1240]
extends constraint-aware generation to multi-step bimanual mobile manipulation by satisfying hard
constraints such as reachability and collision avoidance while balancing soft constraints associated
with visibility during navigation and manipulation. These methods mark a shift from unconstrained
demonstration replay toward data generation that preserves physical and task structure.
Autonomous and Self-Improving Generation. Recent methods further close the loop between policy
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
RoboTurk
Automation
Generation
XR Interfaces
Human Teleoperation and Demonstration
Crowdsourcing
Synthetic and Automatic Data Generation
Human-in-the-Loop Enhancement

## sec:data-2 Data
_Pages 80-84_

Collection
Figure 22 | Overview of Data Collection. DEXUMI [1224] employs Replica arms, and ARCAP [1220]
uses XR Interfaces to represent the data collection methods for Human Teleoperation and Demonstra-
tion. DexCap [1223] stands for Human-in-the-Loop Enhancement, NILS [1271] represents Automatic
Data Generation, MimicGen [1233] refers to Synthetic Data Generation, and RoboTurk represents
Crowdsourcing-based Data Collection.
learning and data generation, allowing progressively improved policies to generate subsequent training
experience. RoboCat [1241] alternates policy adaptation with autonomous experience generation,
incorporating newly acquired successful trajectories into subsequent training rounds to progressively
expand task coverage. DexFlyWheel [1242] develops a more explicit data flywheel for dexterous
manipulation by integrating imitation learning, residual reinforcement learning, policy rollouts,
trajectory filtering, and data augmentation in an iterative cycle. Rather than treating synthetic
generation as a one-shot preprocessing step, these systems progressively expand the data distribution
as the underlying policy improves.
iv) Crowdsourcing-based Data Collection
Crowdsourcing reduces the cost and expertise barriers of robot demonstration collection by
distributing data acquisition across large numbers of contributors. Early work established the feasibility
of platform-based crowdsourced imitation learning [1243], while RoboTurk [1244] introduced
smartphone-based remote teleoperation with a cloud backend, allowing geographically distributed
workers to collect large-scale manipulation demonstrations using commodity devices. Subsequent
systems extended crowdsourcing toward real-robot and multi-arm settings [1245, 1246]. AR2-
D2 [1247] reduces dependence on robot hardware during collection by using an iOS augmented-
reality interface to capture human–object interactions and scene geometry for subsequent robot
retargeting, while EgoZero [1248] explores lightweight smart glasses for distributed in-the-wild
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
human demonstration collection. More recently, COBALT [1249] combines cloud-based infrastructure
with concurrent teleoperation and commodity interfaces including smartphones and VR devices,
substantially broadening the geographic and hardware accessibility of crowdsourced robot-data
acquisition.
Overall, robot data collection is evolving along several complementary axes. Teleoperation systems
increasingly improve accessibility, multimodal feedback, and embodiment alignment; human-in-the-
loop methods concentrate supervision around informative failures; synthetic generation increasingly
preserves physical and task constraints; self-improving systems close the loop between data and policy
learning; and crowdsourcing distributes collection across broader populations. These paradigms are
complementary rather than mutually exclusive and can be combined within large-scale data engines
that jointly balance human effort, data quality, diversity, embodiment fidelity, and scalability.
7.1.2. Data Utilization
Effectively utilizing existing data is essential for improving robot policy performance, especially under
constraints of limited data collection budgets. Recent research has explored strategies for selecting,
retrieving, relabeling, augmenting, expanding, and reweighting data so that existing experience
contributes more effectively to downstream policy learning.
i) Data Selection
Raw robot datasets often contain noise, redundancy, inconsistent demonstrations, or imbalanced
domains. Recent work [1250–1257] therefore studies how to select, filter, and adjust training
data through trajectory filtering, preference-based pruning, domain-mixture curation, and source
selection. EIL [1251] filters extraneous demonstration segments by learning action-conditioned
embeddings with temporal cycle consistency and applying an unsupervised voting-based alignment
procedure. L2D [1254] evaluates heterogeneous human demonstrations through latent trajectory
representations and preference learning, then selects higher-quality examples for offline imitation
learning. Re-Mix [1256] formulates dataset curation as minimax reweighting over domain mixtures
using excess behavior-cloning loss, automatically emphasizing domains that improve generalist policy
performance. CUPID [1258] further introduces policy-aware data curation by estimating the influence
of individual demonstrations on downstream closed-loop policy return, allowing harmful trajectories
to be removed and newly collected trajectories to be prioritized according to their expected benefit.
Other approaches include EAD [1250], which elicits demonstrations through compatibility signals;
DC-IL [1252], which characterizes data quality using action divergence and transition diversity;
UVP [1253], which highlights the importance of pretraining-data distribution; ILID [1255], which
selects state–action pairs using a state-only discriminator; and MimicLabs [1257], which emphasizes
camera-pose and spatial diversity when constructing training subsets.
ii) Data Retrieval
Retrieval-based approaches address the data bottleneck by mining task-relevant demonstrations
or sub-trajectories from large prior corpora, thereby reducing sample complexity and improving
transferability [1259–1268]. A first line of work couples representation learning with non-parametric
retrieval. VINN [1259] learns a self-supervised visual encoder and performs nearest-neighbor search
in latent space, yielding a strong policy without gradient-based fine-tuning. SAILOR [1260] organizes
prior experience into a latent space of short-horizon skills and retrieves similar sub-trajectories as
reusable motion primitives, accelerating few-shot adaptation. Behavior Retrieval [1261] introduces a
variational encoder to score state–action similarity, seeding retrieval with limited expert rollouts and
jointly training on expert and retrieved data.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
More recent methods emphasize adaptation and integration of retrieved experience. Di Palo and
Johns [1262] retrieve and replay demonstrations through a decide–align–execute framework, while
DINOBot [1263] adapts demonstrations to novel objects through pixel-level alignment using DINO-ViT
features. RAEA [1264] integrates trajectories retrieved from multimodal memory directly into action
prediction, and GSR [1265] organizes prior interactions as a graph over pretrained embeddings
to identify high-value behaviors through search. FlowRetrieval [1266] leverages optical flow to
mine cross-task motion segments, STRAP [1267] retrieves sub-trajectories using visual foundation
models and time-invariant alignment, and COLLAGE [1268] combines multiple similarity signals
with adaptive weighting to curate task-relevant subsets. Together, these methods show that retrieval
can serve as both an alternative and a complement to parametric policy learning, enabling efficient
reuse of large heterogeneous experience corpora.
iii) Data Augmentation
Data augmentation increases the effective diversity of existing datasets without requiring propor-
tional collection effort. We organize existing approaches into three families: language and trajectory
relabeling, physics- and geometry-consistent augmentation, and generative visual, viewpoint, and
embodiment augmentation.
Language, Goal, and Trajectory Relabeling. This family reinterprets existing demonstrations by mod-
ifying their semantic labels, goals, temporal decomposition, or trajectory assignments. DIAL [1269]
automatically generates language instructions for unlabeled demonstrations using pretrained vision–
language models, while SPRINT [1270] relabels and composes language instructions across exist-
ing trajectories to support long-horizon skill chaining. NILS [1271] performs zero-shot natural-
language annotation of long-horizon robot videos using foundation models. Beyond language labels,
DAAG [1272] generates temporally and geometrically consistent trajectory relabelings using diffusion
models, and S2I [1273] segments demonstrations, selects useful segments, and optimizes trajectories
to better exploit mixed-quality data. Related efforts include goal relabeling in GoalGAIL [1274] and
counterfactual sample generation through variational reasoning in OILCA [1275].
Physics- and Geometry-Consistent Augmentation. This family transforms existing trajectories while
preserving physical or geometric validity. Mitrano and Berenson [1276] formulate augmentation as
an optimization problem that applies rigid-body transformations while maintaining manipulation
constraints. Wang et al. [1277] identify high-quality rollouts and exploit environmental symmetries
to construct principled augmentations. SEIL [1278] similarly exploits task symmetries to combine
expert demonstrations with simulation-augmented equivariant transitions, improving data efficiency
while preserving task structure.
Generative Visual, Viewpoint, and Embodiment Augmentation. Generative models provide another
mechanism for increasing perceptual and embodiment diversity while preserving the underlying
behavior. GenAug [1279] applies pretrained generative models to perform semantic scene edits
that preserve demonstrated actions. RoVi-Aug [1280] uses diffusion-based image translation to
synthesize demonstrations across robot embodiments and camera viewpoints, enabling transfer to
unseen configurations. RoboPearls [1281] leverages editable 3D Gaussian Splatting reconstructions
for language-guided demonstration synthesis. Additional approaches include text-guided visual modi-
fication in ROSIE [1282], novel-view generation in DMD [1283], single-image 3D-aware viewpoint
synthesis in VISTA [1284], and multi-rate sensory alignment in DABI [1285].
iv) Data Expansion
Data expansion goes beyond modifying individual training samples and instead increases the
amount of usable experience by synthesizing, recombining, or selectively collecting additional trajec-
tories. Existing approaches can be broadly divided into synthesis and imagined rollouts, and reuse
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
and corrective expansion.
Synthesis and Imagined Rollouts. Generative Predecessor Models [1286] learn distributions over
predecessor states and synthesize state–action samples that lead into expert trajectories, densifying the
space of successful behaviors. Self-Imitation by Planning [1289] uses planners to generate improved
rollouts for existing tasks and iteratively appends them to the dataset, creating an improve–add–imitate
loop. Category-Level Manipulation [1290] applies adversarial self-imitation to generate additional
category-level trajectories, improving generalization across object instances. SAFARI [1287] generates
imagined rollouts under safety and corrective constraints, while TASTE-Rob [1288] produces task-
oriented hand–object interaction videos that provide additional visual and interaction supervision.
Reuse and Corrective Expansion. Scalable Multi-Task Imitation Learning [1291] relabels collected
trajectories across tasks so that individual demonstrations provide supervision for multiple goals.
JUICER [1292] decomposes demonstrations into reusable motion segments and recomposes them into
new task sequences, enabling combinatorial expansion from a limited skill library. Diff-DAgger [1293]
estimates policy uncertainty with diffusion models and selectively acquires corrective demonstrations
in uncertain regions, concentrating additional supervision around likely failures.
v) Data Reweighting
Data reweighting assigns different importance to demonstrations according to quality, feasibility,
expertise, or preference signals rather than treating all data uniformly. Beliaev et al. [1294] estimate
individual demonstrator expertise and use the resulting estimates to weight demonstrations during
imitation learning. FABCO [1295] evaluates demonstration feasibility using robot dynamics and
assigns higher training weight to trajectories that are more compatible with the target embodiment.
PLARE [1296] instead queries a large vision–language model for preference labels over trajectory
segments and optimizes the policy directly from these pairwise preferences using a contrastive
objective. Together, these approaches show that weighting data according to expertise, feasibility, or
preference can improve policy learning under heterogeneous and imperfect demonstrations.
7.2. Generalization
Robotic manipulation generalization can be broadly categorized into three dimensions: environ-
ment generalization, task generalization, and cross-embodiment generalization. Environment
generalization concerns robustness to variations in conditions such as Sim2Real transfer, spatial
transformations, lighting, and background or distractor changes. Task generalization emphasizes
maintaining performance across different task configurations, including long-horizon tasks, few-shot
or meta-learning, continual learning, and skill composition. Cross-embodiment generalization focuses
on transferring skills across robots with diverse morphologies, kinematics, dynamics, or sensing
modalities, which is crucial for building general-purpose embodied agents. In what follows, we
structure our survey along these three perspectives.
7.2.1. Environment Generalization
Environment generalization in robotic manipulation refers to the ability of policies trained under
specific conditions to maintain performance across varying environments, scenes, viewpoints, and
physical settings. Such generalization is challenged by discrepancies between simulation and reality,
spatial transformations of objects and cameras, and visual appearance changes such as lighting,
backgrounds, and distractors. Existing approaches address these challenges from several complemen-
tary perspectives, including sim-to-real and real-to-sim-to-real transfer, geometric equivariance and
viewpoint robustness, and robustness to other visual environmental variations.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Environment
Generalization
1. Sim2Real and Real2Sim2Real
2. SE(3) and SIM(3)-Equivariance
Task
Generalization
1. Long-Horizon Tasks
2. Compositional Generalization
3. Few-shot Learning
Cross-Embodiment
Generalization
1. Human2Robot Generalization
2. Similar-embodiment Cross-robot
Generalization
Real2Sim
Sim2Real
Real2Real
Equivariant policy
4. Meta Learning
5. Lifelong and Incremental Learning
decomposition
few
demos
complete
Train
Adaptation
press
button
drawer
open
box
close
3. Others

## sec:background-3 Background
_Pages 84-99_

Distractor
Lighting
3. Heterogeneous Cross-embodiment
Generalization
Figure 23 | Overview of generalization. The figure is adapted from representative studies in environ-
ment generalization [1168, 1297, 1298], task generalization [1299, 1300], and cross-embodiment
generalization [1301–1303].
i) Sim2Real and Real2Sim2Real Generalization
Simulation offers a scalable alternative for training and evaluating manipulation policies, alle-
viating the cost, operational risk, and safety concerns associated with large-scale real-world data
collection. However, discrepancies in dynamics, sensing, visual appearance, and environmental
complexity often result in poor transferability, commonly referred to as the sim-to-real gap [1304].
Existing approaches can be broadly organized into three paradigms according to how simulated and
real-world experience are combined: simulation-only training, sim–real adaptation and co-training,
and real2sim2real reconstruction.
Simulation-Only Training. This paradigm assumes that sufficient variability introduced during
simulation training can enable policies to transfer directly to the real world without further adaptation.
Domain randomization is a representative strategy, where physical parameters such as mass, friction,
and damping [1305], as well as perceptual factors such as textures [1306], lighting [1307], and
object poses [1308], are systematically perturbed to prevent policies from overfitting to a specific
simulator configuration. Peng et al. [1309] demonstrate that randomized dynamics can substantially
improve real-world transfer, while more recent systems such as DexScale [1310] scale simulation
diversity and augmentation to increasingly complex manipulation settings. Nevertheless, zero-shot
transfer remains difficult when simulated variability fails to capture fine-grained visual, contact, or
dynamic properties of real environments.
Sim–Real Adaptation and Co-Training. Rather than relying exclusively on simulation, another
line of work introduces a limited amount of real-world experience to anchor policy learning. Earlier
approaches primarily adapt simulation-trained policies through real-world fine-tuning or continual
learning; for example, Josifovski et al. [1311] study safe continual adaptation under deployment
constraints. Natural Language Can Help Bridge the Sim2Real Gap [1312] instead uses language
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
descriptions as a shared semantic signal across simulated and real observations, encouraging domain-
invariant representations while training with abundant simulated and sparse real demonstrations.
More recently, Sim-and-Real Co-Training [1313] systematically demonstrates that directly training a
shared policy on mixed simulated and real datasets can substantially improve real-world manipulation
performance even when noticeable visual and behavioral discrepancies remain between domains.
Generalizable Domain Adaptation [1314] further aligns the joint distributions of observations and
actions across simulation and reality through optimal-transport-based objectives, learning task-
relevant domain-invariant representations and enabling simulated experience to improve real-world
performance even in scenarios not represented by the limited real demonstrations. These developments
shift sim-to-real learning from post-hoc policy correction toward joint exploitation of large-scale
simulation and sparse real-world supervision.
Real2Sim2Real Reconstruction. A complementary paradigm closes the loop by reconstructing
simulatable or renderable environments from real-world observations and subsequently using these
reconstructions for policy learning [1315, 1316]. RialTo [1315] constructs task-specific digital twins
from limited real-world sensing and introduces inverse distillation to transfer real demonstrations into
simulation, where reinforcement learning can safely improve policy robustness before deployment
back in the real world. Real2Render2Real [1316] reduces dependence on both dynamics simulation
and physical robot collection by reconstructing object geometry and appearance from smartphone
scans and tracking object motion from a single human demonstration, enabling large-scale rendering
of robot-compatible training trajectories. Real2Edit2Real [1317] further introduces a metric 3D
control interface that edits reconstructed scenes and manipulation trajectories and uses depth-
conditioned video generation to synthesize geometrically consistent demonstrations under new
spatial configurations. These approaches illustrate an emerging transition from manually constructed
simulation environments toward real-world-grounded digital reconstruction and editable synthetic
environments for scalable policy generalization.
ii) SE(3) and SIM(3)-Equivariance Generalization
A complementary strategy for environment generalization is to explicitly encode geometric
symmetry into policy architectures. SE(3)- and SIM(3)-equivariant models constrain representations
or actions to transform predictably under changes in translation, rotation, and, for SIM(3), scale,
thereby reducing the need to independently observe every spatial configuration during training.
EquiBot [1168] introduces a SIM(3)-equivariant diffusion policy that improves data efficiency and
generalization across changes in object pose and scale. ET-SEED [1318] develops an efficient trajectory-
level SE(3)-equivariant diffusion policy and relaxes the requirement that every transition in the
diffusion process must independently employ expensive equivariant computation. More recently,
E3Flow [1319] combines spherical-harmonic-based equivariant representations with rectified flow
and multimodal visual features, extending geometric equivariance toward more efficient flow-based
visuomotor policy learning. Together, these methods demonstrate how explicit geometric structure
can provide strong inductive biases for spatial generalization.
Viewpoint Robustness Beyond Explicit Equivariance. Related approaches address viewpoint
changes without requiring the policy to satisfy explicit SE(3) or SIM(3) equivariance. Adapt3R [892]
combines pretrained semantic visual features with end-effector-relative 3D localization, enabling
imitation policies to transfer across unseen camera viewpoints and robot embodiments. Another
direction actively changes the observation process itself rather than passively requiring the policy
to tolerate arbitrary viewpoints. Vision in Action [1320] learns task-dependent searching, tracking,
and focusing behaviors from human demonstrations using an actuated robotic neck, allowing the
robot to recover informative viewpoints when objects become occluded. SaPaVe [1321] extends
active perception to VLA-based manipulation by decoupling camera motion from manipulation
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
actions and coordinating semantic camera control with geometry-aware execution. These methods
complement explicit equivariance by either constructing viewpoint-robust spatial representations or
actively controlling perception to maintain informative observations during manipulation.
iii) Others
Lighting, background, and distractor variations constitute another major source of environment
shift, as visuomotor policies can overfit to visual cues that correlate with demonstrations but are
irrelevant to task execution. Existing approaches address these variations through augmentation,
invariant representation learning, and training across heterogeneous visual contexts. Physically based
augmentation methods explicitly vary illumination during training to improve robustness under
lighting changes [1322]. Decomposing the Generalization Gap [1323] systematically analyzes how
individual visual factors contribute to imitation-learning generalization failures, highlighting the
importance of separating task-relevant information from nuisance variations. Maniwhere [1324] com-
bines multi-view representation learning with curriculum-based randomization and augmentation to
improve robustness across combinations of visual disturbances and support sim-to-real transfer. Other
approaches reduce dependence on incidental scene context through position-invariant regulariza-
tion [1325] or by learning from demonstrations collected under changing contexts [1326, 1327]. At
a larger scale, Diffusion-VLA [913] demonstrates that large multimodal foundation policies can retain
manipulation performance under unseen objects, distractors, and new backgrounds, suggesting that
broad pretraining can complement explicit augmentation and invariance mechanisms. Collectively,
these methods aim to prevent policies from relying on spurious visual correlations and preserve
task-relevant behavior under substantial changes in environmental appearance.
7.2.2. Task Generalization
Task generalization in robotic manipulation refers to the ability of learned policies to adapt to new,
complex, or unseen tasks without extensive retraining. It encompasses the generalization of learned
skills, structures, and adaptation mechanisms across variations in task composition, semantics, and
temporal scope. Robust task generalization requires policies not only to execute individual skills but
also to compose, transfer, and refine them under new configurations and objectives.
i) Generalization for Long-horizon Tasks
Long-horizon robotic manipulation represents a core challenge for embodied intelligence. Unlike
short-horizon tasks that typically involve single-skill execution, long-horizon problems demand the
coordination of multiple sub-skills, hierarchical reasoning, and temporally abstract decision-making.
Robust generalization requires agents not only to plan and execute extended action sequences but
also to adapt across variations in task structure, object arrangement, and dynamic environments.
Recent advances approach this challenge along three interconnected axes: skill compositionality,
semantic task decomposition, and structure-aware representation learning.
Skill Compositionality. At the foundation lies the ability to compose and reuse modular skills [1328–
1334]. STAP [1332] addresses sequencing by optimizing the feasibility of action chains. Generative
frameworks such as BOSS [1333] and BLADE [1334] leverage large language models to autonomously
expand skill libraries and incorporate semantic grounding into action spaces, thereby enabling flexible
skill reuse and extension.
Semantic Task Decomposition. Beyond static skill composition, multimodal semantics have been
introduced to parse and decompose tasks into modular components [1335–1340]. PALO [1336]
employs vision-language models to translate high-level task descriptions into reusable sub-tasks,
enabling rapid adaptation with minimal supervision. ManipGen [1337] integrates local policies that
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
encode invariances in pose, skill order, and scene layout, combining them with foundational models
in vision and motion planning to generalize across unseen long-horizon sequences.
Structure-aware Representation Learning. A finer level of generalization is achieved through
task-level abstraction and representation learning [1341–1346]. TBBF [1344] decomposes complex
tasks into primitive therbligs, facilitating efficient action-object mappings and trajectory synthesis.
RoboHorizon [1345] formalizes a Recognize-Sense-Plan-Act pipeline by fusing LLMs with multi-view
world models, addressing sparse reward supervision and perceptual complexity. HD-Space [1346]
identifies atomic sub-task boundaries from demonstrations, improving sample efficiency and policy
robustness with limited data.
ii) Compositional Generalization
Compositional generalization in robotic manipulation emphasizes the ability to solve novel tasks
by systematically recombining known skills, objects, and instructions. Recent research explores
diverse strategies to achieve this capability. One line of work focuses on data-driven efficiency, where
targeted data collection strategies are designed to maximize coverage of compositional variations with
minimal demonstrations, enabling scalable policy training [1299]. Another approach grounds policies
in programmatic or symbolic structures, allowing robots to leverage modular task representations
for systematic recomposition and generalization to unseen task combinations [1347]. Complemen-
tary efforts investigate policy architectures that explicitly factorize control into entities or modules,
facilitating the recombination of learned components to improve adaptability in complex environ-
ments [1348]. Together, these methods illustrate a growing effort to move beyond rote memorization
of tasks toward systematic generalization, enabling robots to flexibly adapt to combinatorial task
spaces.
iii) Few-shot Learning
Few-shot learning enables robots to acquire skills from only a handful of demonstrations [1349–
1353], alleviating the high cost of large-scale data collection. Research in this area can be broadly
grouped into two directions: embedding structured priors and leveraging semantic transfer. One line of
work embeds structured inductive biases into perception and control to maximize the utility of limited
demonstrations. Domain-invariant constraints, including spatial equivariance, 3D geometry, or action
continuity, are incorporated to reduce data requirements and improve generalization. For example,
Ren et al. [1354] combine point cloud representations with a diffusion-based policy, achieving robust
generalization from as few as ten demonstrations. A complementary line of research emphasizes
semantic transfer and compositional generalization. These methods extract transferable knowledge
from alternative sources, such as human demonstrations or previously solved tasks, and adapt it to
new objectives. For instance, YOTO [1206] maps human hand motions from video to dual-arm robotic
skills, while TOPIC [1355] constructs task prompts and a dynamic relation graph to systematically
reuse prior experience for new policy learning.
iv) Meta Learning
While closely related to few-shot learning, meta learning distinguishes itself by focusing on the
ability to amortize task adaptation. Instead of relying directly on structural priors or semantic transfer
to generalize from a handful of demonstrations, meta learning trains over a distribution of tasks so
that the model acquires a generic adaptation procedure. This paradigm equips robots with rapid
adaptability to unseen tasks, even under extremely limited supervision [10, 1356–1361].
Task-Conditioned Meta-Representations. One direction focuses on learning task-conditioned embed-
dings that serve as meta-representations. Early approaches such as Duan et al. [10] and TecNets [1356]
encode demonstrations into low-dimensional vectors for policy conditioning. Later works extend
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
this idea with relational graph networks [1357] or invariance-based objectives [1358], enforcing
structural consistency across tasks. These embedding-based approaches highlight the importance of
compact task representations in accelerating policy adaptation.
Cross-Modal and Instruction-Driven Adaptation. Another direction emphasizes the integration
of additional modalities and task instructions into the adaptation process. MILLION [1359] incor-
porates natural language into the meta-learning loop, enabling semantically guided adaptation.
FISH [1360] demonstrates versatile skill acquisition from just one minute of demonstrations, while
interaction-warping [1361] aligns novel trajectories with past interaction structures to facilitate
transfer. Collectively, these works establish meta learning as a principled framework for scalable and
data-efficient generalization.
v) Lifelong, Continual and Incremental Learning
Endowing robots with the ability to continuously acquire new capabilities is a key step toward
adaptive and autonomous embodied agents. Unlike conventional task generalization, which typi-
cally evaluates transfer to a fixed set of unseen tasks, lifelong and incremental learning consider
a non-stationary setting in which new tasks or skills arrive sequentially. The central challenge is
therefore twofold: newly acquired knowledge should benefit future learning, while previously learned
capabilities should be retained without repeated full retraining. In robotic manipulation, existing
approaches can be broadly distinguished into lifelong or continual learning, which emphasizes knowl-
edge retention and transfer across a sequence of tasks, and skill-incremental learning, which focuses
more explicitly on expanding and updating an evolving repertoire of manipulation skills.
Lifelong and Continual Learning. Lifelong and continual learning aims to retain and reuse knowl-
edge as robots encounter a sequence of new manipulation tasks [1362–1365]. A major direction is to
organize manipulation knowledge into reusable modular components. LOTUS [1300] continually
discovers recurring skills from incoming task demonstrations, incrementally expands or updates
a skill library, and composes these skills through a hierarchical meta-controller, enabling forward
and backward transfer across sequential tasks. PPL [1362] instead represents shared motion prim-
itives as reusable and extensible prompts; pretrained primitive prompts are preserved while new
prompts are introduced for incoming skills, allowing previous knowledge to facilitate subsequent
learning without overwriting existing capabilities. Complementary approaches focus more directly
on preserving learned representations. M2Distill [1363] employs multimodal knowledge distillation
to maintain consistent representations across sequential tasks and mitigate catastrophic forgetting,
while CRIL [1364] uses generative replay to preserve experience from previously learned behaviors.
Together, these approaches show that continual robot learning increasingly combines modular skill
reuse with explicit mechanisms for knowledge preservation, balancing forward transfer to new tasks
against retention of previously acquired capabilities.
Incremental Learning. In contrast, skill-incremental learning focuses more explicitly on settings
in which robots progressively acquire or refine atomic manipulation skills while preserving their
existing skill repertoire. iManip [1366] formalizes this setting with a skill-incremental benchmark
built on RLBench [101] and introduces temporal replay together with an Extendable PerceiverIO,
whose expandable action prompts accommodate new action primitives while mitigating catastrophic
forgetting of previously learned skills. SIL-C [1367] further reveals that incremental skill acquisi-
tion introduces an additional challenge beyond forgetting: as the underlying skill library evolves,
previously learned high-level policies may become incompatible with newly added or updated skills.
To address this issue, SIL-C introduces a lazy-learning interface that dynamically aligns policy-level
subtasks with the evolving skill space according to trajectory-distribution similarity, allowing new
skills to be incorporated while maintaining compatibility with existing downstream policies. These
approaches highlight two complementary aspects of skill-incremental manipulation: extending the
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
policy representation to accommodate new primitives and maintaining a stable interface between an
evolving skill library and previously learned task policies.
7.2.3. Cross-Embodiment Generalization
Cross-embodiment generalization refers to the ability to transfer manipulation knowledge across
agents or robotic platforms with different visual appearances, kinematics, action spaces, morpholo-
gies, or sensing configurations. Rather than categorizing existing approaches according to specific
algorithmic mechanisms, we organize this direction according to the relationship between the source
and target embodiments. Specifically, existing studies can be broadly divided into human-to-robot
generalization, cross-robot transfer between functionally similar embodiments, and heterogeneous
cross-embodiment generalization across substantially different robot morphologies and action spaces.
i) Human-to-Robot Generalization
Human demonstrations provide a scalable source of manipulation experience, but transferring
them to robots requires bridging substantial differences in appearance, sensing, morphology, and
action spaces. Early approaches therefore seek embodiment-invariant representations or trans-
ferable intermediate signals that preserve task semantics while suppressing embodiment-specific
motion details. XSkill [1301] discovers shared skill prototypes from unlabeled human and robot
manipulation videos and maps them to robot actions through a skill-conditioned diffusion policy.
Human2Sim2Robot [1368] instead extracts object trajectories and hand configurations from a single
human RGB-D demonstration and converts them into embodiment-agnostic rewards and initialization
priors for reinforcement learning in simulation. X-Sim [1369] similarly avoids direct human-to-robot
action mapping by reconstructing photorealistic simulation from human videos and using object
motion as a transferable learning signal before distilling the resulting behavior into a real-world policy.
More recent methods explicitly align human and robot representations during policy learning.
UniSkill [881] learns embodiment-agnostic skill representations from large-scale unlabeled cross-
embodiment videos, allowing skills extracted from human video prompts to guide robot policies
trained with robot actions. ImMimic [1370] maps retargeted human trajectories to robot trajectories
and constructs intermediate domains through trajectory interpolation, reducing visual, morphological,
and physical discrepancies during co-training. EgoBridge [1371] further formulates human-to-robot
transfer as domain adaptation and aligns joint latent feature–action distributions using optimal
transport guided by trajectory similarity. Together, these approaches illustrate a progression from
indirect motion and object-centric transfer toward explicit human–robot representation alignment.
ii) Similar-Embodiment Cross-Robot Generalization
A second setting considers transfer between robot platforms that retain similar functional struc-
tures, such as serial manipulators equipped with comparable end effectors. Although these robots
may differ in appearance, degrees of freedom, kinematics, or control dynamics, substantial policy
knowledge can often be reused without learning entirely new behavioral abstractions. Mirage [1303]
enables zero-shot transfer between different robot arms and grippers by separately correcting percep-
tual and control discrepancies through cross-painting, state alignment, and dynamics compensation.
Wang et al. [1372] instead project heterogeneous state and action spaces into a shared latent control
space, enabling transfer across manipulators with mismatched kinematics. Modularity through Atten-
tion [1373] takes a complementary approach by decomposing language-conditioned manipulation
policies into reusable functional components and robot-specific modules, so that only embodiment-
dependent components need to be adapted. These studies show that when source and target robots
remain functionally similar, transfer can often be achieved through selective alignment of perception,
control, or modular policy components.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
iii) Heterogeneous Cross-Embodiment Generalization
The most challenging setting considers substantially heterogeneous embodiments whose observa-
tion spaces, action dimensions, kinematic structures, or functional capabilities may differ significantly.
One direction addresses this problem through large-scale heterogeneous co-training and shared
policy representations. Pushing the Limits of Cross-Embodiment Learning [1302] jointly learns from
manipulation and navigation data spanning robotic arms, mobile bases, quadrupeds, and aerial robots,
demonstrating positive transfer across markedly different embodiments. CrossFormer [1374] further
represents heterogeneous observations and actions as variable-length token sequences processed by a
shared Transformer, supporting manipulation, navigation, locomotion, and aviation within a unified
policy. HPT [876] adopts a modular alternative by combining embodiment-specific input stems and
output heads with a shared Transformer trunk, allowing heterogeneous visual and proprioceptive
data to contribute to common policy pretraining.
A complementary direction constructs explicit structural, functional, or system-level bridges
between different morphologies. AnyBimanual [1375] transfers pretrained unimanual skills to
bimanual manipulation by composing reusable skill representations and aligning arm-specific visual
observations. LEGATO [1376] introduces a shared grasping tool that provides a common interaction
interface across embodiments, allowing manipulation behaviors to be retargeted through embodiment-
specific inverse kinematics. CEI [1377] explicitly models functional similarity between different robot
arms and end effectors and aligns trajectories in 3D space, including transfer between parallel-jaw
grippers and dexterous hands. At a higher abstraction level, RoboOS [1378] organizes heterogeneous
robot capabilities through standardized interfaces for perception, control, communication, and skill
execution, enabling reusable high-level skills to operate across different robotic platforms. Together,
these methods show that heterogeneous cross-embodiment transfer can be supported through shared
policies, functional correspondence, common physical interfaces, and system-level abstraction.
7.3. Agent
Recent advances in foundation models have motivated agent-based robotic manipulation systems that
augment learned policies with higher-level reasoning, tool use, memory, verification, and adaptation.
Rather than replacing low-level manipulation policies or VLA models, agents typically orchestrate
these components within closed perception–reasoning–action loops, enabling long-horizon task
decomposition, execution monitoring, failure recovery, and continual improvement. This paradigm
extends language-based robotic planning toward persistent embodied systems that can adapt their
behavior during deployment.
Planning and Tool Orchestration. Early language-grounded systems establish the foundation for
agent-based manipulation by connecting high-level reasoning with executable robot skills. Say-
Can [420] grounds language-model planning in learned skill affordances, Code as Policies [455]
synthesizes executable robot programs, Inner Monologue [422] incorporates environmental feedback
for closed-loop replanning, and VoxPoser [465] grounds language instructions into spatial value
maps. Recent agentic systems increasingly orchestrate learned policies and external tools. Agentic
Robot [1379] coordinates reasoning, VLA execution, and temporal verification for long-horizon manip-
ulation, while VLA2 [1380] invokes external perception and retrieval tools to improve manipulation
of unseen concepts. Guava [1381] studies agent workflows, action abstractions, and multimodal
observations for embodied tool use, whereas Harness VLA [1382] combines a frozen VLA with analytic
primitives and execution memory to improve robustness beyond its original task distribution.
Memory and Runtime Adaptation. Memory enables agents to accumulate execution experience and
adapt without repeatedly modifying the underlying policy. SOMA [1383] augments frozen VLAs with
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
dual-memory retrieval, failure attribution, and agent-driven interventions for in-context adaptation.
Long-Term Memory for VLA-based Agents [1384] similarly combines hierarchical planning with
persistent trajectory memory for long-horizon execution. Agentic-VLA [1385] further integrates
experience memory with adaptive reward synthesis and language-guided exploration for efficient
online adaptation. These methods shift robot deployment from isolated policy execution toward
persistent agents that reuse prior successes and failures to improve subsequent decisions.
Policy Synthesis and Self-Improvement. Beyond runtime adaptation, recent agents increasingly
modify the programs, data, or policies that govern robot behavior. ARCHITECT [1386] formulates
robot policy acquisition as interactive program synthesis, using language corrections and execu-
tion traces to build reusable skill libraries. ENPIRE [1387] establishes an autonomous real-world
improvement loop in which agents execute, evaluate, diagnose, and improve robot policies, while
RoboClaw [1388] unifies autonomous data collection, policy refinement, and long-horizon deploy-
ment through self-resetting manipulation loops and policy orchestration. Together, these approaches
extend agents from policy consumers toward active participants in robot learning and improvement.
Systemization and Multi-Agent Coordination. As agentic manipulation becomes more complex,
recent work increasingly treats orchestration, verification, memory, and safety as system-level capa-
bilities. PhyAgentOS [1389] provides a runtime abstraction that decouples cognitive planning from
physical execution while exposing scheduling, semantic verification, persistent memory, benchmark-
ing, and safety as shared services across embodiments. Multi-agent approaches further distribute
these responsibilities across specialized components. A Closed-Loop Multi-Agent Framework [1390],
for example, separates planning, manipulation, and verification among dedicated agents and uses
execution feedback to coordinate multiple robots during long-horizon manipulation. These develop-
ments suggest a transition from monolithic robot policies toward modular agent systems in which
reasoning models, learned controllers, tools, memories, and physical embodiments interact through
explicit closed-loop interfaces.
7.4. Human–Robot Interaction and Collaboration
Real-world manipulation increasingly requires robots to operate with humans rather than as isolated
autonomous agents. This introduces challenges beyond conventional policy generalization: human
goals may be implicit or change during execution, feedback may arrive through language, gaze, motion,
or physical contact, and the appropriate division of autonomy may vary with uncertainty and user
preference. Recent approaches therefore increasingly treat interaction itself as an information channel
through which robots infer intent, receive corrections, align behavior, and coordinate collaborative
actions.
Human Intent Understanding and Proactive Assistance. A central challenge in human–robot
collaboration is inferring human intent early enough for the robot to provide timely assistance. Pérez-
D’Arpino and Shah [1391] predict human reaching targets from partial motion observations, enabling
robots to anticipate intended objects during cooperative manipulation. More recent approaches
exploit richer interaction signals: EDITH [1392] combines speech with egocentric vision and gaze
to infer human intent and generate grounded subtasks, while Sticky-Glance [1393] stabilizes gaze-
based object intent for continuous interaction. Physical feedback provides another channel, with
TATIC [1394] interpreting brief physical corrections as both task-level intent and motion-level guidance.
Recent methods further address dynamic or underspecified goals: I’ve Changed My Mind [1395]
adapts to changing human objectives, BALI [1396] jointly reasons over actions and language for
open-ended goal inference, and NIABench [1397] studies when and how robots should proactively
assist without interrupting ongoing human activity.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Preference and Uncertainty Alignment. Beyond immediate corrections, effective collaboration
requires robots to infer persistent human preferences and recognize when autonomous decisions
are unreliable. Jain et al. [1398] establish an early framework for manipulation preference learn-
ing from online coactive feedback, allowing users to iteratively improve robot trajectories without
providing explicit reward functions. KnowNo [1399] calibrates uncertainty in language-based robot
planners and requests human assistance when ambiguity is high, while Text2Interaction [1400]
translates natural-language preferences into task, motion, and safety constraints. RAPL [1401] learns
visual rewards from sparse human preferences to align pretrained visuomotor policies with behavior.
M2HRI [1402] incorporates multimodal interaction and long-term memory, extending alignment
from task-level preferences toward persistent human-centered adaptation.
Learning Collaborative Behaviors. Beyond interpreting human feedback, robots must learn policies
whose behavior is inherently coupled with other agents. GenH2R [684] develops scalable simulation
and imitation learning for generalizable human-to-robot handover, while generative simulation for
physical HRI [1403] automatically synthesizes diverse human–robot interaction scenarios for policy
training and sim-to-real transfer. Collaboration also extends to multiple robotic agents: Sequential
Asymmetric Imitation [1404] learns physically coupled robot policies through staged imitation rather
than synchronized multi-operator demonstrations. Together, these directions indicate a transition
from robots that merely respond to explicit instructions toward collaborative agents that continuously
infer human state, adapt autonomy, incorporate feedback, and coordinate their actions with humans
and other robots.
8. Applications
Robotics research plays a central role in advancing intelligent systems with tangible real-world impact.
Over the past decades, robots have evolved from rigid, hard-coded tools executing predefined routines
into perceptive agents capable of interpreting and interacting with their environments, with vision as
a primary modality. Today, empowered by large language models and multimodal foundation models,
the field is rapidly progressing toward embodied intelligence, where robots integrate perception,
planning, and control to accomplish complex tasks in dynamic and uncertain settings [1405, 1406].
This paradigm shift requires not only precise mechanical design but also robust and generalizable
decision-making that enables robots to adapt flexibly across diverse tasks and user instructions. These
advances are fueling applications in domestic, healthcare, industrial, and scientific domains. To
illustrate these developments, Figure 24 presents representative application domains and typical
tasks across sectors. The remainder of this section focuses on these application scenarios, outlining
how robots are being deployed in practice across different fields.
8.1. Household Assistance
Robotic manipulation in household environments targets essential daily activities such as dress-
ing, cooking, feeding, assisting, stowing, object rearrangement, and tool use. Dressing assistance
has been studied through bimanual strategies and safe human-robot interaction with deformable
garments [1407, 1408, 1428]. Cooking and feeding tasks emphasize contact-rich manipulation
and adaptive policies for varied food types and configurations [1408, 1409, 1429]. Assistive care
applications explore shared control, personalized physical interaction, and soft manipulators for
elderly support [309, 1430, 1431]. In particular, PrioriTouch adapts whole-arm physical interaction
to individual user contact preferences, highlighting the growing importance of personalized assistance.
Stowing and object rearrangement tasks leverage behavior primitives, language-guided planning,
and vision-language models to enable flexible scene organization [1410, 1411, 1432–1434]. Finally,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Dressing
Cooking
Feeding
Object Rearrangement
Tool Use
Badminton
Object Unfolding
Pepper Harvesting
Surgery
Endoscopy Capsule
Manipulation
Liquid Handling
Aerospace
Household Assistance
Agriculture
Solution Mixing
Industry
AI4Science
Table Tennis
Art
Sports
Piano Performance
Calligraphy
Drawing
Fruit Harvesting
Cornstalk Sensing
Part Picking and Delivery
Figure 24 | Overview of robotic manipulation applications across diverse domains. The figure is
adapted from representative works in household assistance [1407–1412], agriculture [1413–1415],
industry [1416–1418], AI4Science [1419–1422], art [1423–1425], and sports [1426, 1427].
tool manipulation has emerged as a critical subdomain, where function-centric imitation, language
grounding, and generative design support skill transfer across diverse household tasks [1412, 1435–
1437].
8.2. Agriculture
Agriculture is an important yet highly challenging application domain for robotic manipulation,
where robots must operate in unstructured environments characterized by dense canopies, variable
lighting, irregular crop shapes, and the need for delicate handling. Recent works demonstrate
progress across multiple crop types and farming conditions. For instance, robotic systems have been
deployed for fruit and pepper harvesting in outdoor fields, showing the feasibility of autonomous
harvesting under occlusion and cluttered backgrounds [1413, 1414, 1438]. Other efforts address
the safe manipulation of fragile bio-products, such as irregular poultry carcasses, by integrating
customized grippers with learned control strategies [1439]. Beyond harvesting, new controllers
have been designed for navigating dense plant canopies and adapting to complex interactions with
foliage [1440]. Together, these studies highlight the potential of robotics to enhance productivity,
safety, and precision in agriculture, paving the way toward scalable automation in one of the most
labor-intensive sectors.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
8.3. Industry
In industrial contexts, robotic manipulation plays a crucial role in automating complex and large-scale
processes such as assembly, logistics, and material handling. Early efforts emphasized enabling
autonomous mobile manipulation in structured factory settings, laying the foundation for robots
to navigate and interact in dynamic production environments [1417]. To support system design
and deployment, modeling frameworks such as RobotML have been developed for simulating and
validating industrial manipulation scenarios [1441]. More recent advances demonstrate how intelli-
gent systems can enhance manufacturing flexibility, with reinforcement learning enabling adaptive
assembly strategies that improve efficiency and reduce manual intervention [1442]. At the same
time, specialized applications have emerged to address challenging settings, such as vision-based
manipulation of transparent plastic bags, which are common in industrial packaging and logistics
but difficult for traditional perception systems [1416]. Collectively, these applications illustrate how
robotic manipulation is transitioning from fixed, rigid automation pipelines toward more adaptive,
perception-driven systems capable of handling diverse tasks in real-world industrial environments. It
should be noted, however, that most learning-driven approaches are still evaluated in simulation or
laboratory setups rather than on fully deployed factory lines, as industrial deployment demands strict
reliability and safety, where rule-based systems remain the prevailing choice.
8.4. AI4Science
Robotic manipulation is increasingly being applied as a powerful enabler for scientific discovery, where
precision, repeatability, and autonomy are critical. In medical science, robotic systems are advancing
surgical assistance and minimally invasive procedures, ranging from autonomous intubation [1443],
capsule robot navigation [1420], and robotic spinal fixation [1419], to language-conditioned surgical
planning [1444, 1445] and high-fidelity training simulators such as SonoGym for ultrasound-guided
surgery [1446]. Beyond medicine, robotics also supports biology and life sciences, with platforms like
RoboCulture [1421] enabling automated biological experimentation and robotic micromanipulation
systems providing real-time spatiotemporal assistance in microscopy [1447]. In chemistry, the recently
proposed robotic AI chemist [1448] demonstrates how multi-agent robotic systems can autonomously
conduct chemical experiments on demand, accelerating discovery by integrating automation with
intelligent decision-making. In aerospace, manipulation technologies extend to high-stakes envi-
ronments, such as space assembly and in-orbit trajectory learning for robotic arms [1422, 1449].
More broadly, simulation frameworks like LabUtopia [1450] establish standardized environments
for training and benchmarking embodied scientific agents. Collectively, these applications highlight
how robotics is becoming an essential tool in AI4Science, accelerating progress in medicine, biology,
aerospace, and beyond.
8.5. Art
Robotic manipulation has also found applications in the artistic domain, where tasks such as music
performance, calligraphy, drawing, and co-creative design showcase the expressive and demonstrative
potential of embodied agents. In music, RP1M provides a large-scale motion dataset enabling
robots to perform piano playing with bi-manual dexterous hands, highlighting how robotic systems
can be trained to execute highly coordinated and nuanced actions beyond traditional industrial
tasks [1451]. In visual art, robotic calligraphy demonstrates how imitation learning can support
the reproduction of culturally significant practices by planning precise brush trajectories in three-
dimensional space [1423, 1452], while RoboCoDraw integrates GAN-based style transfer with time-
efficient path optimization to allow robots to generate stylized portrait drawings [1425]. Beyond
performance, robotics has also been integrated into design and architecture through co-intelligent
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
processes, where robots learn to translate design intent into executable construction paths, expanding
their role as creative collaborators [1418]. Together, these studies illustrate how robotics can extend
from functional manipulation to artistic expression, providing both a testbed for fine-grained motor
control and a platform for human–robot collaboration in creative fields.
8.6. Sports
Robotic manipulation has also entered the domain of sports, where dynamic, high-speed interactions
demand precise perception–action coordination. Recent advances demonstrate robots learning to
perform complex athletic skills, such as legged manipulators executing coordinated badminton
movements that couple locomotion with dexterous striking [1426]. In table tennis, robots have been
trained to handle fast-paced rallies, from early efforts in sample-efficient reinforcement learning
for controlled ball exchanges [1453] to more recent systems like SpikePingpong, which leverages
spike-based vision sensors for real-time, high-frequency striking with enhanced precision [1427].
These applications not only showcase robotics as a platform for pushing the limits of real-time control
and multimodal perception but also offer new opportunities for human–robot interaction, training,
and performance augmentation in competitive sports.
9. Prospective Future Research Directions
To advance robotic manipulation from controlled laboratory settings to open, dynamic, and real-world
environments, the long-term goal is to build increasingly autonomous embodied systems that can
perceive, reason, act, and improve through interaction. Achieving this goal requires more than scaling
individual perception or control modules. Future robots must generalize across embodiments, learn
from data far beyond conventional robot demonstrations, predict the consequences of their actions,
continually acquire new capabilities, and remain reliable during complex physical interaction. We
highlight five closely connected directions toward this goal: general-purpose and self-evolving robot
brains, scalable embodied data, predictive world models, multimodal physical interaction, and safe
autonomous operation.
9.1. Building a General-Purpose and Self-Evolving Robot Brain
– Core Challenge 1: From “One Brain, Multiple Embodiments” to Autonomous and Self-
Evolving Robotic Agents.
Robotics is gradually shifting from the paradigm of ‘one model per task” toward general-purpose
foundation models capable of supporting many tasks and embodiments. Beyond simply increasing
model scale, the more ambitious objective is to build a reusable robotic ‘brain” that can reason over
complex tasks, coordinate specialized capabilities, adapt to different bodies, and continuously improve
after deployment.
General-Purpose Architecture Across Embodiments. A universal robotic model must operate across
heterogeneous observation and action spaces, ranging from cameras with different viewpoints and
resolutions to systems with or without tactile sensing, and from joint-level control of fixed manipulators
to whole-body coordination of mobile and humanoid robots. This diversity makes direct parameter
sharing difficult because the same high-level intention may correspond to substantially different
low-level actions across embodiments. Future architectures therefore need to separate transferable
task knowledge from embodiment-specific execution through morphology-aware representations,
modular action interfaces, embodiment-conditioned policies, or shared latent action spaces. The
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
ultimate objective is not merely to train one large policy on many robots, but to enable knowledge
acquired on one embodiment to accelerate learning and execution on others.
Agentic Planning and Long-Horizon Autonomy. As manipulation tasks become longer and more
compositional, directly mapping an instruction to a fixed sequence of actions becomes increasingly
fragile. Everyday activities such as “making a cup of coffee” may require task decomposition, tool
selection, intermediate state tracking, recovery from unexpected outcomes, and coordination among
multiple skills. Future robotic systems are therefore likely to evolve from monolithic policies toward
agentic architectures that can reason over task progress, invoke specialized perception or manipulation
skills, interact with external tools or memory, monitor execution, and replan when necessary. In this
view, a robot is no longer merely an action generator but an embodied agent that actively manages
the entire perception–reasoning–execution loop.
Continual and Self-Evolving Learning. A truly autonomous robot should not remain fixed after
deployment. Beyond preventing catastrophic forgetting when acquiring new skills, robots should
achieve positive transfer, where new experience improves existing capabilities and enriches their
understanding of the physical world. More importantly, future systems should be able to identify
informative successes and failures during operation, convert them into reusable experience, and
selectively update memories, skills, data, or model parameters. This creates a self-evolving loop of
interaction, evaluation, learning, and redeployment. Active exploration, autonomous skill discov-
ery, memory-based adaptation, and large-scale parallel experience collection may all contribute to
such systems. A major challenge, however, is ensuring that self-improvement accumulates reliable
knowledge rather than amplifying model errors or undesirable behaviors.
Stable and Adaptive Motion Generation. High-level intelligence must ultimately be translated into
physically feasible motion. Advanced policies should therefore generate smooth and dynamically
consistent actions while adapting online to contact, disturbances, and embodiment-specific constraints.
Rather than treating learned action generation and classical control as competing paradigms, future
systems may increasingly combine learned policies with impedance control, model predictive control,
or other feedback mechanisms. Such integration can provide the flexibility required for open-world
manipulation while retaining the stability and compliance needed for precise and safety-critical
physical interaction.
Predictive World Models and Internal Simulation. A general-purpose robot brain should not only
react to current observations but also anticipate how the environment may evolve under different
actions. World models provide such predictive capability by learning compact representations of
objects, spatial relations, robot states, and task progress, together with their action-conditioned
dynamics. The key challenge is to move beyond visually plausible future prediction toward physically
grounded models that capture contact, force transmission, object permanence, and causal interactions,
particularly for deformable, articulated, and partially observed environments. More importantly,
these predictions should directly support decision-making by enabling robots to compare possible
futures, evaluate action consequences, and select plans before execution. Such internal simulation
could bridge reactive policy learning with deliberate planning and provide a foundation for continual
policy refinement through imagined experience.
9.2. Scaling Robot Intelligence Beyond Robot Data
– Core Challenge 2: Breaking the Robot-Data Bottleneck through Heterogeneous Embodied
Experience.
Modern robot learning is increasingly data-driven, yet high-quality robot interaction remains
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
expensive to collect and difficult to scale. Compared with the vast corpora available to language
and vision models, existing robot datasets cover only a small fraction of the diversity of objects,
environments, embodiments, and interaction patterns encountered in the real world. Addressing this
limitation requires both more efficient use of robot-generated experience and systematic exploitation
of data that were not originally collected by robots.
From Data Collection to a Data Flywheel. Real-world robot datasets remain fragmented across
hardware platforms, action spaces, sensor configurations, and collection protocols. Their quality is
also highly variable: successful demonstrations, suboptimal trajectories, exploratory behaviors, and
outright failures may coexist within the same dataset. Simply increasing dataset size can therefore
provide diminishing returns if low-value or redundant samples dominate training. Future research
should move from passive data accumulation toward an efficient data flywheel in which current models
help identify missing capabilities, collect informative experience, evaluate trajectory quality, and
prioritize data for subsequent training. Data filtering, automatic annotation, uncertainty estimation,
trajectory valuation, and failure mining will become increasingly important for extracting useful
supervision from large-scale interaction logs.
Learning from Robot-Free and Weakly Embodied Data. An especially promising direction is to
expand robotic learning beyond conventional teleoperated robot demonstrations. Egocentric human
videos contain rich information about object interaction, temporal structure, and task intent; Internet
videos capture enormous diversity in objects and activities; portable interfaces such as UMI reduce
the cost of collecting manipulation demonstrations without requiring a complete robot platform; and
human motion or hand-object interaction datasets provide additional priors about physical behavior.
These sources dramatically expand the potential scale of embodied experience, but they do not
directly provide robot-compatible actions. The key challenge is therefore to recover action-relevant
physical knowledge despite differences in embodiment, viewpoint, kinematics, and control interfaces.
Cross-embodiment alignment, action inference, retargeting, and shared latent representations will be
essential for transforming abundant human-centered data into useful robot supervision.
Simulation, Synthetic Experience, and Sim-to-Real Transfer. Simulation remains another important
source of scalable experience because it enables controlled variation, automatic annotation, and
inexpensive exploration. However, the gap between simulated and real interaction remains particularly
severe for contact-rich manipulation, where friction, compliance, collision, deformation, and sensor
noise are difficult to reproduce accurately. Future work should therefore pursue both higher-fidelity
simulation and methods that explicitly reduce dependence on perfect simulation, including domain
randomization, system identification, adaptive sim-to-real transfer, generative environment synthesis,
and hybrid training with small amounts of real-world experience. Differentiable simulation and
learned simulators may further provide efficient mechanisms for optimizing behaviors and physical
parameters. The broader objective is to combine real robot data, human-centered data, and synthetic
experience rather than relying on any single source.
9.3. Multimodal and Contact-Rich Physical Interaction
– Core Challenge 4: From Visual Intelligence to Deep Physical Interaction.
Robots interact with the world through a perception–action loop involving vision, proprioception,
touch, force, audition, and other sensory signals. Although vision provides rich semantic and geometric
information, many manipulation states cannot be reliably inferred from appearance alone. True
physical intelligence therefore requires robots to reason from multimodal feedback and adapt their
actions during interaction.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
Fusing a Broader Spectrum of Sensory Modalities. Consider how a human can locate a key and
unlock a door in darkness using touch, or determine whether two parts have snapped together
through force and sound. Future robots will similarly need to exploit tactile sensing to estimate
contact location, texture, slip, and pressure; force sensing to regulate interaction; proprioception to
track body configuration and dynamics; and audio to detect events that may be difficult to observe
visually. The main challenge is not simply adding more sensors, but learning representations that
align heterogeneous, asynchronous, and multi-rate signals while preserving information relevant to
action. Effective multimodal fusion should also remain robust when individual modalities become
noisy, delayed, or temporarily unavailable.
Contact-Rich and Complex Manipulation. Many practically important tasks are dominated by
contact rather than free-space motion. Insertion, wiping, polishing, assembly, tool use, cloth folding,
cable organization, and fluid manipulation require continuous adaptation to interaction forces and
uncertain object states. Small errors in geometry or force can rapidly turn into task failure. Future
research therefore needs policies that jointly reason about geometry, contact, compliance, and dy-
namics rather than treating motion as purely kinematic trajectory generation. Combining multimodal
perception with predictive physical models and adaptive feedback control will be particularly im-
portant for extending robotic manipulation from structured pick-and-place tasks to richer forms of
physical interaction.
9.4. Safety, Recovery, and Collaborative Autonomy
– Core Challenge 5: Making Autonomous Manipulation Reliable in the Open World.
As robots leave controlled laboratory environments and increasingly operate around humans, other
robots, and valuable objects, reliability becomes as important as task success. Safety should therefore
not be treated as an independent post-processing layer, but as a property that spans perception,
decision-making, control, and learning.
Intrinsic Safety and Self-Constrained Control. Future robots must protect both their surroundings
and themselves. Excessive joint velocities, abrupt accelerations, unstable force outputs, or repeated
operation near mechanical limits can damage hardware or create unsafe interaction. Next-generation
systems should therefore explicitly reason about kinematic, dynamic, force, energy, and workspace
constraints during action generation. Learning-based policies can provide adaptability, while classical
mechanisms such as model predictive control, impedance control, barrier functions, and rule-based
safety constraints can offer predictable safeguards. Hybrid architectures that combine these comple-
mentary strengths are likely to remain important for safety-critical deployment.
Autonomous Fault Detection and Recovery. Real-world manipulation inevitably encounters failures,
including missed grasps, unexpected contacts, sensor anomalies, actuator degradation, planning
loops, and environmental changes. A robust system should therefore behave less like an open-loop
executor and more like an organism with an “immune system”: continuously monitoring its own state,
recognizing anomalous outcomes, diagnosing likely causes, and selecting an appropriate recovery
strategy. Depending on the situation, recovery may involve local replanning, retrying with a modified
strategy, retreating to a safe configuration, switching to another skill, or requesting human assistance.
Integrating anomaly detection, uncertainty estimation, causal diagnosis, and agentic replanning will
be central to such capabilities.
Human–Robot and Inter-Robot Collaboration. Future robots will increasingly operate as collabora-
tive agents rather than isolated machines. Effective human–robot interaction requires understanding
not only explicit language commands but also contextual cues such as human motion, gaze, object
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
interaction, and task progress. A robot assisting with assembly, for example, should be able to infer
when to provide a tool, stabilize an object, or yield control without requiring detailed instructions
at every step. Similar challenges arise in multi-robot settings, where robots must share workspaces,
anticipate one another’s motion, negotiate task allocation, and avoid interference. Achieving such
collaboration will require predictive interaction models, shared representations of task state, and
explicit mechanisms for uncertainty, communication, and responsibility.
Ultimately, progress across these directions is tightly coupled. Diverse robot and human-centered
data provide the experience from which general-purpose models can learn; world models provide
predictive understanding of physical consequences; agentic systems organize reasoning, skills, and
recovery over long horizons; multimodal sensing grounds these capabilities in physical interaction; and
safety mechanisms constrain autonomous behavior during real-world deployment. The convergence
of these components may gradually transform robotic manipulation from task-specific policy execution
into continuously learning, predictive, and autonomous embodied intelligence.

## sec:conclusion-2 10. Conclusion
_Pages 99-99_

This survey provides a comprehensive and systematic overview of robot manipulation, covering
fundamental background knowledge, task-specific benchmarks, representative methods, critical
bottlenecks, and real-world applications. Despite substantial progress, robotic manipulation remains
far from achieving human-level versatility. Major open challenges persist, including the development
of a unified “robot brain,” the resolution of data and perception bottlenecks, and the assurance of
safety in human–robot collaboration. Bridging these gaps is essential for enabling learning-based
robotic systems to move beyond controlled laboratory environments and into everyday life and diverse
industries. We hope this survey will serve as both a roadmap for newcomers and a comprehensive
reference for experienced researchers, fostering a unified understanding of robotic manipulation and
inspiring future advances in embodied intelligence.

## sec:acknowledgments Acknowledgments
_Pages 99-100_

This work was supported by the National Natural Science Foundation of China (Grant No. U21A20485).
Author Contributions
The contributions of all participating authors are summarized below, indicating the primary author
responsible for each section and the supporting contributors. The detailed roles of each author are as
follows:
• Corresponding Authors: Shanghang Zhang, Badong Chen
• Project Lead: Shuanghao Bai
• Background: Shuanghao Bai, Han Zhao
• Benchmarks and Datasets: Shuanghao Bai
• Manipulation Tasks: Shuanghao Bai
• High-level Planning: Zhide Zhong, Wei Zhao
• Low-level Learning-based Action Modeling:
– Learning Strategy:
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
∗Reinforcement Learning: Han Zhao
∗All other subsections: Shuanghao Bai
– Input Modeling:
∗Vision Action Models: Zhe Li
∗Vision-Language-Action Models: Yuheng Ji, Wenxuan Song, Jiayi Chen
∗Tactile-based Action Models: Wenxuan Song
– Latent Learning: Wenxuan Song
– Policy Learning: Wenxuan Song, Jiayi Chen
• Challenges and Bottlenecks: Jiayi Chen, Jin Yang
• Applications: Wanqi Zhou
• Prospective Future Research Directions: Pengxiang Ding, Shuanghao Bai
• Other Contributions:
– Figures: Shuanghao Bai, Wenxuan Song, Jiayi Chen, Yuheng Ji, Zhide Zhong, Jin Yang,
Wanqi Zhou
– Review and Editing: Cheng Chi, Haoang Li, Chang Xu, Xiaolong Zheng, Donglin Wang,
Shanghang Zhang, Badong Chen
The second version of this survey was independently developed and substantially revised by
Shuanghao Bai.
In addition, we distilled the core content and methodological framework of this survey into a
concise version [1454].
We also welcome constructive feedback and suggestions from the broader research community,
which will help us further improve this work and enhance its value as a resource for the field.

## sec:references References
_Pages 100-212_

[1] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020.
[2] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open
and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.
[3] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning.
Advances in neural information processing systems, 36:34892–34916, 2023.
[4] Bernard Espiau, François Chaumette, and Patrick Rives. A new approach to visual servoing
in robotics. In Workshop on Geometric Reasoning for Perception and Action, pages 106–136.
Springer, 1991.
[5] Steven LaValle. Rapidly-exploring random trees: A new tool for path planning. Research
Report 9811, 1998.
[6] Seth Hutchinson, Gregory D Hager, and Peter I Corke. A tutorial on visual servo control. IEEE
transactions on robotics and automation, 12(5):651–670, 2002.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[7] Mrinal Kalakrishnan, Sachin Chitta, Evangelos Theodorou, Peter Pastor, and Stefan Schaal.
Stomp: Stochastic trajectory optimization for motion planning. In 2011 IEEE international
conference on robotics and automation, pages 4569–4574. IEEE, 2011.
[8] Sergey Levine, Chelsea Finn, Trevor Darrell, and Pieter Abbeel. End-to-end training of deep
visuomotor policies. Journal of Machine Learning Research, 17(39):1–40, 2016.
[9] Lerrel Pinto and Abhinav Gupta. Supersizing self-supervision: Learning to grasp from 50k
tries and 700 robot hours. In 2016 IEEE international conference on robotics and automation
(ICRA), pages 3406–3413. IEEE, 2016.
[10] Yan Duan, Marcin Andrychowicz, Bradly Stadie, OpenAI Jonathan Ho, Jonas Schneider, Ilya
Sutskever, Pieter Abbeel, and Wojciech Zaremba. One-shot imitation learning. Advances in
neural information processing systems, 30, 2017.
[11] Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel
Todorov, and Sergey Levine. Learning complex dexterous manipulation with deep reinforce-
ment learning and demonstrations. In Robotics: Science and Systems, 2018.
[12] Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted Xiao, Fei Xia, Jialin Wu, Paul Wohlhart,
Stefan Welker, Ayzaan Wahid, et al. Rt-2: Vision-language-action models transfer web
knowledge to robotic control. In Conference on Robot Learning, pages 2165–2183. PMLR,
2023.
[13] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair,
Rafael Rafailov, Ethan P Foster, Pannag R Sanketi, Quan Vuong, et al. Openvla: An open-
source vision-language-action model. In Conference on Robot Learning, pages 2679–2713.
PMLR, 2025.
[14] Shan An, Ziyu Meng, Chao Tang, Yuning Zhou, Tengyu Liu, Fangqiang Ding, Shufang Zhang,
Yao Mu, Ran Song, Wei Zhang, et al. Dexterous manipulation through imitation learning: A
survey. arXiv preprint arXiv:2504.03515, 2025.
[15] Gaofeng Li, Ruize Wang, Peisen Xu, Qi Ye, and Jiming Chen. The developments and challenges
toward dexterous and embodied robotic manipulation: A survey. IEEE Robotics & Automation
Magazine, 2025.
[16] David Blanco-Mulero, Yifei Dong, Julia Borras, Florian T Pokorny, and Carme Torras. T-dom:
A taxonomy for robotic manipulation of deformable objects. arXiv preprint arXiv:2412.20998,
2024.
[17] Shantanu Thakar, Srivatsan Srinivasan, Sarah Al-Hussaini, Prahar M Bhatt, Pradeep Rajen-
dran, Yeo Jung Yoon, Neel Dhanaraj, Rishi K Malhan, Matthias Schmid, Venkat N Krovi,
et al. A survey of wheeled mobile manipulation: A decision-making perspective. Journal of
Mechanisms and Robotics, 15(2):020801, 2023.
[18] Zhaoyuan Gu, Junheng Li, Wenlan Shen, Wenhao Yu, Zhaoming Xie, Stephen McCrory, Xianyi
Cheng, Abdulaziz Shamsah, Robert Griffin, C Karen Liu, et al. Humanoid locomotion and
manipulation: Current progress and challenges in control, planning, and learning. IEEEASME
transactions on mechatronics, 2025.
[19] Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, and Irwin King. A survey on vision–
language–action models for embodied ai. IEEE Transactions on Neural Networks and Learning
Systems, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[20] Yifan Zhong, Fengshuo Bai, Shaofei Cai, Xuchuan Huang, Zhang Chen, Xiaowei Zhang,
Yuanfei Wang, Shaoyang Guo, Tianrui Guan, Ka Nam Lui, et al. A survey on vision-language-
action models: An action tokenization perspective. arXiv preprint arXiv:2507.01925, 2025.
[21] Tian-Yu Xiang, Ao-Qun Jin, Xiao-Hu Zhou, Mei-Jiang Gui, Xiao-Liang Xie, Shi-Qi Liu, Shuang-
Yi Wang, Sheng-Bin Duan, Fu-Chao Xie, Wen-Kai Wang, et al. Parallels between vla model
post-training and human motor learning: Progress, challenges, and trends. arXiv preprint
arXiv:2506.20966, 2025.
[22] Haoran Li, Yuhui Chen, Wenbo Cui, Weiheng Liu, Kai Liu, Mingcai Zhou, Zhengtao Zhang,
and Dongbin Zhao. Survey of vision-language-action models for embodied manipulation.
arXiv preprint arXiv:2508.15201, 2025.
[23] Rosa Petra Wolf, Yitian Shi, Sheng Liu, and Rania Rayyes. Diffusion models for robotic
manipulation: A survey. Frontiers in Robotics and AI, 12:1606247, 2025.
[24] Kun Zhang, Peng Yun, Jun Cen, Junhao Cai, Didi Zhu, Hangjie Yuan, Chao Zhao, Tao Feng,
Michael Yu Wang, Qifeng Chen, et al. Generative artificial intelligence in robotic manipulation:
A survey. arXiv preprint arXiv:2503.03464, 2025.
[25] Hongkuan Zhou, Xiangtong Yao, Yuan Meng, Siming Sun, Zhenshan Bing, Kai Huang, and
Alois Knoll. Language-conditioned learning for robotic manipulation: A survey. arXiv preprint
arXiv:2312.10807, 2023.
[26] Ying Zheng, Lei Yao, Yuejiao Su, Yi Zhang, Yi Wang, Sicheng Zhao, Yiyi Zhang, and Lap-Pui
Chau. A survey of embodied learning for object-centric robotic manipulation. Machine
Intelligence Research, pages 1–39, 2025.
[27] Yang Liu, Weixing Chen, Yongjie Bai, Xiaodan Liang, Guanbin Li, Wen Gao, and Liang
Lin. Aligning cyber space with physical world: A comprehensive survey on embodied ai.
IEEE/ASME Transactions on Mechatronics, 2025.
[28] Lik Hang Kenny Wong, Xueyang Kang, Kaixin Bai, and Jianwei Zhang. A survey of robotic
navigation and manipulation with physics simulators in the era of embodied ai. arXiv preprint
arXiv:2505.01458, 2025.
[29] Martin Peticco, Gabriella E Ulloa, John Marangola, and Pulkit Agrawal. Dexwrist: A robotic
wrist for constrained and dynamic manipulation. In 3rd RSS Workshop on Dexterous Manipu-
lation: Learning and Control with Diverse Data, 2025.
[30] Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ
Tedrake, and Shuran Song. Universal manipulation interface: In-the-wild robot teaching
without in-the-wild robots. In Robotics: Science and Systems, 2024.
[31] Michael Ahn, Henry Zhu, Kristian Hartikainen, Hugo Ponte, Abhishek Gupta, Sergey Levine,
and Vikash Kumar.
Robel: Robotics benchmarks for learning with low-cost robots.
Conference on robot learning, pages 1300–1313. PMLR, 2020.
[32] Kenneth Shaw, Ananye Agarwal, Shikhar Bahl, Mohan Kumar Srirama, Alexandre Kirchmeyer,
Aditya Kannan, Aravind Sivakumar, and Deepak Pathak. Demonstrating learning from humans
on open-source dexterous robot hands. In Robotics: Science and Systems, 2024.
[33] Zhaoliang Wan, Zetong Bi, Zida Zhou, Hao Ren, Yiming Zeng, Yihan Li, Lu Qi, Xu Yang,
Ming-Hsuan Yang, and Hui Cheng. Rapid hand: Robust, affordable, perception-integrated,
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
dexterous manipulation platform for embodied intelligence. In Advances in Neural Information
Processing Systems, volume 38, pages 97012–97046, 2025.
[34] Steffen Puhlmann, Jason Harris, and Oliver Brock. Rbo hand 3: A platform for soft dexterous
manipulation. IEEE Transactions on Robotics, 38(6):3434–3449, 2022.
[35] Zhanchi Wang, Nikolaos M Freris, and Xi Wei. Spirobs: Logarithmic spiral-shaped robots for
versatile grasping across scales. Device, 3(4), 2025.
[36] Sami Haddadin. The franka emika robot: A standard platform in robotics research. IEEE
Robotics & Automation Magazine, 2024.
[37] Zipeng Fu, Tony Z Zhao, and Chelsea Finn.
Mobile aloha: Learning bimanual mobile
manipulation using low-cost whole-body teleoperation. In Conference on Robot Learning,
pages 4066–4083. PMLR, 2025.
[38] Pierre Duysinx, Olivier Bruls, and Michel Géradin. An introduction to robotics-mechanical
aspects. Lecture notes, 2006.
[39] Lianfang Tian and Curtis Collins. An effective robot trajectory planning method using a
genetic algorithm. Mechatronics, 14(5):455–470, 2004.
[40] Mohamed Elbanhawi and Milan Simic. Sampling-based robot motion planning: A review.
Ieee access, 2:56–77, 2014.
[41] Jongwoo Kim, Joel M Esposito, and Vijay Kumar. Sampling-based algorithm for testing
and validating robot controllers. The International Journal of Robotics Research, 25(12):
1257–1272, 2006.
[42] Philipp S Schmitt, Werner Neubauer, Wendelin Feiten, Kai M Wurm, Georg V Wichert,
and Wolfram Burgard. Optimal, sampling-based manipulation planning. In 2017 IEEE
International Conference on Robotics and Automation (ICRA), pages 3426–3432. IEEE, 2017.
[43] Jinwook Huh, Bhoram Lee, and Daniel D Lee. Constrained sampling-based planning for
grasping and manipulation. In 2018 IEEE International Conference on Robotics and Automation
(ICRA), pages 223–230. IEEE, 2018.
[44] Matt Zucker, Nathan Ratliff, Anca D Dragan, Mihail Pivtoraiko, Matthew Klingensmith,
Christopher M Dellin, J Andrew Bagnell, and Siddhartha S Srinivasa. Chomp: Covariant
hamiltonian optimization for motion planning. The International journal of robotics research,
32(9-10):1164–1193, 2013.
[45] Siyu Dai, Matthew Orton, Shawn Schaffert, Andreas Hofmann, and Brian Williams. Improv-
ing trajectory optimization using a roadmap framework. In 2018 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 8674–8681. IEEE, 2018.
[46] Basil Kouvaritakis and Mark Cannon.
Model predictive control.
Switzerland: Springer
International Publishing, 38(13-56):7, 2016.
[47] Mohak Bhardwaj, Balakumar Sundaralingam, Arsalan Mousavian, Nathan D Ratliff, Dieter
Fox, Fabio Ramos, and Byron Boots. Storm: An integrated framework for fast joint-space
model-predictive control for reactive manipulation. In Conference on Robot Learning, pages
750–759. PMLR, 2022.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[48] Dong Han, Beni Mulyana, Vladimir Stankovic, and Samuel Cheng. A survey on deep rein-
forcement learning algorithms for robotic manipulation. Sensors, 23(7):3762, 2023.
[49] Christopher JCH Watkins and Peter Dayan. Q-learning. Machine learning, 8:279–292, 1992.
[50] Tuomas Haarnoja, Vitchyr Pong, Aurick Zhou, Murtaza Dalal, Pieter Abbeel, and Sergey
Levine. Composable deep reinforcement learning for robotic manipulation. In 2018 IEEE
international conference on robotics and automation (ICRA), pages 6244–6251. IEEE, 2018.
[51] Richard S Sutton, David McAllester, Satinder Singh, and Yishay Mansour. Policy gradi-
ent methods for reinforcement learning with function approximation. Advances in neural
information processing systems, 12, 1999.
[52] Jan Peters and Stefan Schaal. Policy gradient methods for robotics. In 2006 IEEE/RSJ
international conference on intelligent robots and systems, pages 2219–2225. IEEE, 2006.
[53] Ivo Grondman, Lucian Busoniu, Gabriel AD Lopes, and Robert Babuska. A survey of actor-
critic reinforcement learning: Standard and natural policy gradients. IEEE Transactions on
Systems, Man, and Cybernetics, part C (applications and reviews), 42(6):1291–1307, 2012.
[54] Tuomas Haarnoja, Aurick Zhou, Kristian Hartikainen, George Tucker, Sehoon Ha, Jie Tan,
Vikash Kumar, Henry Zhu, Abhishek Gupta, Pieter Abbeel, et al. Soft actor-critic algorithms
and applications. arXiv preprint arXiv:1812.05905, 2018.
[55] Sergey Levine, Aviral Kumar, George Tucker, and Justin Fu. Offline reinforcement learning:
Tutorial, review, and perspectives on open problems. arXiv preprint arXiv:2005.01643, 2020.
[56] Lili Chen, Kevin Lu, Aravind Rajeswaran, Kimin Lee, Aditya Grover, Misha Laskin, Pieter
Abbeel, Aravind Srinivas, and Igor Mordatch. Decision transformer: Reinforcement learning
via sequence modeling. Advances in neural information processing systems, 34:15084–15097,
2021.
[57] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.
[58] Seunghyun Lee, Younggyo Seo, Kimin Lee, Pieter Abbeel, and Jinwoo Shin. Offline-to-online
reinforcement learning via balanced replay and pessimistic q-ensemble. In Conference on
Robot Learning, pages 1702–1712. PMLR, 2022.
[59] Mitsuhiko Nakamoto, Simon Zhai, Anikait Singh, Max Sobol Mark, Yi Ma, Chelsea Finn, Aviral
Kumar, and Sergey Levine. Cal-ql: Calibrated offline rl pre-training for efficient online fine-
tuning. In Advances in Neural Information Processing Systems, volume 36, pages 62244–62269,
2023.
[60] Faraz Torabi, Garrett Warnell, and Peter Stone. Behavioral cloning from observation. In
Proceedings of the 27th International Joint Conference on Artificial Intelligence, pages 4950–
4957, 2018.
[61] Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, and Badong Chen.
Rethinking latent redundancy in behavior cloning: An information bottleneck approach for
robot manipulation. In Forty-second International Conference on Machine Learning, 2025.
[62] Saurabh Arora and Prashant Doshi. A survey of inverse reinforcement learning: Challenges,
methods and progress. Artificial Intelligence, 297:103500, 2021.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[63] Neha Das, Sarah Bechtle, Todor Davchev, Dinesh Jayaraman, Akshara Rai, and Franziska
Meier. Model-based inverse reinforcement learning from visual demonstrations. In Conference
on Robot Learning, pages 1930–1942. PMLR, 2021.
[64] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image
recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition,
pages 770–778, 2016.
[65] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information
processing systems, 30, 2017.
[66] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun Zhu, Lionel Ni, and Heung-Yeung
Shum. Dino: Detr with improved denoising anchor boxes for end-to-end object detection. In
The Eleventh International Conference on Learning Representations, 2023.
[67] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas. Pointnet: Deep learning on point
sets for 3d classification and segmentation. In Proceedings of the IEEE conference on computer
vision and pattern recognition, pages 652–660, 2017.
[68] Hengshuang Zhao, Li Jiang, Jiaya Jia, Philip HS Torr, and Vladlen Koltun. Point transformer. In
Proceedings of the IEEE/CVF international conference on computer vision, pages 16259–16268,
2021.
[69] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal,
Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning transferable visual
models from natural language supervision. In International conference on machine learning,
pages 8748–8763. PmLR, 2021.
[70] Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and Lucas Beyer. Sigmoid loss for language
image pre-training. In Proceedings of the IEEE/CVF international conference on computer vision,
pages 11975–11986, 2023.
[71] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, and
Sergey Zagoruyko. End-to-end object detection with transformers. In European conference on
computer vision, pages 213–229. Springer, 2020.
[72] Nikita Karaev, Ignacio Rocco, Benjamin Graham, Natalia Neverova, Andrea Vedaldi, and
Christian Rupprecht. Cotracker: It is better to track together. In European Conference on
Computer Vision, pages 18–35. Springer, 2024.
[73] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training
of deep bidirectional transformers for language understanding. In Proceedings of the 2019
conference of the North American chapter of the association for computational linguistics: human
language technologies, volume 1 (long and short papers), pages 4171–4186, 2019.
[74] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al.
Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
[75] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm:
Scaling language modeling with pathways. Journal of Machine Learning Research, 24(240):
1–113, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[76] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter,
Ayzaan Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, et al. Palm-e: An embodied
multimodal language model. In International Conference on Machine Learning, pages 8469–
8488. PMLR, 2023.
[77] Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, and
Dorsa Sadigh. Prismatic vlms: Investigating the design space of visually-conditioned language
models. In Forty-first International Conference on Machine Learning, 2024.
[78] Tim Brooks, Aleksander Holynski, and Alexei A Efros. Instructpix2pix: Learning to follow
image editing instructions. In Proceedings of the IEEE/CVF conference on computer vision and
pattern recognition, pages 18392–18402, 2023.
[79] Yixin Liu, Kai Zhang, Yuan Li, Zhiling Yan, Chujie Gao, Ruoxi Chen, Zhengqing Yuan,
Yue Huang, Hanchi Sun, Jianfeng Gao, et al. Sora: A review on background, technology,
limitations, and opportunities of large vision models. arXiv preprint arXiv:2402.17177, 2024.
[80] Ya Jing, Xuelin Zhu, Xingbin Liu, Qie Sima, Taozheng Yang, Yunhai Feng, and Tao Kong.
Exploring visual pre-training for robot manipulation: Datasets, models and methods. In
2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
11390–11395. IEEE, 2023.
[81] Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, and
Shuran Song. Diffusion policy: Visuomotor policy learning via action diffusion. In Robotics:
Science and Systems XIX, 2023.
[82] Oier Mees, Lukas Hermann, Erick Rosete-Beas, and Wolfram Burgard. Calvin: A benchmark
for language-conditioned policy learning for long-horizon robot manipulation tasks. IEEE
Robotics and Automation Letters, 7(3):7327–7334, 2022.
[83] Yun Jiang, Stephen Moseson, and Ashutosh Saxena. Efficient grasping from rgbd images:
Learning using a new rectangle representation. In 2011 IEEE International conference on
robotics and automation, pages 3304–3311. IEEE, 2011.
[84] Amaury Depierre, Emmanuel Dellandréa, and Liming Chen. Jacquard: A large scale dataset
for robotic grasp detection. In 2018 IEEE/RSJ International Conference on Intelligent Robots
and Systems (IROS), pages 3511–3516. IEEE, 2018.
[85] Hao-Shu Fang, Chenxi Wang, Minghao Gou, and Cewu Lu. Graspnet-1billion: A large-scale
benchmark for general object grasping. In Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, pages 11444–11453, 2020.
[86] Clemens Eppner, Arsalan Mousavian, and Dieter Fox. Acronym: A large-scale grasp dataset
based on simulation. In 2021 IEEE International Conference on Robotics and Automation
(ICRA), pages 6222–6227. IEEE, 2021.
[87] Hanbo Zhang, Deyu Yang, Han Wang, Binglei Zhao, Xuguang Lan, Jishiyu Ding, and Nanning
Zheng. Regrad: A large-scale relational grasp dataset for safe and object-specific robotic
grasping in clutter. IEEE Robotics and Automation Letters, 7(2):2929–2936, 2022.
[88] Maximilian Gilles, Yuhao Chen, Tim Robin Winter, E Zhixuan Zeng, and Alexander Wong.
Metagraspnet: A large-scale benchmark dataset for scene-aware ambidextrous bin picking via
physics-based metaverse synthesis. In 2022 IEEE 18th international conference on automation
science and engineering (CASE), pages 220–227. IEEE, 2022.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[89] Ruicheng Wang, Jialiang Zhang, Jiayi Chen, Yinzhen Xu, Puhao Li, Tengyu Liu, and He Wang.
Dexgraspnet: A large-scale robotic dexterous grasp dataset for general objects based on
simulation. In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages
11359–11366. IEEE, 2023.
[90] Maximilian Gilles, Yuhao Chen, Emily Zhixuan Zeng, Yifan Wu, Kai Furmans, Alexander
Wong, and Rania Rayyes. Metagraspnetv2: All-in-one dataset enabling fast and reliable
robotic bin picking via object relationship reasoning and dexterous grasping. IEEE Transactions
on Automation Science and Engineering, 21(3):2302–2320, 2023.
[91] An Dinh Vuong, Minh Nhat Vu, Hieu Le, Baoru Huang, Huynh Thi Thanh Binh, Thieu Vo,
Andreas Kugi, and Anh Nguyen. Grasp-anything: Large-scale grasp dataset from foundation
models. In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages
14030–14037. IEEE, 2024.
[92] An Dinh Vuong, Minh Nhat Vu, Baoru Huang, Nghia Nguyen, Hieu Le, Thieu Vo, and Anh
Nguyen. Language-driven grasp detection. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, pages 17902–17912, 2024.
[93] Toan Nguyen, Minh Nhat Vu, Baoru Huang, An Vuong, Quan Vuong, Ngan Le, Thieu Vo, and
Anh Nguyen. Language-driven 6-dof grasp detection using negative prompt guidance. In
European Conference on Computer Vision, pages 363–381. Springer, 2024.
[94] Jianglong Ye, Keyi Wang, Chengjing Yuan, Ruihan Yang, Yiquan Li, Jiyue Zhu, Yuzhe Qin,
Xueyan Zou, and Xiaolong Wang. Dex1b: Learning with 1b demonstrations for dexterous
manipulation. In Robotics: Science and Systems, 2025.
[95] Seunghyeok Back, Joosoon Lee, Kangmin Kim, Heeseon Rho, Geonhyup Lee, Raeyoung Kang,
Sangbeom Lee, Sangjun Noh, Youngjin Lee, Taeyeop Lee, et al. Graspclutter6d: A large-scale
real-world dataset for robust perception and grasping in cluttered scenes. IEEE Robotics and
Automation Letters, 2025.
[96] Linfei Li, Lin Zhang, and Ying Shen. Realvlg-r1: A large-scale real-world visual-language
grounding benchmark for robotic perception and manipulation. In Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition, 2026.
[97] Haoran Lin, Wenrui Chen, Xianchi Chen, Fan Yang, Qiang Diao, Wenxin Xie, Sijie Wu,
Kailun Yang, Maojun Li, and Yaonan Wang. Unifucgrasp: Human-hand-inspired unified
functional grasp annotation strategy and dataset for diverse dexterous hands. IEEE Robotics
and Automation Letters, 11(2):1994–2001, 2025.
[98] Jialiang Zhang, Haoran Liu, Danshi Li, XinQiang Yu, Haoran Geng, Yufei Ding, Jiayi Chen,
and He Wang. Dexgraspnet 2.0: Learning generative dexterous grasping in large-scale
synthetic cluttered scenes. In 8th Annual Conference on Robot Learning, 2024.
[99] Tianhe Yu, Deirdre Quillen, Zhanpeng He, Ryan Julian, Karol Hausman, Chelsea Finn,
and Sergey Levine. Meta-world: A benchmark and evaluation for multi-task and meta
reinforcement learning. In Conference on robot learning, pages 1094–1100. PMLR, 2020.
[100] Abhishek Gupta, Vikash Kumar, Corey Lynch, Sergey Levine, and Karol Hausman. Relay
policy learning: Solving long-horizon tasks via imitation and reinforcement learning. In
Conference on Robot Learning, pages 1025–1037. PMLR, 2020.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[101] Stephen James, Zicong Ma, David Rovick Arrojo, and Andrew J Davison. Rlbench: The robot
learning benchmark & learning environment. IEEE Robotics and Automation Letters, 5(2):
3019–3026, 2020.
[102] Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush Nasiriany, Chen Wang, Rohun Kulkarni,
Li Fei-Fei, Silvio Savarese, Yuke Zhu, and Roberto Martín-Martín. What matters in learning
from offline human demonstrations for robot manipulation. In Conference on Robot Learning,
pages 1678–1690. PMLR, 2022.
[103] Tongzhou Mu, Zhan Ling, Fanbo Xiang, Derek Cathera Yang, Xuanlin Li, Stone Tao, Zhiao
Huang, Zhiwei Jia, and Hao Su. Maniskill: Generalizable manipulation skill benchmark
with large-scale demonstrations. In Thirty-fifth Conference on Neural Information Processing
Systems Datasets and Benchmarks Track (Round 2), 2021.
[104] Kaizhi Zheng, Xiaotong Chen, Odest Chadwicke Jenkins, and Xin Wang. Vlmbench: A com-
positional benchmark for vision-and-language manipulation. Advances in Neural Information
Processing Systems, 35:665–678, 2022.
[105] Jiayuan Gu, Fanbo Xiang, Xuanlin Li, Zhan Ling, Xiqiang Liu, Tongzhou Mu, Yihe Tang, Stone
Tao, Xinyue Wei, Yunchao Yao, et al. Maniskill2: A unified benchmark for generalizable
manipulation skills. In The Eleventh International Conference on Learning Representations,
2023.
[106] Yunfan Jiang, Agrim Gupta, Zichen Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen,
Li Fei-Fei, Anima Anandkumar, Yuke Zhu, and Linxi Fan. Vima: General robot manipulation
with multimodal prompts. In International Conference on Machine Learning, 2023.
[107] Ran Gong, Jiangyong Huang, Yizhou Zhao, Haoran Geng, Xiaofeng Gao, Qingyang Wu, Wensi
Ai, Ziheng Zhou, Demetri Terzopoulos, Song-Chun Zhu, et al. Arnold: A benchmark for
language-grounded task learning with continuous states in realistic 3d scenes. In Proceedings
of the IEEE/CVF International Conference on Computer Vision, pages 20483–20495, 2023.
[108] Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, and Peter Stone.
Libero: Benchmarking knowledge transfer for lifelong robot learning. In Advances in Neural
Information Processing Systems, volume 36, pages 44776–44791, 2023.
[109] Yuke Zhu, Josiah Wong, Ajay Mandlekar, Roberto Martín-Martín, Abhishek Joshi, Soroush
Nasiriany, and Yifeng Zhu. robosuite: A modular simulation framework and benchmark for
robot learning. arXiv preprint arXiv:2009.12293, 2020.
[110] Wilbert Pumacay, Ishika Singh, Jiafei Duan, Ranjay Krishna, Jesse Thomason, and Dieter Fox.
The colosseum: A benchmark for evaluating generalization for robotic manipulation. In RSS
2024 Workshop: Data Generation for Robotics, 2024.
[111] Xuanlin Li, Kyle Hsu, Jiayuan Gu, Oier Mees, Karl Pertsch, Homer Rich Walke, Chuyuan Fu,
Ishikaa Lunawat, Isabel Sieh, Sean Kirmani, et al. Evaluating real-world robot manipulation
policies in simulation. In Conference on Robot Learning, pages 3705–3728. PMLR, 2025.
[112] Pu Hua, Minghuan Liu, Annabella Macaluso, Yunfeng Lin, Weinan Zhang, Huazhe Xu, and
Lirui Wang. Gensim2: Scaling robot data generation with multi-modal and reasoning llms.
In Conference on Robot Learning, pages 5030–5066. PMLR, 2025.
[113] Ricardo Garcia, Shizhe Chen, and Cordelia Schmid. Towards generalizable vision-language
robotic manipulation: A benchmark and llm-guided 3d policy. In 2025 IEEE International
Conference on Robotics and Automation (ICRA), pages 8996–9002. IEEE, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[114] Yao Mu, Tianxing Chen, Zanxin Chen, Shijia Peng, Zhiqian Lan, Zeyu Gao, Zhixuan Liang,
Qiaojun Yu, Yude Zou, Mingkun Xu, et al. Robotwin: Dual-arm robot benchmark with
generative digital twins.
In Proceedings of the Computer Vision and Pattern Recognition
Conference, pages 27649–27660, 2025.
[115] Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Hinrichsen, Xiaodi Yuan, Chen Bao,
Xinsong Lin, Yulin Liu, Tse-kai Chan, et al. Maniskill3: Gpu parallelized robotics simulation
and rendering for generalizable embodied ai. In Robotics: Science and Systems, 2025.
[116] Ning Gao, Yilun Chen, Shuai Yang, Xinyi Chen, Yang Tian, Hao Li, Haifeng Huang, Hanqing
Wang, Tai Wang, and Jiangmiao Pang. Genmanip: Llm-driven simulation for generaliz-
able instruction-following manipulation. In Proceedings of the Computer Vision and Pattern
Recognition Conference, pages 12187–12198, 2025.
[117] Shiduo Zhang, Zhe Xu, Peiju Liu, Xiaopeng Yu, Yuan Li, Qinghui Gao, Zhaoye Fei, Zhangyue
Yin, Zuxuan Wu, Yu-Gang Jiang, et al. Vlabench: A large-scale benchmark for language-
conditioned robotics manipulation with long-horizon reasoning tasks. In Proceedings of the
IEEE/CVF International Conference on Computer Vision, pages 11142–11152, 2025.
[118] Jiaming Zhou, Ke Ye, Jiayi Liu, Teli Ma, Zifan Wang, Ronghe Qiu, Kun-Yu Lin, Zhilin Zhao,
and Junwei Liang. Exploring the limits of vision-language-action manipulation in cross-
task generalization. In The Thirty-ninth Annual Conference on Neural Information Processing
Systems, 2025.
[119] Tianxing Chen, Zanxin Chen, Baijun Chen, Zijian Cai, Yibin Liu, Qiwei Liang, Zixuan Li,
Xianliang Lin, Yiheng Ge, Zhenyu Gu, et al. Robotwin 2.0: A scalable data generator and
benchmark with strong domain randomization for robust bimanual robotic manipulation.
arXiv preprint arXiv:2506.18088, 2025.
[120] Yi Ru Wang, Carter Ung, Grant Tannert, Jiafei Duan, Josephine Li, Amy Le, Rishabh Oswal,
Markus Grotz, Wilbert Pumacay, Yuquan Deng, et al. Roboeval: Where robotic manipulation
meets structured and scalable evaluation. arXiv preprint arXiv:2507.00435, 2025.
[121] Irving Fang, Juexiao Zhang, Shengbang Tong, and Chen Feng. From intention to execution:
Probing the generalization boundaries of vision-language-action models. arXiv preprint
arXiv:2506.09930, 2025.
[122] Tianxing Chen, Yue Chen, Zixuan Li, Junyuan Tang, Kailun Su, Weijie Wan, Baijun Chen,
Haoran Lu, Haowen Yan, Honghao Su, et al. Robodojo: A unified sim-and-real bench-
mark for comprehensive evaluation of generalist robot manipulation policies. arXiv preprint
arXiv:2607.04434, 2026.
[123] Iretiayo Akinola, Jie Xu, Jan Carius, Dieter Fox, and Yashraj Narang. Tacsl: A library for
visuotactile sensor simulation and learning. IEEE Transactions on Robotics, 2025.
[124] Quan Khanh Luu, Pokuang Zhou, Zhengtong Xu, Zhiyuan Zhang, Qiang Qiu, and Yu She.
Manifeel: Benchmarking and understanding visuotactile manipulation policy learning. arXiv
preprint arXiv:2505.18472, 2025.
[125] Manuel Wuthrich, Felix Widmaier, Felix Grimminger, Shruti Joshi, Vaibhav Agrawal, Bilal
Hammoud, Majid Khadiv, Miroslav Bogdanovic, Vincent Berenz, Julian Viereck, et al. Trifinger:
An open-source robot for learning dexterity. In Conference on Robot Learning, pages 1871–
1882. PMLR, 2021.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[126] Zhiao Huang, Yuanming Hu, Tao Du, Siyuan Zhou, Hao Su, Joshua B Tenenbaum, and
Chuang Gan. Plasticinelab: A soft-body manipulation benchmark with differentiable physics.
In International Conference on Learning Representations, 2021.
[127] Xingyu Lin, Yufei Wang, Jake Olkin, and David Held. Softgym: Benchmarking deep reinforce-
ment learning for deformable object manipulation. In Conference on Robot Learning, pages
432–448. PMLR, 2021.
[128] Siwei Chen, Yiqing Xu, Cunjun Yu, Linfeng Li, Xiao Ma, Zhongwen Xu, and David Hsu.
Daxbench: Benchmarking deformable object manipulation with differentiable physics. In The
Eleventh International Conference on Learning Representations, 2023.
[129] Junyi Cao, Yian Wang, Ziyan Xiong, Chunru Lin, Zhehuan Chen, and Chuang Gan. Dlo-
lab: Benchmarking deformable linear object manipulations with differentiable physics. In
Forty-third International Conference on Machine Learning, 2026.
[130] Kiana Ehsani, Winson Han, Alvaro Herrasti, Eli VanderBilt, Luca Weihs, Eric Kolve, Aniruddha
Kembhavi, and Roozbeh Mottaghi. Manipulathor: A framework for visual object manipulation.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages
4497–4506, 2021.
[131] Sriram Yenamandra, Arun Ramachandran, Karmesh Yadav, Austin S Wang, Mukul Khanna,
Theophile Gervet, Tsung-Yen Yang, Vidhi Jain, Alexander Clegg, John M Turner, et al. Home-
robot: Open-vocabulary mobile manipulation. In Conference on Robot Learning, pages 1975–
2011. PMLR, 2023.
[132] Chengshu Li, Ruohan Zhang, Josiah Wong, Cem Gokmen, Sanjana Srivastava, Roberto Martín-
Martín, Chen Wang, Gabrael Levine, Michael Lingelbach, Jiankai Sun, et al. Behavior-1k:
A benchmark for embodied ai with 1,000 everyday activities and realistic simulation. In
Conference on Robot Learning, pages 80–93. PMLR, 2023.
[133] Kaijun Wang, Liqin Lu, Mingyu Liu, Jianuo Jiang, Zeju Li, Bolin Zhang, Wancai Zheng,
Xinyi Yu, Hao Chen, and Chunhua Shen. Odyssey: Open-world quadrupeds exploration
and manipulation for long-horizon tasks. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 40, pages 18602–18610, 2026.
[134] Nikita Chernyadev, Nicholas Backshall, Xiao Ma, Yunfan Lu, Younggyo Seo, and Stephen
James. Bigym: A demo-driven mobile bi-manual manipulation benchmark. In Conference on
Robot Learning, pages 4201–4217. PMLR, 2025.
[135] Carmelo Sferrazza, Dun-Ming Huang, Xingyu Lin, Youngwoon Lee, and Pieter Abbeel. Hu-
manoidbench: Simulated humanoid benchmark for whole-body locomotion and manipulation.
In Robotics: Science and Systems, 2024.
[136] Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, and Chenjia Bai. Humanoidgen:
Data generation for bimanual dexterous manipulation via llm reasoning. Advances in Neural
Information Processing Systems, 38:156210–156256, 2025.
[137] Songlin Wei, Zhenhao Ni, Jie Liu, Zhenyu Zhao, Junjie Ye, Hongyi Jing, Junkai Xia, Xiawei Liu,
Michael Leong, Liang Heng, et al. Simple: Simulation-based policy learning and evaluation
for humanoid loco-manipulation. arXiv preprint arXiv:2606.08278, 2026.
[138] Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen, Haodong Yan, Han
Zhao, Pengxiang Ding, Zhipeng Zhang, Lida Huang, et al. Robomemarena: A comprehensive
and challenging robotic memory benchmark. arXiv preprint arXiv:2605.10921, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[139] Senyu Fei, Siyin Wang, Junhao Shi, Zihao Dai, Jikun Cai, Pengfang Qian, Li Ji, Xinzhe He,
Shiduo Zhang, Zhaoye Fei, et al. Libero-plus: In-depth robustness analysis of vision-language-
action models. arXiv preprint arXiv:2510.13626, 2025.
[140] Arnav Balaji, Arpit Bahety, Sriniket Ambatipudi, Daniel Lam, Junhong Xu, and Roberto
Martín-Martín. Oopsieverse: A safety benchmark with damage-aware simulation for robot
manipulation. In Robotics: Science and Systems, 2026.
[141] Rongxu Cui, Zongzheng Zhang, Jingrui Pang, Haohan Chi, Jinbang Guo, Saining Zhang,
Shaoxuan Xie, Xin Jin, Yao Mu, Jiaolong Yang, et al.
Libero-safety: A comprehensive
benchmark for physical and semantic safety in vision-language-action models. In European
Conference on Computer Vision, 2026.
[142] Markus Grotz, Mohit Shridhar, Yu-Wei Chao, Tamim Asfour, and Dieter Fox. Peract2: Bench-
marking and learning for robotic bimanual manipulation tasks. In CoRL 2024 Workshop
on Whole-body Control and Bimanual Manipulation: Applications in Humanoids and Beyond,
2024.
[143] Jie Xu, Sangwoon Kim, Tao Chen, Alberto Rodriguez Garcia, Pulkit Agrawal, Wojciech Matusik,
and Shinjiro Sueda. Efficient tactile simulation with differentiability for robotic manipulation.
In Conference on Robot Learning, pages 1488–1498. PMLR, 2023.
[144] Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao
Xu, Gang Wang, Yao Mu, He Wang, et al. Dexjoco: A benchmark and toolkit for task-oriented
dexterous manipulation on mujoco. arXiv preprint arXiv:2605.16257, 2026.
[145] Yunchao Yao, Zhuxiu Xu, Tianqi Zhang, Zixian Liu, Sikai Li, Zhenyu Wei, Feng Chen, Dihong
Huang, Kechang Wan, Chenyang Ma, et al. Dexverse: A modular benchmark for multi-task,
multi-embodiment dexterous manipulation. arXiv preprint arXiv:2607.08751, 2026.
[146] Wenkang Hu, Xincheng Tang, Yitong Li, Zhengjie Shu, Wei Li, Huamin Wang, Ruigang Yang,
et al. Real garment benchmark (rgbench): A comprehensive benchmark for robotic garment
manipulation featuring a high-fidelity scalable simulator. In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 40, pages 18306–18314, 2026.
[147] Yuying Zhang, Kevin Sebastian Luck, Francesco Verdoja, Ville Kyrki, and Joni Pajarinen.
Modesuite: Robot learning task suite for benchmarking mobile manipulation with deformable
objects. IEEE Robotics and Automation Letters, 2026.
[148] Taowen Wang, Zikang Xie, Bin Yang, Yunheng Wang, Zizhao Yuan, Yuetong Fang, Yixiao Feng,
Yichi Wang, Xingyu Chen, Haodong Chen, et al. Humanoidarena: Benchmarking egocentric
hierarchical whole-body learning. arXiv preprint arXiv:2606.17833, 2026.
[149] Zehao Yu, Jiakun Zheng, Weiji Xie, Jiyuan Shi, Chenyun Zhang, Chenjia Bai, and Xuelong
Li. Oasis: From simulation data collection to real-world humanoid loco-manipulation. arXiv
preprint arXiv:2606.08548, 2026.
[150] Tianyi Xie, Haotian Zhang, Jinhyung Park, Zi Wang, Bowen Wen, Jiefeng Li, Xueting Li,
Qingwei Ben, Haoyang Weng, Yufei Ye, et al. Grail: Generating humanoid loco-manipulation
from 3d assets and video priors. arXiv preprint arXiv:2606.05160, 2026.
[151] Arjun Majumdar, Karmesh Yadav, Sergio Arnaud, Jason Ma, Claire Chen, Sneha Silwal, Aryan
Jain, Vincent-Pierre Berges, Tingfan Wu, Jay Vakil, et al. Where are we in the search for an
artificial visual cortex for embodied intelligence? In Advances in Neural Information Processing
Systems, volume 36, pages 655–677, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[152] Vikash Kumar, Rutav Shah, Gaoyue Zhou, Vincent Moens, Vittorio Caggiano, Abhishek Gupta,
and Aravind Rajeswaran. Robohive: A unified framework for robot learning. In Advances in
Neural Information Processing Systems, volume 36, pages 44323–44340, 2023.
[153] Haoran Geng, Feishi Wang, Songlin Wei, Yuyang Li, Bangjun Wang, Boshi An, Charlie Tianyue
Cheng, Haozhe Lou, Peihao Li, Yen-Jen Wang, et al. Roboverse: Towards a unified platform,
dataset and benchmark for scalable and generalizable robot learning. In Robotics: Science
and Systems, 2025.
[154] Mayank Mittal, Calvin Yu, Qinxi Yu, Jingzhou Liu, Nikita Rudin, David Hoeller, Jia Lin Yuan,
Ritvik Singh, Yunrong Guo, Hammad Mazhar, et al. Orbit: A unified simulation framework
for interactive robot learning environments. IEEE Robotics and Automation Letters, 8(6):
3740–3747, 2023.
[155] Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek
Joshi, Ajay Mandlekar, and Yuke Zhu. Robocasa: Large-scale simulation of everyday tasks for
generalist robots. In RSS 2024 Workshop: Data Generation for Robotics, 2024.
[156] Genesis Authors. Genesis: A universal and generative physics engine for robotics and beyond.
https://github.com/Genesis-Embodied-AI/Genesis, December 2024.
[157] Yizheng Zhang, Zhenjun Yu, JiaXin Lai, Cewu Lu, and Lei Han. Agentworld: An interactive
simulation platform for scene construction and mobile robotic manipulation. In 9th Annual
Conference on Robot Learning, 2025.
[158] Li Kang, Xiufeng Song, Heng Zhou, Yiran Qin, Jie Yang, Xiaohong Liu, Philip Torr, Lei Bai,
and Zhenfei Yin. Viki-r: Coordinating embodied multi-agent cooperation via reinforcement
learning. In Advances in Neural Information Processing Systems, volume 38, 2025.
[159] Yufei Jia, Heng Zhang, Ziheng Zhang, Junzhe Wu, Mingrui Yu, Zifan Wang, Dixuan Jiang,
Zheng Li, Chenyu Cao, Zhuoyuan Yu, et al. Gs-playground: A high-throughput photorealistic
simulator for vision-informed robot learning. In Robotics: Science and Systems, 2026.
[160] Pratyusha Sharma, Lekha Mohan, Lerrel Pinto, and Abhinav Gupta. Multiple interactions
made easy (mime): Large scale demonstrations data for imitation. In Conference on robot
learning, pages 906–915. PMLR, 2018.
[161] Frederik Ebert, Yanlai Yang, Karl Schmeckpeper, Bernadette Bucher, Georgios Georgakis,
Kostas Daniilidis, Chelsea Finn, and Sergey Levine. Bridge data: Boosting generalization of
robotic skills with cross-domain datasets. In Robotics: Science and Systems, 2022.
[162] Eric Jang, Alex Irpan, Mohi Khansari, Daniel Kappler, Frederik Ebert, Corey Lynch, Sergey
Levine, and Chelsea Finn. Bc-z: Zero-shot task generalization with robotic imitation learning.
In Conference on Robot Learning, pages 991–1002. PMLR, 2022.
[163] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea
Finn, Keerthana Gopalakrishnan, Karol Hausman, Alex Herzog, Jasmine Hsu, et al. Rt-1:
Robotics transformer for real-world control at scale. In Robotics: Science and Systems, 2023.
[164] Hao-Shu Fang, Hongjie Fang, Zhenyu Tang, Jirong Liu, Junbo Wang, Haoyi Zhu, and Cewu
Lu. Rh20t: A robotic dataset for learning diverse skills in one-shot. In RSS 2023 Workshop on
Learning for Task and Motion Planning, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[165] Homer Rich Walke, Kevin Black, Tony Z Zhao, Quan Vuong, Chongyi Zheng, Philippe Hansen-
Estruch, Andre Wang He, Vivek Myers, Moo Jin Kim, Max Du, et al. Bridgedata v2: A dataset
for robot learning at scale. In Conference on Robot Learning, pages 1723–1736. PMLR, 2023.
[166] Homanga Bharadhwaj, Jay Vakil, Mohit Sharma, Abhinav Gupta, Shubham Tulsiani, and
Vikash Kumar. Roboagent: Generalization and efficiency in robot manipulation via semantic
augmentations and action chunking. In 2024 IEEE International Conference on Robotics and
Automation (ICRA), pages 4788–4795. IEEE, 2024.
[167] Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar,
Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, Ajinkya Jain, et al. Open x-
embodiment: Robotic learning datasets and rt-x models: Open x-embodiment collaboration 0.
In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 6892–6903.
IEEE, 2024.
[168] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth
Karamcheti, Soroush Nasiriany, Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis,
et al. Droid: A large-scale in-the-wild robot manipulation dataset. In Robotics: Science and
Systems, 2024.
[169] Qingwen Bu, Jisong Cai, Li Chen, Xiuqi Cui, Yan Ding, Siyuan Feng, Shenyuan Gao, Xindong
He, Xuan Hu, Xu Huang, et al. Agibot world colosseo: A large-scale manipulation platform
for scalable and intelligent embodied systems. In 2025 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), 2025.
[170] Zhiqiang Wang, Hao Zheng, Yunshuang Nie, Wenjun Xu, Qingwei Wang, Hua Ye, Zhe Li,
Kaidong Zhang, Xuewen Cheng, Wanxi Dong, et al. All robots in one: A new standard and uni-
fied dataset for versatile, general-purpose embodied agents. arXiv preprint arXiv:2408.10899,
2024.
[171] Kun Wu, Chengkai Hou, Jiaming Liu, Zhengping Che, Xiaozhu Ju, Zhuqin Yang, Meng Li,
Yinuo Zhao, Zhiyuan Xu, Guang Yang, et al. Robomind: Benchmark on multi-embodiment
intelligence normative data for robot manipulation. In Robotics: Science and Systems, 2025.
[172] Weifeng Lu, Minghao Ye, Zewei Ye, Ruihan Tao, Shuo Yang, and Bo Zhao. Robofac: A compre-
hensive framework for robotic failure analysis and correction. arXiv preprint arXiv:2505.12224,
2025.
[173] Shihan Wu, Xuecheng Liu, Shaoxuan Xie, Pengwei Wang, Xinghang Li, Bowen Yang, Zhe Li,
Kai Zhu, Hongyu Wu, Yiheng Liu, et al. Robocoin: An open-sourced bimanual robotic data
collection for integrated manipulation. arXiv preprint arXiv:2511.17441, 2025.
[174] Zhenyu Zhao, Hongyi Jing, Xiawei Liu, Jiageng Mao, Abha Jha, Hanwen Yang, Rong Xue,
Sergey Zakharov, Vitor Guizilini, and Yue Wang. Humanoid everyday: A comprehensive
robotic dataset for open-world humanoid manipulation. In 2026 IEEE International Conference
on Robotics and Automation (ICRA), 2026.
[175] Arjun Majumdar, Anurag Ajay, Xiaohan Zhang, Pranav Putta, Sriram Yenamandra, Mikael
Henaff, Sneha Silwal, Paul Mcvay, Oleksandr Maksymets, Sergio Arnaud, et al. Openeqa:
Embodied question answering in the era of foundation models. In Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition, pages 16488–16498, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[176] Siyuan Huang, Iaroslav Ponomarenko, Zhengkai Jiang, Xiaoqi Li, Xiaobin Hu, Peng Gao, Hong-
sheng Li, and Hao Dong. Manipvqa: Injecting robotic affordance and physically grounded
information into multi-modal large language models. In 2024 IEEE/RSJ International Confer-
ence on Intelligent Robots and Systems (IROS), pages 7580–7587. IEEE, 2024.
[177] Enyu Zhao, Vedant Raval, Hejia Zhang, Jiageng Mao, Zeyu Shangguan, Stefanos Nikolaidis,
Yue Wang, and Daniel Seita. Manipbench: Benchmarking vision-language models for low-level
robot manipulation. In Conference on Robot Learning, pages 3413–3462. PMLR, 2025.
[178] Enshen Zhou, Jingkun An, Cheng Chi, Yi Han, Shanyu Rong, Chi Zhang, Pengwei Wang,
Zhongyuan Wang, Tiejun Huang, Lu Sheng, et al. Roborefer: Towards spatial referring with
reasoning in vision-language models for robotics. In Advances in Neural Information Processing
Systems, 2025.
[179] Kaiyuan Eric Chen, Shuangyu Xie, Zehan Ma, Pannag Sanketi, and Ken Goldberg. Robo2vlm:
Improving visual question answering using large-scale robot manipulation data. In Advances
in Neural Information Processing Systems, volume 38, 2025.
[180] Atharva Gundawar, Som Sagar, and Ransalu Senanayake. Pac bench: Do foundation models
understand prerequisites for executing manipulation policies? Advances in Neural Information
Processing Systems, 38, 2025.
[181] Long Cheng, Jiafei Duan, Yi Ru Wang, Haoquan Fang, Boyang Li, Yushan Huang, Elvis Wang,
Ainaz Eftekhar, Jason Lee, Wentao Yuan, et al. Pointarena: Probing multimodal grounding
through language-guided pointing. arXiv preprint arXiv:2505.09990, 2025.
[182] Kristen Grauman, Andrew Westbury, Eugene Byrne, Zachary Chavis, Antonino Furnari, Rohit
Girdhar, Jackson Hamburger, Hao Jiang, Miao Liu, Xingyu Liu, et al. Ego4d: Around the world
in 3,000 hours of egocentric video. In Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, pages 18995–19012, 2022.
[183] Kristen Grauman, Andrew Westbury, Lorenzo Torresani, Kris Kitani, Jitendra Malik, Tri-
antafyllos Afouras, Kumar Ashutosh, Vijay Baiyya, Siddhant Bansal, Bikram Boote, et al.
Ego-exo4d: Understanding skilled human activity from first-and third-person perspectives.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
19383–19400, 2024.
[184] Ryan Hoque, Peide Huang, David J Yoon, Mouli Sivapurapu, and Jian Zhang. Egodex: Learn-
ing dexterous manipulation from large-scale egocentric video. In International Conference on
Learning Representations, 2026.
[185] Ryan Punamiya, Simar Kareer, Zeyi Liu, Josh Citron, Ri-Zhao Qiu, Xiongyi Cai, Alexey
Gavryushin, Jiaqi Chen, Davide Liconti, Lawrence Y Zhu, et al. Egoverse: An egocentric
human dataset for robot learning from around the world. arXiv preprint arXiv:2604.07607,
2026.
[186] Tim Engelbracht, René Zurbrügg, Matteo Wohlrapp, Martin Büchner, Abhinav Valada, Marc
Pollefeys, Hermann Blum, and Zuria Bauer. Hoi!-a multimodal dataset for force-grounded,
cross-view articulated manipulation. arXiv preprint arXiv:2512.04884, 2025.
[187] Rui Zhao, Kaiming Yang, Jifeng Zhu, Siyang Chen, Ziqi Wang, Weijia Wu, Kevin Qinghong
Lin, Heng Wang, and Mike Zheng Shou. Dream. exe: Can video generation models dream
executable robot manipulation? arXiv preprint arXiv:2606.04811, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[188] Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu,
Shengze Huang, Yuanfei Wang, Chen Xie, et al. Robowm-bench: A benchmark for evaluating
world models in robotic manipulation. arXiv preprint arXiv:2604.19092, 2026.
[189] Chun-Kai Fan, Xiaowei Chi, Xiaozhu Ju, Hao Li, Yong Bao, Yu-Kai Wang, Lizhang Chen,
Zhiyuan Jiang, Kuangzhi Ge, Ying Li, et al. Wow, wo, val! a comprehensive embodied world
model evaluation turing test. arXiv preprint arXiv:2601.04137, 2026.
[190] Joseph L Jones and Tomás Lozano-Pérez. Planning two-fingered grasps for pick-and-place
operations on polyhedra. In Proceedings., IEEE International Conference on Robotics and
Automation, pages 683–688. IEEE, 1990.
[191] Andrew T Miller and Peter K Allen. Graspit! a versatile simulator for robotic grasping. IEEE
Robotics & Automation Magazine, 11(4):110–122, 2004.
[192] Alexander Stoytchev. Behavior-grounded representation of tool affordances. In Proceedings
of the 2005 ieee international conference on robotics and automation, pages 3060–3065. IEEE,
2005.
[193] Joseph Redmon and Anelia Angelova. Real-time grasp detection using convolutional neural
networks. In 2015 IEEE international conference on robotics and automation (ICRA), pages
1316–1322. IEEE, 2015.
[194] Sulabh Kumra and Christopher Kanan. Robotic grasp detection using deep convolutional
neural networks. In 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS), pages 769–776. IEEE, 2017.
[195] Douglas Morrison, Peter Corke, and Jürgen Leitner. Closing the loop for robotic grasping: a
real-time, generative grasp synthesis approach. In Robotics: Science and Systems 2018. The
MIT Press, 2018.
[196] Sulabh Kumra, Shirin Joshi, and Ferat Sahin. Antipodal robotic grasping using genera-
tive residual convolutional neural network. In 2020 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 9626–9633. IEEE, 2020.
[197] Shaochen Wang, Zhangli Zhou, and Zhen Kan. When transformer meets robotic grasping:
Exploits context for efficient grasp detection. IEEE robotics and automation letters, 7(3):
8170–8177, 2022.
[198] Nghia Nguyen, Minh Nhat Vu, Baoru Huang, An Vuong, Ngan Le, Thieu Vo, and Anh Nguyen.
Lightweight language-driven grasp detection using conditional consistency model. In 2024
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 13719–
13725. IEEE, 2024.
[199] Haoran Zhang, Shuanghao Bai, Wanqi Zhou, Yuedi Zhang, Qi Zhang, Pengxiang Ding, Cheng
Chi, Donglin Wang, and Badong Chen. Vcot-grasp: Grasp foundation models with visual chain-
of-thought reasoning for language-driven grasp generation. In 2026 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), 2026.
[200] Xinchen Yan, Jasmined Hsu, Mohammad Khansari, Yunfei Bai, Arkanath Pathak, Abhinav
Gupta, James Davidson, and Honglak Lee. Learning 6-dof grasping interaction via deep
geometry-aware 3d representations. In 2018 IEEE International Conference on Robotics and
Automation (ICRA), pages 3766–3773. IEEE, 2018.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[201] Guangyao Zhai, Dianye Huang, Shun-Cheng Wu, HyunJun Jung, Yan Di, Fabian Manhardt,
Federico Tombari, Nassir Navab, and Benjamin Busam. Monograspnet: 6-dof grasping with a
single rgb image. In ICRA, 2023.
[202] Hao-Shu Fang, Chenxi Wang, Hongjie Fang, Minghao Gou, Jirong Liu, Hengxu Yan, Wenhai
Liu, Yichen Xie, and Cewu Lu. Anygrasp: Robust and efficient grasp perception in spatial and
temporal domains. IEEE Transactions on Robotics, 39(5):3929–3945, 2023.
[203] Qingyu Fan, Yinghao Cai, Chao Li, Chunting Jiao, Xudong Zheng, Tao Lu, Bin Liang, and
Shuo Wang. Miscgrasp: Leveraging multiple integrated scales and contrastive learning for
enhanced volumetric grasping. 2025 IEEE/RSJ International Conference on Intelligent Robots
and Systems (IROS), 2025.
[204] Arsalan Mousavian, Clemens Eppner, and Dieter Fox. 6-dof graspnet: Variational grasp
generation for object manipulation. In Proceedings of the IEEE/CVF international conference
on computer vision, pages 2901–2910, 2019.
[205] Shun Iwase, Muhammad Zubair Irshad, Katherine Liu, Vitor Guizilini, Robert Lee, Takuya
Ikeda, Ayako Amma, Koichi Nishiwaki, Kris Kitani, Rares Ambrus, et al. Zerograsp: Zero-shot
shape reconstruction enabled robotic grasping. In Proceedings of the Computer Vision and
Pattern Recognition Conference, pages 17405–17415, 2025.
[206] Pengwei Xie, Siang Chen, Wei Tang, Kaiqin Yang, and Guijin Wang. Rethinking 6-dof grasp
detection: A flexible framework for high-quality grasping. Pattern Recognition, page 112088,
2025.
[207] Adithyavairavan Murali, Arsalan Mousavian, Clemens Eppner, Chris Paxton, and Dieter Fox.
6-dof grasping for target-driven object manipulation in clutter. In 2020 IEEE International
Conference on Robotics and Automation (ICRA), pages 6232–6238. IEEE, 2020.
[208] Siang Chen, Wei Tang, Pengwei Xie, Wenming Yang, and Guijin Wang. Efficient heatmap-
guided 6-dof grasp detection in cluttered scenes. IEEE Robotics and Automation Letters, 8(8):
4895–4902, 2023.
[209] Martin Sundermeyer, Arsalan Mousavian, Rudolph Triebel, and Dieter Fox. Contact-graspnet:
Efficient 6-dof grasp generation in cluttered scenes. In 2021 IEEE International Conference on
Robotics and Automation (ICRA), pages 13438–13444. IEEE, 2021.
[210] Ali Rashidi Moghadam, Mehdi Tale Masouleh, and Ahmad Kalhor. Grasp the graph (gtg): A
super light graph-rl framework for robotic grasping. In 2023 11th RSI International Conference
on Robotics and Mechatronics (ICRoM), pages 861–868. IEEE, 2023.
[211] Xiao-Ming Wu, Jia-Feng Cai, Jian-Jian Jiang, Dian Zheng, Yi-Lin Wei, and Wei-Shi Zheng. An
economic framework for 6-dof grasp detection. In European Conference on Computer Vision,
pages 357–375. Springer, 2024.
[212] Yaofeng Cheng, Fusheng Zha, Wei Guo, Pengfei Wang, Chao Zeng, Lining Sun, and Chenguang
Yang. Pcf-grasp: Converting point completion to geometry feature to enhance 6-dof grasp.
IEEE Transactions on Systems, Man, and Cybernetics: Systems, 56(1):617–628, 2025.
[213] Jia-Feng Cai, Zibo Chen, Xiao-Ming Wu, Jian-Jian Jiang, Yi-Lin Wei, and Wei-Shi Zheng.
Real-to-sim grasp: Rethinking the gap between simulation and real world in grasp detection.
In Conference on Robot Learning, pages 1109–1124. PMLR, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[214] Byeongdo Lim, Jongmin Kim, Jihwan Kim, Yonghyeon Lee, and Frank C Park. Equigraspflow:
Se (3)-equivariant 6-dof grasp pose generative flows. In Conference on Robot Learning, pages
5067–5086. PMLR, 2025.
[215] Boce Hu, Xupeng Zhu, Dian Wang, Zihao Dong, Haojie Huang, Chenghao Wang, Robin
Walters, and Robert Platt. Orbitgrasp: Se (3)-equivariant grasp learning. In Conference on
Robot Learning, pages 2456–2474. PMLR, 2025.
[216] Michel Breyer, Jen Jen Chung, Lionel Ott, Roland Siegwart, and Juan Nieto. Volumetric
grasping network: Real-time 6 dof grasp detection in clutter. In Conference on robot learning,
pages 1602–1611. PMLR, 2021.
[217] Pinhao Song, Pengteng Li, and Renaud Detry. Implicit grasp diffusion: Bridging the gap
between dense prediction and sampling-based grasping. In Conference on Robot Learning,
pages 2948–2964. PMLR, 2025.
[218] Snehal Jauhri, Ishikaa Lunawat, and Georgia Chalvatzaki. Learning any-view 6dof robotic
grasping in cluttered scenes via neural surface rendering. In RSS 2024 Workshop on Geometric
and Algebraic Structure in Robot Learning, 2024.
[219] Adam Rashid, Satvik Sharma, Chung Min Kim, Justin Kerr, Lawrence Yunliang Chen, Angjoo
Kanazawa, and Ken Goldberg. Language embedded radiance fields for zero-shot task-oriented
grasping. In Conference on Robot Learning, pages 178–200. PMLR, 2023.
[220] Qiyu Dai, Yan Zhu, Yiran Geng, Ciyu Ruan, Jiazhao Zhang, and He Wang. Graspnerf:
Multiview-based 6-dof grasp detection for transparent and specular objects using generalizable
nerf. In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages 1757–
1763. IEEE, 2023.
[221] Yuhang Zheng, Xiangyu Chen, Yupeng Zheng, Songen Gu, Runyi Yang, Bu Jin, Pengfei Li,
Chengliang Zhong, Zengmao Wang, Lina Liu, et al. Gaussiangrasper: 3d language gaussian
splatting for open-vocabulary robotic grasping. IEEE Robotics and Automation Letters, 2024.
[222] Mazeyu Ji, Ri-Zhao Qiu, Xueyan Zou, and Xiaolong Wang. Graspsplats: Efficient manipulation
with 3d feature splatting. In Conference on Robot Learning, pages 1443–1460. PMLR, 2025.
[223] Junqiu Yu, Xinlin Ren, Yongchong Gu, Haitao Lin, Tianyu Wang, Yi Zhu, Hang Xu, Yu-Gang
Jiang, Xiangyang Xue, and Yanwei Fu. Sparsegrasp: Robotic grasping via 3d semantic gaussian
splatting from sparse multi-view rgb images. arXiv preprint arXiv:2412.02140, 2024.
[224] Kechun Xu, Shuqi Zhao, Zhongxiang Zhou, Zizhang Li, Huaijin Pi, Yifeng Zhu, Yue Wang,
and Rong Xiong. A joint modeling of vision-language-action for target-oriented grasping
in clutter. In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages
11597–11604. IEEE, 2023.
[225] Toan Nguyen, Minh Nhat Vu, Baoru Huang, Tuan Van Vo, Vy Truong, Ngan Le, Thieu Vo, Bac
Le, and Anh Nguyen. Language-conditioned affordance-pose detection in 3d point clouds. In
2024 IEEE International Conference on Robotics and Automation (ICRA), pages 3071–3078.
IEEE, 2024.
[226] Chao Tang, Dehao Huang, Wenqi Ge, Weiyu Liu, and Hong Zhang. Graspgpt: Leveraging
semantic knowledge from a large language model for task-oriented grasping. IEEE Robotics
and Automation Letters, 8(11):7551–7558, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[227] Yaoyao Qian, Xupeng Zhu, Ondrej Biza, Shuo Jiang, Linfeng Zhao, Haojie Huang, Yu Qi, and
Robert Platt. Thinkgrasp: A vision-language system for strategic part grasping in clutter. In
Conference on Robot Learning, pages 3568–3586. PMLR, 2025.
[228] Yingbo Tang, Shuaike Zhang, Xiaoshuai Hao, Pengwei Wang, Jianlong Wu, Zhongyuan Wang,
and Shanghang Zhang. Affordgrasp: In-context affordance reasoning for open-vocabulary
task-oriented grasping in clutter. In 2025 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 9433–9439. IEEE, 2025.
[229] Yuhao Lu, Yixuan Fan, Beixing Deng, Fangfu Liu, Yali Li, and Shengjin Wang. Vl-grasp:
a 6-dof interactive grasp policy for language-oriented objects in cluttered indoor scenes.
In 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
976–983. IEEE, 2023.
[230] Georgios Tziafas and Hamidreza Kasaei. Towards open-world grasping with large vision-
language models. In Conference on Robot Learning, pages 3304–3332. PMLR, 2025.
[231] Shiyu Jin, JINXUAN XU, Yutian Lei, and Liangjun Zhang. Reasoning grasping via multimodal
large language model. In Conference on Robot Learning, pages 3809–3827. PMLR, 2025.
[232] Zhen Luo, Yixuan Yang, Yanfu Zhang, and Feng Zheng. Roboreflect: A robotic reflective rea-
soning framework for grasping ambiguous-condition objects. arXiv preprint arXiv:2501.09307,
2025.
[233] Yang Yang, Houjian Yu, Xibai Lou, Yuanhao Liu, and Changhyun Choi. Attribute-based
robotic grasping with data-efficient adaptation. IEEE Transactions on Robotics, 40:1566–1579,
2024.
[234] Wenlong Dong, Dehao Huang, Jiangshan Liu, Chao Tang, and Hong Zhang. Rtagrasp:
Learning task-oriented grasping from human videos via retrieval, transfer, and alignment.
2025 IEEE international conference on robotics and automation (ICRA), 2025.
[235] Yaoxian Song, Penglei Sun, Piaopiao Jin, Yi Ren, Yu Zheng, Zhixu Li, Xiaowen Chu, Yue
Zhang, Tiefeng Li, and Jason Gu. Learning 6-dof fine-grained grasp detection based on part
affordance grounding. IEEE Transactions on Automation Science and Engineering, 2025.
[236] Abhay Deshpande, Yuquan Deng, Jordi Salvador, Arijit Ray, Winson Han, Jiafei Duan, Rose
Hendrix, Yuke Zhu, and Ranjay Krishna. Graspmolmo: Generalizable task-oriented grasping
via large-scale synthetic data generation. In Conference on Robot Learning, pages 2983–3007.
PMLR, 2025.
[237] Jinxuan Xu, Shiyu Jin, Yutian Lei, Yuqian Zhang, and Liangjun Zhang. Rt-grasp: Reasoning
tuning robotic grasping via multi-modal large language model. In 2024 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 7323–7330. IEEE, 2024.
[238] Guo-Hao Xu, Yi-Lin Wei, Dian Zheng, Xiao-Ming Wu, and Wei-Shi Zheng. Dexterous grasp
transformer. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 17933–17942, 2024.
[239] Zehang Weng, Haofei Lu, Danica Kragic, and Jens Lundell. Dexdiffuser: Generating dexterous
grasps with diffusion models. IEEE Robotics and Automation Letters, 2024.
[240] Yi-Lin Wei, Jian-Jian Jiang, Chengyi Xing, Xian-Tuo Tan, Xiao-Ming Wu, Hao Li, Mark
Cutkosky, and Wei-Shi Zheng. Grasp as you say: Language-guided dexterous grasp generation.
Advances in Neural Information Processing Systems, 37:46881–46907, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[241] Puhao Li, Tengyu Liu, Yuyang Li, Yiran Geng, Yixin Zhu, Yaodong Yang, and Siyuan Huang.
Gendexgrasp: Generalizable dexterous grasping. In 2023 IEEE International Conference on
Robotics and Automation (ICRA), pages 8068–8074. IEEE, 2023.
[242] Zhenyu Wei, Zhixuan Xu, Jingxiang Guo, Yiwen Hou, Chongkai Gao, Zhehao Cai, Jiayu
Luo, and Lin Shao. D (r, o) grasp: A unified representation of robot and object interaction
for cross-embodiment dexterous grasping. In CoRL Workshop on Learning Robot Fine and
Dexterous Manipulation: Perception and Control, 2024.
[243] Jeffrey Mahler, Matthew Matl, Vishal Satish, Michael Danielczuk, Bill DeRose, Stephen
McKinley, and Ken Goldberg. Learning ambidextrous robot grasping policies. Science Robotics,
4(26):eaau4984, 2019.
[244] Jun Yamada, Alexander Luis Mitchell, Jack Collins, and Ingmar Posner.
Combo-grasp:
Learning constraint-based manipulation for bimanual occluded grasping. In Conference on
Robot Learning, pages 1102–1119. PMLR, 2025.
[245] Hongyu Deng, Tianfan Xue, and He Chen. Fusegrasp: Radar-camera fusion for robotic
grasping of transparent objects. IEEE Transactions on Mobile Computing, 2025.
[246] Bardienus P Duisterhof, Yuemin Mao, Si Heng Teng, and Jeffrey Ichnowski. Residual-nerf:
Learning residual nerfs for transparent object manipulation. In 2024 IEEE International
Conference on Robotics and Automation (ICRA), pages 13918–13924. IEEE, 2024.
[247] Jun Shi, A Yong, Yixiang Jin, Dingzhe Li, Haoyu Niu, Zhezhu Jin, and He Wang. Asgrasp:
Generalizable transparent object reconstruction and 6-dof grasp detection from rgb-d active
stereo camera. In 2024 IEEE international conference on robotics and automation (ICRA),
pages 5441–5447. IEEE, 2024.
[248] Young Hun Kim, Seungyeon Kim, Yonghyeon Lee, and Frank C Park. T2sqnet: A recognition
model for manipulating partially observed transparent tableware objects. In Conference on
Robot Learning, pages 3622–3655. PMLR, 2025.
[249] Anusha Nagabandi, Kurt Konolige, Sergey Levine, and Vikash Kumar. Deep dynamics models
for learning dexterous manipulation. In Conference on robot learning, pages 1101–1112.
PMLR, 2020.
[250] Henry Zhu, Abhishek Gupta, Aravind Rajeswaran, Sergey Levine, and Vikash Kumar. Dexter-
ous manipulation with deep reinforcement learning: Efficient, general, and low-cost. In 2019
International Conference on Robotics and Automation (ICRA), pages 3651–3657. IEEE, 2019.
[251] Zhixuan Liang, Yao Mu, Yixiao Wang, Tianxing Chen, Wenqi Shao, Wei Zhan, Masayoshi
Tomizuka, Ping Luo, and Mingyu Ding. Dexhanddiff: Interaction-aware diffusion planning
for adaptive dexterous manipulation. In Proceedings of the Computer Vision and Pattern
Recognition Conference, pages 1745–1755, 2025.
[252] Yankai Fu, Qiuxuan Feng, Ning Chen, Zichen Zhou, Mengzhen Liu, Mingdong Wu, Tianxing
Chen, Shanyu Rong, Jiaming Liu, Hao Dong, et al. Cordvip: Correspondence-based visuomotor
policy for dexterous manipulation in real-world. In Robotics: Science and Systems, 2025.
[253] Zheyuan Hu, Aaron Rovinsky, Jianlan Luo, Vikash Kumar, Abhishek Gupta, and Sergey Levine.
Reboot: Reuse data for bootstrapping efficient real-world dexterous manipulation. In 7th
Annual Conference on Robot Learning, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[254] Zerui Chen, Shizhe Chen, Etienne Arlaud, Ivan Laptev, and Cordelia Schmid. Vividex:
Learning vision-based dexterous manipulation from human videos. In 2025 IEEE international
conference on robotics and automation (ICRA), 2025.
[255] Yihang Li, Tianle Zhang, Xuelong Wei, Jiayi Li, Lin Zhao, Dongchi Huang, Zhirui Fang,
Minhua Zheng, Wenjun Dai, and Xiaodong He. Object-focus actor for data-efficient robot
generalization dexterous manipulation. arXiv preprint arXiv:2505.15098, 2025.
[256] Jose Barreiros, Andrew Beaulieu, Aditya Bhat, Rick Cory, Eric Cousineau, Hongkai Dai, Ching-
Hsin Fang, Kunimatsu Hashimoto, Muhammad Zubair Irshad, Masha Itkina, et al. A careful
examination of large behavior models for multitask dexterous manipulation. arXiv preprint
arXiv:2507.05331, 2025.
[257] Thomas George Thuruthel, Egidio Falotico, Federico Renda, and Cecilia Laschi. Model-based
reinforcement learning for closed-loop dynamic control of soft robotic manipulators. IEEE
Transactions on Robotics, 35(1):124–134, 2018.
[258] Yingqi Li, Xiaomei Wang, and Ka-Wai Kwok. Towards adaptive continuous control of soft
robotic manipulator using reinforcement learning. In 2022 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS), pages 7074–7081. IEEE, 2022.
[259] Muhammad Sunny Nazeer, Cecilia Laschi, and Egidio Falotico. Soft dagger: Sample-efficient
imitation learning for control of soft robots. Sensors, 23(19):8278, 2023.
[260] Uksang Yoo, Jonathan Francis, Jean Oh, and Jeffrey Ichnowski. Kinesoft: Learning proprio-
ceptive manipulation policies with soft robot hands. In Conference on Robot Learning, pages
633–651. PMLR, 2025.
[261] Yinan Meng, Kun Qian, Jiong Yang, Renbo Su, Zhenhong Li, and Charlie CL Wang. Sensor-
space based robust kinematic control of redundant soft manipulator by learning. arXiv preprint
arXiv:2507.16842, 2025.
[262] Jan Matas, Stephen James, and Andrew J Davison. Sim-to-real reinforcement learning for
deformable object manipulation. In Conference on Robot Learning, pages 734–743. PMLR,
2018.
[263] Zhe Hu, Tao Han, Peigen Sun, Jia Pan, and Dinesh Manocha. 3-d deformable object manipu-
lation using deep neural networks. IEEE Robotics and Automation Letters, 4(4):4255–4261,
2019.
[264] Sizhe Li, Zhiao Huang, Tao Chen, Tao Du, Hao Su, Joshua B Tenenbaum, and Chuang Gan.
Dexdeform: Dexterous deformable object manipulation with human demonstrations and
differentiable physics. In The Eleventh International Conference on Learning Representations,
2023.
[265] Gautam Salhotra, I-Chun Arthur Liu, Marcus Dominguez-Kuhne, and Gaurav S Sukhatme.
Learning deformable object manipulation from expert demonstrations. IEEE Robotics and
Automation Letters, 7(4):8775–8782, 2022.
[266] Checheng Yu, Chonghao Sima, Gangcheng Jiang, Hai Zhang, Haoguang Mai, Hongyang Li,
Huijie Wang, Jin Chen, Kaiyang Wu, Li Chen, et al. 𝜒0: Resource-aware robust manipulation
via taming distributional inconsistencies. arXiv preprint arXiv:2602.09021, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[267] Jimmy Wu, Xingyuan Sun, Andy Zeng, Shuran Song, Johnny Lee, Szymon Rusinkiewicz, and
Thomas Funkhouser. Spatial action maps for mobile manipulation. In Robotics: Science and
Systems, 2020.
[268] Jiaheng Hu, Peter Stone, and Roberto Martín-Martín. Causal policy gradient for whole-body
mobile manipulation. In Robotics: Science and Systems, 2023.
[269] Taozheng Yang, Ya Jing, Hongtao Wu, Jiafeng Xu, Kuankuan Sima, Guangzeng Chen, Qie
Sima, and Tao Kong. Moma-force: Visual-force imitation for real-world mobile manipulation.
In 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
6847–6852. IEEE, 2023.
[270] Xiaoyu Huang, Dhruv Batra, Akshara Rai, and Andrew Szot. Skill transformer: A monolithic
policy for mobile manipulation. In Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 10852–10862, 2023.
[271] Haoyu Xiong, Russell Mendonca, Kenneth Shaw, and Deepak Pathak. Adaptive mobile
manipulation for articulated objects in the open world. arXiv preprint arXiv:2401.14403,
2024.
[272] Zhenyu Wu, Yuheng Zhou, Xiuwei Xu, Ziwei Wang, and Haibin Yan. Momanipvla: Transfer-
ring vision-language-action models for general mobile manipulation. In Proceedings of the
Computer Vision and Pattern Recognition Conference, pages 1714–1723, 2025.
[273] Minghuan Liu, Zixuan Chen, Xuxin Cheng, Yandong Ji, Ri-Zhao Qiu, Ruihan Yang, and
Xiaolong Wang. Visual whole-body control for legged loco-manipulation. In Conference on
Robot Learning, pages 234–257. PMLR, 2025.
[274] Jiazhao Zhang, Nandiraju Gireesh, Jilong Wang, Xiaomeng Fang, Chaoyi Xu, Weiguang Chen,
Liu Dai, and He Wang. Gamma: Graspability-aware mobile manipulation policy learning
based on online grasping pose fusion. In 2024 IEEE International Conference on Robotics and
Automation (ICRA), pages 1399–1405. IEEE, 2024.
[275] Yaru Niu, Yunzhe Zhang, Mingyang Yu, Changyi Lin, Chenhao Li, Yikai Wang, Yuxiang Yang,
Wenhao Yu, Tingnan Zhang, Bingqing Chen, et al. Human2locoman: Learning versatile
quadrupedal manipulation with human pretraining. In Robotics: Science and Systems, 2025.
[276] Zhengmao He, Kun Lei, Yanjie Ze, Koushil Sreenath, Zhongyu Li, and Huazhe Xu. Learning
visual quadrupedal loco-manipulation from demonstrations. In 2024 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 9102–9109. IEEE, 2024.
[277] Ri-Zhao Qiu, Yuchen Song, Xuanbin Peng, Sai Aneesh Suryadevara, Ge Yang, Minghuan
Liu, Mazeyu Ji, Chengzhe Jia, Ruihan Yang, Xueyan Zou, et al. Wildlma: Long horizon loco-
manipulation in the wild. In 2025 IEEE International Conference on Robotics and Automation
(ICRA), pages 10011–10019. IEEE, 2025.
[278] Pengxiang Ding, Han Zhao, Wenjie Zhang, Wenxuan Song, Min Zhang, Siteng Huang, Ningxi
Yang, and Donglin Wang. Quar-vla: Vision-language-action model for quadruped robots. In
European Conference on Computer Vision, pages 352–367. Springer, 2024.
[279] Wenxuan Song, Han Zhao, Pengxiang Ding, Can Cui, Shangke Lyu, Yaning Fan, and Donglin
Wang. Germ: A generalist robotic model with mixture-of-experts for quadruped robot. In
2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
11879–11886. IEEE, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[280] Zhaoming Xie, Jonathan Tseng, Sebastian Starke, Michiel van de Panne, and C Karen Liu.
Hierarchical planning and control for box loco-manipulation. Proceedings of the ACM on
Computer Graphics and Interactive Techniques, 6(3):1–18, 2023.
[281] Xianqi Zhang, Hongliang Wei, Wenrui Wang, Xingtao Wang, Xiaopeng Fan, and Debin Zhao.
Flam: Foundation model-based body stabilization for humanoid locomotion and manipulation.
arXiv preprint arXiv:2503.22249, 2025.
[282] Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris M Kitani,
Changliu Liu, and Guanya Shi. Omnih2o: Universal and dexterous human-to-humanoid
whole-body teleoperation and learning. In Conference on Robot Learning, pages 1516–1540.
PMLR, 2025.
[283] Yanjie Ze, Zixuan Chen, Wenhao Wang, Tianyi Chen, Xialin He, Ying Yuan, Xue Bin Peng, and
Jiajun Wu. Generalizable humanoid manipulation with 3d diffusion policies. 2025 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), 2025.
[284] André Schakkal, Ben Zandonati, Zhutian Yang, and Navid Azizan. Hierarchical vision-
language planning for multi-step humanoid manipulation. arXiv preprint arXiv:2506.22827,
2025.
[285] Johan Bjorck, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi Fan,
Yu Fang, Dieter Fox, Fengyuan Hu, Spencer Huang, et al. Gr00t n1: An open foundation
model for generalist humanoid robots. arXiv preprint arXiv:2503.14734, 2025.
[286] Pengxiang Ding, Jianfei Ma, Xinyang Tong, Binghong Zou, Xinxin Luo, Yiguo Fan, Ting Wang,
Hongchao Lu, Panzhong Mo, Jinxin Liu, et al. Humanoid-vla: Towards universal humanoid
control with visual integration. arXiv preprint arXiv:2502.14795, 2025.
[287] Edgar Welte and Rania Rayyes. Interactive imitation learning for dexterous robotic manip-
ulation: challenges and perspectives—a survey. Frontiers in Robotics and AI, 12:1682437,
2025.
[288] Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, and Xiaolong Wang. Dexpoint: Gen-
eralizable point cloud reinforcement learning for sim-to-real dexterous manipulation. In
Conference on Robot Learning, pages 594–605. PMLR, 2023.
[289] Yuanpei Chen, Chen Wang, Li Fei-Fei, and Karen Liu. Sequential dexterity: Chaining dexterous
policies for long-horizon manipulation. In Conference on Robot Learning, pages 3809–3829.
PMLR, 2023.
[290] Jun Wang, Yuzhe Qin, Kaiming Kuang, Yigit Korkmaz, Akhilan Gurumoorthy, Hao Su, and
Xiaolong Wang. Cyberdemo: Augmenting simulated human demonstration for real-world
dexterous manipulation. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 17952–17963, 2024.
[291] Yunfei Bai and C Karen Liu. Dexterous manipulation using both palm and fingers. In 2014
IEEE International Conference on Robotics and Automation (ICRA), pages 1560–1565. IEEE,
2014.
[292] Jianlan Luo, Charles Xu, Jeffrey Wu, and Sergey Levine. Precise and dexterous robotic
manipulation via human-in-the-loop reinforcement learning. Science Robotics, 10(105):
eads5033, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[293] Elvis Hsieh, Wen-Han Hsieh, Yen-Jen Wang, Toru Lin, Jitendra Malik, Koushil Sreenath, and
Haozhi Qi. Learning dexterous manipulation skills from imperfect simulations. In 2026 IEEE
International Conference on Robotics and Automation (ICRA), 2026.
[294] Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, and Xiaolong
Wang. Dexmv: Imitation learning for dexterous manipulation from human videos. In European
Conference on Computer Vision, pages 570–587. Springer, 2022.
[295] Ilija Radosavovic, Xiaolong Wang, Lerrel Pinto, and Jitendra Malik. State-only imitation
learning for dexterous manipulation. In 2021 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 7865–7871. IEEE, 2021.
[296] Xiaohan Lei, Min Wang, Bohong Weng, Wengang Zhou, and Houqiang Li. Structural action
transformer for 3d dexterous manipulation. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, 2026.
[297] Vikash Kumar, Abhishek Gupta, Emanuel Todorov, and Sergey Levine. Learning dexterous
manipulation policies from experience and imitation. arXiv preprint arXiv:1611.05095, 2016.
[298] Sridhar Pandian Arunachalam, Sneha Silwal, Ben Evans, and Lerrel Pinto. Dexterous imitation
made easy: A learning-based framework for efficient dexterous manipulation. In 2023 IEEE
International Conference on Robotics and Automation (ICRA), pages 5954–5961. IEEE, 2023.
[299] Yifan Zhong, Xuchuan Huang, Ruochong Li, Ceyao Zhang, Zhang Chen, Tianrui Guan,
Fanlian Zeng, Ka Nam Lui, Yuyao Ye, Yitao Liang, et al. Dexgraspvla: A vision-language-
action framework towards general dexterous grasping. In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 40, pages 18836–18844, 2026.
[300] Hao Luo, Yicheng Feng, Wanpeng Zhang, Sipeng Zheng, Ye Wang, Haoqi Yuan, Jiazheng Liu,
Chaoyi Xu, Qin Jin, and Zongqing Lu. Being-h0: Vision-language-action pretraining from
large-scale human videos. In Forty-third International Conference on Machine Learning, 2026.
[301] Gu Zhang, Qicheng Xu, Haozhe Zhang, Jianhan Ma, Long He, Yiming Bao, Zeyu Ping,
Zhecheng Yuan, Chenhao Lu, Chengbo Yuan, et al.
Unidex: A robot foundation suite
for universal dexterous hand control from egocentric human videos. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2026.
[302] Zongzheng Zhang, Jingrui Pang, Zhuo Yang, Kun Li, Minwen Liao, Saining Zhang, Guoxuan
Chi, Jinbang Guo, Huan-ang Gao, Modi Shi, et al. Dexora: Open-source vla for high-dof
bimanual dexterity. In 2026 IEEE International Conference on Robotics and Automation (ICRA),
2026.
[303] Yuanpei Chen, Chen Wang, Yaodong Yang, and Karen Liu. Object-centric dexterous manipu-
lation from human motion data. In Conference on Robot Learning, pages 3828–3846. PMLR,
2025.
[304] Zhao Mandi, Yifan Hou, Dieter Fox, Yashraj Narang, Ajay Mandlekar, and Shuran Song.
Dexmachina: Functional retargeting for bimanual dexterous manipulation. arXiv preprint
arXiv:2505.24853, 2025.
[305] Aditya Kannan, Kenneth Shaw, Shikhar Bahl, Pragna Mannam, and Deepak Pathak. Deft:
Dexterous fine-tuning for hand policies. In Conference on Robot Learning, pages 928–942.
PMLR, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[306] Ananye Agarwal, Shagun Uppal, Kenneth Shaw, and Deepak Pathak. Dexterous functional
grasping. In Conference on Robot Learning, pages 3453–3467. PMLR, 2023.
[307] Sudeep Dasari, Abhinav Gupta, and Vikash Kumar. Learning dexterous manipulation from
exemplar object trajectories and pre-grasps. In 2023 IEEE International Conference on Robotics
and Automation (ICRA), pages 3889–3896. IEEE, 2023.
[308] Xiaoqian Chen, Xiang Zhang, Yiyong Huang, Lu Cao, and Jinguo Liu. A review of soft
manipulator research, applications, and opportunities. Journal of Field Robotics, 39(3):
281–311, 2022.
[309] Yasmin Ansari, Mariangela Manti, Egidio Falotico, Yoan Mollard, Matteo Cianchetti, and
Cecilia Laschi. Towards the development of a soft manipulator as an assistive robot for
personal care of elderly people. International Journal of Advanced Robotic Systems, 14(2):
1729881416687132, 2017.
[310] Thomas George Thuruthel, Egidio Falotico, Mariangela Manti, and Cecilia Laschi. Stable
open loop control of soft robotic manipulators. IEEE Robotics and Automation Letters, 3(2):
1292–1298, 2018.
[311] Wenbo Liu, Youning Duo, Jiaqi Liu, Feiyang Yuan, Lei Li, Luchen Li, Gang Wang, Bohan Chen,
Siqi Wang, Hui Yang, et al. Touchless interactive teaching of soft robots through flexible
bimodal sensory interfaces. Nature communications, 13(1):5030, 2022.
[312] Bryan A Jones and Ian D Walker. Kinematics for multisection continuum robots. IEEE
Transactions on Robotics, 22(1):43–55, 2006.
[313] Chengshi Wang, Chase G Frazelle, John R Wagner, and Ian D Walker. Dynamic control of
multisection three-dimensional continuum manipulators based on virtual discrete-jointed
robot models. IEEE/ASME Transactions on Mechatronics, 26(2):777–788, 2020.
[314] Daniel Bruder, Brent Gillespie, C David Remy, and Ram Vasudevan. Modeling and control of
soft robots using the koopman operator and model predictive control. In Robotics: Science
and Systems, 2019.
[315] Lei Lv, Lei Liu, Lei Bao, Fuchun Sun, Jiahong Dong, Jianwei Zhang, Xuemei Shan, Kai Sun,
Hao Huang, and Yu Luo. Multi-segment soft robot control via deep koopman-based model
predictive control. In 2025 IEEE International Conference on Robotics and Automation (ICRA),
pages 9266–9272. IEEE, 2025.
[316] Amirhossein Kazemipour, Oliver Fischer, Yasunori Toshimitsu, Ki Wan Wong, and Robert K
Katzschmann. Adaptive dynamic sliding mode control of soft continuum manipulators. In
2022 International Conference on Robotics and Automation (ICRA), pages 3259–3265. IEEE,
2022.
[317] Thomas George Thuruthel, Egidio Falotico, Federico Renda, and Cecilia Laschi. Learning
dynamic models for open loop predictive control of soft robotic manipulators. Bioinspiration
& biomimetics, 12(6):066003, 2017.
[318] Xuanke You, Yixiao Zhang, Xiaotong Chen, Xinghua Liu, Zhanchi Wang, Hao Jiang, and
Xiaoping Chen. Model-free control for soft manipulators based on reinforcement learning.
In 2017 IEEE/RSJ international conference on intelligent robots and systems (IROS), pages
2909–2915. IEEE, 2017.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[319] Andrea Centurelli, Luca Arleo, Alessandro Rizzo, Silvia Tolu, Cecilia Laschi, and Egidio
Falotico.
Closed-loop dynamic control of a soft manipulator using deep reinforcement
learning. IEEE Robotics and Automation Letters, 7(2):4741–4748, 2022.
[320] Kunyu Zhou, Baijin Mao, Yuzhu Zhang, Yaozhen Chen, Yuyaocen Xiang, Zhenping Yu,
Hongwei Hao, Wei Tang, Yanwen Li, Houde Liu, et al. A cable-actuated soft manipulator for
dexterous grasping based on deep reinforcement learning. Advanced Intelligent Systems, 6
(10):2400112, 2024.
[321] Jose Sanchez, Juan-Antonio Corrales, Belhassen-Chedli Bouzgarrou, and Youcef Mezouar.
Robotic manipulation and sensing of deformable objects in domestic and industrial applica-
tions: a survey. The International Journal of Robotics Research, 37(7):688–716, 2018.
[322] Feida Gu, Yanmin Zhou, Zhipeng Wang, Shuo Jiang, and Bin He. A survey on robotic
manipulation of deformable objects: Recent advances, open challenges and new frontiers.
arXiv preprint arXiv:2312.10419, 2023.
[323] Mitul Saha and Pekka Isto. Manipulation planning for deformable linear objects. IEEE
Transactions on Robotics, 23(6):1141–1150, 2007.
[324] Adrià Luque, David Parent, Adrià Colomé, Carlos Ocampo-Martinez, and Carme Torras. Model
predictive control for dynamic cloth manipulation: Parameter learning and experimental
validation. IEEE Transactions on Control Systems Technology, 32(4):1254–1270, 2024.
[325] Haochen Shi, Huazhe Xu, Samuel Clarke, Yunzhu Li, and Jiajun Wu. Robocook: Long-horizon
elasto-plastic object manipulation with diverse tools. In Conference on Robot Learning, pages
642–660. PMLR, 2023.
[326] Vainavi Viswanath, Kaushik Shivakumar, Mallika Parulekar, Jainil Ajmera, Justin Kerr, Jeffrey
Ichnowski, Richard Cheng, Thomas Kollar, and Ken Goldberg. Handloom: Learned tracing of
one-dimensional objects for inspection and manipulation. In Conference on Robot Learning,
pages 341–357. PMLR, 2023.
[327] Zehang Weng, Peng Zhou, Hang Yin, Alexander Kravberg, Anastasiia Varava, David Navarro-
Alarcon, and Danica Kragic. Interactive perception for deformable object manipulation. IEEE
Robotics and Automation Letters, 2024.
[328] Feng Luan, Shaoqiang Meng, Zhipeng Wang, Yanchao Dong, Yanmin Zhou, Bin He, et al.
Learning efficient robotic garment manipulation with standardization. In Forty-second Inter-
national Conference on Machine Learning, 2025.
[329] Bao Thach, Tanner Watts, Shing-Hei Ho, Tucker Hermans, and Alan Kuntz. Defgoalnet:
Contextual goal learning from demonstrations for deformable object manipulation. In 2024
IEEE International Conference on Robotics and Automation (ICRA), pages 3145–3152. IEEE,
2024.
[330] Paul Maria Scheikl, Nicolas Schreiber, Christoph Haas, Niklas Freymuth, Gerhard Neumann,
Rudolf Lioutikov, and Franziska Mathis-Ullrich. Movement primitive diffusion: Learning
gentle robotic manipulation of deformable objects. IEEE Robotics and Automation Letters, 9
(6):5338–5345, 2024.
[331] Bardienus P Duisterhof, Zhao Mandi, Yunchao Yao, Jia-Wei Liu, Jenny Seidenschwarz,
Mike Zheng Shou, Deva Ramanan, Shuran Song, Stan Birchfield, Bowen Wen, et al. Deformgs:
Scene flow in highly deformable scenes for deformable object manipulation. Workshop on
The Algorithmic Foundations OF Robotics, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[332] Ruihai Wu, Chuanruo Ning, and Hao Dong. Learning foresightful dense visual affordance for
deformable object manipulation. In Proceedings of the IEEE/CVF International Conference on
Computer Vision, pages 10947–10956, 2023.
[333] Yuhong Deng, Kai Mo, Chongkun Xia, and Xueqian Wang. Learning language-conditioned
deformable object manipulation with graph dynamics. In 2024 IEEE International Conference
on Robotics and Automation (ICRA), pages 7508–7514. IEEE, 2024.
[334] Alessio Caporali, Piotr Kicki, Kevin Galassi, Riccardo Zanella, Krzysztof Walas, and Gianluca
Palli. Deformable linear objects manipulation with online model parameters estimation. IEEE
Robotics and Automation Letters, 9(3):2598–2605, 2024.
[335] So Kuroki, Jiaxian Guo, Tatsuya Matsushima, Takuya Okubo, Masato Kobayashi, Yuya Ikeda,
Ryosuke Takanami, Paul Yoo, Yutaka Matsuo, and Yusuke Iwasawa. Gendom: Generaliz-
able one-shot deformable object manipulation with parameter-aware policy. In 2024 IEEE
International Conference on Robotics and Automation (ICRA), pages 14792–14799. IEEE, 2024.
[336] Chenchang Li, Zihao Ai, Tong Wu, Xiaosa Li, Wenbo Ding, and Huazhe Xu. Deformnet:
Latent space modeling and dynamics prediction for deformable object manipulation. In 2024
IEEE International Conference on Robotics and Automation (ICRA), pages 14770–14776. IEEE,
2024.
[337] Dominik Bauer, Zhenjia Xu, and Shuran Song. Doughnet: A visual predictive model for
topological manipulation of deformable objects. In European Conference on Computer Vision,
pages 92–108. Springer, 2024.
[338] Robert Holmberg and Oussama Khatib. Development and control of a holonomic mobile
robot for mobile manipulation tasks. The International Journal of Robotics Research, 19(11):
1066–1074, 2000.
[339] Paul Hebert, Max Bajracharya, Jeremy Ma, Nicolas Hudson, Alper Aydemir, Jason Reid,
Charles Bergh, James Borders, Matthew Frost, Michael Hagman, et al. Mobile manipulation
and mobility as manipulation—design and algorithms of robosimian. Journal of Field Robotics,
32(2):255–274, 2015.
[340] Dmitry Berenson, James Kuffner, and Howie Choset. An optimization approach to planning
for mobile manipulation. In 2008 IEEE International Conference on Robotics and Automation,
pages 1187–1192. IEEE, 2008.
[341] Sachin Chitta, E Gil Jones, Matei Ciocarlie, and Kaijen Hsiao. Mobile manipulation in
unstructured environments: Perception, planning, and execution. IEEE Robotics & Automation
Magazine, 19(2):58–71, 2012.
[342] Johannes Pankert and Marco Hutter. Perceptive model predictive control for continuous
mobile manipulation. IEEE Robotics and Automation Letters, 5(4):6177–6184, 2020.
[343] Jimmy Wu, William Chong, Robert Holmberg, Aaditya Prasad, Yihuai Gao, Oussama Khatib,
Shuran Song, Szymon Rusinkiewicz, and Jeannette Bohg. Tidybot++: An open-source
holonomic mobile manipulator for robot learning. In Conference on Robot Learning, pages
3729–3741. PMLR, 2025.
[344] Priya Sundaresan, Rhea Malhotra, Phillip Miao, Jingyun Yang, Jimmy Wu, Hengyuan Hu,
Rika Antonova, Francis Engelmann, Dorsa Sadigh, and Jeannette Bohg. Homer: Learning
in-the-wild mobile manipulation via hybrid imitation and whole-body control. arXiv preprint
arXiv:2506.01185, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[345] Cong Wang, Qifeng Zhang, Qiyan Tian, Shuo Li, Xiaohui Wang, David Lane, Yvan Petillot,
and Sen Wang. Learning mobile manipulation through deep reinforcement learning. Sensors,
20(3):939, 2020.
[346] Ruihan Yang, Yejin Kim, Rose Hendrix, Aniruddha Kembhavi, Xiaolong Wang, and Kiana
Ehsani. Harmonic mobile manipulation. In 2024 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 3658–3665. IEEE, 2024.
[347] Daniel Honerkamp, Tim Welschehold, and Abhinav Valada. Learning kinematic feasibility for
mobile manipulation through deep reinforcement learning. IEEE Robotics and Automation
Letters, 6(4):6289–6296, 2021.
[348] Wang Zhicheng, Satoshi Yagi, Satoshi Yamamori, and Jun Morimoto. Object-centric mo-
bile manipulation through sam2-guided perception and imitation learning. arXiv preprint
arXiv:2507.10899, 2025.
[349] Daniel Honerkamp, Martin Büchner, Fabien Despinoy, Tim Welschehold, and Abhinav Val-
ada. Language-grounded dynamic scene graphs for interactive object search with mobile
manipulation. IEEE Robotics and Automation Letters, 2024.
[350] Krishan Rana, Jesse Haviland, Sourav Garg, Jad Abou-Chakra, Ian Reid, and Niko Suender-
hauf. Sayplan: Grounding large language models using 3d scene graphs for scalable robot
task planning. In Conference on Robot Learning, pages 23–72. PMLR, 2023.
[351] Snehal Jauhri, Sophie Lueth, and Georgia Chalvatzaki. Active-perceptive motion generation
for mobile manipulation. In 2024 IEEE International Conference on Robotics and Automation
(ICRA), pages 1413–1419. IEEE, 2024.
[352] Jiawei Hou, Tianyu Wang, Tongying Pan, Shouyan Wang, Xiangyang Xue, and Yanwei Fu.
Tamma: Target-driven multi-subscene mobile manipulation. In Conference on Robot Learning,
pages 4119–4140. PMLR, 2025.
[353] Matei Ciocarlie, Kaijen Hsiao, Adam Leeper, and David Gossow. Mobile manipulation through
an assistive home robot. In 2012 IEEE/RSJ International Conference on Intelligent Robots and
Systems, pages 5313–5320. IEEE, 2012.
[354] Anxing Xiao, Nuwan Janaka, Tianrun Hu, Anshul Gupta, Kaixin Li, Cunjun Yu, and David
Hsu. Robi butler: Multimodal remote interaction with a household robot assistant. In 2025
IEEE International Conference on Robotics and Automation, 2025.
[355] Jesse Haviland, Niko Sünderhauf, and Peter Corke. A holistic approach to reactive mobile
manipulation. IEEE Robotics and Automation Letters, 7(2):3122–3129, 2022.
[356] Ben Burgess-Limerick, Chris Lehnert, Jurgen Leitner, and Peter Corke. An architecture for
reactive mobile manipulation on-the-move. In IEEE International Conference on Robotics and
Automation 2023, pages 1623–1629. IEEE, Institute of Electrical and Electronics Engineers,
2023.
[357] Seunghun Jeon, Moonkyu Jung, Suyoung Choi, Beomjoon Kim, and Jemin Hwangbo. Learn-
ing whole-body manipulation for quadrupedal robot. IEEE Robotics and Automation Letters, 9
(1):699–706, 2023.
[358] Xiaoyu Huang, Qiayuan Liao, Yiming Ni, Zhongyu Li, Laura Smith, Sergey Levine, Xue Bin
Peng, and Koushil Sreenath. Hilma-res: A general hierarchical framework via residual rl
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
for combining quadrupedal locomotion and manipulation. In 2024 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 9050–9057. IEEE, 2024.
[359] Yutao Ouyang, Jinhan Li, Yunfei Li, Zhongyu Li, Chao Yu, Koushil Sreenath, and Yi Wu.
Long-horizon locomotion and manipulation on a quadrupedal robot with large language
models. In 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS),
pages 11157–11164. IEEE, 2025.
[360] Han Zhao, Wenxuan Song, Donglin Wang, Xinyang Tong, Pengxiang Ding, Xuelian Cheng, and
Zongyuan Ge. More: Unlocking scalability in reinforcement learning for quadruped vision-
language-action models. In 2025 IEEE international conference on robotics and automation
(ICRA), 2025.
[361] Xuxin Cheng, Ashish Kumar, and Deepak Pathak. Legs as manipulator: Pushing quadrupedal
agility beyond locomotion. In 2023 IEEE International Conference on Robotics and Automation
(ICRA), pages 5106–5112. IEEE, 2023.
[362] Philip Arm, Mayank Mittal, Hendrik Kolvenbach, and Marco Hutter. Pedipulate: Enabling
manipulation skills using a quadruped robot’s leg. In 2024 IEEE International Conference on
Robotics and Automation (ICRA), pages 5717–5723. IEEE, 2024.
[363] Wouter J Wolfslag, Christopher McGreavy, Guiyang Xin, Carlo Tiseo, Sethu Vijayakumar,
and Zhibin Li. Optimisation of body-ground contact for augmenting the whole-body loco-
manipulation of quadruped robots. In 2020 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 3694–3701. IEEE, 2020.
[364] Zipeng Fu, Xuxin Cheng, and Deepak Pathak. Deep whole-body control: learning a unified
policy for manipulation and locomotion. In Conference on Robot Learning, pages 138–149.
PMLR, 2023.
[365] Elena Arcari, Maria Vittoria Minniti, Anna Scampicchio, Andrea Carron, Farbod Farshidian,
Marco Hutter, and Melanie N Zeilinger. Bayesian multi-task learning mpc for robotic mobile
manipulation. IEEE Robotics and Automation Letters, 8(6):3222–3229, 2023.
[366] Henrique Ferrolho, Vladimir Ivan, Wolfgang Merkt, Ioannis Havoutis, and Sethu Vijayakumar.
Roloma: Robust loco-manipulation for quadruped robots with arms. Autonomous Robots, 47
(8):1463–1481, 2023.
[367] Naoki Yokoyama, Alex Clegg, Joanne Truong, Eric Undersander, Tsung-Yen Yang, Sergio
Arnaud, Sehoon Ha, Dhruv Batra, and Akshara Rai. Asc: Adaptive skill coordination for
robotic mobile manipulation. IEEE Robotics and Automation Letters, 9(1):779–786, 2023.
[368] Ri-Zhao Qiu, Yafei Hu, Yuchen Song, Ge Yang, Yang Fu, Jianglong Ye, Jiteng Mu, Ruihan
Yang, Nikolay Atanasov, Sebastian Scherer, et al. Learning generalizable feature fields for
mobile manipulation. In 2025 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), 2025.
[369] Russell Mendonca, Emmanuel Panov, Bernadette Bucher, Jiuguang Wang, and Deepak Pathak.
Continuously improving mobile manipulation with autonomous real-world rl. In Conference
on Robot Learning, pages 5204–5219. PMLR, 2025.
[370] Kaiwen Jiang, Zhen Fu, Junde Guo, Wei Zhang, and Hua Chen. Learning whole-body
loco-manipulation for omni-directional task space pose tracking with a wheeled-quadrupedal-
manipulator. IEEE Robotics and Automation Letters, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[371] Jilong Wang, Javokhirbek Rajabov, Chaoyi Xu, Yiming Zheng, and He Wang. Quadwbg:
Generalizable quadrupedal whole-body grasping. 2025 IEEE International Conference on
Robotics and Automation (ICRA), 2025.
[372] Guoping Pan, Qingwei Ben, Zhecheng Yuan, Guangqi Jiang, Yandong Ji, Shoujie Li, Jiangmiao
Pang, Houde Liu, and Huazhe Xu. Roboduet: Learning a cooperative policy for whole-body
legged loco-manipulation. IEEE Robotics and Automation Letters, 2025.
[373] Peiyuan Zhi, Peiyang Li, Jianqin Yin, Baoxiong Jia, and Siyuan Huang. Learning unified force
and position control for legged loco-manipulation. In Conference on Robot Learning, 2025.
[374] Dianyong Hou, Chengrui Zhu, Zhen Zhang, Zhibin Li, Chuang Guo, and Yong Liu. Efficient
learning of a unified policy for whole-body manipulation and locomotion skills. In 2025
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 5455–5461.
IEEE, 2025.
[375] Changyi Lin, Xingyu Liu, Yuxiang Yang, Yaru Niu, Wenhao Yu, Tingnan Zhang, Jie Tan,
Byron Boots, and Ding Zhao. Locoman: Advancing versatile quadrupedal dexterity with
lightweight loco-manipulators. In 2024 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 6877–6884. IEEE, 2024.
[376] Haichao Zhang, Haonan Yu, Le Zhao, Andrew Choi, Qinxun Bai, Yiqing Yang, and Wei Xu.
Learning multi-stage pick-and-place with a legged mobile manipulator. IEEE Robotics and
Automation Letters, 2025.
[377] Xinrong Yang, Peizhuo Li, Hongyi Li, Junkai Lu, Linnan Chang, Yuhong Cao, Yifeng Zhang,
Ge Sun, and Guillaume Sartoretti.
Helom: Hierarchical learning for whole-body loco-
manipulation in hexapod robot. In The Fourteenth International Conference on Learning
Representations, 2026.
[378] Xinyang Tong, Pengxiang Ding, Yiguo Fan, Donglin Wang, Wenjie Zhang, Can Cui, Mingyang
Sun, Han Zhao, Hongyin Zhang, Yonghao Dang, et al. Quart-online: Latency-free large
multimodal language model for quadruped robot learning. In 2025 IEEE International
Conference on Robotics and Automation (ICRA), 2025.
[379] Zipeng Fu, Qingqing Zhao, Qi Wu, Gordon Wetzstein, and Chelsea Finn.
Humanplus:
Humanoid shadowing and imitation from humans. In Conference on Robot Learning, pages
2828–2844. PMLR, 2025.
[380] Guang Gao, Jianan Wang, Jinbo Zuo, Junnan Jiang, Jingfan Zhang, Xianwen Zeng, Yuejiang
Zhu, Lianyang Ma, Ke Chen, Minhua Sheng, et al. Towards human-level intelligence via
human-like whole-body manipulation. arXiv preprint arXiv:2507.17141, 2025.
[381] Ri-Zhao Qiu, Shiqi Yang, Xuxin Cheng, Chaitanya Chawla, Jialong Li, Tairan He, Ge Yan,
David J Yoon, Ryan Hoque, Lars Paulsen, et al. Humanoid policy human policy. In Conference
on Robot Learning, pages 2888–2906. PMLR, 2025.
[382] Jiacheng Liu, Pengxiang Ding, Qihang Zhou, Yuxuan Wu, Da Huang, Zimian Peng, Wei Xiao,
Weinan Zhang, Lixin Yang, Cewu Lu, et al. Trajbooster: Boosting humanoid whole-body
manipulation via trajectory-centric learning. In 2026 IEEE International Conference on Robotics
and Automation (ICRA), 2026.
[383] Kensuke Harada, Shuuji Kajita, Kenji Kaneko, and Hirohisa Hirukawa. Dynamics and balance
of a humanoid robot during manipulation tasks. IEEE Transactions on Robotics, 22(3):568–575,
2006.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[384] Karim Bouyarmane and Abderrahmane Kheddar. Humanoid robot locomotion and manipula-
tion step planning. Advanced Robotics, 26(10):1099–1126, 2012.
[385] Jinhan Li, Yifeng Zhu, Yuqi Xie, Zhenyu Jiang, Mingyo Seo, Georgios Pavlakos, and Yuke
Zhu. Okami: Teaching humanoid robots manipulation skills through single video imitation.
In Conference on Robot Learning, pages 299–317. PMLR, 2025.
[386] Lujie Yang, Xiaoyu Huang, Zhen Wu, Angjoo Kanazawa, Pieter Abbeel, Carmelo Sferrazza,
C Karen Liu, Rocky Duan, and Guanya Shi. Omniretarget: Interaction-preserving data
generation for humanoid whole-body loco-manipulation and scene interaction. In 2026 IEEE
International Conference on Robotics and Automation (ICRA), 2026.
[387] Mingyo Seo, Steve Han, Kyutae Sim, Seung Hyeon Bang, Carlos Gonzalez, Luis Sentis, and
Yuke Zhu. Deep imitation learning for humanoid loco-manipulation through human teleop-
eration. In 2023 IEEE-RAS 22nd International Conference on Humanoid Robots (Humanoids),
pages 1–8. IEEE, 2023.
[388] Masaki Murooka, Takahiro Hoshi, Kensuke Fukumitsu, Shimpei Masuda, Marwan Hamze,
Tomoya Sasaki, Mitsuharu Morisawa, and Eiichi Yoshida. Tact: Humanoid whole-body
contact manipulation through deep imitation learning with tactile modality. IEEE Robotics
and Automation Letters, 2025.
[389] Yuhui Fu, Feiyang Xie, Chaoyi Xu, Jing Xiong, Haoqi Yuan, and Zongqing Lu. Demohlm:
From one demonstration to generalizable humanoid loco-manipulation. IEEE Robotics and
Automation Letters, 2026.
[390] Rutav Shah, Shuijing Liu, Qi Wang, Zhenyu Jiang, Sateesh Kumar, Mingyo Seo, Roberto
Martín-Martín, and Yuke Zhu. Mimicdroid: In-context learning for humanoid robot ma-
nipulation from human play videos. In 2026 IEEE International Conference on Robotics and
Automation (ICRA), 2026.
[391] Xinyu Xu, Yizheng Zhang, Yong-Lu Li, Lei Han, and Cewu Lu. Humanvla: Towards vision-
language directed object rearrangement by physical humanoid. Advances in Neural Information
Processing Systems, 37:18633–18659, 2024.
[392] Haoran Jiang, Jin Chen, Qingwen Bu, Li Chen, Modi Shi, Yanjie Zhang, Delong Li, Chuanzhe
Suo, Chuang Wang, Zhihui Peng, et al. Wholebodyvla: Towards unified latent vla for whole-
body loco-manipulation control. In The Fourteenth International Conference on Learning
Representations, 2026.
[393] Songlin Wei, Hongyi Jing, Boqian Li, Zhenyu Zhao, Jiageng Mao, Zhenhao Ni, Sicheng He,
Jie Liu, Xiawei Liu, Kaidi Kang, et al. Ψ0: An open foundation model towards universal
humanoid loco-manipulation. In Robotics: Science and Systems, 2026.
[394] Shuanghao Bai, Meng Li, Xinyuan Lv, Jiawei Wang, Xinhua Wang, Fei Liao, Chengkai
Hou, Langzhe Gu, Wanqi Zhou, Kun Wu, et al. Hex: Humanoid-aligned experts for cross-
embodiment whole-body manipulation. arXiv preprint arXiv:2604.07993, 2026.
[395] Yingdong Hu, Haodong Zhu, Boyuan Zheng, Yihang Hu, Tong Zhang, Zunhao Chen, Junming
Zhao, Ruiqian Nai, and Yang Gao. Openhlm: An empirical recipe for whole-body humanoid
loco-manipulation. arXiv preprint arXiv:2606.22174, 2026.
[396] Jia Zheng, Teli Ma, Yudong Fan, Zifan Wang, Shuo Yang, and Junwei Liang. Motionwam:
Towards foundation world action models for real-time humanoid loco-manipulation. arXiv
preprint arXiv:2606.09215, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[397] Jiawei Gao, Ziqin Wang, Zeqi Xiao, Jingbo Wang, Tai Wang, Jinkun Cao, Xiaolin Hu, Si Liu,
Jifeng Dai, and Jiangmiao Pang. Coohoi: Learning cooperative human-object interaction
with manipulated object dynamics. Advances in Neural Information Processing Systems, 37:
79741–79763, 2024.
[398] Toru Lin, Kartik Sachdev, Linxi Fan, Jitendra Malik, and Yuke Zhu. Sim-to-real reinforcement
learning for vision-based dexterous manipulation on humanoids. In Conference on Robot
Learning, pages 4926–4940. PMLR, 2025.
[399] Johnathan Tucker, Denis Liu, Aiden Swann, Allen Ren, Javier Yu, Jiankai Sun, Brandon Kim,
Lachlain McGranahan, Quan Vuong, and Mac Schwager. 𝜋, but make it fly: Physics-guided
transfer of vla models to aerial manipulation. arXiv preprint arXiv:2603.25038, 2026.
[400] Jianli Sun, Bin Tian, Qiyao Zhang, Chengxiang Li, Zihan Song, Zhiyong Cui, Yisheng Lv, and
Yonglin Tian. Air-vla: Vision-language-action systems for aerial manipulation. arXiv preprint
arXiv:2601.21602, 2026.
[401] Guanqi He, Xiaofeng Guo, Luyi Tang, Yuanhang Zhang, Mohammadreza Mousaei, Jiahe Xu,
Junyi Geng, Sebastian Scherer, and Guanya Shi. Flying hand: End-effector-centric framework
for versatile aerial manipulation teleoperation and policy learning. In Robotics: Science and
Systems, 2025.
[402] Paul EI Pounds, Daniel R Bersak, and Aaron M Dollar. Grasping from the air: Hovering
capture and load stability. In 2011 IEEE international conference on robotics and automation,
pages 2491–2498. IEEE, 2011.
[403] Suseong Kim, Seungwon Choi, and H Jin Kim. Aerial manipulation using a quadrotor with
a two dof robotic arm. In 2013 IEEE/RSJ International Conference on Intelligent Robots and
Systems, pages 4990–4995. IEEE, 2013.
[404] Matko Orsag, Christopher Korpela, Stjepan Bogdan, and Paul Oh.
Dexterous aerial
robots—mobile manipulation using unmanned aerial systems. IEEE Transactions on Robotics,
33(6):1453–1466, 2017.
[405] Dongjae Lee, Byeongjun Kim, and Hyoun Jin Kim. Autonomous aerial manipulation at
arbitrary pose in se (3) with robust control and whole-body planning. The International
Journal of Robotics Research, 45(7):1021–1045, 2026.
[406] Biyu Ye, Na Fan, Zhengping Fan, Weiliang Deng, Hongming Chen, Qifeng Chen, and Ximin
Lyu. Flyaware: Inertia-aware aerial manipulation via vision-based estimation and post-grasp
adaptation. arXiv preprint arXiv:2601.22686, 2026.
[407] Cora A Dimmig and Marin Kobilarov. Non-prehensile aerial manipulation using model-based
deep reinforcement learning. In 2024 IEEE 20th International Conference on Automation
Science and Engineering (CASE), pages 2194–2200. IEEE, 2024.
[408] Ziken Huang, Xinze Niu, Bowen Chai, Renbiao Jin, and Danping Zou. Swooper: Learning
high-speed aerial grasping with a simple gripper. IEEE Robotics and Automation Letters, 11
(2):2298–2305, 2026.
[409] Claudio Zito and Eliseo Ferrante. One-shot learning for autonomous aerial manipulation.
Frontiers in Robotics and AI, 9:960571, 2022.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[410] Jianli Sun, Bin Tian, Qiyao Zhang, Zijian Liu, Yutong Wang, Zhiyong Cui, Bai Li, Yisheng Lv,
and Yonglin Tian. Air-vla+: Decoupling movement and manipulation via cascaded dual-action
decoders with asymmetric moe for aerial robots. arXiv preprint arXiv:2606.12859, 2026.
[411] Enrico Simetti, Giuseppe Casalino, Sandro Torelli, Alessandro Sperinde, and Alessio Turetta.
Floating underwater manipulation: Developed control methodology and experimental vali-
dation within the trident project. Journal of Field Robotics, 31(3):364–385, 2014.
[412] Oussama Khatib, Xiyang Yeh, Gerald Brantner, Brian Soe, Boyeon Kim, Shameek Ganguly,
Hannah Stuart, Shiquan Wang, Mark Cutkosky, Aaron Edsinger, et al. Ocean one: A robotic
avatar for oceanic discovery. IEEE Robotics & Automation Magazine, 23(4):20–29, 2016.
[413] Gerald Brantner and Oussama Khatib. Controlling ocean one: Human–robot collaboration
for deep-sea manipulation. Journal of Field Robotics, 38(1):28–51, 2021.
[414] Jeremi Gancet, Diego Urbina, Pierre Letier, Michel Ilzkovitz, Peter Weiss, Fred Gauch, Bertrand
Chemisky, Gianluca Antonelli, Giuseppe Casalino, Giovanni Indiveri, et al. Dexrov: Enabling
effective dexterous rov operations in presence of communication latency. In OCEANS 2015-
Genova, pages 1–6. IEEE, 2015.
[415] Kohei Nishi, Masato Kobayashi, and Yuki Uranishi. Mr-ubi: Mixed reality-based underwater
robot arm teleoperation system with reaction torque indicator via bilateral control. IEEE
Access, 2026.
[416] Ignacio Carlucho, Mariano De Paula, Corina Barbalata, and Gerardo G Acosta. A reinforcement
learning control approach for underwater manipulation under position and torque constraints.
In Global oceans 2020: Singapore–US gulf coast, pages 1–7. IEEE, 2020.
[417] Ruoshi Liu, Huy Ha, Mengxue Hou, Shuran Song, and Carl Vondrick. Self-improving au-
tonomous underwater manipulation. In 2025 IEEE International Conference on Robotics and
Automation (ICRA), pages 16915–16922. IEEE, 2025.
[418] Takeru Tsunoori, Masato Kobayashi, and Yuki Uranishi. Bi-aqua: Bilateral control-based imita-
tion learning for underwater robot arms via lighting-aware action chunking with transformers.
arXiv preprint arXiv:2511.16050, 2025.
[419] Hao Li, Long Yin Chung, Jack Goler, Ryan Zhang, Xiaochi Xie, Huy Ha, Shuran Song, and
Mark Cutkosky. Umi-underwater: Learning underwater manipulation without underwater
teleoperation. arXiv preprint arXiv:2603.27012, 2026.
[420] Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel
Ho, Julian Ibarz, Alex Irpan, Eric Jang, Ryan Julian, et al. Do as i can, not as i say: Grounding
language in robotic affordances. In Conference on robot learning, pages 287–318. PMLR,
2023.
[421] Wenlong Huang, Fei Xia, Dhruv Shah, Danny Driess, Andy Zeng, Yao Lu, Pete Florence,
Igor Mordatch, Sergey Levine, Karol Hausman, et al. Grounded decoding: Guiding text
generation with grounded models for embodied agents. Advances in Neural Information
Processing Systems, 36:59636–59661, 2023.
[422] Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng,
Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, et al. Inner monologue: Embodied
reasoning through planning with language models. arXiv preprint arXiv:2207.05608, 2022.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[423] Chan Hee Song, Jiaman Wu, Clayton Washington, Brian M Sadler, Wei-Lun Chao, and Yu Su.
Llm-planner: Few-shot grounded planning for embodied agents with large language models.
In Proceedings of the IEEE/CVF international conference on computer vision, pages 2998–3009,
2023.
[424] Tianyu Wang, Haitao Lin, Junqiu Yu, and Yanwei Fu. Polaris: Open-ended interactive robotic
manipulation via syn2real visual grounding and large language models. In 2024 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 9676–9683. IEEE,
2024.
[425] Bo Liu, Yuqian Jiang, Xiaohan Zhang, Qiang Liu, Shiqi Zhang, Joydeep Biswas, and Peter
Stone. Llm+ p: Empowering large language models with optimal planning proficiency. arXiv
preprint arXiv:2304.11477, 2023.
[426] Shu Wang, Muzhi Han, Ziyuan Jiao, Zeyu Zhang, Ying Nian Wu, Song-Chun Zhu, and
Hangxin Liu. Llm^ 3: Large language model-based task and motion planning with motion
failure reasoning. In 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS), pages 12086–12092. IEEE, 2024.
[427] Zeyi Liu, Arpit Bahety, and Shuran Song. Reflect: Summarizing robot experiences for failure
explanation and correction. In Conference on Robot Learning, pages 3468–3484. PMLR, 2023.
[428] Huaxiaoyue Wang, Nathaniel Chin, Gonzalo Gonzalez-Pumariega, Xiangwan Sun, Neha
Sunkara, Maximus Adrian Pace, Jeannette Bohg, and Sanjiban Choudhury. Apricot: Active
preference learning and constraint-aware task planning with llms. In Proceedings of The 8th
Conference on Robot Learning, volume 270, pages 1590–1642. PMLR, 2025.
[429] Harsh Singh, Rocktim Jyoti Das, Mingfei Han, Preslav Nakov, and Ivan Laptev. Malmm:
Multi-agent large language models for zero-shot robotics manipulation.
arXiv preprint
arXiv:2411.17636, 2024.
[430] Zhao Mandi, Shreeya Jain, and Shuran Song. Roco: Dialectic multi-robot collaboration with
large language models. In 2024 IEEE International Conference on Robotics and Automation
(ICRA), pages 286–299. IEEE, 2024.
[431] Yilun Du, Sherry Yang, Pete Florence, Fei Xia, Ayzaan Wahid, Pierre Sermanet, Tianhe Yu,
Pieter Abbeel, Joshua B Tenenbaum, Leslie Pack Kaelbling, et al. Video language planning.
In The Twelfth International Conference on Learning Representations, 2024.
[432] Jensen Gao, Bidipta Sarkar, Fei Xia, Ted Xiao, Jiajun Wu, Brian Ichter, Anirudha Majumdar,
and Dorsa Sadigh. Physically grounded vision-language models for robotic manipulation. In
2024 IEEE International Conference on Robotics and Automation (ICRA), pages 12462–12469.
IEEE, 2024.
[433] Qiang Guan, Shiguang Wu, Dafeng Chi, Yuzheng Zhuang, Xingyue Quan, Jianye Hao,
et al. Evlp: Learning unified embodied vision-language planner with reinforced supervised
fine-tuning. In International Conference on Learning Representations, volume 2026, pages
73160–73182, 2026.
[434] Yao Mu, Qinglong Zhang, Mengkang Hu, Wenhai Wang, Mingyu Ding, Jun Jin, Bin Wang,
Jifeng Dai, Yu Qiao, and Ping Luo. Embodiedgpt: Vision-language pre-training via embodied
chain of thought. Advances in Neural Information Processing Systems, 36:25081–25094, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[435] Boyuan Chen, Zhuo Xu, Sean Kirmani, Brian Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei
Xia. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
14455–14465, 2024.
[436] Wenxiao Cai, Iaroslav Ponomarenko, Jianhao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and
Bo Zhao. Spatialbot: Precise spatial understanding with vision language models. 2025 IEEE
International Conference on Robotics and Automation (ICRA), 2025.
[437] Chan Hee Song, Valts Blukis, Jonathan Tremblay, Stephen Tyree, Yu Su, and Stan Birchfield.
Robospatial: Teaching spatial understanding to 2d and 3d vision-language models for robotics.
In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 15768–15780,
2025.
[438] Yi Zhang, Qiang Zhang, Xiaozhu Ju, Zhaoyang Liu, Jilei Mao, Jingkai Sun, Jintao Wu,
Shixiong Gao, Shihan Cai, Zhiyuan Qin, et al. Embodiedvsr: Dynamic scene graph-guided
chain-of-thought reasoning for visual spatial tasks. arXiv preprint arXiv:2503.11089, 2025.
[439] Zekun Qi, Wenyao Zhang, Yufei Ding, Runpei Dong, Xinqiang Yu, Jingwen Li, Lingyun Xu,
Baoyu Li, Xialin He, Guofan Fan, et al. Sofar: Language-grounded orientation bridges spatial
reasoning and object manipulation. Advances in neural information processing systems, 38:
76367–76412, 2025.
[440] Huajie Tan, Sixiang Chen, Yijie Xu, Zixiao Wang, Yuheng Ji, Cheng Chi, Yaoxu Lyu, Zhongxia
Zhao, Xiansheng Chen, Peterson Co, et al. Robo-dopamine: General process reward modeling
for high-precision robotic manipulation. In 2026 IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR), 2026.
[441] Tony Lee, Andrew Wagenmaker, Karl Pertsch, Percy Liang, Sergey Levine, and Chelsea Finn.
Roboreward: General-purpose vision-language reward models for robotics. arXiv preprint
arXiv:2601.00675, 2026.
[442] Anthony Liang, Yigit Korkmaz, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant
Kaushik, Aditya Shah, Alex S Huang, Luke Zettlemoyer, Dieter Fox, et al.
Robometer:
Scaling general-purpose robotic reward models via trajectory comparisons. arXiv preprint
arXiv:2603.02115, 2026.
[443] Youhe Feng, Hansen Shi, Haoyang Li, Xinlei Guo, Yang Wang, Chengyang Zhang, Jinkai
Zhang, Xiaohan Zhang, Jie Tang, and Jing Zhang. Procvlm: Learning procedure-grounded
progress rewards for robotic manipulation. arXiv preprint arXiv:2605.08774, 2026.
[444] Jiafei Duan, Wilbert Pumacay, Nishanth Kumar, Yi Ru Wang, Shulin Tian, Wentao Yuan,
Ranjay Krishna, Dieter Fox, Ajay Mandlekar, and Yijie Guo. Aha: A vision-language-model for
detecting and reasoning over failures in robotic manipulation. In The Thirteenth International
Conference on Learning Representations, 2025.
[445] Enshen Zhou, Qi Su, Cheng Chi, Zhizheng Zhang, Zhongyuan Wang, Tiejun Huang, Lu Sheng,
and He Wang. Code-as-monitor: Constraint-aware visual programming for reactive and
proactive robotic failure detection. In 2025 IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), pages 6919–6929. IEEE, 2025.
[446] Clémence Grislain, Hamed Rahimi, Olivier Sigaud, and Mohamed Chetouani. I-failsense:
Towards general robotic failure detection with vision-language models. In 2026 IEEE Interna-
tional Conference on Robotics and Automation (ICRA), 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[447] Gehan Zheng, Sanjay Seenivasan, Matthew Johnson-Roberson, and Weiming Zhi. Rewind-
il: Online failure detection and state respawning for imitation learning. arXiv preprint
arXiv:2604.16683, 2026.
[448] Sheng Xu, Ruixing Jin, Huayi Zhou, Bo Yue, Guanren Qiao, Yunxin Tai, Yueci Deng, Kui Jia,
and Guiliang Liu. From reaction to anticipation: Proactive failure recovery through agentic
task graph for robotic manipulation. In Robotics: Science and Systems, 2026.
[449] Yuheng Ji, Huajie Tan, Jiayu Shi, Xiaoshuai Hao, Yuan Zhang, Hengyuan Zhang, Pengwei
Wang, Mengdi Zhao, Yao Mu, Pengju An, et al. Robobrain: A unified brain model for robotic
manipulation from abstract to concrete. In Proceedings of the Computer Vision and Pattern
Recognition Conference, pages 1724–1734, 2025.
[450] BAAI RoboBrain Team, Mingyu Cao, Huajie Tan, Yuheng Ji, Minglan Lin, Zhiyu Li, Zhou Cao,
Pengwei Wang, Enshen Zhou, Yi Han, et al. Robobrain 2.0 technical report. arXiv preprint
arXiv:2507.02029, 2025.
[451] Ronghao Dang, Jiayan Guo, Bohan Hou, Sicong Leng, Kehan Li, Xin Li, Jiangpin Liu, Yunxuan
Mao, Zhikai Wang, Yuqian Yuan, et al. Rynnbrain: Open embodied foundation models. arXiv
preprint arXiv:2602.14979, 2026.
[452] Yifu Yuan, Haiqin Cui, Yibin Chen, Zibin Dong, Fei Ni, Longxin Kou, Jinyi Liu, Pengyi Li, Yan
Zheng, and Jianye Hao. From seeing to doing: Bridging reasoning and decision for robotic
manipulation. In International Conference on Learning Representations, volume 2026, pages
129927–129960, 2026.
[453] Yifu Yuan, Haiqin Cui, Yaoting Huang, Yibin Chen, Fei Ni, Zibin Dong, Pengyi Li, Yan Zheng,
Hongyao Tang, and Jianye Hao. Embodied-r1: Reinforced embodied reasoning for general
robotic manipulation. In International Conference on Learning Representations, volume 2026,
pages 8984–9009, 2026.
[454] Gemini Robotics Team, Saminda Abeyruwan, Joshua Ainslie, Jean-Baptiste Alayrac, Montser-
rat Gonzalez Arenas, Travis Armstrong, Ashwin Balakrishna, Robert Baruch, Maria Bauza,
Michiel Blokzijl, et al. Gemini robotics: Bringing ai into the physical world. arXiv preprint
arXiv:2503.20020, 2025.
[455] Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence,
and Andy Zeng. Code as policies: Language model programs for embodied control. In 2023
IEEE International Conference on Robotics and Automation (ICRA), pages 9493–9500. IEEE,
2023.
[456] Ishika Singh, Valts Blukis, Arsalan Mousavian, Ankit Goyal, Danfei Xu, Jonathan Tremblay,
Dieter Fox, Jesse Thomason, and Animesh Garg. Progprompt: Generating situated robot task
plans using large language models. In 2023 IEEE International Conference on Robotics and
Automation (ICRA), pages 11523–11530. IEEE, 2023.
[457] Sai H Vemprala, Rogerio Bonatti, Arthur Bucker, and Ashish Kapoor. Chatgpt for robotics:
Design principles and model abilities. Ieee Access, 12:55682–55696, 2024.
[458] Siyuan Huang, Zhengkai Jiang, Hao Dong, Yu Qiao, Peng Gao, and Hongsheng Li. Instruct2act:
Mapping multi-modality instructions to robotic actions with large language model. arXiv
preprint arXiv:2305.11176, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[459] Yuki Wang, Gonzalo Gonzalez-Pumariega, Yash Sharma, and Sanjiban Choudhury.
Demo2code: From summarizing demonstrations to synthesizing code via extended chain-
of-thought. In Advances in Neural Information Processing Systems, volume 36, pages 14848–
14956, 2023.
[460] Michael Murray, Abhishek Gupta, and Maya Cakmak. Teaching robots with show and tell:
Using foundation models to synthesize robot policies from language and visual demonstration.
In 8th Annual Conference on Robot Learning, 2024.
[461] Takuma Yoneda, Jiading Fang, Peng Li, Huanyu Zhang, Tianchong Jiang, Shengjie Lin, Ben
Picker, David Yunis, Hongyuan Mei, and Matthew R Walter. Statler: State-maintaining
language models for embodied reasoning. In 2024 IEEE International Conference on Robotics
and Automation (ICRA), pages 15083–15091. IEEE, 2024.
[462] Muzhi Han, Yifeng Zhu, Song-Chun Zhu, Ying Nian Wu, and Yuke Zhu. Interpret: Interactive
predicate learning from language feedback for generalizable task planning. In Robotics:
Science and Systems, 2024.
[463] Sanghyun Ahn, Wonje Choi, Junyong Lee, Jinwoo Park, and Honguk Woo. Towards reliable
code-as-policies: A neuro-symbolic framework for embodied task planning. Advances in
Neural Information Processing Systems, 38:75428–75459, 2026.
[464] Yibin Liu, Zhixuan Liang, Zanxin Chen, Tianxing Chen, Mengkang Hu, Wanxi Dong, Cong-
sheng Xu, Zhaoming Han, Yusen Qin, and Yao Mu. Hycodepolicy: Hybrid language controllers
for multimodal monitoring and decision in embodied agents. arXiv preprint arXiv:2508.02629,
2025.
[465] Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, and Li Fei-Fei. Voxposer:
Composable 3d value maps for robotic manipulation with language models. In Conference on
Robot Learning, pages 540–562. PMLR, 2023.
[466] Shivansh Patel, Xinchen Yin, Wenlong Huang, Shubham Garg, Hooshang Nayyeri, Li Fei-Fei,
Svetlana Lazebnik, and Yunzhu Li. A real-to-sim-to-real approach to robotic manipulation
with vlm-generated iterative keypoint rewards. In 2025 IEEE International Conference on
Robotics and Automation (ICRA), pages 8258–8266. IEEE, 2025.
[467] Haoxu Huang, Fanqi Lin, Yingdong Hu, Shengjie Wang, and Yang Gao. Copa: General robotic
manipulation through spatial constraints of parts with foundation models. In 2024 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 9488–9495. IEEE,
2024.
[468] Wenlong Huang, Chen Wang, Yunzhu Li, Ruohan Zhang, and Li Fei-Fei. Rekep: Spatio-
temporal reasoning of relational keypoint constraints for robotic manipulation. In Conference
on Robot Learning, pages 4573–4602. PMLR, 2025.
[469] Weiliang Tang, Jia-Hui Pan, Yun-Hui Liu, Masayoshi Tomizuka, Li Erran Li, Chi-Wing Fu, and
Mingyu Ding. Geomanip: Geometric constraints as general interfaces for robot manipulation.
arXiv preprint arXiv:2501.09783, 2025.
[470] Bowen Jiang, William Painter Reger, and Roberto Martin-Martin. Codex: Learning composi-
tional dexterous functional manipulation without demonstrations. In 2026 IEEE International
Conference on Robotics and Automation (ICRA), 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[471] Zhenyu Jiang, Cheng-Chun Hsu, and Yuke Zhu. Ditto: Building digital twins of articulated
objects from interaction. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 5616–5626, 2022.
[472] Haoran Geng, Helin Xu, Chengyang Zhao, Chao Xu, Li Yi, Siyuan Huang, and He Wang.
Gapartnet: Cross-category domain-generalizable object perception and manipulation via
generalizable and actionable parts. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 7081–7091, 2023.
[473] Weiyu Liu, Jiayuan Mao, Joy Hsu, Tucker Hermans, Animesh Garg, and Jiajun Wu. Compos-
able part-based manipulation. In Conference on Robot Learning, pages 1300–1315. PMLR,
2023.
[474] Zhanqi Xiao, Ruiping Wang, and Xilin Chen. Robopca: Pose-centered affordance learning
from human demonstrations for robot manipulation. In 2026 IEEE International Conference
on Robotics and Automation (ICRA), 2026.
[475] Andy Zeng, Pete Florence, Jonathan Tompson, Stefan Welker, Jonathan Chien, Maria Attarian,
Travis Armstrong, Ivan Krasin, Dan Duong, Vikas Sindhwani, et al. Transporter networks:
Rearranging the visual world for robotic manipulation. In Conference on Robot Learning,
pages 726–747. PMLR, 2021.
[476] Jessica Borja-Diaz, Oier Mees, Gabriel Kalweit, Lukas Hermann, Joschka Boedecker, and
Wolfram Burgard. Affordance learning from play for sample-efficient policy learning. In 2022
International Conference on Robotics and Automation (ICRA), pages 6372–6378. IEEE, 2022.
[477] Qiyuan Zhuang, He-Yang Xu, Yijun Wang, Xin-Yang Zhao, Yang-Yang Li, and Xiu-Shen Wei.
Raap: Retrieval-augmented affordance prediction with cross-image action alignment. In 2026
IEEE International Conference on Robotics and Automation (ICRA), 2026.
[478] Manuel Lopes, Francisco S Melo, and Luis Montesano. Affordance-based imitation learning
in robots. In 2007 IEEE/RSJ international conference on intelligent robots and systems, pages
1015–1021. IEEE, 2007.
[479] Haoran Geng, Songlin Wei, Congyue Deng, Bokui Shen, He Wang, and Leonidas Guibas.
Sage: Bridging semantic and actionable parts for generalizable manipulation of articulated
objects. In Robotics: Science and Systems, 2024.
[480] Mohit Shridhar, Lucas Manuelli, and Dieter Fox. Cliport: What and where pathways for
robotic manipulation. In Conference on robot learning, pages 894–906. PMLR, 2022.
[481] Xiaoqi Li, Mingxu Zhang, Yiran Geng, Haoran Geng, Yuxing Long, Yan Shen, Renrui Zhang,
Jiaming Liu, and Hao Dong. Manipllm: Embodied multimodal large language model for
object-centric robotic manipulation. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 18061–18070, 2024.
[482] Fangchen Liu, Kuan Fang, Pieter Abbeel, and Sergey Levine. Moka: Open-world robotic
manipulation through mark-based visual prompting. In Robotics: Science and Systems, 2024.
[483] Siyuan Huang, Haonan Chang, Yuhan Liu, Yimeng Zhu, Hao Dong, Peng Gao, Abdeslam
Boularias, and Hongsheng Li. A3vlm: Actionable articulation-aware vision language model.
In Proceedings of The 8th Conference on Robot Learning, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[484] Wentao Yuan, Jiafei Duan, Valts Blukis, Wilbert Pumacay, Ranjay Krishna, Adithyavairavan
Murali, Arsalan Mousavian, and Dieter Fox. Robopoint: A vision-language model for spatial
affordance prediction in robotics. In Conference on Robot Learning, pages 4005–4020. PMLR,
2025.
[485] Qiaojun Yu, Siyuan Huang, Xibin Yuan, Zhengkai Jiang, Ce Hao, Xin Li, Haonan Chang,
Junbo Wang, Liu Liu, Hongsheng Li, et al. Uniaff: A unified representation of affordances
for tool usage and articulation with vision-language models. In 2025 IEEE International
Conference on Robotics and Automation (ICRA), pages 8980–8987. IEEE, 2025.
[486] Yan Shen, Feng Jiang, Zichen He, Xiaoqi Li, Yuchen Liu, Zhiyu Li, Ruihai Wu, and Hao
Dong. Bipremanip: Learning affordance-based bimanual preparatory manipulation through
anticipatory collaboration. In 2026 IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), 2026.
[487] Kallol Saha, Amber Li, Angela Rodriguez-Izquierdo, Lifan Yu, Ben Eisner, Maxim Likhachev,
and David Held. Planning from point clouds over continuous actions for multi-object rear-
rangement. In Conference on Robot Learning, 2025.
[488] Yue Chen, Muqing Jiang, Kaifeng Zheng, Jiaqi Liang, Chenrui Tie, Haoran Lu, Ruihai Wu, and
Hao Dong. Pa3ff: Learning part-aware dense 3d feature field for generalizable articulated
object manipulation. In International Conference on Learning Representations, volume 2026,
pages 50604–50626, 2026.
[489] Anthony Simeonov, Yilun Du, Andrea Tagliasacchi, Joshua B Tenenbaum, Alberto Rodriguez,
Pulkit Agrawal, and Vincent Sitzmann. Neural descriptor fields: Se (3)-equivariant object
representations for manipulation. In 2022 International Conference on Robotics and Automation
(ICRA), pages 6394–6400. IEEE, 2022.
[490] Anthony Simeonov, Yilun Du, Yen-Chen Lin, Alberto Rodriguez Garcia, Leslie Pack Kaelbling,
Tomás Lozano-Pérez, and Pulkit Agrawal. Se (3)-equivariant relational rearrangement with
neural descriptor fields. In Conference on Robot Learning, pages 835–846. PMLR, 2023.
[491] William Shen, Ge Yang, Alan Yu, Jansen Wong, Leslie Pack Kaelbling, and Phillip Isola.
Distilled feature fields enable few-shot language-guided manipulation. In Conference on Robot
Learning, pages 405–424. PMLR, 2023.
[492] Yixuan Wang, Mingtong Zhang, Zhuoran Li, Tarik Kelestemur, Katherine Rose Driggs-
Campbell, Jiajun Wu, Li Fei-Fei, and Yunzhu Li. D3fields: Dynamic 3d descriptor fields
for zero-shot generalizable rearrangement. In Conference on Robot Learning, pages 272–298.
PMLR, 2025.
[493] Olaolu Shorinwa, Johnathan Tucker, Aliyah Smith, Aiden Swann, Timothy Chen, Roya Firoozi,
Monroe David Kennedy, and Mac Schwager. Splat-mover: Multi-stage, open-vocabulary
robotic manipulation via editable gaussian splatting. In Conference on Robot Learning, pages
4748–4770. PMLR, 2025.
[494] Jad Abou-Chakra, Krishan Rana, Feras Dayoub, and Niko Suenderhauf. Physically embodied
gaussian splatting: A visually learnt and physically grounded 3d representation for robotics.
In Conference on Robot Learning, pages 513–530. PMLR, 2025.
[495] Yu Sheng, Runfeng Lin, Lidian Wang, Quecheng Qiu, YanYong Zhang, Yu Zhang, Bei Hua,
and Jianmin Ji. Msgfield: A unified scene representation integrating motion, semantics, and
geometry for robotic manipulation. arXiv preprint arXiv:2410.15730, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[496] Sizhe Yang, Wenye Yu, Jia Zeng, Jun Lv, Kerui Ren, Cewu Lu, Dahua Lin, and Jiangmiao Pang.
Novel demonstration generation with gaussian splatting enables robust one-shot manipulation.
In Robotics: Science and Systems, 2025.
[497] Haojie Huang, Karl Schmeckpeper, Dian Wang, Ondrej Biza, Yaoyao Qian, Haotian Liu,
Mingxi Jia, Robert Platt, and Robin Walters. Imagination policy: Using generative point cloud
models for learning manipulation policies. In Conference on Robot Learning, pages 5150–5165.
PMLR, 2025.
[498] Hanxiao Jiang, Binghao Huang, Ruihai Wu, Zhuoran Li, Shubham Garg, Hooshang Nayyeri,
Shenlong Wang, and Yunzhu Li. Roboexp: Action-conditioned scene graph via interactive
exploration for robotic manipulation. In Conference on Robot Learning, pages 3027–3052.
PMLR, 2025.
[499] De-An Huang, Danfei Xu, Yuke Zhu, Animesh Garg, Silvio Savarese, Li Fei-Fei, and Juan Carlos
Niebles. Continuous relaxation of symbolic planner for one-shot imitation learning. In 2019
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 2635–2642.
IEEE, 2019.
[500] Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. Blip-2: Bootstrapping language-
image pre-training with frozen image encoders and large language models. In International
conference on machine learning, pages 19730–19742. PMLR, 2023.
[501] Wenliang Dai, Junnan Li, Dongxu Li, Anthony Tiong, Junqi Zhao, Weisheng Wang, Boyang Li,
Pascale N Fung, and Steven Hoi. Instructblip: Towards general-purpose vision-language mod-
els with instruction tuning. In Advances in neural information processing systems, volume 36,
pages 49250–49267, 2023.
[502] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le,
Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models.
Advances in neural information processing systems, 35:24824–24837, 2022.
[503] Kaifeng Zhang, Zhao-Heng Yin, Weirui Ye, and Yang Gao. Learning manipulation skills
through robot chain-of-thought with sparse failure guidance. In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 8012–8018. IEEE, 2025.
[504] Xufeng Zhao, Mengdi Li, Cornelius Weber, Muhammad Burhan Hafez, and Stefan Wermter.
Chat with the environment: Interactive multimodal perception using large language models.
In 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
3590–3596. IEEE, 2023.
[505] Andy Zeng, Maria Attarian, Krzysztof Marcin Choromanski, Adrian Wong, Stefan Welker,
Federico Tombari, Aveek Purohit, Michael S Ryoo, Vikas Sindhwani, Johnny Lee, et al.
Socratic models: Composing zero-shot multimodal reasoning with language. In The Eleventh
International Conference on Learning Representations, 2023.
[506] Suyeon Shin, Sujin Jeon, Junghyun Kim, Gi-Cheon Kang, and Byoung-Tak Zhang. Socratic
planner: Inquiry-based zero-shot planning for embodied instruction following. CoRR, 2024.
[507] Carl Qi, Xiaojie Wang, Silong Yong, Stephen Sheng, Huitan Mao, Manikantan Nambi, Amy
Zhang, Yeshwant Dattatreya, et al. Self-refining vision language model for robotic failure
detection and reasoning. In International Conference on Learning Representations, volume
2026, pages 113934–113956, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[508] Ronghao Dang, Yuqian Yuan, Yunxuan Mao, Kehan Li, Jiangpin Liu, Zhikai Wang, Xin Li,
Fan Wang, and Deli Zhao. Rynnec: Bringing mllms into embodied world. arXiv preprint
arXiv:2508.14160, 2025.
[509] Hanyang Chen, Mark Zhao, Rui Yang, Qinwei Ma, Ke Yang, Jiarui Yao, Kangrui Wang, Hao
Bai, Zhenhailong Wang, Rui Pan, et al. Era: Transforming vlms into embodied agents via
embodied prior learning and online reinforcement learning. arXiv preprint arXiv:2510.12693,
2025.
[510] Yi Liu, Sukai Wang, Dafeng Wei, Xiaowei Cai, Linqing Zhong, Jiange Yang, Guanghui Ren,
Jinyu Zhang, Maoqing Yao, Chuankang Li, et al. Unified embodied vlm reasoning with robotic
action via autoregressive discretized pre-training. arXiv preprint arXiv:2512.24125, 2025.
[511] Xiaopeng Lin, Shijie Lian, Bin Yu, Ruoqi Yang, Zhaolong Shen, Changti Wu, Yuzhuo Miao,
Yurun Jin, Yukun Shi, Jiyan He, et al. Physbrain: Human egocentric data as a bridge from
vision language models to physical intelligence. arXiv preprint arXiv:2512.16793, 2025.
[512] HY Team, Xumin Yu, Zuyan Liu, Ziyi Wang, He Zhang, Yongming Rao, Fangfu Liu, Yani
Zhang, Ruowen Zhao, Oran Wang, et al. Hy-embodied-0.5: Embodied foundation models for
real-world agents. arXiv preprint arXiv:2604.07430, 2026.
[513] Ziyang Gong, Zehang Luo, Anke Tang, Zhe Liu, Shi Fu, Zhi Hou, Ganlin Yang, Weiyun Wang,
Xiaofeng Wang, Jianbo Liu, et al. Ace-brain-0: Spatial intelligence as a shared scaffold for
universal embodiments. arXiv preprint arXiv:2603.03198, 2026.
[514] Sagar Gubbi Venkatesh, Raviteja Upadrashta, and Bharadwaj Amrutur. Translating natural
language instructions to computer programs for robot manipulation. In 2021 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 1919–1926. IEEE,
2021.
[515] Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, and Honguk Woo. Functional cache
grafting: Robust and rapid code-policy synthesis for embodied agents. In Forty-third Interna-
tional Conference on Machine Learning, 2026.
[516] James J Gibson. The theory of affordances:(1979). In The people, place, and space reader,
pages 56–60. Routledge, 2014.
[517] Haoran Geng, Ziming Li, Yiran Geng, Jiayi Chen, Hao Dong, and He Wang. Partmanip:
Learning cross-category generalizable part manipulation policy from point cloud observations.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
2978–2988, 2023.
[518] Wenke Xia, Dong Wang, Xincheng Pang, Zhigang Wang, Bin Zhao, Di Hu, and Xuelong Li.
Kinematic-aware prompting for generalizable articulated object manipulation with llms. In
2024 IEEE International Conference on Robotics and Automation (ICRA), pages 2073–2080.
IEEE, 2024.
[519] Seungyeon Kim, Junsu Ha, Young Hun Kim, Yonghyeon Lee, and Frank C Park. Screwsplat:
An end-to-end method for articulated object recognition. In Conference on Robot Learning,
2025.
[520] Priya Sundaresan, Suneel Belkhale, Dorsa Sadigh, and Jeannette Bohg. Kite: Keypoint-
conditioned policies for semantic manipulation. In Conference on Robot Learning, pages
1006–1021. PMLR, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[521] Yihe Tang, Wenlong Huang, Yingke Wang, Chengshu Li, Roy Yuan, Ruohan Zhang, Jiajun
Wu, and Li Fei-Fei. Uad: Unsupervised affordance distillation for generalization in robotic
manipulation. In 2025 IEEE International Conference on Robotics and Automation (ICRA),
2025.
[522] Yifan Yin, Zhengtao Han, Shivam Aarya, Jianxin Wang, Shuhang Xu, Jiawei Peng, Angtian
Wang, Alan Yuille, and Tianmin Shu. Partinstruct: Part-level instruction following for fine-
grained robot manipulation. In Robotics: Science and Systems, 2025.
[523] Soroush Nasiriany, Fei Xia, Wenhao Yu, Ted Xiao, Jacky Liang, Ishita Dasgupta, Annie Xie,
Danny Driess, Ayzaan Wahid, Zhuo Xu, et al. Pivot: iterative visual prompting elicits actionable
knowledge for vlms. In Proceedings of the 41st International Conference on Machine Learning,
pages 37321–37341, 2024.
[524] Yuxuan Kuang, Junjie Ye, Haoran Geng, Jiageng Mao, Congyue Deng, Leonidas Guibas,
He Wang, and Yue Wang. Ram: Retrieval-based affordance transfer for generalizable zero-
shot robotic manipulation. In Conference on Robot Learning, pages 547–565. PMLR, 2025.
[525] Chuyan Xiong, Chengyu Shen, Xiaoqi Li, Kaichen Zhou, Jiaming Liu, Ruiping Wang, and Hao
Dong. Autonomous interactive correction mllm for robust robotic manipulation. In Conference
on Robot Learning, pages 3139–3156. PMLR, 2025.
[526] Boyuan Chen, Tianyuan Zhang, Haoran Geng, Caiyi Zhang, Peihao Li, Kiwhan Song, William T
Freeman, Jitendra Malik, Pieter Abbeel, Russ Tedrake, et al. Large video planner enables
generalizable robot control. arXiv preprint arXiv:2512.15840, 2025.
[527] Shivansh Patel, Shraddhaa Mohan, Hanlin Mai, Unnat Jain, Svetlana Lazebnik, and Yunzhu
Li. Robotic manipulation by imitating generated videos without physical demonstrations.
In International Conference on Learning Representations, volume 2026, pages 71634–71658,
2026.
[528] Zeyi Liu, Shuang Li, Eric Cousineau, Siyuan Feng, Benjamin Burchfiel, and Shuran Song.
Geometry-aware 4d video generation for robot manipulation. In International Conference on
Learning Representations, volume 2026, pages 140751–140773, 2026.
[529] Kaichen Zhou, Yuzhen Chen, Fangneng Zhan, Hang Hua, Grace Chen, Xinhai Chang, Ao Qu,
Yilun Du, Zhuang Liu, Paul Pu Liang, et al. Gem-4d: Geometry-enhanced video world models
for robot manipulation. arXiv preprint arXiv:2605.22882, 2026.
[530] Sen Wang, Jingyi Tian, Le Wang, Zhimin Liao, Huaiyi Dong, Kun Xia, Sanping Zhou, Wei
Tang, and Gang Hua. Sampo: Scale-wise autoregression with motion prompt for generative
world models. Advances in Neural Information Processing Systems, 38:90560–90589, 2025.
[531] Quanyi Li, Lan Feng, Haonan Zhang, Wuyang Li, Letian Wang, Alexandre Alahi, and
Harold Soh. Grounded world model for semantically generalizable planning. arXiv preprint
arXiv:2604.11751, 2026.
[532] Emily Yue-Ting Jia, Weiduo Yuan, Tianheng Shi, Vitor Guizilini, Jiageng Mao, and Yue Wang.
Dreamplan: Efficient reinforcement fine-tuning of vision-language planners via video world
models. arXiv preprint arXiv:2603.16860, 2026.
[533] Harold Haodong Chen, Sirui Chen, Yingjie Xu, Wenhang Ge, and Ying-Cong Chen. Roboevolve:
Co-evolving planner-simulator for robotic manipulation with limited data. arXiv preprint
arXiv:2605.13775, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[534] Boxiang Qiu, Liliang Chen, Yue Liao, Nan Wang, Lintao Wang, Jiayi Luo, Wenzhi Zhao,
Shengcong Chen, Di Chen, Ye Li, et al. Ge-sim 2.0: A roadmap towards comprehensive
closed-loop video world simulators for robotic manipulation. arXiv preprint arXiv:2605.27491,
2026.
[535] Kalashnikov Dmitry, Irpan Alex, Pastor Peter, Ibarz Julian, Herzog Alexander, Jang Eric,
Quillen Deirdre, Holly Ethan, Kalakrishnan Mrinal, Vanhoucke Vincent, et al. Qt-opt. scalable
deep reinforcement learning for vision-based robotic manipulation. arXiv preprint, 2018.
[536] Aviral Kumar, Anikait Singh, Frederik Ebert, Mitsuhiko Nakamoto, Yanlai Yang, Chelsea Finn,
and Sergey Levine. Pre-training for robots: Offline rl enables learning new tasks from a
handful of trials. arXiv preprint arXiv:2210.05178, 2022.
[537] Chethan Anand Bhateja, Derek Guo, Dibya Ghosh, Anikait Singh, Manan Tomar, Quan Vuong,
Yevgen Chebotar, Sergey Levine, and Aviral Kumar. Robotic offline rl from internet videos
via value-function pre-training. In NeurIPS 2023 Foundation Models for Decision Making
Workshop, 2023.
[538] Tobias Johannink, Shikhar Bahl, Ashvin Nair, Jianlan Luo, Avinash Kumar, Matthias Loskyll,
Juan Aparicio Ojea, Eugen Solowjow, and Sergey Levine. Residual reinforcement learning
for robot control. In 2019 international conference on robotics and automation (ICRA), pages
6023–6029. IEEE, 2019.
[539] Charles Xu, Qiyang Li, Jianlan Luo, and Sergey Levine. Rldg: Robotic generalist policy
distillation via reinforcement learning. In Robotics: Science and Systems, 2025.
[540] Mitsuhiko Nakamoto, Oier Mees, Aviral Kumar, and Sergey Levine. Steering your generalists:
Improving robotic foundation models via value guidance. In Conference on Robot Learning,
pages 4996–5013. PMLR, 2025.
[541] Max Sobol Mark, Tian Gao, Georgia Gabriela Sampaio, Mohan Kumar Srirama, Archit Sharma,
Chelsea Finn, and Aviral Kumar. Policy-agnostic rl: Offline rl and online rl fine-tuning of
any class and backbone. In 7th Robot Learning Workshop: Towards Robots with Human-Level
Abilities, 2024.
[542] Yanjiang Guo, Jianke Zhang, Xiaoyu Chen, Xiang Ji, Yen-Jen Wang, Yucheng Hu, and Jianyu
Chen. Improving vision-language-action model with online reinforcement learning. In 2025
IEEE International Conference on Robotics and Automation (ICRA), pages 15665–15672. IEEE,
2025.
[543] Shuhan Tan, Kairan Dou, Yue Zhao, and Philipp Kraehenbuehl. Interactive post-training for
vision-language-action models. In Workshop on Foundation Models Meet Embodied Agents at
CVPR 2025, 2025.
[544] Guanxing Lu, Wenkai Guo, Chubin Zhang, Yuheng Zhou, Haonan Jiang, Zifeng Gao, Yansong
Tang, and Ziwei Wang. Vla-rl: Towards masterful and general robotic manipulation with
scalable reinforcement learning. arXiv preprint arXiv:2505.18719, 2025.
[545] Yuhui Chen, Shuai Tian, Shugao Liu, Yingting Zhou, Haoran Li, and Dongbin Zhao. Conrft:
A reinforced fine-tuning method for vla models via consistency policy. In Robotics: Science
and Systems, 2025.
[546] Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. Dream to control:
Learning behaviors by latent imagination. In International Conference on Learning Representa-
tions, 2020.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[547] Younggyo Seo, Danijar Hafner, Hao Liu, Fangchen Liu, Stephen James, Kimin Lee, and Pieter
Abbeel. Masked world models for visual control. In Conference on Robot Learning, pages
1332–1344. PMLR, 2023.
[548] Sergey Levine and Vladlen Koltun. Guided policy search. In International conference on
machine learning, pages 1–9. PMLR, 2013.
[549] Nicklas A Hansen, Hao Su, and Xiaolong Wang. Temporal difference learning for model
predictive control. In International Conference on Machine Learning, pages 8387–8406. PMLR,
2022.
[550] Eliot Xing, Vernon Luk, and Jean Oh. Stabilizing reinforcement learning in differentiable mul-
tiphysics simulation. In The Thirteenth International Conference on Learning Representations,
2025.
[551] Jun Lv, Yunhai Feng, Cheng Zhang, Shuang Zhao, Lin Shao, and Cewu Lu. Sam-rl: Sensing-
aware model-based reinforcement learning via differentiable physics-based simulation and
rendering. The International Journal of Robotics Research, page 02783649241284653, 2023.
[552] Weikang Wan, Ziyu Wang, Yufei Wang, Zackory Erickson, and David Held. Difftori: Differ-
entiable trajectory optimization for deep reinforcement and imitation learning. Advances in
Neural Information Processing Systems, 37:109430–109459, 2024.
[553] Yevgen Chebotar, Quan Vuong, Karol Hausman, Fei Xia, Yao Lu, Alex Irpan, Aviral Kumar,
Tianhe Yu, Alexander Herzog, Karl Pertsch, et al. Q-transformer: Scalable offline rein-
forcement learning via autoregressive q-functions. In Conference on Robot Learning, pages
3909–3928. PMLR, 2023.
[554] Chengyang Ying, Hao Zhongkai, Xinning Zhou, Xuezhou Xu, Hang Su, Xingxing Zhang, and
Jun Zhu. Peac: Unsupervised pre-training for cross-embodiment reinforcement learning.
Advances in Neural Information Processing Systems, 37:54632–54669, 2024.
[555] Shaohao Zhu, Yixian Zhao, Yang Xu, Anjun Chen, Jiming Chen, and Jinming Xu. Taskexp:
Enhancing generalization of multi-robot exploration with multi-task pre-training. In 2025
IEEE International Conference on Robotics and Automation (ICRA), pages 6559–6565. IEEE,
2025.
[556] Jingyun Yang, Max Sobol Mark, Brandon Vu, Archit Sharma, Jeannette Bohg, and Chelsea
Finn.
Robot fine-tuning made easy: Pre-training rewards and policies for autonomous
real-world reinforcement learning. In 2024 IEEE International Conference on Robotics and
Automation (ICRA), pages 4804–4811. IEEE, 2024.
[557] Jiahui Zhang, Yusen Luo, Abrar Anwar, Sumedh Anand Sontakke, Joseph J Lim, Jesse
Thomason, Erdem Biyik, and Jesse Zhang. Rewind: Language-guided rewards teach robot
policies without new demonstrations. In Second Workshop on Out-of-Distribution Generalization
in Robotics at RSS 2025, 2025.
[558] Changyeon Kim, Haeone Lee, Younggyo Seo, Kimin Lee, and Yuke Zhu. Deas: Detached
value learning with action sequence for scalable offline rl. In International Conference on
Learning Representations, volume 2026, pages 64035–64058, 2026.
[559] Lars Ankile, Anthony Simeonov, Idan Shenfeld, Marcel Torne, and Pulkit Agrawal. From
imitation to refinement-residual rl for precise assembly. In 2025 IEEE International Conference
on Robotics and Automation (ICRA), pages 01–08. IEEE, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[560] Xiu Yuan, Tongzhou Mu, Stone Tao, Yunhao Fang, Mengke Zhang, and Hao Su. Policy deco-
rator: Model-agnostic online refinement for large policy model. In International Conference
on Learning Representations, volume 2025, pages 28129–28164, 2025.
[561] Perry Dong, Suvir Mirchandani, Dorsa Sadigh, and Chelsea Finn. What matters for batch
online reinforcement learning in robotics? In International Conference on Learning Represen-
tations, volume 2026, pages 112294–112308, 2026.
[562] Perry Dong, Qiyang Li, Dorsa Sadigh, and Chelsea Finn. Expo: Stable reinforcement learning
with expressive policies. In International Conference on Learning Representations, volume
2026, pages 131379–131394, 2026.
[563] Alberta Longhini, David Emukpere, Jean-Michel Renders, and Seungsu Kim. Behavioral mode
discovery for fine-tuning multimodal generative policies. arXiv preprint arXiv:2605.11387,
2026.
[564] Jijia Liu, Feng Gao, Bingwen Wei, Xinlei Chen, Qingmin Liao, Yi Wu, Chao Yu, and Yu Wang.
What can rl bring to vla generalization? an empirical study. Advances in Neural Information
Processing Systems, 38:97121–97151, 2025.
[565] Junyang Shu, Zhiwei Lin, and Yongtao Wang. Rftf: Reinforcement fine-tuning for embodied
agents with temporal feedback. arXiv preprint arXiv:2505.19767, 2025.
[566] Zengjue Chen, Runliang Niu, He Kong, and Qi Wang.
Tgrpo:
Fine-tuning vision-
language-action model via trajectory-wise group relative policy optimization. arXiv preprint
arXiv:2506.08440, 2025.
[567] Haoming Song, Delin Qu, Yuanqi Yao, Qizhi Chen, Qi Lv, Yiwen Tang, Modi Shi, Guanghui Ren,
Maoqing Yao, Bin Zhao, et al. Hume: Introducing system-2 thinking in visual-language-action
model. arXiv preprint arXiv:2505.21432, 2025.
[568] Andrew Wagenmaker, Mitsuhiko Nakamoto, Yunchu Zhang, Seohong Park, Waleed Yagoub,
Anusha Nagabandi, Abhishek Gupta, and Sergey Levine. Steering your diffusion policy with
latent space reinforcement learning. In Conference on Robot Learning, 2025.
[569] Kevin Chen, Marco Cusumano-Towner, Brody Huval, Aleksei Petrenko, Jackson Hamburger,
Vladlen Koltun, and Philipp Krähenbühl. Reinforcement learning for long-horizon interactive
llm agents. arXiv preprint arXiv:2502.01600, 2025.
[570] Richard S Sutton. Dyna, an integrated architecture for learning, planning, and reacting. ACM
Sigart Bulletin, 2(4):160–163, 1991.
[571] Danijar Hafner, Timothy P Lillicrap, Mohammad Norouzi, and Jimmy Ba. Mastering atari
with discrete world models. In International Conference on Learning Representations, 2021.
[572] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse control
tasks through world models. Nature, pages 1–7, 2025.
[573] Younggyo Seo, Kimin Lee, Stephen L James, and Pieter Abbeel. Reinforcement learning with
action-free pre-training from videos. In International Conference on Machine Learning, pages
19561–19579. PMLR, 2022.
[574] Philipp Wu, Alejandro Escontrela, Danijar Hafner, Pieter Abbeel, and Ken Goldberg. Day-
dreamer: World models for physical robot learning. In Conference on robot learning, pages
2226–2240. PMLR, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[575] Rafael Rafailov, Tianhe Yu, Aravind Rajeswaran, and Chelsea Finn. Offline reinforcement
learning from images with latent space models. In Learning for dynamics and control, pages
1154–1168. PMLR, 2021.
[576] Minting Pan, Yitao Zheng, Jiajian Li, Yunbo Wang, and Xiaokang Yang. Video-enhanced offline
reinforcement learning: A model-based approach. In Forty-second International Conference on
Machine Learning, 2025.
[577] Guanxing Lu, Baoxiong Jia, Puhao Li, Yixin Chen, Ziwei Wang, Yansong Tang, and Siyuan
Huang. Gwm: Towards scalable gaussian world models for robotic manipulation. In 2025
IEEE/CVF International Conference on Computer Vision (ICCV), pages 9263–9274. IEEE, 2025.
[578] Fan Feng, Yujia Zheng, Minghao Fu, Yongqiang Chen, Guangyi Chen, Kevin Murphy, Biwei
Huang, and Kun Zhang. Learning task-sufficient world models by synergizing agentic explo-
ration and structured modeling. In Forty-third International Conference on Machine Learning,
2026.
[579] Sergey Levine and Vladlen Koltun. Variational policy search via trajectory optimization.
Advances in neural information processing systems, 26, 2013.
[580] Sergey Levine and Vladlen Koltun. Learning complex neural network policies with trajectory
optimization. In International Conference on Machine Learning, pages 829–837. PMLR, 2014.
[581] Sergey Levine and Pieter Abbeel. Learning neural network policies with guided policy search
under unknown dynamics. Advances in neural information processing systems, 27, 2014.
[582] Nicklas Hansen, Hao Su, and Xiaolong Wang. Td-mpc2: Scalable, robust world models for
continuous control. In The Twelfth International Conference on Learning Representations, 2024.
[583] Cyrus Neary, Omar G Younis, Artur Kuramshin, Ozgur Aslan, and Glen Berseth. Improv-
ing pre-trained vision-language-action policies with model-based search. arXiv preprint
arXiv:2508.12211, 2025.
[584] Xiaoyuan Cheng, Wenxuan Yuan, Zhancun Mu, Yuanzhao Zhang, Yiming Yang, Hai Wang,
Zhuo Sun, and Che Liu. Scaling world-model reinforcement learning through diffusion policy
optimization. arXiv preprint arXiv:2605.26282, 2026.
[585] Stefan Schaal. Is imitation learning the route to humanoid robots? Trends in cognitive sciences,
3(6):233–242, 1999.
[586] Maryam Zare, Parham M Kebria, Abbas Khosravi, and Saeid Nahavandi. A survey of imitation
learning: Algorithms, recent developments, and challenges. IEEE Transactions on Cybernetics,
2024.
[587] Fan Xie, Alexander Chowdhury, M De Paolis Kaluza, Linfeng Zhao, Lawson Wong, and Rose Yu.
Deep imitation learning for bimanual robotic manipulation. Advances in neural information
processing systems, 33:2327–2337, 2020.
[588] Fanqi Lin, Yingdong Hu, Pingyue Sheng, Chuan Wen, Jiacheng You, and Yang Gao. Data
scaling laws in imitation learning for robotic manipulation. In The Thirteenth International
Conference on Learning Representations, 2025.
[589] Han Sun, Yizhao Wang, Zhenning Zhou, Shuai Wang, Haibo Yang, Jingyuan Sun, and Qixin
Cao. Exploring pose-guided imitation learning for robotic precise insertion. arXiv preprint
arXiv:2505.09424, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[590] Junyao Shi, Zhuolun Zhao, Tianyou Wang, Ian Pedroza, Amy Luo, Jie Wang, Jason Ma, and
Dinesh Jayaraman. Zeromimic: Distilling robotic manipulation skills from web videos. In
2025 IEEE International Conference on Robotics and Automation (ICRA), pages 16939–16947.
IEEE, 2025.
[591] Chongkai Gao, Zhengrong Xue, Shuying Deng, Tianhai Liang, Siqi Yang, Lin Shao, and
Huazhe Xu. Riemann: Near real-time se (3)-equivariant robot manipulation without point
cloud segmentation. In Conference on Robot Learning, pages 2164–2182. PMLR, 2025.
[592] Stefan Schaal, Auke Ijspeert, and Aude Billard. Computational approaches to motor learning
by imitation. Philosophical Transactions of the Royal Society of London. Series B: Biological
Sciences, 358(1431):537–547, 2003.
[593] Auke Jan Ijspeert, Jun Nakanishi, Heiko Hoffmann, Peter Pastor, and Stefan Schaal. Dynamical
movement primitives: learning attractor models for motor behaviors. Neural computation, 25
(2):328–373, 2013.
[594] Alexandros Paraschos, Christian Daniel, Jan R Peters, and Gerhard Neumann. Probabilistic
movement primitives. Advances in neural information processing systems, 26, 2013.
[595] Ajay Kumar Tanwani, Jonathan Lee, Brijen Thananjeyan, Michael Laskey, Sanjay Krishnan,
Roy Fox, Ken Goldberg, and Sylvain Calinon. Generalizing robot imitation learning with
invariant hidden semi-markov models. In International workshop on the algorithmic foundations
of robotics, pages 196–211. Springer, 2018.
[596] Yinlong Dai, Benjamin A Christie, Daniel J Evans, Dylan P Losey, and Simon Stepputtis.
Language movement primitives: Grounding language models in robot motion. arXiv preprint
arXiv:2602.02839, 2026.
[597] Xirui Shi, Arya Ebrahimi, Yi Hu, and Jun Jin. Fodmp: Fast one-step diffusion of movement
primitives generation for time-dependent robot actions. arXiv preprint arXiv:2603.24806,
2026.
[598] Aude Billard, Yann Epars, Sylvain Calinon, Stefan Schaal, and Gordon Cheng. Discovering
optimal imitation strategies. Robotics and autonomous systems, 47(2-3):69–77, 2004.
[599] Nathan D Ratliff, David Silver, and J Andrew Bagnell. Learning to search: Functional gradient
techniques for imitation learning. Autonomous Robots, 27(1):25–53, 2009.
[600] Anqing Duan, Iason Batzianoulis, Raffaello Camoriano, Lorenzo Rosasco, Daniele Pucci, and
Aude Billard. A structured prediction approach for robot imitation learning. The International
Journal of Robotics Research, 43(2):113–133, 2024.
[601] Michael James McDonald and Dylan Hadfield-Menell. Guided imitation of task and motion
planning. In Conference on Robot Learning, pages 630–640. PMLR, 2022.
[602] Arnav Kumar Jain, Vibhakar Mohta, Subin Kim, Atiksh Bhardwaj, Juntao Ren, Yunhai Feng,
Sanjiban Choudhury, and Gokul Swamy. A smooth sea never made a skilled sailor: Robust
imitation via learning to search. Advances in Neural Information Processing Systems, 38:
62676–62707, 2025.
[603] Dennis Mronga and Frank Kirchner. Learning context-adaptive task constraints for robotic
manipulation. Robotics and Autonomous Systems, 141:103779, 2021.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[604] Akshay Dhonthi, Philipp Schillinger, Leonel Rozo, and Daniele Nardi. Optimizing demon-
strated robot manipulation skills for temporal logic constraints. In 2022 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 1255–1262. IEEE, 2022.
[605] Zhengtong Xu and Yu She. Leto: Learning constrained visuomotor policy with differentiable
trajectory optimization. IEEE Transactions on Automation Science and Engineering, 2024.
[606] Shiyao Zhao, Yucheng Xu, Mohammadreza Kasaei, Mohsen Khadem, and Zhibin Li. Neural
ode-based imitation learning (node-il): Data-efficient imitation learning for long-horizon
multi-skill robot manipulation. In 2024 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 8524–8530. IEEE, 2024.
[607] Amin Abyaneh, Mahrokh Ghoddousi Boroujeni, Hsiu-Chin Lin, and Giancarlo Ferrari-Trecate.
Contractive dynamical imitation policies for efficient out-of-sample recovery. In The Thirteenth
International Conference on Learning Representations, 2025.
[608] Peter Englert, Ngo Anh Vien, and Marc Toussaint. Inverse kkt: Learning cost functions of
manipulation tasks from demonstrations. The International Journal of Robotics Research, 36
(13-14):1474–1488, 2017.
[609] Huy Hoang, Tien Mai, and Pradeep Varakantham. Sprinql: Sub-optimal demonstrations
driven offline imitation learning. Advances in Neural Information Processing Systems, 37:
136837–136872, 2024.
[610] Minyoung Hwang, Alexandra Forsey-Smerek, Nathaniel Dennler, and Andreea Bobu. Masked
irl: Llm-guided reward disambiguation from demonstrations and language. arXiv preprint
arXiv:2511.14565, 2025.
[611] Xinhu Li, Ayush Jain, Zhaojing Yang, Yigit Korkmaz, and Erdem Bıyık. When a robot is more
capable than a human: Learning from constrained demonstrators. In International Conference
on Learning Representations, volume 2026, pages 90429–90446, 2026.
[612] Jonathan Ho and Stefano Ermon. Generative adversarial imitation learning. Advances in
neural information processing systems, 29, 2016.
[613] Mingxuan Jing, Wenbing Huang, Fuchun Sun, Xiaojian Ma, Tao Kong, Chuang Gan, and Lei
Li. Adversarial option-aware hierarchical imitation learning. In International Conference on
Machine Learning, pages 5097–5106. PMLR, 2021.
[614] Tianyu Wang, Nikhil Karnwal, and Nikolay Atanasov. Latent policies for adversarial imitation
learning. arXiv preprint arXiv:2206.11299, 2022.
[615] Chun-Mao Lai, Hsiang-Chun Wang, Ping-Chun Hsieh, Frank Wang, Min-Hung Chen, and Shao-
Hua Sun. Diffusion-reward adversarial imitation learning. Advances in Neural Information
Processing Systems, 37:95456–95487, 2024.
[616] Sheng Yue, Xingyuan Hua, Ju Ren, Sen Lin, Junshan Zhang, and Yaoxue Zhang. Ollie:
Imitation learning from offline pretraining to online finetuning. In Proceedings of the 41st
International Conference on Machine Learning, 2024.
[617] Vittorio Giammarino, James Queeney, and Ioannis Ch Paschalidis. Visually robust adversarial
imitation learning from videos with contrastive learning. In 2025 IEEE International Conference
on Robotics and Automation (ICRA), pages 15642–15648. IEEE, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[618] Aviv Tamar, Khashayar Rohanimanesh, Yinlam Chow, Chris Vigorito, Ben Goodrich, Michael
Kahane, and Derik Pridmore. Imitation learning from visual data with multiple intentions. In
International Conference on Learning Representations, 2018.
[619] Allen Ren, Sushant Veer, and Anirudha Majumdar. Generalization guarantees for imitation
learning. In Conference on Robot Learning, pages 1426–1442. PMLR, 2021.
[620] Simon Stepputtis, Maryam Bandari, Stefan Schaal, and Heni Ben Amor. A system for imitation
learning of contact-rich bimanual manipulation policies. In 2022 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 11810–11817. IEEE, 2022.
[621] Martijn JA Zeestraten, Ioannis Havoutis, Joao Silvério, Sylvain Calinon, and Darwin G
Caldwell. An approach for imitation learning on riemannian manifolds. IEEE Robotics and
Automation Letters, 2(3):1240–1247, 2017.
[622] Konrad Zolna, Scott Reed, Alexander Novikov, Sergio Gomez Colmenarejo, David Budden,
Serkan Cabi, Misha Denil, Nando De Freitas, and Ziyu Wang. Task-relevant adversarial
imitation learning. In Conference on Robot Learning, pages 247–263. PMLR, 2021.
[623] Kaustubh Sridhar, Souradeep Dutta, Dinesh Jayaraman, James Weimer, and Insup Lee.
Memory-consistent neural networks for imitation learning. In The Twelfth International
Conference on Learning Representations, 2024.
[624] Zhanyi Sun and Shuran Song. Latent policy barrier: Learning robust visuomotor policies by
staying in-distribution. Advances in Neural Information Processing Systems, 38:174280–174305,
2025.
[625] Sudeep Dasari and Abhinav Gupta. Transformers for one-shot visual imitation. In Conference
on Robot Learning, pages 2071–2084. PMLR, 2021.
[626] Letian Fu, Huang Huang, Gaurav Datta, Lawrence Yunliang Chen, William Chung-Ho Panitch,
Fangchen Liu, Hui Li, and Ken Goldberg.
In-context imitation learning via next-token
prediction. In 2025 IEEE International Conference on Robotics and Automation (ICRA), 2025.
[627] Vitalis Vosylius and Edward Johns. Instant policy: In-context imitation learning via graph
diffusion. In The Thirteenth International Conference on Learning Representations, 2025.
[628] Hanbit Oh, Andrea M Salcedo-Vázquez, Ixchel G Ramirez-Alpizar, and Yukiyasu Domae.
Robust instant policy: Leveraging student’s t-regression model for robust in-context imitation
learning of robot manipulation. In 2025 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), 2025.
[629] Fawad Javed Fateh, Ali Shah Ali, Murad Popattia, Usman Nizamani, Andrey Konin, M Zeeshan
Zia, and Quoc-Huy Tran. A hierarchical spatiotemporal action tokenizer for in-context
imitation learning in robotics. arXiv preprint arXiv:2604.15215, 2026.
[630] Toan Nguyen, Weiduo Yuan, Songlin Wei, Hui Li, Daniel Seita, and Yue Wang. Iclr: In-context
imitation learning with visual reasoning. arXiv preprint arXiv:2603.07530, 2026.
[631] Snehal Jauhri, Carlos Celemin, and Jens Kober. Interactive imitation learning in state-space.
In Conference on Robot Learning, pages 682–692. PMLR, 2021.
[632] Ajay Mandlekar, Danfei Xu, Roberto Martín-Martín, Yuke Zhu, Li Fei-Fei, and Silvio
Savarese. Human-in-the-loop imitation learning using remote teleoperation. arXiv preprint
arXiv:2012.06733, 2020.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[633] Huihan Liu, Soroush Nasiriany, Lance Zhang, Zhiyao Bao, and Yuke Zhu. Robot learning on
the job: Human-in-the-loop autonomy and learning during deployment. The International
Journal of Robotics Research, page 02783649241273901, 2022.
[634] Yuchen Cui, Siddharth Karamcheti, Raj Palleti, Nidhya Shivakumar, Percy Liang, and Dorsa
Sadigh. No, to the right: Online language corrections for robotic manipulation via shared
autonomy. In Proceedings of the 2023 ACM/IEEE International Conference on Human-Robot
Interaction, pages 93–101, 2023.
[635] Ryan Hoque, Ashwin Balakrishna, Carl Putterman, Michael Luo, Daniel S Brown, Daniel Seita,
Brijen Thananjeyan, Ellen Novoseller, and Ken Goldberg. Lazydagger: Reducing context
switching in interactive imitation learning. In 2021 IEEE 17th international conference on
automation science and engineering (case), pages 502–509. IEEE, 2021.
[636] Ryan Hoque, Ashwin Balakrishna, Ellen Novoseller, Albert Wilcox, Daniel S Brown, and Ken
Goldberg. Thriftydagger: Budget-aware novelty and risk gating for interactive imitation
learning. In Conference on Robot Learning, pages 598–608. PMLR, 2022.
[637] Taro Takahashi, Yutaro Ishida, Takayuki Kanai, and Naveen Kuppuswamy. Chg-dagger:
Interactive imitation learning with human-policy cooperative control. In CoRL 2024 Workshop
CoRoboLearn: Advancing Learning for Human-Centered Collaborative Robots, 2024.
[638] Michael Murray, Daphne Chen, Simran Bagaria, Dean Fortier, Tess Hellebrekers, Galen
Mullins, Harshavardhan Gajarla, Oier Mees, Maya Cakmak, and Andrey Kolobov. Flowdagger:
Human-in-the-loop adaptation of generative robot policies in latent space. arXiv preprint
arXiv:2607.08877, 2026.
[639] Zhaoting Li, Gang Chen, Javier Alonso-Mora, Cosimo Della Santina, and Jens Kober. Set-
supervised diffusion policy: Learning action-chunking diffusion through corrections. arXiv
preprint arXiv:2606.01865, 2026.
[640] Wenye Yu, Jun Lv, Zixi Ying, Yang Jin, Chuan Wen, and Cewu Lu. Armada: Autonomous
online failure detection and human shared control empower scalable real-world deployment
and adaptation. IEEE Robotics and Automation Letters, 2026.
[641] Michael Laskey, Jonathan Lee, Roy Fox, Anca Dragan, and Ken Goldberg. Dart: Noise injection
for robust imitation learning. In Conference on robot learning, pages 143–156. PMLR, 2017.
[642] Peter Valletta, Rodrigo Pérez-Dattari, and Jens Kober. Imitation learning with inconsistent
demonstrations through uncertainty-based data manipulation. In 2021 IEEE International
Conference on Robotics and Automation (ICRA), pages 3655–3661. IEEE, 2021.
[643] Hanbit Oh, Hikaru Sasaki, Brendan Michael, and Takamitsu Matsubara. Bayesian disturbance
injection: Robust imitation learning of flexible policies for robot manipulation.
Neural
Networks, 158:42–58, 2023.
[644] Shahabedin Sagheb and Dylan P Losey. Counterfactual behavior cloning: Offline imitation
learning from imperfect human demonstrations. arXiv preprint arXiv:2505.10760, 2025.
[645] Siyuan Huang, Yue Liao, Siyuan Feng, Shu Jiang, Si Liu, Hongsheng Li, Maoqing Yao, and
Guanghui Ren. Adversarial data collection: Human-collaborative perturbations for efficient
and robust robotic imitation learning. arXiv preprint arXiv:2503.11646, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[646] Liyiming Ke, Yunchu Zhang, Abhay Deshpande, Siddhartha Srinivasa, and Abhishek Gupta.
Ccil: Continuity-based data augmentation for corrective imitation learning. In The Twelfth
International Conference on Learning Representations, 2024.
[647] Tabitha E Lee, Jialiang Alan Zhao, Amrita S Sawhney, Siddharth Girdhar, and Oliver Kroemer.
Causal reasoning in simulation for structure and transfer learning of robot manipulation
policies. In 2021 IEEE International Conference on Robotics and Automation (ICRA), pages
4776–4782. IEEE, 2021.
[648] Wonsuhk Jung, Dennis Anthony, Utkarsh Aashu Mishra, Nadun Ranawaka Arachchige, Danfei
Xu, and Shreyas Kousik. Rail: Reachability-aided imitation learning for safe policy execution.
In 2025 IEEE International Conference on Robotics and Automation (ICRA), 2025.
[649] Chen Xu, Tony Khuong Nguyen, Emma Dixon, Christopher Rodriguez, Patrick Miller, Robert
Lee, Paarth Shah, Rares Ambrus, Haruki Nishimura, and Masha Itkina. Can we detect failures
without failure data? uncertainty-aware runtime failure detection for imitation learning
policies. In Robotics: Science and Systems, 2025.
[650] Yixin Lin, Austin S Wang, Eric Undersander, and Akshara Rai. Efficient and interpretable
robot manipulation with graph neural networks. IEEE Robotics and Automation Letters, 7(2):
2740–2747, 2022.
[651] Haizhou Ge, Ruixiang Wang, Zhu-ang Xu, Hongrui Zhu, Ruichen Deng, Yuhang Dong, Zeyu
Pang, Guyue Zhou, Junyu Zhang, and Lu Shi. Bridging the resource gap: Deploying advanced
imitation learning models onto affordable embedded platforms. In 2024 IEEE International
Conference on Robotics and Biomimetics (ROBIO), pages 1882–1887. IEEE, 2024.
[652] Jun Xie, Zhicheng Wang, Jianwei Tan, Huanxu Lin, and Xiaoguang Ma. Subconscious robotic
imitation learning. arXiv preprint arXiv:2412.20368, 2024.
[653] Lingxiao Guo, Zhengrong Xue, Zijing Xu, and Huazhe Xu. Demospeedup: Accelerating
visuomotor policies via entropy-guided demonstration acceleration. In Conference on Robot
Learning, 2025.
[654] Nadun Ranawaka Arachchige, Zhenyang Chen, Wonsuhk Jung, Woo Chul Shin, Rohan Bansal,
Pierre Barroso, Yu Hang He, Yingyang Celine Lin, Benjamin Joffe, Shreyas Kousik, et al. Sail:
Faster-than-demonstration execution of imitation learning policies. In Conference on Robot
Learning, 2025.
[655] Minttu Alakuijala, Gabriel Dulac-Arnold, Julien Mairal, Jean Ponce, and Cordelia Schmid.
Learning reward functions for robotic manipulation by observing humans. In 2023 IEEE
International Conference on Robotics and Automation (ICRA), pages 5006–5012. IEEE, 2023.
[656] Yuyang Liu, Weijun Dong, Yingdong Hu, Chuan Wen, Zhao-Heng Yin, Chongjie Zhang, and
Yang Gao. Imitation learning from observation with automatic discount scheduling. In The
Twelfth International Conference on Learning Representations, 2024.
[657] Bo-Ruei Huang, Chun-Kai Yang, Chun-Mao Lai, Dai-Jie Wu, and Shao-Hua Sun. Diffusion
imitation from observation. Advances in Neural Information Processing Systems, 37:137190–
137217, 2024.
[658] Harshit Sikchi, Caleb Chuck, Amy Zhang, and Scott Niekum. A dual approach to imitation
learning from observations with offline datasets. In Conference on Robot Learning, pages
1125–1147. PMLR, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[659] Antonio Chella, Haris Dindo, and Ignazio Infantino. A cognitive framework for imitation
learning. Robotics and Autonomous Systems, 54(5):403–408, 2006.
[660] Maximilian Sieb, Zhou Xian, Audrey Huang, Oliver Kroemer, and Katerina Fragkiadaki.
Graph-structured visual imitation. In Conference on Robot learning, pages 979–989. PMLR,
2020.
[661] Youngwoon Lee, Edward S Hu, Zhengyu Yang, and Joseph J Lim. To follow or not to follow:
Selective imitation learning from observations. In Conference on Robot Learning, pages 11–23.
PMLR, 2020.
[662] Jun Jin, Laura Petrich, Masood Dehghan, and Martin Jagersand. A geometric perspective on
visual imitation learning. In 2020 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), pages 5194–5200. IEEE, 2020.
[663] Shikhar Bahl, Abhinav Gupta, and Deepak Pathak. Human-to-robot imitation in the wild. In
Robotics: Science and Systems, 2022.
[664] Yuchen Cui, Scott Niekum, Abhinav Gupta, Vikash Kumar, and Aravind Rajeswaran. Can
foundation models perform zero-shot task specification for robot manipulation? In Learning
for dynamics and control conference, pages 893–905. PMLR, 2022.
[665] Zeyu Huang, Juzhan Xu, Sisi Dai, Kai Xu, Hao Zhang, Hui Huang, and Ruizhen Hu. Nift:
Neural interaction field and template for object manipulation. In 2023 IEEE International
Conference on Robotics and Automation (ICRA), pages 1875–1881. IEEE, 2023.
[666] Yecheng Jason Ma, Shagun Sodhani, Dinesh Jayaraman, Osbert Bastani, Vikash Kumar, and
Amy Zhang. Vip: Towards universal visual reward and representation via value-implicit
pre-training. In The Eleventh International Conference on Learning Representations, 2023.
[667] Yecheng Jason Ma, Vikash Kumar, Amy Zhang, Osbert Bastani, and Dinesh Jayaraman. Liv:
Language-image representations and rewards for robotic control. In International Conference
on Machine Learning, pages 23301–23320. PMLR, 2023.
[668] Siwei Chen, Xiao Ma, and Zhongwen Xu. Imitation learning as state matching via differentiable
physics. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition,
pages 7846–7855, 2023.
[669] Xinghao Zhu, JingHan Ke, Zhixuan Xu, Zhixin Sun, Bizhe Bai, Jun Lv, Qingtao Liu, Yuwei
Zeng, Qi Ye, Cewu Lu, et al. Diff-lfd: Contact-aware model-based learning from visual
demonstration for robotic manipulation via differentiable physics-based simulation and
rendering. In Conference on Robot Learning, pages 499–512. PMLR, 2023.
[670] Junchi Liang, Bowen Wen, Kostas Bekris, and Abdeslam Boularias. Learning sensorimotor
primitives of sequential manipulation tasks from visual demonstrations. In 2022 International
Conference on Robotics and Automation (ICRA), pages 8591–8597. IEEE, 2022.
[671] Siddhant Haldar and Lerrel Pinto. Point policy: Unifying observations and actions with key
points for robot manipulation. In Conference on Robot Learning, 2025.
[672] Homanga Bharadhwaj, Abhinav Gupta, Shubham Tulsiani, and Vikash Kumar. Zero-shot
robot manipulation from passive human videos. arXiv preprint arXiv:2302.02011, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[673] Chao Tang, Anxing Xiao, Yuhong Deng, Tianrun Hu, Wenlong Dong, Hanbo Zhang, David
Hsu, and Hong Zhang. Mimicfunc: Imitating tool manipulation from a single human video
via functional correspondence. In Conference on Robot Learning, 2025.
[674] Bhawna Paliwal, Haritheja Etukuru, William Liang, Pieter Abbeel, Nur Muhammad Mahi
Shafiullah, and Jitendra Malik. Do as i do: Dexterous manipulation data from everyday
human videos. arXiv preprint arXiv:2606.19333, 2026.
[675] Gaotian Wang, Kejia Ren, Andrew Morgan, Yiting Chen, Howard H Qian, Podshara Chan-
rungmaneekul, and Kaiyu Hang. Egoinfinity: A web-scale 4d hand-object interaction data
engine for any-view robot retargeting and video-to-action robot learning. arXiv preprint
arXiv:2606.17385, 2026.
[676] Shuo Yang, Wei Zhang, Weizhi Lu, Hesheng Wang, and Yibin Li. Learning actions from human
demonstration video for robotic manipulation. In 2019 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 1805–1811. IEEE, 2019.
[677] De-An Huang, Yu-Wei Chao, Chris Paxton, Xinke Deng, Li Fei-Fei, Juan Carlos Niebles,
Animesh Garg, and Dieter Fox. Motion reasoning for goal-based imitation learning. In 2020
IEEE International Conference on Robotics and Automation (ICRA), pages 4878–4884. IEEE,
2020.
[678] Yuanlin Duan, Yuning Wang, Wenjie Qiu, and He Zhu. Learning from demonstrations
via capability-aware goal sampling. In Advances in Neural Information Processing Systems,
volume 38, pages 90760–90794, 2025.
[679] Yanlong Huang, Leonel Rozo, Joao Silvério, and Darwin G Caldwell. Non-parametric imitation
learning of robot motor skills. In 2019 International Conference on Robotics and Automation
(ICRA), pages 5266–5272. IEEE, 2019.
[680] Garrett Katz, Di-Wei Huang, Rodolphe Gentili, and James Reggia. Imitation learning as
cause-effect reasoning. In International Conference on Artificial General Intelligence, pages
64–73. Springer, 2016.
[681] Pratyusha Sharma, Deepak Pathak, and Abhinav Gupta. Third-person visual imitation learning
via decoupled hierarchical controller. In Advances in Neural Information Processing Systems,
volume 32, 2019.
[682] Yilun Hao, Ruinan Wang, Zhangjie Cao, Zihan Wang, Yuchen Cui, and Dorsa Sadigh. Masked
imitation learning: Discovering environment-invariant modalities in multimodal demonstra-
tions. In 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS),
pages 1–7. IEEE, 2023.
[683] Dionis Totsila, Konstantinos Chatzilygeroudis, Denis Hadjivelichkov, Valerio Modugno, Ioannis
Hatzilygeroudis, and Dimitrios Kanoulas. End-to-end stable imitation learning via autonomous
neural dynamic policies. arXiv preprint arXiv:2305.12886, 2023.
[684] Zifan Wang, Junyu Chen, Ziqing Chen, Pengwei Xie, Rui Chen, and Li Yi. Genh2r: learning
generalizable human-to-robot handover via scalable simulation demonstration and imitation.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
16362–16372, 2024.
[685] Kento Kawaharazuka, Yoichiro Kawamura, Kei Okada, and Masayuki Inaba. Imitation learn-
ing with additional constraints on motion style using parametric bias. IEEE Robotics and
Automation Letters, 6(3):5897–5904, 2021.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[686] Andrew Wagenmaker, Zhiyuan Zhou, and Sergey Levine. Behavioral exploration: Learning
to explore via in-context adaptation. In Forty-second International Conference on Machine
Learning, 2025.
[687] Yinlong Dai, Robert Ramirez Sanchez, Ryan Jeronimus, Shahabedin Sagheb, Cara M Nunez,
Heramb Nemlekar, and Dylan P Losey. Civil: Causal and intuitive visual imitation learning.
arXiv preprint arXiv:2504.17959, 2025.
[688] Mumuksh Tayal, Manan Tayal, and Ravi Prakash. Genosil: Generalized optimal and safe robot
control using parameter-conditioned imitation learning. arXiv preprint arXiv:2503.12243,
2025.
[689] Jingkai Xu and Xiangli Nie. Speci: Skill prompts based hierarchical continual imitation
learning for robot manipulation. IEEE Transactions on Cognitive and Developmental Systems,
2025.
[690] Wenbo Zhang, Yang Li, Yanyuan Qiao, Siyuan Huang, Jiajun Liu, Feras Dayoub, Xiao Ma,
and Lingqiao Liu. Effective tuning strategies for generalist robot manipulation policies. In
2025 IEEE International Conference on Robotics and Automation (ICRA), pages 7255–7262.
IEEE, 2025.
[691] Michael Drolet, Simon Stepputtis, Siva Kailas, Ajinkya Jain, Jan Peters, Stefan Schaal, and
Heni Ben Amor. A comparison of imitation learning algorithms for bimanual manipulation.
IEEE Robotics and Automation Letters, 2024.
[692] Zhao Mandi, Homanga Bharadhwaj, Vincent Moens, Shuran Song, Aravind Rajeswaran,
and Vikash Kumar. Cacti: A framework for scalable multi-task multi-scene visual imitation
learning. In CoRL 2022 Workshop on Pre-training Robot Learning, 2022.
[693] Murtaza Dalal, Ajay Mandlekar, Caelan Reed Garrett, Ankur Handa, Ruslan Salakhutdinov,
and Dieter Fox. Imitating task and motion planning with visuomotor transformers. In
Conference on Robot Learning, pages 2565–2593. PMLR, 2023.
[694] Cristian Alejandro Vergara Perico, Joris De Schutter, and Erwin Aertbeliën. Combining
imitation learning with constraint-based task specification and control. IEEE Robotics and
Automation Letters, 4(2):1892–1899, 2019.
[695] Ning Wang, Chuize Chen, and Alessandro Di Nuovo. A framework of hybrid force/motion
skills learning for robots. IEEE Transactions on Cognitive and Developmental Systems, 13(1):
162–170, 2020.
[696] Antonio Paolillo, Paolo Robuffo Giordano, and Matteo Saveriano. Dynamical system-based
imitation learning for visual servoing using the large projection formulation. In ICRA 2023-
IEEE International Conference on Robotics and Automation, pages 1–7. IEEE, 2023.
[697] Seyed Kamyar Seyed Ghasemipour, Richard Zemel, and Shixiang Gu. A divergence mini-
mization perspective on imitation learning methods. In Conference on robot learning, pages
1259–1277. PMLR, 2020.
[698] Rafael Rafailov, Tianhe Yu, Aravind Rajeswaran, and Chelsea Finn. Visual adversarial imitation
learning using variational models. Advances in Neural Information Processing Systems, 34:
3016–3028, 2021.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[699] Aleksandar Taranovic, Andras Gabor Kupcsik, Niklas Freymuth, and Gerhard Neumann.
Adversarial imitation learning with preferences. In The Eleventh International Conference on
Learning Representations, 2023.
[700] Wenjia Zhang, Haoran Xu, Haoyi Niu, Peng Cheng, Ming Li, Heming Zhang, Guyue Zhou, and
Xianyuan Zhan. Discriminator-guided model-based offline imitation learning. In Conference
on robot learning, pages 1266–1276. PMLR, 2023.
[701] Dafni Antotsiou, Carlo Ciliberto, and Tae-Kyun Kim. Adversarial imitation learning with
trajectorial augmentation and correction. In 2021 IEEE International Conference on Robotics
and Automation (ICRA), pages 4724–4730. IEEE, 2021.
[702] Trevor Ablett, Bryan Chan, and Jonathan Kelly. Learning from guided play: A scheduled
hierarchical approach for improving exploration in adversarial imitation learning. arXiv
preprint arXiv:2112.08932, 2021.
[703] Ankur Deka, Changliu Liu, and Katia P Sycara. Arc-actor residual critic for adversarial
imitation learning. In Conference on robot learning, pages 1446–1456. PMLR, 2023.
[704] Manu Orsini, Anton Raichuk, Léonard Hussenot, Damien Vincent, Robert Dadashi, Sertan
Girgin, Matthieu Geist, Olivier Bachem, Olivier Pietquin, and Marcin Andrychowicz. What
matters for adversarial imitation learning? Advances in Neural Information Processing Systems,
34:14656–14668, 2021.
[705] Zhixin Jia, Mengxiang Lin, Zhixin Chen, and Shibo Jian. Vision-based robot manipulation
learning via human demonstrations. arXiv preprint arXiv:2003.00385, 2020.
[706] Dong Liu, Binpeng Lu, Ming Cong, Honghua Yu, Qiang Zou, and Yu Du. Robotic manipulation
skill acquisition via demonstration policy learning.
IEEE Transactions on Cognitive and
Developmental Systems, 14(3):1054–1065, 2021.
[707] Vitalis Vosylius and Edward Johns. Few-shot in-context imitation learning via implicit graph
alignment. In Conference on Robot Learning, pages 3194–3213. PMLR, 2023.
[708] Manuel Mühlig, Michael Gienger, and Jochen J Steil. Interactive imitation learning of object
movement skills. Autonomous Robots, 32(2):97–114, 2012.
[709] Eugenio Chisari, Tim Welschehold, Joschka Boedecker, Wolfram Burgard, and Abhinav Valada.
Correct me if i am wrong: Interactive learning for robotic manipulation. IEEE Robotics and
Automation Letters, 7(2):3695–3702, 2022.
[710] Ajay Mandlekar, Caelan Reed Garrett, Danfei Xu, and Dieter Fox. Human-in-the-loop task and
motion planning for imitation learning. In Conference on Robot Learning, pages 3030–3060.
PMLR, 2023.
[711] Hamidreza Kasaei and Mohammadreza Kasaei. Vital: Interactive few-shot imitation learning
via visual human-in-the-loop corrections. arXiv preprint arXiv:2407.21244, 2024.
[712] Philipp Wu, Yide Shentu, Qiayuan Liao, Ding Jin, Menglong Guo, Koushil Sreenath, Xingyu
Lin, and Pieter Abbeel. Robocopilot: Human-in-the-loop interactive imitation learning for
robot manipulation. arXiv preprint arXiv:2503.07771, 2025.
[713] Jonas Werner, Kun Chu, Cornelius Weber, and Stefan Wermter. Llm-based interactive imitation
learning for robotic manipulation. In 2025 International Joint Conference on Neural Networks
(IJCNN), pages 1–9. IEEE, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[714] Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng,
and Ruoshi Wen. Hand-in-the-loop: Improving vla policies for dexterous manipulation via
seamless hand-arm intervention. arXiv preprint arXiv:2605.15157, 2026.
[715] Huihan Liu, Shivin Dass, Roberto Martín-Martín, and Yuke Zhu. Model-based runtime
monitoring with interactive imitation learning. In 2024 IEEE International Conference on
Robotics and Automation (ICRA), pages 4154–4161. IEEE, 2024.
[716] George Jiayuan Gao, Tianyu Li, and Nadia Figueroa. Out-of-distribution recovery with
object-centric keypoint inverse policy for visuomotor imitation learning. In 2025 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), 2025.
[717] Aleksandra Kalinowska, Ahalya Prabhakar, Kathleen Fitzsimons, and Todd Murphey. Ergodic
imitation: Learning from what to do and what not to do. In 2021 IEEE International Conference
on Robotics and Automation (ICRA), pages 3648–3654. IEEE, 2021.
[718] Minghua Liu, Xuanlin Li, Zhan Ling, Yangyan Li, and Hao Su. Frame mining: a free lunch for
learning robotic manipulation from 3d point clouds. In Conference on Robot Learning, pages
527–538. PMLR, 2023.
[719] Peter Pastor, Mrinal Kalakrishnan, Sachin Chitta, Evangelos Theodorou, and Stefan Schaal.
Skill learning and task outcome prediction for manipulation. In 2011 IEEE international
conference on robotics and automation, pages 3828–3834. IEEE, 2011.
[720] Karl Pertsch, Youngwoon Lee, Yue Wu, and Joseph J Lim. Guided reinforcement learning
with learned skills. In Conference on Robot Learning, pages 729–739. PMLR, 2021.
[721] Albert Zhan, Ruihan Zhao, Lerrel Pinto, Pieter Abbeel, and Michael Laskin. A framework for
efficient robotic manipulation. In Deep RL Workshop NeurIPS 2021, 2021.
[722] Stephen James and Andrew J Davison. Q-attention: Enabling efficient learning for vision-
based robotic manipulation. IEEE Robotics and Automation Letters, 7(2):1612–1619, 2022.
[723] Joe Watson, Sandy Huang, and Nicolas Heess. Coherent soft imitation learning. Advances in
Neural Information Processing Systems, 36:14540–14583, 2023.
[724] Amisha Bhaskar, Zahiruddin Mahammad, Sachin R Jadhav, and Pratap Tokekar. Planrl: A
motion planning and imitation learning framework to bootstrap reinforcement learning. arXiv
preprint arXiv:2408.04054, 2024.
[725] H Sikchi, A Zhang, and S Niekum. Dual rl: Unification and new methods for reinforcement
and imitation learning. In International Conference on Learning Representations. International
Conference on Learning Representations, 2024.
[726] Peihong Yu, Amisha Bhaskar, Anukriti Singh, Zahiruddin Mahammad, and Pratap Tokekar.
Sketch-to-skill: Bootstrapping robot learning with human drawn trajectory sketches. In
Robotics: Science and Systems, 2025.
[727] Matthew M Hong, Jesse Zhang, Anusha Nagabandi, and Abhishek Gupta. Tmrl: Diffusion
timestep-modulated pretraining enables exploration for efficient policy finetuning. arXiv
preprint arXiv:2605.12236, 2026.
[728] Kun Lei, Huanyu Li, Dongjie Yu, Zhenyu Wei, Lingxiao Guo, Zhennan Jiang, Ziyu Wang,
Shiyu Liang, and Huazhe Xu. Rl-100: Performant robotic manipulation with real-world
reinforcement learning. arXiv preprint arXiv:2510.14830, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[729] Dongjie Yu, Kun Lei, Zhennan Jiang, Jia Pan, and Huazhe Xu. Beyond action residuals:
Real-world robot policy steering via bottleneck latent reinforcement learning. arXiv preprint
arXiv:2605.19919, 2026.
[730] Lakshita Dodeja, Ondrej Biza, Shivam Vats, Stephen Hart, Stefanie Tellex, Robin Walters,
Karl Schmeckpeper, and Thomas Weng. When life gives you bc, make q-functions: Ex-
tracting q-values from behavior cloning for on-robot reinforcement learning. arXiv preprint
arXiv:2605.05172, 2026.
[731] I-Chun Arthur Liu, Shagun Uppal, Gaurav S Sukhatme, Joseph J Lim, Peter Englert, and
Youngwoon Lee. Distilling motion planner augmented policies into visual control policies for
robot manipulation. In Conference on Robot Learning, pages 641–650. PMLR, 2022.
[732] Alex X Lee, Coline Devin, Jost Tobias Springenberg, Yuxiang Zhou, Thomas Lampe, Abbas Ab-
dolmaleki, and Konstantinos Bousmalis. How to spend your robot time: Bridging kickstarting
and offline reinforcement learning for vision-based robotic manipulation. In 2022 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 2468–2475. IEEE,
2022.
[733] Chelsea Finn, Sergey Levine, and Pieter Abbeel. Guided cost learning: Deep inverse optimal
control via policy optimization. In International conference on machine learning, pages 49–58.
PMLR, 2016.
[734] Daniel S Brown, Wonjoon Goo, and Scott Niekum. Better-than-demonstrator imitation
learning via automatically-ranked demonstrations. In Conference on robot learning, pages
330–359. PMLR, 2020.
[735] YuXuan Liu, Abhishek Gupta, Pieter Abbeel, and Sergey Levine. Imitation from observa-
tion: Learning to imitate behaviors from raw video via context translation. In 2018 IEEE
international conference on robotics and automation (ICRA), pages 1118–1125. IEEE, 2018.
[736] Haoyu Xiong, Quanzhou Li, Yun-Chun Chen, Homanga Bharadhwaj, Samarth Sinha, and
Animesh Garg. Learning by watching: Physical imitation of manipulation skills from human
videos. In 2021 IEEE/RSJ international conference on intelligent robots and systems (iros),
pages 7827–7834. IEEE, 2021.
[737] Youngwoon Lee, Andrew Szot, Shao-Hua Sun, and Joseph J Lim. Generalizable imitation
learning from observation via inferring goal proximity.
Advances in neural information
processing systems, 34:16118–16130, 2021.
[738] Siddhant Haldar, Vaibhav Mathur, Denis Yarats, and Lerrel Pinto. Watch and match: Su-
percharging imitation with regularized optimal transport. In Conference on Robot Learning,
pages 32–43. PMLR, 2023.
[739] Sumedh Sontakke, Jesse Zhang, Séb Arnold, Karl Pertsch, Erdem Bıyık, Dorsa Sadigh, Chelsea
Finn, and Laurent Itti. Roboclip: One demonstration is enough to learn robot policies. Advances
in Neural Information Processing Systems, 36:55681–55693, 2023.
[740] Ajay Mandlekar, Fabio Ramos, Byron Boots, Silvio Savarese, Li Fei-Fei, Animesh Garg, and
Dieter Fox. Iris: Implicit reinforcement without interaction at scale for learning control
from offline robot manipulation data. In 2020 IEEE International Conference on Robotics and
Automation (ICRA), pages 4414–4420. IEEE, 2020.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[741] Konrad Zolna, Alexander Novikov, Ksenia Konyushkova, Caglar Gulcehre, Ziyu Wang, Yusuf
Aytar, Misha Denil, Nando De Freitas, and Scott Reed. Offline learning from demonstrations
and unlabeled experience. arXiv preprint arXiv:2011.13885, 2020.
[742] Yuke Zhu, Ziyu Wang, Josh Merel, Andrei Rusu, Tom Erez, Serkan Cabi, Saran Tunyasuvu-
nakool, János Kramár, Raia Hadsell, Nando de Freitas, et al. Reinforcement and imitation
learning for diverse visuomotor skills. In Robotics: Science and Systems, 2018.
[743] William Huey, Huaxiaoyue Wang, Anne Wu, Yoav Artzi, and Sanjiban Choudhury. Imitation
learning from a single temporally misaligned video. In Proceedings of the 42nd International
Conference on Machine Learning, 2025.
[744] Lin Shao, Toki Migimatsu, Qiang Zhang, Karen Yang, and Jeannette Bohg. Concept2robot:
Learning manipulation concepts from instructions and human demonstrations. The Interna-
tional Journal of Robotics Research, 40(12-14):1419–1434, 2021.
[745] Rohit Jena, Changliu Liu, and Katia Sycara. Augmenting gail with bc for sample efficient
imitation learning. In Conference on Robot Learning, pages 80–90. PMLR, 2021.
[746] Yao Lu, Karol Hausman, Yevgen Chebotar, Mengyuan Yan, Eric Jang, Alexander Herzog, Ted
Xiao, Alex Irpan, Mohi Khansari, Dmitry Kalashnikov, et al. Aw-opt: Learning robotic skills
with imitation and reinforcement at scale. In Conference on Robot Learning, pages 1078–1088.
PMLR, 2022.
[747] Malte Mosbach, Kara Moraw, and Sven Behnke. Accelerating interactive human-like ma-
nipulation learning with gpu-based simulation and high-quality demonstrations. In 2022
IEEE-RAS 21st International Conference on Humanoid Robots (Humanoids), pages 435–441.
IEEE, 2022.
[748] Dechen Gao, Hang Wang, Hanchu Zhou, Nejib Ammar, Shatadal Mishra, Ahmadreza Moradi-
pari, Iman Soltani, and Junshan Zhang. In-ril: Interleaved reinforcement and imitation
learning for policy fine-tuning. arXiv preprint arXiv:2505.10442, 2025.
[749] Yinsen Jia and Boyuan Chen.
Temporal self-imitation learning.
arXiv preprint
arXiv:2606.19752, 2026.
[750] Yinuo Zhao, Huiqian Jin, Lechun Jiang, Xinyi Zhang, Kun Wu, Pei Ren, Zhiyuan Xu, Zheng-
ping Che, Lei Sun, Dapeng Wu, et al. Real-world reinforcement learning from suboptimal
interventions. arXiv preprint arXiv:2512.24288, 2025.
[751] Christopher R Dance, Julien Perez, and Théo Cachet. Conditioned reinforcement learning
for few-shot imitation. In International Conference on Machine Learning, pages 2376–2387.
PMLR, 2021.
[752] Pierre Sermanet, Kelvin Xu, and Sergey Levine. Unsupervised perceptual rewards for imitation
learning. In Robotics: Science and Systems, 2017.
[753] Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek
Gupta. Unified world models: Coupling video and action diffusion for pretraining on large
robotic datasets. In Robotics: Science and Systems, 2025.
[754] Zijian Song, Sihan Qin, Tianshui Chen, Liang Lin, and Guangrun Wang.
Physical au-
toregressive model for robotic manipulation without action pretraining.
arXiv preprint
arXiv:2508.09822, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[755] Siqiao Huang, Jialong Wu, Qixing Zhou, Shangchen Miao, and Mingsheng Long. Vid2world:
Crafting video diffusion models to interactive world models. In The Fourteenth International
Conference on Learning Representations, 2026.
[756] Raktim Goswami, Prashanth Krishnamurthy, Yann LeCun, and Farshad Khorrami. Osvi-wm:
One-shot visual imitation for unseen tasks using world-model-guided trajectory generation.
Advances in Neural Information Processing Systems, 38:54725–54745, 2025.
[757] Leonardo Barcellona, Andrii Zadaianchuk, Davide Allegro, Samuele Papa, Stefano Ghidoni,
and Efstratios Gavves. Dream to manipulate: Compositional world models empowering robot
imitation learning with imagination. In The Thirteenth International Conference on Learning
Representations, 2025.
[758] Wentao Zhao, Jiaming Chen, Ziyu Meng, Donghui Mao, Ran Song, and Wei Zhang. Vlmpc:
Vision-language model predictive control for robotic manipulation. In Robotics: Science and
Systems, 2024.
[759] Russell Mendonca, Shikhar Bahl, and Deepak Pathak. Structured world models from human
videos. In Robotics: Science and Systems, 2023.
[760] Guanxing Lu, Shiyi Zhang, Ziwei Wang, Changliu Liu, Jiwen Lu, and Yansong Tang. Manigaus-
sian: Dynamic gaussian splatting for multi-task robotic manipulation. In European Conference
on Computer Vision, pages 349–366. Springer, 2024.
[761] Tengbo Yu, Guanxing Lu, Zaijia Yang, Haoyuan Deng, Season Si Chen, Jiwen Lu, Wenbo Ding,
Guoqiang Hu, Yansong Tang, and Ziwei Wang. Manigaussian++: General robotic bimanual
manipulation with hierarchical gaussian world model.
In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), 2025.
[762] Xiuyu Yang, Bohan Li, Shaocong Xu, Nan Wang, Chongjie Ye, Zhaoxi Chen, Minghan Qin,
Yikang Ding, Xin Jin, Hang Zhao, et al. Orv: 4d occupancy-centric robot video generation. In
Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2026.
[763] Suning Huang, Qianzhong Chen, Xiaohan Zhang, Jiankai Sun, and Mac Schwager. Particle-
former: A 3d point cloud world model for multi-object, multi-material robotic manipulation.
In Conference on Robot Learning, 2025.
[764] Ying Chai, Litao Deng, Ruizhi Shao, Jiajun Zhang, Liangjun Xing, Hongwen Zhang, and Yebin
Liu. Gaf: Gaussian action field as a dynamic world model for robotic manipulation. arXiv
preprint arXiv:2506.14135, 2025.
[765] Hongyan Zhi, Peihao Chen, Siyuan Zhou, Yubo Dong, Quanxi Wu, Lei Han, and Mingkui Tan.
3dflowaction: Learning cross-embodiment manipulation from 3d flow world model. arXiv
preprint arXiv:2506.06199, 2025.
[766] Rafael Rafailov, Kyle Beltran Hatch, Victor Kolev, John D Martin, Mariano Phielipp, and
Chelsea Finn. Moto: Offline pre-training to online fine-tuning for model-based robot learning.
In Conference on Robot Learning, pages 3654–3671. PMLR, 2023.
[767] Yunhai Feng, Nicklas Hansen, Ziyan Xiong, Chandramouli Rajagopalan, and Xiaolong Wang.
Finetuning offline world models in the real world. In Conference on Robot Learning, pages
425–445. PMLR, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[768] Akshay L Chandra, Iman Nematollahi, Chenguang Huang, Tim Welschehold, Wolfram Bur-
gard, and Abhinav Valada. Diwa: Diffusion policy adaptation with world models. In Conference
on Robot Learning, 2025.
[769] Iman Nematollahi, Branton DeMoss, Akshay L Chandra, Nick Hawes, Wolfram Burgard, and
Ingmar Posner. Lumos: Language-conditioned imitation learning with world models. In 2025
IEEE International Conference on Robotics and Automation (ICRA), 2025.
[770] Jing-Cheng Pang, Nan Tang, Kaiyuan Li, Yuting Tang, Xin-Qiang Cai, Zhen-Yu Zhang, Gang
Niu, Masashi Sugiyama, and Yang Yu. Learning view-invariant world models for visual robotic
manipulation. In The Thirteenth International Conference on Learning Representations, 2025.
[771] Pengzhen Ren, Kaidong Zhang, Hetao Zheng, Zixuan Li, Yuhang Wen, Fengda Zhu, Mas Ma,
and Xiaodan Liang. Surfer: Progressive reasoning with world models for robotic manipulation.
arXiv preprint arXiv:2306.11335, 2023.
[772] Younggyo Seo, Junsu Kim, Stephen James, Kimin Lee, Jinwoo Shin, and Pieter Abbeel. Multi-
view masked world models for visual robotic manipulation. In International Conference on
Machine Learning, pages 30613–30632. PMLR, 2023.
[773] Xinyue Wang and Biwei Huang. Modeling unseen environments with language-guided
composable causal components in reinforcement learning. In The Thirteenth International
Conference on Learning Representations, 2025.
[774] Yi Zhao, Aidan Scannell, Yuxin Hou, Tianyu Cui, Le Chen, Dieter Büchler, Arno Solin, Juho
Kannala, and Joni Pajarinen. Generalist world model pre-training for efficient reinforcement
learning. In ICLR 2025 Workshop on World Models: Understanding, Modelling and Scaling,
2025.
[775] Adrià López Escoriza, Nicklas Hansen, Stone Tao, Tongzhou Mu, and Hao Su. Multi-stage
manipulation with demonstration-augmented reward, policy, and world model learning. In
Forty-second International Conference on Machine Learning, 2025.
[776] Shangzhe Li, Zhiao Huang, and Hao Su. Coupled distributional random expert distillation
for world model online imitation learning. arXiv preprint arXiv:2505.02228, 2025.
[777] Tenny Yin, Zhiting Mei, Tao Sun, Lihan Zha, Emily Zhou, Jeremy Bao, Miyu Yamane, Ola
Sho, and Anirudha Majumdar. Womap: World models for embodied open-vocabulary ob-
ject localization. In RSS 2025 Workshop: Mobile Manipulation: Emerging Opportunities &
Contemporary Challenges, 2025.
[778] Huihan Liu, Yu Zhang, Vaarij Betala, Evan Zhang, James Liu, Crystal Ding, and Yuke Zhu.
Multi-task interactive robot fleet learning with visual world models. In Conference on Robot
Learning, pages 4286–4313. PMLR, 2025.
[779] Niket Agarwal, Arslan Ali, Maciej Bala, Yogesh Balaji, Erik Barker, Tiffany Cai, Prithvijit
Chattopadhyay, Yongxin Chen, Yin Cui, Yifan Ding, et al. Cosmos world foundation model
platform for physical ai. arXiv preprint arXiv:2501.03575, 2025.
[780] Yue Liao, Pengfei Zhou, Siyuan Huang, Donglin Yang, Shengcong Chen, Yuxin Jiang, Yue
Hu, Si Liu, Jianlan Luo, Liliang Chen, et al. Genie envisioner: A unified world foundation
platform for robotic manipulation. In International Conference on Learning Representations,
volume 2026, pages 88446–88463, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[781] Zhengtong Xu, Qiang Qiu, and Yu She. Vilp: Imitation learning with latent video planning.
IEEE Robotics and Automation Letters, 2025.
[782] Junbang Liang, Pavel Tokmakov, Ruoshi Liu, Sruthi Sudhakar, Paarth Shah, Rares Ambrus,
and Carl Vondrick. Video generators are robot policies. arXiv preprint arXiv:2508.00795,
2025.
[783] Hongtao Wu, Ya Jing, Chilam Cheang, Guangzeng Chen, Jiafeng Xu, Xinghang Li, Minghuan
Liu, Hang Li, and Tao Kong. Unleashing large-scale video generative pre-training for visual
robot manipulation. In The Twelfth International Conference on Learning Representations,
2024.
[784] Peiyan Li, Hongtao Wu, Yan Huang, Chilam Cheang, Liang Wang, and Tao Kong. Gr-mg:
Leveraging partially-annotated data via multi-modal goal-conditioned policy. IEEE Robotics
and Automation Letters, 2025.
[785] Chi-Lam Cheang, Guangzeng Chen, Ya Jing, Tao Kong, Hang Li, Yifeng Li, Yuxiao Liu,
Hongtao Wu, Jiafeng Xu, Yichu Yang, et al. Gr-2: A generative video-language-action model
with web-scale knowledge for robot manipulation. arXiv preprint arXiv:2410.06158, 2024.
[786] Homanga Bharadhwaj, Abhinav Gupta, Vikash Kumar, and Shubham Tulsiani. Towards
generalizable zero-shot manipulation via translating human interaction plans. In 2024 IEEE
International Conference on Robotics and Automation (ICRA), pages 6904–6911. IEEE, 2024.
[787] Homanga Bharadhwaj, Debidatta Dwibedi, Abhinav Gupta, Shubham Tulsiani, Carl Doersch,
Ted Xiao, Dhruv Shah, Fei Xia, Dorsa Sadigh, and Sean Kirmani. Gen2act: Human video
generation in novel scenarios enables generalizable robot manipulation. Conference on Robot
Learning, 2025.
[788] Liang Heng, Xiaoqi Li, Shangqing Mao, Jiaming Liu, Ruolin Liu, Jingli Wei, Yu-Kai Wang,
Yueru Jia, Chenyang Gu, Rui Zhao, et al. Rwor: Generating robot demonstrations from
human hand collection for policy learning without robot. In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 13544–13551. IEEE, 2025.
[789] Litao Liu, Wentao Wang, Yifan Han, Zhuoli Xie, Pengfei Yi, Junyan Li, and Wenzhao Lian.
Foam: Foresight-augmented multi-task imitation policy for robotic manipulation. In Pro-
ceedings of the AAAI Conference on Artificial Intelligence, volume 40, pages 18460–18468,
2026.
[790] Yucheng Hu, Yanjiang Guo, Pengchao Wang, Xiaoyu Chen, Yen-Jen Wang, Jianke Zhang,
Koushil Sreenath, Chaochao Lu, and Jianyu Chen. Video prediction policy: A generalist robot
policy with predictive visual representations. In Forty-second International Conference on
Machine Learning, 2025.
[791] Yang Tian, Sizhe Yang, Jia Zeng, Ping Wang, Dahua Lin, Hao Dong, and Jiangmiao Pang.
Predictive inverse dynamics models are scalable learners for robotic manipulation. In The
Thirteenth International Conference on Learning Representations, 2025.
[792] Kevin Black, Mitsuhiko Nakamoto, Pranav Atreya, Homer Rich Walke, Chelsea Finn, Aviral
Kumar, and Sergey Levine. Zero-shot robotic manipulation with pre-trained image-editing
diffusion models. In The Twelfth International Conference on Learning Representations, 2024.
[793] Chang Nie, Guangming Wang, Zhe Lie, and Hesheng Wang. Ermv: Editing 4d robotic
multi-view images to enhance embodied agents. arXiv preprint arXiv:2507.17462, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[794] Qingwen Bu, Jia Zeng, Li Chen, Yanchao Yang, Guyue Zhou, Junchi Yan, Ping Luo, Heming
Cui, Yi Ma, and Hongyang Li. Closed-loop visuomotor control with generative expectation for
robotic manipulation. Advances in Neural Information Processing Systems, 37:139002–139029,
2024.
[795] Hongyin Zhang, Pengxiang Ding, Shangke Lyu, Ying Peng, and Donglin Wang. Gevrm:
Goal-expressive video generation model for robust visual manipulation. In The Thirteenth
International Conference on Learning Representations, 2025.
[796] Kyle B Hatch, Ashwin Balakrishna, Oier Mees, Suraj Nair, Seohong Park, Blake Wulfe, Masha
Itkina, Benjamin Eysenbach, Sergey Levine, Thomas Kollar, et al. Ghil-glue: Hierarchical
control with filtered subgoal images. arXiv preprint arXiv:2410.20018, 2024.
[797] Haonan Chen, Bangjun Wang, Jingxiang Guo, Tianrui Zhang, Yiwen Hou, Xuchuan Huang,
Chenrui Tie, and Lin Shao. World4omni: A zero-shot framework from image generation
world model to robotic manipulation. arXiv preprint arXiv:2506.23919, 2025.
[798] Takeru Oba and Norimichi Ukita. Future-guided offline imitation learning for long action
sequences via video interpolation and future-trajectory prediction. Neurocomputing, 547:
126325, 2023.
[799] Achint Soni, Sreyas Venkataraman, Abhranil Chandra, Sebastian Fischmeister, Percy Liang,
Bo Dai, and Sherry Yang. Videoagent: Self-improving video generation. arXiv preprint
arXiv:2410.10076, 2024.
[800] Youpeng Wen, Junfan Lin, Yi Zhu, Jianhua Han, Hang Xu, Shen Zhao, and Xiaodan Liang.
Vidman: Exploiting implicit dynamics from video diffusion model for effective robot manipu-
lation. Advances in Neural Information Processing Systems, 37:41051–41075, 2024.
[801] Suraj Nair, Aravind Rajeswaran, Vikash Kumar, Chelsea Finn, and Abhinav Gupta. R3m:
A universal visual representation for robot manipulation. In Conference on Robot Learning,
pages 892–909. PMLR, 2023.
[802] Teli Ma, Jiaming Zhou, Zifan Wang, Ronghe Qiu, and Junwei Liang. Contrastive imitation
learning for language-guided multi-task robotic manipulation. In Conference on Robot Learning,
pages 4651–4669. PMLR, 2025.
[803] Yanjie Ze, Ge Yan, Yueh-Hua Wu, Annabella Macaluso, Yuying Ge, Jianglong Ye, Nicklas
Hansen, Li Erran Li, and Xiaolong Wang. Gnfactor: Multi-task real robot learning with
generalizable neural feature fields. In Conference on robot learning, pages 284–301. PMLR,
2023.
[804] Siddharth Karamcheti, Suraj Nair, Annie S Chen, Thomas Kollar, Chelsea Finn, Dorsa Sadigh,
and Percy Liang. Language-driven representation learning for robotics. In Robotics: Science
and Systems, 2023.
[805] Yinpei Dai, Jayjun Lee, Nima Fazeli, and Joyce Chai. Racer: Rich language-guided failure
recovery policies for imitation learning. In 2025 IEEE international conference on robotics and
automation (ICRA), pages 15657–15664. IEEE, 2025.
[806] Liquan Wang, Ankit Goyal, Haoping Xu, and Animesh Garg. Discovering robotic interaction
modes with discrete representation learning. In Conference on Robot Learning, pages 830–863.
PMLR, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[807] Ian Chuang, Andrew Lee, Dechen Gao, Jinyu Zou, and Iman Soltani. Look, focus, act:
Efficient and robust robot learning via human gaze and foveated vision transformers. arXiv
preprint arXiv:2507.15833, 2025.
[808] Xiaolin Fang, Bo-Ruei Huang, Jiayuan Mao, Jasmine Shone, Joshua B Tenenbaum, Tomás
Lozano-Pérez, and Leslie Pack Kaelbling. Keypoint abstraction using large models for object-
relative imitation learning. In 2025 IEEE International Conference on Robotics and Automation
(ICRA), 2025.
[809] Youngsun Wi, Mark Van der Merwe, Pete Florence, Andy Zeng, and Nima Fazeli. Calamari:
Contact-aware and language conditioned spatial action mapping for contact-rich manipulation.
In Conference on Robot Learning, pages 2753–2771. PMLR, 2023.
[810] Dongjie Yu, Hang Xu, Yizhou Chen, Yi Ren, and Jia Pan. Bikc: Keypose-conditioned consistency
policy for bimanual robotic manipulation. In International Workshop on the Algorithmic
Foundations of Robotics, pages 283–302. Springer, 2024.
[811] Lucy Xiaoyang Shi, Archit Sharma, Tony Z Zhao, and Chelsea Finn. Waypoint-based imitation
learning for robotic manipulation. In Conference on Robot Learning, pages 2195–2209. PMLR,
2023.
[812] Shaunak A Mehta, Heramb Nemlekar, Hari Sumant, and Dylan P Losey. L2d2: Robot learning
from 2d drawings. Autonomous Robots, 49(3):25, 2025.
[813] Chuan Wen, Xingyu Lin, John So, Kai Chen, Qi Dou, Yang Gao, and Pieter Abbeel. Any-point
trajectory modeling for policy learning. In Robotics: Science and Systems, 2024.
[814] Mengda Xu, Zhenjia Xu, Yinghao Xu, Cheng Chi, Gordon Wetzstein, Manuela Veloso, and
Shuran Song. Flow as the cross-domain manipulation interface. In Conference on Robot
Learning, pages 2475–2499. PMLR, 2025.
[815] Yifeng Zhu, Abhishek Joshi, Peter Stone, and Yuke Zhu. Viola: Imitation learning for vision-
based manipulation with object proposal priors. In Conference on Robot Learning, pages
1199–1210. PMLR, 2023.
[816] Xiang Li, Cristina Mata, Jongwoo Park, Kumara Kahatapitiya, Yoo Jang, Jinghuan Shang,
Kanchana Ranasinghe, Ryan Burgert, Mu Cai, Yong Jae Lee, et al. Llara: Supercharging
robot learning data for vision-language policy.
In International Conference on Learning
Representations, volume 2025, pages 57463–57509, 2025.
[817] Yuhang Dong, Haizhou Ge, Yupei Zeng, Jiangning Zhang, Beiwen Tian, Guanzhong Tian, Hon-
grui Zhu, Yufei Jia, Ruixiang Wang, Ran Yi, et al. Imit diff: Semantics guided diffusion trans-
former with dual resolution fusion for imitation learning. arXiv preprint arXiv:2502.09649,
2025.
[818] Shizhe Chen, Ricardo Garcia, Paul Pacaud, and Cordelia Schmid. Gondola: Grounded vision
language planning for generalizable robotic manipulation. arXiv preprint arXiv:2506.11261,
2025.
[819] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Qing Jiang, Chunyuan
Li, Jianwei Yang, Hang Su, et al. Grounding dino: Marrying dino with grounded pre-training
for open-set object detection. In European conference on computer vision, pages 38–55. Springer,
2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[820] Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson,
Tete Xiao, Spencer Whitehead, Alexander C Berg, Wan-Yen Lo, et al. Segment anything. In
Proceedings of the IEEE/CVF international conference on computer vision, pages 4015–4026,
2023.
[821] Heecheol Kim, Yoshiyuki Ohmura, and Yasuo Kuniyoshi. Gaze-based dual resolution deep imi-
tation learning for high-precision dexterous robot manipulation. IEEE Robotics and Automation
Letters, 6(2):1630–1637, 2021.
[822] Heecheol Kim, Yoshiyuki Ohmura, and Yasuo Kuniyoshi. Using human gaze to improve ro-
bustness against irrelevant objects in robot manipulation tasks. IEEE Robotics and Automation
Letters, 5(3):4415–4422, 2020.
[823] Shogo Hamano, Heecheol Kim, Yoshiyuki Ohmura, and Yasuo Kuniyoshi. Using human
gaze in few-shot imitation learning for robot manipulation. In 2022 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 8622–8629. IEEE, 2022.
[824] Heecheol Kim, Yoshiyuki Ohmura, and Yasuo Kuniyoshi. Memory-based gaze prediction in
deep imitation learning for robot manipulation. In 2022 International Conference on Robotics
and Automation (ICRA), pages 2427–2433. IEEE, 2022.
[825] Ryo Takizawa, Yoshiyuki Ohmura, and Yasuo Kuniyoshi. Gaze-guided task decomposition for
imitation learning in robotic manipulation. In 2025 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 7965–7972. IEEE, 2025.
[826] Ryo Takizawa, Izumi Karino, Koki Nakagawa, Yoshiyuki Ohmura, and Yasuo Kuniyoshi.
Enhancing reusability of learned skills for robot manipulation via gaze information and
motion bottlenecks. IEEE Robotics and Automation Letters, 2025.
[827] Chen Wang, Rui Wang, Ajay Mandlekar, Li Fei-Fei, Silvio Savarese, and Danfei Xu. Gener-
alization through hand-eye coordination: An action space for learning spatially-invariant
visuomotor control. In 2021 IEEE/RSJ International Conference on Intelligent Robots and
Systems (IROS), pages 8913–8920. IEEE, 2021.
[828] Zhuoling Li, Liangliang Ren, Jinrong Yang, Yong Zhao, Xiaoyang Wu, Zhenhua Xu, Xiang Bai,
and Hengshuang Zhao. Virt: Vision instructed transformer for robotic manipulation. arXiv
e-prints, pages arXiv–2410, 2024.
[829] Jianfeng Gao, Zhi Tao, Noémie Jaquier, and Tamim Asfour. K-vil: Keypoints-based visual
imitation learning. IEEE Transactions on Robotics, 39(5):3888–3908, 2023.
[830] Jianfeng Gao, Xiaoshu Jin, Franziska Krebs, Noémie Jaquier, and Tamim Asfour. Bi-kvil:
Keypoints-based visual imitation learning of bimanual manipulation tasks. In 2024 IEEE
International Conference on Robotics and Automation (ICRA), pages 16850–16857. IEEE, 2024.
[831] Shengjie Wang, Jiacheng You, Yihang Hu, Jiongye Li, and Yang Gao. Skil: Semantic keypoint
imitation learning for generalizable data-efficient manipulation. In Robotics: Science and
Systems, 2025.
[832] Yunchu Zhang, Shubham Mittal, Zhengyu Zhang, Liyiming Ke, Siddhartha Srinivasa, and
Abhishek Gupta. Atk: Automatic task-driven keypoint selection for robust policy learning. In
9th Annual Conference on Robot Learning, 2025.
[833] Norman Di Palo and Edward Johns. Keypoint action tokens enable in-context imitation
learning in robotics. In Robotics: Science and Systems, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[834] Yi Li, Yuquan Deng, Jesse Zhang, Joel Jang, Marius Memmel, Caelan Reed Garrett, Fabio
Ramos, Dieter Fox, Anqi Li, Abhishek Gupta, et al. Hamster: Hierarchical action models
for open-world robot manipulation. In The Thirteenth International Conference on Learning
Representations, 2025.
[835] Zhuochen Miao, Jun Lv, Hongjie Fang, Yang Jin, and Cewu Lu. Knowledge-driven imitation
learning: Enabling generalization across diverse conditions. In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 9800–9807. IEEE, 2025.
[836] Jingxian Lu, Wenke Xia, Dong Wang, Zhigang Wang, Bin Zhao, Di Hu, and Xuelong Li. Koi:
Accelerating online imitation learning via hybrid key-state guidance. In Conference on Robot
Learning, pages 3847–3865. PMLR, 2025.
[837] Ananth Jonnavittula, Sagar Parekh, and Dylan P. Losey. View: Visual imitation learning with
waypoints. Autonomous Robots, 49(1):5, 2025.
[838] Yinpei Dai, Jayjun Lee, Yichi Zhang, Ziqiao Ma, Jed Yang, Amir Zadeh, Chuan Li, Nima
Fazeli, and Joyce Chai. Aimbot: A simple auxiliary visual cue to enhance spatial awareness
of visuomotor policies. In Conference on Robot Learning, 2026.
[839] Juntao Ren, Priya Sundaresan, Dorsa Sadigh, Sanjiban Choudhury, and Jeannette Bohg.
Motion tracks: A unified representation for human-robot transfer in few-shot imitation
learning. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages
8802–8810. IEEE, 2025.
[840] Homanga Bharadhwaj, Roozbeh Mottaghi, Abhinav Gupta, and Shubham Tulsiani. Track2act:
Predicting point tracks from internet videos enables generalizable robot manipulation. In
European Conference on Computer Vision, pages 306–324. Springer, 2024.
[841] Shichao Fan, Quantao Yang, Yajie Liu, Kun Wu, Zhengping Che, Qingjie Liu, and Min Wan.
Diffusion trajectory-guided policy for long-horizon robot manipulation. IEEE Robotics and
Automation Letters, 2025.
[842] Mara Levy, Siddhant Haldar, Lerrel Pinto, and Abhinav Shirivastava. P3-po: Prescriptive point
priors for visuo-spatial generalization of robot policies. In 2025 IEEE International Conference
on Robotics and Automation (ICRA), pages 4167–4174. IEEE, 2025.
[843] Po-Chen Ko, Jiayuan Mao, Yilun Du, Shao-Hua Sun, and Joshua B Tenenbaum. Learning
to act from actionless videos through dense correspondences. In The Twelfth International
Conference on Learning Representations, 2024.
[844] Zhide Zhong, Haodong Yan, Junfeng Li, Xiangchen Liu, Xin Gong, Wenxuan Song, Jiayi Chen,
and Haoang Li. Flowvla: Thinking in motion with a visual chain of thought. arXiv preprint
arXiv:2508.18269, 2025.
[845] Shanshan Guo, Xiwen Liang, Junfan Lin, Yuzheng Zhuang, Liang Lin, and Xiaodan Liang.
Actionsink: Toward precise robot manipulation with dynamic integration of action flow. arXiv
preprint arXiv:2508.03218, 2025.
[846] Jiaming Chen, Yiyu Jiang, Aoshen Huang, Yang Li, and Wei Pan. Vlm-sfd: Vlm-assisted
siamese flow diffusion framework for dual-arm cooperative manipulation. IEEE Robotics and
Automation Letters, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[847] Yixiang Chen, Peiyan Li, Yan Huang, Jiabing Yang, Kehan Chen, and Liang Wang. Ec-flow:
Enabling versatile robotic manipulation from action-unlabeled videos via embodiment-centric
flow. In Proceedings of the IEEE/CVF international conference on computer vision, 2025.
[848] Kelin Yu, Sheng Zhang, Harshit Soora, Furong Huang, Heng Huang, Pratap Tokekar, and
Ruohan Gao. Genflowrl: Shaping rewards with generative object-centric flow in visual
reinforcement learning. In Proceedings of the IEEE/CVF international conference on computer
vision, 2025.
[849] Tianxing Chen, Yao Mu, Zhixuan Liang, Zanxin Chen, Shijia Peng, Qiangyu Chen, Mingkun
Xu, Ruizhen Hu, Hongyuan Zhang, Xuelong Li, et al. G3flow: Generative 3d semantic flow
for pose-aware and generalizable object manipulation. In Proceedings of the Computer Vision
and Pattern Recognition Conference, pages 1735–1744, 2025.
[850] Yuxin He and Qiang Nie. Manitrend: Bridging future generation and action prediction with
3d flow for robotic manipulation. arXiv preprint arXiv:2502.10028, 2025.
[851] Zhuoling Li, LiangLiang Ren, Jinrong Yang, Yong Zhao, Xiaoyang Wu, Zhenhua Xu, Xiang
Bai, and Hengshuang Zhao. Vip: Vision instructed pre-training for robotic manipulation. In
Forty-second International Conference on Machine Learning, 2025.
[852] Daniel Seita, Yufei Wang, Sarthak J Shetty, Edward Yao Li, Zackory Erickson, and David Held.
Toolflownet: Robotic manipulation with tools via predicting tool flow from point clouds. In
Conference on Robot Learning, pages 1038–1049. PMLR, 2023.
[853] Zhiwei Jia, Vineet Thumuluri, Fangchen Liu, Linghao Chen, Zhiao Huang, and Hao Su.
Chain-of-thought predictive control. In International Conference on Machine Learning, pages
21768–21790. PMLR, 2024.
[854] Junjie Wen, Yichen Zhu, Minjie Zhu, Jinming Li, Zhiyuan Xu, Zhengping Che, Chaomin Shen,
Yaxin Peng, Dong Liu, Feifei Feng, et al. Object-centric instruction augmentation for robotic
manipulation. In 2024 IEEE International Conference on Robotics and Automation (ICRA),
pages 4318–4325. IEEE, 2024.
[855] Oier Mees, Lukas Hermann, and Wolfram Burgard. What matters in language conditioned
robotic imitation learning over unstructured data. IEEE Robotics and Automation Letters, 7
(4):11205–11212, 2022.
[856] Vidhi Jain, Maria Attarian, Nikhil J Joshi, Ayzaan Wahid, Danny Driess, Quan Vuong, Pannag R
Sanketi, Pierre Sermanet, Stefan Welker, Christine Chan, et al. Vid2robot: End-to-end video-
conditioned policy learning with cross-attention transformers. In Robotics: Science and Systems,
2024.
[857] Sung-Wook Lee, Xuhui Kang, Brandon Yang, and Yen-Ling Kuo. Class: Contrastive learning
via action sequence supervision for robot manipulation. In Conference on Robot Learning,
2026.
[858] Tete Xiao, Ilija Radosavovic, Trevor Darrell, and Jitendra Malik. Masked visual pre-training
for motor control. arXiv:2203.06173, 2022.
[859] Jiange Yang, Bei Liu, Jianlong Fu, Bocheng Pan, Gangshan Wu, and Limin Wang. Spatiotem-
poral predictive pre-training for robotic motor control. arXiv preprint arXiv:2403.05304,
2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[860] Ilija Radosavovic, Baifeng Shi, Letian Fu, Ken Goldberg, Trevor Darrell, and Jitendra Malik.
Robot learning with sensorimotor pre-training. In Conference on Robot Learning, pages
683–693. PMLR, 2023.
[861] Rutav Shah, Roberto Martín-Martín, and Yuke Zhu. Mutex: Learning unified policies from
multimodal task specifications. In Conference on Robot Learning, 2023.
[862] Shizhe Chen, Ricardo Garcia Pinel, Cordelia Schmid, and Ivan Laptev. Polarnet: 3d point
clouds for language-guided robotic manipulation. In Conference on Robot Learning, pages
1761–1781. PMLR, 2023.
[863] Yanjie Ze, Nicklas Hansen, Yinbo Chen, Mohit Jain, and Xiaolong Wang. Visual reinforcement
learning with self-supervised 3d representations. IEEE Robotics and Automation Letters, 8(5):
2890–2897, 2023.
[864] Tong Zhang, Yingdong Hu, Jiacheng You, and Yang Gao. Leveraging locality to boost sample
efficiency in robotic manipulation. In Conference on Robot Learning, pages 3264–3284. PMLR,
2025.
[865] Haoyi Zhu, Honghui Yang, Yating Wang, Jiange Yang, Limin Wang, and Tong He. Spa: 3d
spatial-awareness enables effective embodied representation. In The Thirteenth International
Conference on Learning Representations, 2025.
[866] Shengyi Qian, Kaichun Mo, Valts Blukis, David Fouhey, Dieter Fox, and Ankit Goyal. 3d-mvp:
3d multiview pretraining for robotic manipulation. In Proceedings of the Computer Vision and
Pattern Recognition Conference, 2025.
[867] Yueru Jia, Jiaming Liu, Sixiang Chen, Chenyang Gu, Zhilue Wang, Longzan Luo, Lily Lee,
Pengwei Wang, Zhongyuan Wang, Renrui Zhang, et al. Lift3d foundation policy: Lifting
2d large-scale pretrained models for robust 3d robotic manipulation. In Proceedings of the
Computer Vision and Pattern Recognition Conference, 2025.
[868] Xupeng Zhu, Yu Qi, Yizhe Zhu, Robin Walters, and Robert Platt. Equact: An se (3)-equivariant
multi-task transformer for open-loop robotic manipulation. arXiv preprint arXiv:2505.21351,
2025.
[869] Wenbo Cui, Chengyang Zhao, Yuhui Chen, Haoran Li, Zhizheng Zhang, Dongbin Zhao, and
He Wang. Cl3r: 3d reconstruction and contrastive learning for enhanced robotic manipulation
representations. arXiv preprint arXiv:2507.08262, 2025.
[870] Zhuoling Li, Xiaoyang Wu, Zhenhua Xu, and Hengshuang Zhao. Train once, deploy anywhere:
Realize data-efficient dynamic object manipulation. arXiv preprint arXiv:2508.14042, 2025.
[871] Mohit Shridhar, Lucas Manuelli, and Dieter Fox. Perceiver-actor: A multi-task transformer for
robotic manipulation. In Conference on Robot Learning, pages 785–799. PMLR, 2023.
[872] Wentao Yuan, Adithyavairavan Murali, Arsalan Mousavian, and Dieter Fox. M2t2: Multi-task
masked transformer for object-centric pick and place. In Conference on Robot Learning, pages
3619–3630. PMLR, 2023.
[873] Ankit Goyal, Valts Blukis, Jie Xu, Yijie Guo, Yu-Wei Chao, and Dieter Fox. Rvt-2: Learning
precise manipulation from few demonstrations. In Robotics: Science and Systems, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[874] Allan Zhou, Moo Jin Kim, Lirui Wang, Pete Florence, and Chelsea Finn. Nerf in the palm of
your hand: Corrective augmentation for robotics via novel-view synthesis. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 17907–17917,
2023.
[875] Xiao Ma, Sumit Patidar, Iain Haughton, and Stephen James. Hierarchical diffusion policy for
kinematics-aware multi-task robotic manipulation. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 18081–18090, 2024.
[876] Lirui Wang, Xinlei Chen, Jialiang Zhao, and Kaiming He. Scaling proprioceptive-visual
learning with heterogeneous pre-trained transformers. In Advances in neural information
processing systems, volume 37, pages 124420–124450, 2024.
[877] Zhefei Gong, Pengxiang Ding, Shangke Lyu, Siteng Huang, Mingyang Sun, Wei Zhao, Zhaoxin
Fan, and Donglin Wang. Carp: Visuomotor policy learning via coarse-to-fine autoregressive
prediction. Proceedings of the IEEE international conference on computer vision, 2025.
[878] Xiang Li, Varun Belagali, Jinghuan Shang, and Michael S Ryoo. Crossway diffusion: Improving
diffusion-based visuomotor policy via self-supervised learning. In 2024 IEEE International
Conference on Robotics and Automation (ICRA), pages 16841–16849. IEEE, 2024.
[879] Aaditya Prasad, Kevin Lin, Jimmy Wu, Linqi Zhou, and Jeannette Bohg. Consistency policy:
Accelerated visuomotor policies via consistency distillation. In Robotics: Science and Systems,
2024.
[880] Yifei Su, Ning Liu, Dong Chen, Zhen Zhao, Kun Wu, Meng Li, Zhiyuan Xu, Zhengping Che,
and Jian Tang. Freqpolicy: Efficient flow-based visuomotor policy via frequency consistency.
Advances in Neural Information Processing Systems, 38:27769–27797, 2025.
[881] Hanjung Kim, Jaehyun Kang, Hyolim Kang, Meedeum Cho, Seon Joo Kim, and Youngwoon
Lee.
Uniskill: Imitating human videos via cross-embodiment skill representations.
Proceedings of the 9th Conference on Robot Learning (CoRL), pages 4269–4294, 2025.
[882] Han Xue, Nan Min, Xiaotong Liu, Wendi Chen, Yuan Fang, Jun Lv, Cewu Lu, and Chuan
Wen. Rethinking camera choice: An empirical study on fisheye camera properties in robotic
manipulation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 35059–35069, 2026.
[883] Ankit Goyal, Jie Xu, Yijie Guo, Valts Blukis, Yu-Wei Chao, and Dieter Fox. Rvt: Robotic view
transformer for 3d object manipulation. In Conference on Robot Learning, pages 694–710.
PMLR, 2023.
[884] Yixuan Wang, Guang Yin, Binghao Huang, Tarik Kelestemur, Jiuguang Wang, and Yunzhu Li.
Gendp: 3d semantic fields for category-level generalizable diffusion policy. In 8th Annual
Conference on Robot Learning, volume 2, 2024.
[885] Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan Hu, Muhan Wang, and Huazhe Xu. 3d
diffusion policy: Generalizable visuomotor policy learning via simple 3d representations. In
Robotics: Science and Systems, 2024.
[886] Sangjun Noh, Dongwoo Nam, Kangmin Kim, Geonhyup Lee, Yeonguk Yu, Raeyoung Kang,
and Kyoobin Lee. 3d flow diffusion policy: Visuomotor policy learning via generating flow in
3d space. arXiv preprint arXiv:2509.18676, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[887] Theophile Gervet, Zhou Xian, Nikolaos Gkanatsios, and Katerina Fragkiadaki. Act3d: 3d
feature field transformers for multi-task robotic manipulation. In Conference on Robot Learning,
2023.
[888] Tsung-Wei Ke, Nikolaos Gkanatsios, and Katerina Fragkiadaki. 3d diffuser actor: Policy
diffusion with 3d scene representations. In 8th Annual Conference on Robot Learning, 2024.
[889] Jiahang Cao, Qiang Zhang, Jingkai Sun, Jiaxu Wang, Hao Cheng, Yulin Li, Jun Ma, Kun Wu,
Zhiyuan Xu, Yecheng Shao, et al. Mamba policy: Towards efficient 3d diffusion policy with
hybrid selective state models. In 2025 IEEE/RSJ International Conference on Intelligent Robots
and Systems (IROS), pages 11359–11366. IEEE, 2025.
[890] Guanxing Lu, Zifeng Gao, Tianxing Chen, Wenxun Dai, Ziwei Wang, Wenbo Ding, and
Yansong Tang. Manicm: Real-time 3d diffusion policy via consistency model for robotic
manipulation. arXiv preprint arXiv:2406.01586, 2024.
[891] Nikolaos Gkanatsios, Jiahe Xu, Matthew Bronars, Arsalan Mousavian, Tsung-Wei Ke, and Kate-
rina Fragkiadaki. 3d flowmatch actor: Unified 3d policy for single-and dual-arm manipulation.
arXiv preprint arXiv:2508.11002, 2025.
[892] Albert Wilcox, Mohamed Ghanem, Masoud Moghani, Pierre Barroso, Benjamin Joffe, and
Animesh Garg. Adapt3r: Adaptive 3d scene representation for domain transfer in imitation
learning. In Conference on Robot Learning, 2025.
[893] Oier Mees, Jessica Borja-Diaz, and Wolfram Burgard. Grounding language with visual
affordances over unstructured data. In 2023 IEEE International Conference on Robotics and
Automation (ICRA), pages 11576–11582. IEEE, 2023.
[894] Dibya Ghosh, Homer Rich Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey
Hejna, Tobias Kreiman, Charles Xu, Jianlan Luo, et al. Octo: An open-source generalist robot
policy. In Robotics: Science and Systems, 2024.
[895] Moritz Reuss, Ömer Erdinç Yağmurlu, Fabian Wenzel, and Rudolf Lioutikov. Multimodal
diffusion transformer: Learning versatile behavior from multimodal goals. In Robotics: Science
and Systems, 2024.
[896] Siddhant Haldar, Zhuoran Peng, and Lerrel Pinto. Baku: An efficient transformer for multi-
task policy learning. Advances in Neural Information Processing Systems, 37:141208–141239,
2024.
[897] Saumya Saxena, Mohit Sharma, and Oliver Kroemer. Mrest: Multi-resolution sensing for
real-time control with vision-language models. In Conference on Robot Learning, 2023.
[898] Divyansh Garg, Skanda Vaidyanath, Kuno Kim, Jiaming Song, and Stefano Ermon. Lisa:
Learning interpretable skill abstractions from language. Advances in Neural Information
Processing Systems, 35:21711–21724, 2022.
[899] Zhi Hou, Tianyi Zhang, Yuwen Xiong, Haonan Duan, Hengjun Pu, Ronglei Tong, Chengyang
Zhao, Xizhou Zhu, Yu Qiao, Jifeng Dai, et al. Dita: Scaling diffusion transformer for generalist
vision-language-action policy. In International Conference on Computer Vision (ICCV), 2025.
[900] Huang Huang, Fangchen Liu, Letian Fu, Tingfan Wu, Mustafa Mukadam, Jitendra Malik, Ken
Goldberg, and Pieter Abbeel. Otter: A vision-language-action model with text-aware visual
feature extraction. In International Conference on Machine Learning, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[901] Haifeng Huang, Xinyi Chen, Yilun Chen, Hao Li, Xiaoshen Han, Zehan Wang, Tai Wang,
Jiangmiao Pang, and Zhou Zhao. Roboground: Robotic manipulation with grounded vision-
language priors. In Proceedings of the Computer Vision and Pattern Recognition Conference,
pages 22540–22550, 2025.
[902] Takumi Kobayashi, Masato Kobayashi, Thanpimon Buamanee, and Yuki Uranishi. Bi-lat:
Bilateral control-based imitation learning via natural language and action chunking with
transformers. In 2025 34th IEEE International Conference on Robot and Human Interactive
Communication (RO-MAN), pages 1609–1616. IEEE, 2025.
[903] Hokyun Im, Euijin Jeong, Andrey Kolobov, Jianlong Fu, and Youngwoon Lee. Twinvla:
Data-efficient bimanual manipulation with twin single-arm vision-language-action models.
In International Conference on Learning Representations, volume 2026, pages 61969–61995,
2026.
[904] Laura Smith, Alex Irpan, Montserrat Gonzalez Arenas, Sean Kirmani, Dmitry Kalashnikov,
Dhruv Shah, and Ted Xiao. Steer: Flexible robotic manipulation via dense language grounding.
In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages 16517–16524.
IEEE, 2025.
[905] Xinghang Li, Minghuan Liu, Hanbo Zhang, Cunjun Yu, Jie Xu, Hongtao Wu, Chilam Cheang,
Ya Jing, Weinan Zhang, Huaping Liu, et al. Vision-language foundation models as effective
robot imitators. In The Twelfth International Conference on Learning Representations, 2024.
[906] Moo Jin Kim, Chelsea Finn, and Percy Liang. Fine-tuning vision-language-action models:
Optimizing speed and success. In Robotics: Science and Systems, 2025.
[907] Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo
Fusai, Lachy Groom, Karol Hausman, Brian Ichter, et al. 𝜋0: A vision-language-action flow
model for general robot control. In Robotics: Science and Systems, 2025.
[908] Physical Intelligence, Kevin Black, Noah Brown, James Darpinian, Karan Dhabalia, Danny
Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, et al.
𝜋0.5: a vision-
language-action model with open-world generalization. In Conference on Robot Learning,
2025.
[909] Qixiu Li, Yaobo Liang, Zeyu Wang, Lin Luo, Xi Chen, Mozheng Liao, Fangyun Wei, Yu Deng,
Sicheng Xu, Yizhong Zhang, et al. Cogact: A foundational vision-language-action model for
synergizing cognition and action in robotic manipulation. arXiv preprint arXiv:2411.19650,
2024.
[910] Xinghang Li, Peiyan Li, Minghuan Liu, Dong Wang, Jirong Liu, Bingyi Kang, Xiao Ma, Tao
Kong, Hanbo Zhang, and Huaping Liu. Towards generalist robot policies: What matters in
building vision-language-action models. Nature Machine Intelligence, 2026.
[911] Jiaming Liu, Mengzhen Liu, Zhenyu Wang, Pengju An, Xiaoqi Li, Kaichen Zhou, Senqiao
Yang, Renrui Zhang, Yandong Guo, and Shanghang Zhang. Robomamba: Efficient vision-
language-action model for robotic reasoning and manipulation. Advances in Neural Information
Processing Systems, 37:40085–40110, 2024.
[912] Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu,
Mu Cai, Seonghyeon Ye, Joel Jang, et al. Magma: A foundation model for multimodal ai
agents. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages
14203–14214, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[913] Junjie Wen, Minjie Zhu, Yichen Zhu, Zhibin Tang, Jinming Li, Zhongyi Zhou, Chengmeng Li,
Xiaoyu Liu, Yaxin Peng, Chaomin Shen, et al. Diffusion-vla: Generalizable and interpretable
robot foundation model via self-generated reasoning. In International Conference on Machine
Learning, 2025.
[914] Junjie Wen, Yichen Zhu, Jinming Li, Zhibin Tang, Chaomin Shen, and Feifei Feng. Dexvla:
Vision-language model with plug-in diffusion expert for general robot control. In Conference
on Robot Learning, 2025.
[915] Zhongyi Zhou, Yichen Zhu, Minjie Zhu, Junjie Wen, Ning Liu, Zhiyuan Xu, Weibin Meng,
Yaxin Peng, Chaomin Shen, Feifei Feng, et al. Chatvla: Unified multimodal understanding
and robot control with vision-language-action model. In Proceedings of the 2025 Conference
on Empirical Methods in Natural Language Processing, pages 5377–5395, 2025.
[916] Jiaming Liu, Hao Chen, Zhuoyang Liu, Pengju An, Renrui Zhang, Chenyang Gu, Xiaoqi
Li, Ziyu Guo, Sixiang Chen, Mengzhen Liu, et al. Hybridvla: Collaborative diffusion and
autoregression in a unified vision-language-action model. In International Conference on
Learning Representations, volume 2026, pages 80668–80694, 2026.
[917] Shuai Yang, Hao Li, Bin Wang, Yilun Chen, Yang Tian, Tai Wang, Hanqing Wang, Feng
Zhao, Yiyi Liao, and Jiangmiao Pang. Vision-language-action instruction tuning: From
understanding to manipulation. In International Conference on Learning Representations,
volume 2026, pages 152896–152943, 2026.
[918] Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan
Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, et al. X-vla: Soft-prompted transformer as scalable
cross-embodiment vision-language-action model. In International Conference on Learning
Representations, volume 2026, pages 60580–60606, 2026.
[919] Jiayi Chen, Wenxuan Song, Pengxiang Ding, Ziyang Zhou, Han Zhao, Barrett Tang, Donglin
Wang, and Haoang Li. Unified diffusion vla: Vision-language-action model via joint discrete
denosing diffusion process. In International Conference on Learning Representations, volume
2026, pages 139291–139311, 2026.
[920] Chilam Cheang, Sijin Chen, Zhongren Cui, Yingdong Hu, Liqun Huang, Tao Kong, Hang Li,
Yifeng Li, Yuxiao Liu, Xiao Ma, et al. Gr-3 technical report. arXiv preprint arXiv:2507.15493,
2025.
[921] Cunxin Fan, Xiaosong Jia, Yihang Sun, Yixiao Wang, Jianglan Wei, Ziyang Gong, Xiangyu
Zhao, Masayoshi Tomizuka, Xue Yang, Junchi Yan, et al. Interleave-vla: Enhancing robot
manipulation with interleaved image-text instructions. arXiv preprint arXiv:2505.02152,
2025.
[922] Atharva Mete, Haotian Xue, Albert Wilcox, Yongxin Chen, and Animesh Garg. Quest: Self-
supervised skill abstractions for learning continuous control. Advances in Neural Information
Processing Systems, 37:4062–4089, 2024.
[923] Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping
Luo, and Hongyang Li. Univla: Learning to act anywhere with task-centric latent actions. In
Robotics: Science and Systems, 2025.
[924] Yating Wang, Haoyi Zhu, Mingyu Liu, Jiange Yang, Hao-Shu Fang, and Tong He. Vq-vla:
Improving vision-language-action models via scaling vector-quantized action tokenizers. In
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
2025 IEEE/CVF International Conference on Computer Vision (ICCV), pages 11089–11099.
IEEE, 2025.
[925] Xiaoyu Chen, Hangxing Wei, Pushi Zhang, Chuheng Zhang, Kaixin Wang, Yanjiang Guo,
Rushuai Yang, Yucen Wang, Xinquan Xiao, Li Zhao, et al. Villa-x: enhancing latent ac-
tion modeling in vision-language-action models. In International Conference on Learning
Representations, volume 2026, pages 70673–70703, 2026.
[926] Hao Shi, Bin Xie, Yingfei Liu, Lin Sun, Fengrong Liu, Tiancai Wang, Erjin Zhou, Haoqiang
Fan, Xiangyu Zhang, and Gao Huang. Memoryvla: Perceptual-cognitive memory in vision-
language-action models for robotic manipulation. In International Conference on Learning
Representations, volume 2026, pages 18567–18602, 2026.
[927] Sandeep Kumar Routray, Hengkai Pan, Unnat Jain, Shikhar Bahl, and Deepak Pathak. Vipra:
Video prediction for robot actions. In International Conference on Learning Representations,
volume 2026, pages 68823–68857, 2026.
[928] Mengya Liu, Baoxiong Jia, Jiangyong Huang, Jingze Zhang, and Siyuan Huang. Lara:
Latent action representation alignment for vision-language-action models. In Forty-third
International Conference on Machine Learning, 2026.
[929] Jiangran Lyu, Kai Liu, Xuheng Zhang, Haoran Liao, Yusen Feng, Wenxuan Zhu, Tingrui Shen,
Jiayi Chen, Jiazhao Zhang, Yifei Dong, et al. Lda-1b: Scaling latent dynamics action model
via universal embodied data ingestion. In Robotics: Science and Systems, 2026.
[930] Yihan Lin, Haoyang Li, Yang Li, Haitao Shen, Yihan Zhao, Chao Shao, and Jing Zhang. From
pixels to tokens: A systematic study of latent action supervision for vision-language-action
models. In Forty-third International Conference on Machine Learning, 2026.
[931] Shuanghao Bai, Jing Lyu, Wanqi Zhou, Zhe Li, Dakai Wang, Lei Xing, Xiaoguang Zhao,
Pengwei Wang, Zhongyuan Wang, Cheng Chi, Badong Chen, and Shanghang Zhang. Latent
reasoning vla: Latent thinking and prediction for vision-language-action models. In Forty-third
International Conference on Machine Learning, 2026.
[932] Chi-Pin Huang, Yunze Man, Zhiding Yu, Min-Hung Chen, Jan Kautz, Yu-Chiang Frank Wang,
and Fu-En Yang. Fast-thinkact: Efficient vision-language-action reasoning via verbalizable
latent planning. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 5070–5081, 2026.
[933] Fuxiang Yang, Donglin Di, Lulu Tang, Xuancheng Zhang, Lei Fan, Hao Li, Wei Chen, Tonghua
Su, and Baorui Ma. Chain of world: World model thinking in latent motion. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 6675–6684,
2026.
[934] Hao Luo, Ye Wang, Wanpeng Zhang, Haoqi Yuan, Yicheng Feng, Haiweng Xu, Sipeng Zheng,
and Zongqing Lu. Joint-aligned latent action: Towards scalable vla pretraining in the wild.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR),
pages 35047–35058, 2026.
[935] Jingwen Sun, Wenyao Zhang, Zekun Qi, Shaojie Ren, Zezhi Liu, Hanxin Zhu, Guangzhong
Sun, Xin Jin, and Zhibo Chen. Vla-jepa: Enhancing vision-language-action model with latent
world model. In European Conference on Computer Vision, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[936] Suneel Belkhale, Tianli Ding, Ted Xiao, Pierre Sermanet, Quon Vuong, Jonathan Tompson,
Yevgen Chebotar, Debidatta Dwibedi, and Dorsa Sadigh. Rt-h: Action hierarchies using
language. Robotics: Science and Systems, 2024.
[937] Kaidong Zhang, Pengzhen Ren, Bingqian Lin, Junfan Lin, Shikui Ma, Hang Xu, and Xiaodan
Liang. Pivot-r: Primitive-driven waypoint-aware world model for robotic manipulation.
Advances in Neural Information Processing Systems, 37:54105–54136, 2024.
[938] Lucy Xiaoyang Shi, Brian Ichter, Michael Equi, Liyiming Ke, Karl Pertsch, Quan Vuong, James
Tanner, Anna Walling, Haohuan Wang, Niccolo Fusai, et al. Hi robot: Open-ended instruction
following with hierarchical vision-language-action models. In International Conference on
Machine Learning, 2025.
[939] Hongjun Wu, Heng Zhang, Pengsong Zhang, Jin Wang, and Cong Wang. Hibernac: Hierar-
chical brain-emulated robotic neural agent collective for disentangling complex manipulation.
arXiv preprint arXiv:2506.08296, 2025.
[940] Yijie Zhu, Rui Shao, Ziyang Liu, Jie He, Jizhihui Liu, Jiuru Wang, and Zitong Yu. H-gar: A
hierarchical interaction framework via goal-driven observation-action refinement for robotic
manipulation. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 40, pages
18882–18890, 2026.
[941] Ajay Sridhar, Jennifer Pan, Satvik Sharma, and Chelsea Finn. Scaling up memory for robotic
control via experience retrieval. In International Conference on Learning Representations,
volume 2026, pages 97142–97166, 2026.
[942] Yide Shentu, Philipp Wu, Aravind Rajeswaran, and Pieter Abbeel. From llms to actions: Latent
codes as bridges in hierarchical robot control. In 2024 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 8539–8546. IEEE, 2024.
[943] ByungOk Han, Jaehong Kim, and Jinhyeok Jang. A dual process vla: Efficient robotic
manipulation leveraging vlm. In Conference on Robot Learning, 2024.
[944] Jianke Zhang, Yanjiang Guo, Xiaoyu Chen, Yen-Jen Wang, Yucheng Hu, Chengming Shi,
and Jianyu Chen. Hirt: Enhancing robotic control with hierarchical robot transformers. In
Conference on Robot Learning, pages 933–946. PMLR, 2025.
[945] Qingwen Bu, Hongyang Li, Li Chen, Jisong Cai, Jia Zeng, Heming Cui, Maoqing Yao, and
Yu Qiao. Towards synergistic, generalized, and efficient dual-system for robotic manipulation.
arXiv preprint arXiv:2410.08001, 2024.
[946] Hao Chen, Jiaming Liu, Chenyang Gu, Zhuoyang Liu, Renrui Zhang, Xiaoqi Li, Xiao He,
Yandong Guo, Chi-Wing Fu, Shanghang Zhang, et al. Fast-in-slow: A dual-system founda-
tion model unifying fast manipulation within slow reasoning. In The Thirty-ninth Annual
Conference on Neural Information Processing Systems, 2025.
[947] Can Cui, Pengxiang Ding, Wenxuan Song, Shuanghao Bai, Xinyang Tong, Zirui Ge, Runze Suo,
Wanqi Zhou, Yang Liu, Bofang Jia, et al. Openhelix: A short survey, empirical analysis, and
open-source dual-system vla model for robotic manipulation. arXiv preprint arXiv:2505.03912,
2025.
[948] Wenxuan Song, Jiayi Chen, Wenxue Li, Xu He, Han Zhao, Can Cui, Pengxiang Ding, Shiyan
Su, Feilong Tang, Xuelian Cheng, Donglin Wang, et al. Rationalvla: A rational vision-language-
action model with dual system. arXiv preprint arXiv:2506.10826, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[949] Zhenyang Liu, Yongchong Gu, Sixiao Zheng, Xiangyang Xue, and Yanwei Fu. Trivla: A unified
triple-system-based unified vision-language-action model for general robot control. arXiv
preprint arXiv:2507.01424, 2025.
[950] Tao Jiang, Tianyuan Yuan, Yicheng Liu, Chenhao Lu, Jianning Cui, Xiao Liu, Shuiqi Cheng,
Jiyang Gao, Huazhe Xu, and Hang Zhao. Galaxea open-world dataset and g0 dual-system
vla model. arXiv preprint arXiv:2509.00576, 2025.
[951] Yifei Wei, Linqing Zhong, Yi Liu, Yuxiang Lu, Xindong He, Maoqing Yao, and Guanghui Ren.
Libra-vla: Achieving learning equilibrium via asynchronous coarse-to-fine dual-system. In
Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pages 39799–39815, 2026.
[952] Danny Driess, Jost Springenberg, Brian Ichter, Lili Yu, Adrian Li-Bell, Karl Pertsch, Allen
Ren, Homer Walke, Quan Vuong, Lucy Xiaoyang Shi, et al. Knowledge insulating vision-
language-action models: Train fast, run fast, generalize better. Advances in Neural Information
Processing Systems, 38:102867–102888, 2025.
[953] Yajat Yadav, Zhiyuan Zhou, Andrew Wagenmaker, Karl Pertsch, and Sergey Levine. Robust
fine-tuning of vision-language-action robot policies via parameter merging. In International
Conference on Learning Representations, volume 2026, pages 56385–56417, 2026.
[954] Haochen Niu, Kanyu Zhang, Shuyu Yin, Qinghai Guo, Peilin Liu, and Fei Wen. Boosting vision-
language-action finetuning with feasible action neighborhood prior. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), pages 27956–27966,
2026.
[955] Shuanghao Bai, Dakai Wang, Cheng Chi, Wanqi Zhou, Jing Lyu, Xiaoguang Zhao, Peng-
wei Wang, Zhongyuan Wang, Lei Xing, Shanghang Zhang, et al. Reshaping action error
distributions for reliable vision-language-action models. arXiv preprint arXiv:2602.04228,
2026.
[956] Chengyue Huang, Mellon M Zhang, Robert Azarcon, Glen Chou, and Zsolt Kira. Maps:
Preserving vision-language representations via module-wise proximity scheduling for better
vision-language-action generalization. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 32451–32462, 2026.
[957] Kaustubh Sridhar, Souradeep Dutta, Dinesh Jayaraman, and Insup Lee. Ricl: Adding in-
context adaptability to pre-trained vision-language-action models. In Conference on Robot
Learning, 2025.
[958] Hao Li, Shuai Yang, Yilun Chen, Yang Tian, Xiaoda Yang, Xinyi Chen, Hanqing Wang, Tai
Wang, Feng Zhao, Dahua Lin, et al. Cronusvla: Transferring latent motion across time for
multi-frame prediction in manipulation. In Proceedings of the AAAI Conference on Artificial
Intelligence, 2026.
[959] Tianyi Zhang, Haonan Duan, Haoran Hao, Yu Qiao, Jifeng Dai, and Zhi Hou. Grounding
actions in camera space: Observation-centric vision-language-action policy. In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 40, pages 18782–18790, 2026.
[960] Dmytro Kuzmenko and Nadiya Shvai. Moira: Modular instruction routing architecture for
multi-task robotics. Neurocomputing, page 132962, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[961] Juyi Lin, Amir Taherin, Arash Akbari, Arman Akbari, Lei Lu, Guangyu Chen, Taskin Padir,
Xiaomeng Yang, Weiwei Chen, Yiqian Li, et al. Vote: vision-language-action optimization
with trajectory ensemble voting. arXiv preprint arXiv:2507.05116, 2025.
[962] Jacky Kwok, Christopher Agia, Rohan Sinha, Matt Foutter, Shulu Li, Ion Stoica, Azalia
Mirhoseini, and Marco Pavone. Robomonkey: Scaling test-time sampling and verification for
vision-language-action models. In Conference on Robot Learning, 2025.
[963] Dejie Yang, Zijing Zhao, and Yang Liu. Ar-vrm: Imitating human motions for visual robot
manipulation with analogical reasoning. In 2025 IEEE/CVF International Conference on
Computer Vision (ICCV), pages 6818–6827. IEEE, 2025.
[964] Bear Häon, Kaylene Stocking, Ian Chuang, and Claire Tomlin. Mechanistic interpretability
for steering vision-language-action models. In Conference on Robot Learning, 2025.
[965] Wenkai Guo, Guanxing Lu, Haoyuan Deng, Zhenyu Wu, Yansong Tang, and Ziwei Wang.
Vla-reasoner: Empowering vision-language-action models with reasoning via online monte
carlo tree search. In 2026 IEEE International Conference on Robotics and Automation (ICRA),
2026.
[966] Sizhe Zhao, Shengping Zhang, Shuo Yang, Weiyu Zhao, Shuigen Wang, and Xiangyang Ji.
Tapsampling: Inference-time sampling with a task-progress-understanding verifier for robotic
manipulation. In Forty-third International Conference on Machine Learning, 2026.
[967] Dongchi Huang, Zhirui Fang, Tianle Zhang, Yihang Li, Lin Zhao, and Chunhe Xia. Co-rft:
Efficient fine-tuning of vision-language-action models through chunked offline reinforcement
learning. arXiv preprint arXiv:2508.02219, 2025.
[968] Suhyeok Jang, Dongyoung Kim, Changyeon Kim, Youngsuk Kim, and Jinwoo Shin. Verifier-
free test-time sampling for vision-language-action models. In International Conference on
Learning Representations, volume 2026, pages 139997–140017, 2026.
[969] Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng, Haoyu Chen, David
Kim Huat Chua, and Prahlad Vadakkepat. Adaptive action chunking at inference-time for
vision-language-action models. In Proceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR), pages 20802–20811, 2026.
[970] Chi-Pin Huang, Yueh-Hua Wu, Min-Hung Chen, Yu-Chiang Frank Wang, and Fu-En Yang.
Thinkact: Vision-language-action reasoning via reinforced visual latent planning. In Advances
in Neural Information Processing Systems, 2025.
[971] Haozhan Li, Yuxin Zuo, Jiale Yu, Yuhao Zhang, Zhaohui Yang, Kaiyan Zhang, Xuekai Zhu,
Yuchen Zhang, et al. Simplevla-rl: Scaling vla training via reinforcement learning. In Advances
in Neural Information Processing Systems, 2025.
[972] Zirui Song, Guangxian Ouyang, Mingzhe Li, Yuheng Ji, Chenxi Wang, Zixiang Xu, Zeyu
Zhang, Xiaoqing Zhang, Qian Jiang, Fengxian Ji, et al. Maniplvm-r1: Reinforcement learning
for reasoning in embodied manipulation with large vision-language models. In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 40, pages 18558–18566, 2026.
[973] Wenli Xiao, Haotian Lin, Andy Peng, Haoru Xue, Tairan He, Zhengyi Luo, Yuqi Xie, Fengyuan
Hu, Jim Fan, Guanya Shi, et al. Self-improving vision-language-action models with data
generation via residual rl. In International Conference on Learning Representations, volume
2026, pages 13209–13236, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[974] Hongyin Zhang, Shiyuan Zhang, Junxi Jin, Qixin Zeng, Yifan Qiao, Hongchao Lu, and Donglin
Wang. Balancing signal and variance: Adaptive offline rl post-training for vla flow models. In
Proceedings of the AAAI Conference on Artificial Intelligence, volume 40, pages 18755–18763,
2026.
[975] Sixu Lin, Yunpeng Qing, Litao Liu, Ming Zhou, Ruixing Jin, Xiaoyi Fan, and Guiliang Liu.
Dygro-vla: Cross-task scaling of vision–language–action models via dynamic grouped residual
optimization. In Forty-third International Conference on Machine Learning, 2026.
[976] Hengtao Li, Pengxiang Ding, Runze Suo, Yihao Wang, Zirui Ge, Dongyuan Zang, Kexian Yu,
Mingyang Sun, Hongyin Zhang, Donglin Wang, et al. Vla-rft: Vision-language-action reinforce-
ment fine-tuning with verified rewards in world simulators. arXiv preprint arXiv:2510.00406,
2025.
[977] Michał Zawalski, William Chen, Karl Pertsch, Oier Mees, Chelsea Finn, and Sergey Levine.
Robotic control via embodied chain-of-thought reasoning. In Conference on Robot Learning,
pages 3157–3181. PMLR, 2025.
[978] Qingqing Zhao, Yao Lu, Moo Jin Kim, Zipeng Fu, Zhuoyang Zhang, Yecheng Wu, Zhaoshuo
Li, Qianli Ma, Song Han, Chelsea Finn, et al. Cot-vla: Visual chain-of-thought reasoning for
vision-language-action models. In Proceedings of the Computer Vision and Pattern Recognition
Conference, pages 1702–1713, 2025.
[979] Ruijie Zheng, Yongyuan Liang, Shuaiyi Huang, Jianfeng Gao, Hal Daumé III, Andrey Kolobov,
Furong Huang, and Jianwei Yang. Tracevla: Visual trace prompting enhances spatial-temporal
awareness for generalist robotic policies. In The Thirteenth International Conference on Learning
Representations, 2025.
[980] Jianke Zhang, Yanjiang Guo, Yucheng Hu, Xiaoyu Chen, Xiang Zhu, and Jianyu Chen. Up-vla:
A unified understanding and prediction model for embodied agent. In International Conference
on Machine Learning, 2025.
[981] Austin Stone, Ted Xiao, Yao Lu, Keerthana Gopalakrishnan, Kuang-Huei Lee, Quan Vuong,
Paul Wohlhart, Sean Kirmani, Brianna Zitkovich, Fei Xia, et al. Open-world object manipula-
tion using pre-trained vision-language models. In Conference on Robot Learning, 2023.
[982] Wenyao Zhang, Hongsi Liu, Zekun Qi, Yunnan Wang, Xinqiang Yu, Jiazhao Zhang, Runpei
Dong, Jiawei He, He Wang, Zhizheng Zhang, et al. Dreamvla: a vision-language-action model
dreamed with comprehensive world knowledge. Advances in Neural Information Processing
Systems, 38:24195–24228, 2025.
[983] Wenxuan Song, Ziyang Zhou, Han Zhao, Jiayi Chen, Pengxiang Ding, Haodong Yan, Yuxin
Huang, Feilong Tang, Donglin Wang, and Haoang Li. Reconvla: Reconstructive vision-
language-action model as effective robot perceiver. In Proceedings of the AAAI Conference on
Artificial Intelligence, volume 40, pages 18549–18557, 2026.
[984] Qi Sun, Pengfei Hong, Tej Deep Pala, Vernon Toh, U-Xuan Tan, Deepanway Ghosal, and
Soujanya Poria. Emma-x: An embodied multimodal action model with grounded chain of
thought and look-ahead spatial reasoning. In Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 14199–14214, 2025.
[985] Jaden Clark, Suvir Mirchandani, Dorsa Sadigh, and Suneel Belkhale. Action-free reasoning
for policy generalization. In Conference on Robot Learning, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[986] Chongkai Gao, Zixuan Liu, Zhenghao Chi, Junshan Huang, Xin Fei, Yiwen Hou, Yuxuan
Zhang, Yudi Lin, Zhirui Fang, and Lin Shao. Vla-os: Structuring and dissecting planning rep-
resentations and paradigms in vision-language-action models. Advances in Neural Information
Processing Systems, 38:136705–136736, 2025.
[987] Fanqi Lin, Ruiqian Nai, Yingdong Hu, Jiacheng You, Junming Zhao, and Yang Gao. Onet-
wovla: A unified vision-language-action model with adaptive reasoning. In The Fourteenth
International Conference on Learning Representations, 2026.
[988] Linqing Zhong, Yi Liu, Yifei Wei, Ziyu Xiong, Si Liu, and Guanghui Ren. Acot-vla: Action
chain-of-thought for vision-language-action models. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 8152–8162, 2026.
[989] Hao Li, Zi-han Ding, Shuai Yang, Yilun Chen, Yang Tian, Xiaolin Hu, Tai Wang, Dahua Lin,
Feng Zhao, Si Liu, et al. Robointer: A holistic intermediate representation suite towards
robotic manipulation. In International Conference on Learning Representations, volume 2026,
pages 113314–113381, 2026.
[990] Minghui Lin, Pengxiang Ding, Shu Wang, Zifeng Zhuang, Yang Liu, Xinyang Tong, Wenxuan
Song, Shangke Lyu, Siteng Huang, and Donglin Wang. Hif-vla: Hindsight, insight and
foresight through motion representation for vision-language-action models. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 20732–20742,
2026.
[991] Rongtao Xu, Jian Zhang, Minghao Guo, Youpeng Wen, Haoting Yang, Min Lin, Jianzheng
Huang, Zhe Li, Kaidong Zhang, Liqiong Wang, et al. 𝑎_{0}: An affordance-aware hierarchical
model for general robotic manipulation. In 2025 IEEE/CVF International Conference on
Computer Vision (ICCV), pages 13491–13501. IEEE, 2025.
[992] Huajie Tan, Peterson Co, Yijie Xu, Shanyu Rong, Yuheng Ji, Cheng Chi, Xiansheng Chen,
Zhongxia Zhao, Pengwei Wang, Zhongyuan Wang, et al. Action-sketcher: From reasoning to
action via visual sketches for robotic manipulation. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 22433–22444, 2026.
[993] Xiaoqi Li, Jingyun Xu, Mingxu Zhang, Jiaming Liu, Yan Shen, Iaroslav Ponomarenko, Jiahui
Xu, Liang Heng, Siyuan Huang, Shanghang Zhang, et al. Object-centric prompt-driven
vision-language-action model for robotic manipulation. In 2025 IEEE/CVF Conference on
Computer Vision and Pattern Recognition (CVPR), pages 27638–27648. IEEE, 2025.
[994] Puhao Li, Yingying Wu, Ziheng Xi, Wanlin Li, Yuzhe Huang, Zhiyuan Zhang, Yinghan
Chen, Jianan Wang, Song-Chun Zhu, Tengyu Liu, et al. Controlvla: Few-shot object-centric
adaptation for pre-trained vision-language-action models. In Conference on Robot Learning,
2025.
[995] Dantong Niu, Yuvan Sharma, Giscard Biamby, Jerome Quenum, Yutong Bai, Baifeng Shi,
Trevor Darrell, and Roei Herzig. Llarva: Vision-action instruction tuning enhances robot
learning. In Conference on Robot Learning, 2024.
[996] Junjie Wen, Yichen Zhu, Jinming Li, Minjie Zhu, Zhibin Tang, Kun Wu, Zhiyuan Xu, Ning Liu,
Ran Cheng, Chaomin Shen, et al. Tinyvla: Towards fast, data-efficient vision-language-action
models for robotic manipulation. IEEE Robotics and Automation Letters, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[997] Chia-Yu Hung, Qi Sun, Pengfei Hong, Amir Zadeh, Chuan Li, U Tan, Navonil Majumder,
Soujanya Poria, et al. Nora: A small open-sourced generalist vision language action model
for embodied tasks. arXiv preprint arXiv:2504.19854, 2025.
[998] Mustafa Shukor, Dana Aubakirova, Francesco Capuano, Pepijn Kooijmans, Steven Palma,
Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, et al.
Smolvla: A vision-language-action model for affordable and efficient robotics. arXiv preprint
arXiv:2506.01844, 2025.
[999] Moritz Reuss, Hongyi Zhou, Marcel Rühle, Ömer Erdinç Yağmurlu, Fabian Otto, and Rudolf
Lioutikov. Flower: Democratizing generalist robot policies with efficient vision-language-
action flow policies. In Conference on Robot Learning, 2025.
[1000] Yihao Wang, Pengxiang Ding, Lingxiao Li, Can Cui, Zirui Ge, Xinyang Tong, Wenxuan Song,
Han Zhao, Wei Zhao, Pengxu Hou, et al. Vla-adapter: An effective paradigm for tiny-scale
vision-language-action model. In Proceedings of the AAAI conference on artificial intelligence,
volume 40, pages 18638–18646, 2026.
[1001] Zuxin Liu, Jesse Zhang, Kavosh Asadi, Yao Liu, Ding Zhao, Shoham Sabach, and Rasool
Fakoor. Tail: Task-specific adapters for imitation learning with large pretrained models. In
International Conference on Learning Representations, volume 2024, pages 16330–16353,
2024.
[1002] Tao Lin, Yilei Zhong, Yuxin Du, Jingjing Zhang, Jiting Liu, Yinxinyu Chen, Encheng Gu, Ziyan
Liu, Hongyi Cai, Yanwen Zou, et al. Evo-1: Lightweight vision-language-action model with
preserved semantic alignment. In Proceedings of the IEEE/CVF conference on computer vision
and pattern recognition, pages 13397–13406, 2026.
[1003] Yang Yue, Yulin Wang, Bingyi Kang, Yizeng Han, Shenzhi Wang, Shiji Song, Jiashi Feng, and
Gao Huang. Deer-vla: Dynamic inference of multimodal large language models for efficient
robot execution. Advances in Neural Information Processing Systems, 37:56619–56643, 2024.
[1004] Yantai Yang, Yuhao Wang, Zichen Wen, Luo Zhongwei, Chang Zou, Zhipeng Zhang, Chuan
Wen, and Linfeng Zhang. Efficientvla: Training-free acceleration and compression for vision-
language-action models. Advances in Neural Information Processing Systems, 38:40891–40914,
2025.
[1005] Rongyu Zhang, Menghang Dong, Yuan Zhang, Liang Heng, Xiaowei Chi, Gaole Dai, Li Du, Dan
Wang, Yuan Du, and Shanghang Zhang. Mole-vla: Dynamic layer-skipping vision language
action model via mixture-of-layers for efficient robot manipulation. In Proceedings of the AAAI
Conference on Artificial Intelligence, volume 40, pages 18764–18772, 2026.
[1006] Wei Li, Renshan Zhang, Rui Shao, Jie He, and Liqiang Nie. Cogvla: Cognition-aligned vision-
language-action models via instruction-driven routing & sparsification. Advances in neural
information processing systems, 38:137646–137675, 2025.
[1007] Ye Li, Yuan Meng, Zewen Sun, Kangye Ji, Chen Tang, Jiajun Fan, Xinzhu Ma, Shu-Tao Xia, Zhi
Wang, and Wenwu Zhu. Sp-vla: A joint model scheduling and token pruning approach for vla
model acceleration. In The Fourteenth International Conference on Learning Representations,
2026.
[1008] Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, and Chang Xu. Vla-cache:
Efficient vision-language-action manipulation via adaptive token caching. Advances in Neural
Information Processing Systems, 38:164448–164473, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1009] Yuhao Xu, Yantai Yang, Zhenyang Fan, Yufan Liu, Yuming Li, Bing Li, and Zhipeng Zhang.
Qvla: Not all channels are equal in vision-language-action model’s quantization. In The
Fourteenth International Conference on Learning Representations, 2026.
[1010] Jingxuan Zhang, Yunta Hsieh, Zhongwei Wan, Haokun Lin, Xin Wang, Ziqi Wang, Yingtie Lei,
and Mi Zhang. Quantvla: Scale-calibrated post-training quantization for vision-language-
action models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 39539–39549, 2026.
[1011] Seongmin Park, Hyungmin Kim, Sangwoo Kim, Wonseok Jeon, Juyoung Yang, Byeongwook
Jeon, Yoonseon Oh, and Jungwook Choi. Saliency-aware quantized imitation learning for
efficient robotic control. In 2025 IEEE/CVF International Conference on Computer Vision
(ICCV), pages 13140–13150. IEEE, 2025.
[1012] Songsheng Wang, Rucheng Yu, Zhihang Yuan, Chao Yu, Feng Gao, Yu Wang, and Derek F
Wong. Spec-vla: speculative decoding for vision-language-action models with relaxed ac-
ceptance. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language
Processing, pages 26916–26928, 2025.
[1013] Hongyi Zhou, Weiran Liao, Xi Huang, Yucheng Tang, Fabian Otto, Xiaogang Jia, Xinkai Jiang,
Simon Hilber, Ge Li, Qian Wang, et al. Beast: Efficient tokenization of b-splines encoded
action sequences for imitation learning. Advances in Neural Information Processing Systems,
38:172934–172959, 2025.
[1014] Wenxuan Song, Jiayi Chen, Pengxiang Ding, Han Zhao, Wei Zhao, Zhide Zhong, Zongyuan
Ge, Zhijun Li, Donglin Wang, Lujia Wang, et al. Pd-vla: Accelerating vision-language-action
model integrated with action chunking via parallel decoding. In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 13162–13169. IEEE, 2025.
[1015] Wenxuan Song, Jiayi Chen, Shuai Chen, Jingbo Wang, Pengxiang Ding, Han Zhao, Yikai Qin,
Xinhu Zheng, Donglin Wang, Yan Wang, et al. Fast-dvla: Accelerating discrete diffusion vla
to real-time performance. In European Conference on Computer Vision, 2026.
[1016] Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, and Xiangyu Xu. Blockvla: Ac-
celerating autoregressive vla via block diffusion finetuning. arXiv preprint arXiv:2605.13382,
2026.
[1017] Kevin Black, Manuel Galliker, and Sergey Levine. Real-time execution of action chunking
flow policies. Advances in Neural Information Processing Systems, 38:33383–33407, 2025.
[1018] Haoxuan Wang, Gengyu Zhang, Yan Yan, Yuzhang Shang, Ramana Kompella, and Gaowen
Liu. Real-time robot execution with masked action chunking. In International Conference on
Learning Representations, volume 2026, pages 120161–120179, 2026.
[1019] Chenghao Liu, Jiachen Zhang, Chengxuan Li, Zhimu Zhou, Shixin Wu, Songfang Huang,
and Huiling Duan. Ttf-vla: Temporal token fusion via pixel-attention integration for vision-
language-action models.
In Proceedings of the AAAI Conference on Artificial Intelligence,
volume 40, pages 18452–18459, 2026.
[1020] Wenxuan Song, Jiayi Chen, Pengxiang Ding, Yuxin Huang, Han Zhao, Donglin Wang, and
Haoang Li. Ceed-vla: Consistency vision-language-action model with early-exit decoding. In
European Conference on Computer Vision, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1021] Qiao Gu, Yuanliang Ju, Shengxiang Sun, Igor Gilitschenski, Haruki Nishimura, Masha Itkina,
and Florian Shkurti. Safe: Multitask failure detection for vision-language-action models.
Advances in Neural Information Processing Systems, 38:40041–40076, 2025.
[1022] Asher J Hancock, Allen Z Ren, and Anirudha Majumdar. Run-time observation interven-
tions make vision-language-action models more visually robust. In 2025 IEEE International
Conference on Robotics and Automation (ICRA), pages 9499–9506. IEEE, 2025.
[1023] Jianing Guo, Zhenhong Wu, Chang Tu, Yiyao Ma, Xiangqi Kong, Zhiqian Liu, Jiaming Ji,
Shuning Zhang, Yuanpei Chen, Kai Chen, et al. On robustness of vision-language-action model
against multi-modal perturbations. In International Conference on Learning Representations,
volume 2026, pages 70248–70272, 2026.
[1024] YIYANG FU, Chubin Zhang, Shukai Gong, Yufan Deng, Kaiwei Sun, Qiyang Min, Qibin Hou,
Yansong Tang, Jianan Wang, and Daquan Zhou. Stablevla: Towards robust vision-language-
action models without extra data. In Forty-third International Conference on Machine Learning,
2026.
[1025] Xueyang Zhou, Guiyao Tie, Guowen Zhang, Hecheng Wang, Pan Zhou, and Lichao Sun.
Badvla: Towards backdoor attacks on vision-language-action models via objective-decoupled
optimization. Advances in Neural Information Processing Systems, 38:127496–127523, 2025.
[1026] Xuancun Lu, Jiaxiang Chen, Shilin Xiao, Zizhi Jin, Zhangrui Chen, Hanwen Yu, Bohan Qian,
Ruochen Zhou, Xiaoyu Ji, and Wenyuan Xu. Phantom menace: Exploring and enhancing the
robustness of vla models against physical sensor attacks. In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 40, pages 35689–35697, 2026.
[1027] Taowen Wang, Cheng Han, James Liang, Wenhao Yang, Dongfang Liu, Luna Xinyu Zhang,
Qifan Wang, Jiebo Luo, and Ruixiang Tang. Exploring the adversarial vulnerabilities of
vision-language-action models in robotics. In 2025 IEEE/CVF International Conference on
Computer Vision (ICCV), pages 6948–6958. IEEE, 2025.
[1028] Hui Lu, Yi Yu, Yiming Yang, Chenyu Yi, Qixin Zhang, Bingquan Shen, Alex C Kot, and Xudong
Jiang. When robots obey the patch: Universal transferable patch attacks on vision-language-
action models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 22867–22878, 2026.
[1029] Yiguo Fan, Pengxiang Ding, Shuanghao Bai, Xinyang Tong, Yuyang Zhu, Hongchao Lu, Fengqi
Dai, Wei Zhao, Yang Liu, Siteng Huang, et al. Long-vla: Unleashing long-horizon capability
of vision language action model for robot manipulation. In Conference on Robot Learning,
2025.
[1030] Yi Yang, Jiaxuan Sun, Siqi Kou, Yihan Wang, and Zhijie Deng. Lohovla: A unified vision-
language-action model for long-horizon embodied tasks. arXiv preprint arXiv:2506.00411,
2025.
[1031] Bing Hu, Zaijing Li, Rui Shao, Junda Chen, April Hua Liu, Wei-Shi Zheng, and Liqiang Nie.
From abstraction to instantiation: Learning behavioral representation for vision-language-
action model. In Forty-third International Conference on Machine Learning, 2026.
[1032] Guangqi Jiang, Yutong Liang, Jianglong Ye, Jia-Yang Huang, Changwei Jing, Rocky Duan,
Pieter Abbeel, Xiaolong Wang, and Xueyan Zou. Cross-hand latent representation for vision-
language-action models. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), pages 13496–13507, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1033] Chenyu Hui, Xiaodi Huang, Siyu Xu, Yunke Wang, Shan You, Fei Wang, Tao Huang, and
Chang Xu. Seeing realism from simulation: Efficient video transfer for vision-language-action
data augmentation. In Forty-third International Conference on Machine Learning, 2026.
[1034] Minh Duc Nguyen, Nghiem Tuong Diep, Nguyen Gia Binh, Trong-Bao Ho, Doanh Le Thien,
Quang Tan Nguyen, Thien-Loc Ha, Tran Van Nhiem, Bao Thach, Tran Xuan Nhat, Tuan Anh
Tran, Artur Habuda, Philip Lund Møller, Tran Nguyen Le, Daniel Sonntag, Mathias Niepert,
Khoa D Doan, Vu N. Duong, Hung Ngo, Minh Nhat VU, Duy Minh Ho Nguyen, An Thai Le, and
Vien Anh Ngo. FOCA: Future-oriented conditioning for data-efficient vision-language-action
adaptation. In Forty-third International Conference on Machine Learning, 2026.
[1035] Likui Zhang, Tao Tang, Zhihao Zhan, Xiuwei Chen, Zisheng Chen, Jianhua Han, Jiangtong
Zhu, Pei Xu, Hang Xu, Hefeng Wu, Liang Lin, and Xiaodan Liang. Atomicvla: Unlocking
the potential of atomic skill learning in robots. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition (CVPR), pages 20743–20754, 2026.
[1036] Junhong Zhu, Ji Zhang, Jingkuan Song, Lianli Gao, and Heng Tao Shen. Beyond the majority:
Long-tail imitation learning for robotic manipulation. In 2026 IEEE International Conference
on Robotics and Automation (ICRA), 2026.
[1037] Yucheng Hu, Jianke Zhang, Yuanfei Luo, Yanjiang Guo, Xiaoyu Chen, Xinshu Sun, Kun
Feng, Qingzhou Lu, Sheng Chen, Yangang Zhang, et al. Bagelvla: Enhancing long-horizon
manipulation via interleaved vision-language-action generation. In Robotics: Science and
Systems, 2026.
[1038] Yuanzhe Liu, Jingyuan Zhu, Yuchen Mo, Gen Li, Xu Cao, Jin Jin, Yifan Shen, Zhengyuan
Li, Tianjiao Yu, Wenzhen Yuan, Fangqiang Ding, and Ismini Lourentzou. Palm: Progress-
aware policy learning via affordance reasoning for long-horizon robotic manipulation. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR),
pages 28096–28110, 2026.
[1039] Pengteng Li, Weiyu Guo, He Zhang, Tiefu Cai, Xiao He, Yandong Guo, and Hui Xiong. Spatial
memory for out-of-vision manipulation in vision-language-action. In Forty-third International
Conference on Machine Learning, 2026.
[1040] Delin Qu, Haoming Song, Qizhi Chen, Yuanqi Yao, Xinyi Ye, Yan Ding, Zhigang Wang,
JiaYuan Gu, Bin Zhao, Dong Wang, et al. Spatialvla: Exploring spatial representations for
visual-language-action model. In Robotics: Science and Systems, 2025.
[1041] Vineet Bhat, Yu-Hsiang Lan, Prashanth Krishnamurthy, Ramesh Karri, and Farshad Khorrami.
3d cavla: Leveraging depth and 3d context to generalize vision language action models for
unseen tasks. arXiv preprint arXiv:2505.05800, 2025.
[1042] Lin Sun, Bin Xie, Yingfei Liu, Hao Shi, Tiancai Wang, and Jiale Cao. Geovla: Empowering 3d
representations in vision-language-action models. arXiv preprint arXiv:2508.09071, 2025.
[1043] Rujia Yang, Geng Chen, Chuan Wen, and Yang Gao. Fp3: A 3d foundation policy for robotic
manipulation. arXiv preprint arXiv:2503.08950, 2025.
[1044] I-Chun Arthur Liu, Sicheng He, Daniel Seita, and Gaurav S Sukhatme. Voxact-b: Voxel-based
acting and stabilizing policy for bimanual manipulation. In Conference on Robot Learning,
pages 4354–4370. PMLR, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1045] Weiyao Wang, Yutian Lei, Shiyu Jin, Gregory D Hager, and Liangjun Zhang. Vihe: Virtual in-
hand eye transformer for 3d robotic manipulation. In 2024 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS), pages 403–410. IEEE, 2024.
[1046] Ishika Singh, Ankit Goyal, Stan Birchfield, Dieter Fox, Animesh Garg, and Valts Blukis. Og-vla:
3d-aware vision language action model via orthographic image generation. arXiv preprint
arXiv:2506.01196, 2025.
[1047] Feng Yan, Fanfan Liu, Liming Zheng, Yufeng Zhong, Yiyang Huang, Zechao Guan, Chengjian
Feng, and Lin Ma. Robomm: All-in-one multimodal large model for robotic manipulation. In
International Conference on Computer Vision (ICCV), 2025.
[1048] Shizhe Chen, Paul Pacaud, and Cordelia Schmid. Pointact: Vision-language-action models
with multi-scale point-action interaction. In Robotics: Science and Systems, 2026.
[1049] Chengmeng Li, Junjie Wen, Yaxin Peng, Yan Peng, and Yichen Zhu. Pointvla: Injecting the
3d world into vision-language-action models. IEEE Robotics and Automation Letters, 11(3):
2506–2513, 2026.
[1050] Peiyan Li, Yixiang Chen, Hongtao Wu, Xiao Ma, Xiangnan Wu, Yan Huang, Liang Wang,
Tao Kong, and Tieniu Tan. Bridgevla: Input-output alignment for efficient 3d manipulation
learning with vision-language models. Advances in Neural Information Processing Systems, 38:
63635–63673, 2025.
[1051] Zhengshen Zhang, Hao Li, Yalun Dai, Zhengbang Zhu, Lei Zhou, Chenchen Liu, Dong Wang,
Francis EH Tay, Sijin Chen, Ziwei Liu, et al. From spatial to actions: Grounding vision-
language-action model in spatial foundation priors. In The Fourteenth International Conference
on Learning Representations, 2026.
[1052] Yongjie Bai, Zhouxia Wang, Yang Liu, Weixing Chen, Ziliang Chen, Mingtong Dai, Yongsen
Zheng, Lingbo Liu, Guanbin Li, and Liang Lin. Learning to see and act: Task-aware view
planning for robotic manipulation. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 2026.
[1053] Xuening Zhang, Qi Lv, Xiang Deng, Miao Zhang, Xingbo Liu, and Liqiang Nie. Cortical policy:
A dual-stream view transformer for robotic manipulation. In The Fourteenth International
Conference on Learning Representations, 2026.
[1054] Tao Lin, Gen Li, Yilei Zhong, Yanwen Zou, and Bo Zhao. Evo-0: Vision-language-action model
with implicit spatial understanding. arXiv preprint arXiv:2507.00416, 2025.
[1055] Haoyu Zhen, Xiaowen Qiu, Peihao Chen, Jincheng Yang, Xin Yan, Yilun Du, Yining Hong,
and Chuang Gan. 3d-vla: a 3d vision-language-action generative world model. In Proceedings
of the 41st International Conference on Machine Learning, pages 61229–61245, 2024.
[1056] Wei Li, Jizhihui Liu, Li Yixing, Junwen Tong, Rui Shao, and Liqiang Nie. Consisvla-4d:
Advancing spatiotemporal consistency in efficient 3d-perception and 4d-reasoning for robotic
manipulation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 6706–6717, 2026.
[1057] Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, and Bo Yang. Physmani: Physics-
principled 3d world model for dynamic object manipulation. In European Conference on
Computer Vision, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1058] Helong Huang, Min Cen, Kai Tan, Xingyue Quan, Guowei Huang, and Hong Zhang. Graphcot-
vla: A 3d spatial-aware reasoning vision-language-action model for robotic manipulation
with ambiguous instructions. In Proceedings of the AAAI Conference on Artificial Intelligence,
volume 40, pages 18324–18332, 2026.
[1059] Zhou Xian and Nikolaos Gkanatsios. Chaineddiffuser: Unifying trajectory diffusion and
keypose prediction for robotic manipulation. In Conference on Robot Learning, 2023.
[1060] Fuhao Li, Wenxuan Song, Han Zhao, Jingbo Wang, Pengxiang Ding, Donglin Wang, Long
Zeng, and Haoang Li. Spatial forcing: Implicit spatial representation alignment for vision-
language-action model. In International Conference on Learning Representations, volume 2026,
pages 132324–132345, 2026.
[1061] Jingjing Qian, Boyao Han, Chen Shi, Lei Xiao, Long Yang, Shaoshuai Shi, and Li Jiang.
Geopredict: Leveraging predictive kinematics and 3d gaussian geometry for precise vla
manipulation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 13529–13539, 2026.
[1062] Siyu Xu, Zijian Wang, Yunke Wang, Chenghao Xia, Tao Huang, and Chang Xu. Affordance field
intervention: Enabling vlas to escape memory traps in robotic manipulation. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 37206–37215,
2026.
[1063] Yuquan Li, Lianjie Ma, Han Ding, and Lijun Zhu. Depthcache: Depth-guided training-
free visual token merging for vision-language-action model inference.
arXiv preprint
arXiv:2603.10469, 2026.
[1064] Irmak Guzey, Ben Evans, Soumith Chintala, and Lerrel Pinto. Dexterity from touch: Self-
supervised pre-training of tactile representations with robotic play. In Conference on Robot
Learning, pages 3142–3166. PMLR, 2023.
[1065] Carolina Higuera, Akash Sharma, Chaithanya Krishna Bodduluri, Taosha Fan, Patrick Lan-
caster, Mrinal Kalakrishnan, Michael Kaess, Byron Boots, Mike Lambeta, Tingfan Wu, et al.
Sparsh: Self-supervised touch representations for vision-based tactile sensing. In Conference
on Robot Learning, pages 885–915. PMLR, 2025.
[1066] Wenxuan Ma, Xiaoge Cao, Yixiang Zhang, Chaofan Zhang, Shaobo Yang, Peng Hao, Bin Fang,
Yinghao Cai, Shaowei Cui, and Shuo Wang. Cltp: Contrastive language-tactile pre-training
for 3d contact geometry understanding. Biomimetic Intelligence and Robotics, page 100324,
2026.
[1067] Yue Xu, Litao Wei, Pengyu An, Qingyu Zhang, and Yong-Lu Li. exumi: Extensible robot
teaching system with action-aware task-agnostic tactile representation. In Conference on robot
learning, 2025.
[1068] Carolina Higuera, Akash Sharma, Taosha Fan, Chaithanya Krishna Bodduluri, Byron Boots,
Michael Kaess, Mike Lambeta, Tingfan Wu, Zixi Liu, Francois Robert Hogan, et al. Tactile
beyond pixels: Multisensory touch representations for robot manipulation. In Conference on
Robot Learning, pages 105–123. PMLR, 2025.
[1069] Wenyan Yang, Alexandre Angleraud, Roel S Pieters, Joni Pajarinen, and Joni-Kristian Kämäräi-
nen. Seq2seq imitation learning for tactile feedback-based manipulation. In 2023 IEEE
International Conference on Robotics and Automation (ICRA), pages 5829–5836. IEEE, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1070] Bo Ai, Stephen Tian, Haochen Shi, Yixuan Wang, Cheston Tan, Yunzhu Li, and Jiajun Wu.
Robopack: Learning tactile-informed dynamics models for dense packing. Proceedings of
Robotics: Science and Systems, 2024.
[1071] Kelin Yu, Yunhai Han, Qixian Wang, Vaibhav Saxena, Danfei Xu, and Ye Zhao. Mimictouch:
Leveraging multi-modal human tactile demonstrations for contact-rich manipulation. In
Conference on Robot Learning, pages 4844–4865. PMLR, 2025.
[1072] Ademi Adeniji, Zhuoran Chen, Vincent Liu, Venkatesh Pattabiraman, Raunaq Bhirangi,
Siddhant Haldar, Pieter Abbeel, and Lerrel Pinto. Feel the force: Contact-driven learning
from humans. arXiv preprint arXiv:2506.01944, 2025.
[1073] Kipp McAdam Freud, Yijiong Lin, and Nathan F Lepora. Simshear: Sim-to-real shear-based
tactile servoing. In Conference on robot learning, 2025.
[1074] Haozhi Qi, Brent Yi, Sudharshan Suresh, Mike Lambeta, Yi Ma, Roberto Calandra, and
Jitendra Malik. General in-hand object rotation with vision and touch. In Conference on Robot
Learning, pages 2549–2564. PMLR, 2023.
[1075] Trevor Ablett, Oliver Limoyo, Adam Sigal, Affan Jilani, Jonathan Kelly, Kaleem Siddiqi,
Francois Hogan, and Gregory Dudek. Multimodal and force-matched imitation learning with
a see-through visuotactile sensor. IEEE Transactions on Robotics, 2024.
[1076] Yijun Gu and Yiannis Demiris. Vttb: A visuo-tactile learning approach for robot-assisted bed
bathing. IEEE Robotics and Automation Letters, 9(6):5751–5758, 2024.
[1077] Abraham George, Selam Gano, Pranav Katragadda, and Amir Barati Farimani. Vital pretrain-
ing: Visuo-tactile pretraining for tactile and non-tactile manipulation policies. In 2025 IEEE
International Conference on Robotics and Automation (ICRA), pages 258–264. IEEE, 2025.
[1078] Binghao Huang, Jie Xu, Iretiayo Akinola, Wei Yang, Balakumar Sundaralingam, Rowland
O’Flaherty, Dieter Fox, Xiaolong Wang, Arsalan Mousavian, Yu-Wei Chao, et al. Vt-refine:
Learning bimanual assembly with visuo-tactile feedback via simulation fine-tuning. In Confer-
ence on robot learning, 2025.
[1079] Han Xue, Jieji Ren, Wendi Chen, Gu Zhang, Yuan Fang, Guoying Gu, Huazhe Xu, and Cewu Lu.
Reactive diffusion policy: Slow-fast visual-tactile policy learning for contact-rich manipulation.
In Robotics: Science and Systems, 2025.
[1080] Yufeng Tian, Shuiqi Cheng, Tianming Wei, Tianxing Zhou, Yuanhang Zhang, Zixian Liu,
Qianwei Han, Zhecheng Yuan, and Huazhe Xu. Vitas: Visual tactile soft fusion contrastive
learning for visuomotor learning. In 2026 IEEE International Conference on Robotics and
Automation (ICRA), 2026.
[1081] Zhiyuan Wu, Yijiong Lin, Yongqiang Zhao, Xuyang Zhang, Zhuo Chen, Nathan Lepora, and
Shan Luo. Vitacgen: Robotic pushing with vision-to-touch generation. IEEE Robotics and
Automation Letters, 2025.
[1082] Liang Heng, Haoran Geng, Kaifeng Zhang, Pieter Abbeel, and Jitendra Malik. Vitacformer:
Learning cross-modal representation for visuo-tactile dexterous manipulation. arXiv preprint
arXiv:2506.15953, 2025.
[1083] Shulong Jiang, Shiqi Zhao, Yuxuan Fan, and Peng Yin. Gelfusion: Enhancing robotic ma-
nipulation under visual constraints via visuotactile fusion. arXiv preprint arXiv:2505.07455,
2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1084] Samson Yu, Kelvin Lin, Anxing Xiao, Jiafei Duan, and Harold Soh. Octopi: Object property
reasoning with large tactile-language models. In Robotics: Science and Systems, 2024.
[1085] Peng Hao, Chaofan Zhang, Dingzhe Li, Xiaoge Cao, Xiaoshuai Hao, Shaowei Cui, and Shuo
Wang. Tla: Tactile-language-action model for contact-rich manipulation. arXiv preprint
arXiv:2503.08548, 2025.
[1086] Joshua Jones, Oier Mees, Carmelo Sferrazza, Kyle Stachowicz, Pieter Abbeel, and Sergey
Levine. Beyond sight: Finetuning generalist robot policies with heterogeneous sensors via
language grounding. In 2025 IEEE International Conference on Robotics and Automation
(ICRA), pages 5961–5968. IEEE, 2025.
[1087] Jianxin Bi, Kevin Yuchen Ma, Ce Hao, Mike Shou Zheng, and Harold Soh.
Vla-touch:
Enhancing vision-language-action model with dual-level tactile feedback. IEEE Robotics and
Automation Letters, 2026.
[1088] Jialei Huang, Shuo Wang, Fanqi Lin, Yihang Hu, Chuan Wen, and Yang Gao. Tactile-vla:
Unlocking vision-language-action model’s physical knowledge for tactile generalization. arXiv
preprint arXiv:2507.09160, 2025.
[1089] Zhengxue Cheng, Yiqian Zhang, Anni Tang, Keyu Wang, Wenkang Zhang, Haoyu Li, Hengdi
Zhang, and Li Song. Omnivtla: Vision-tactile-language-action models with semantic-aligned
tactile sensing. IEEE Robotics and Automation Letters, 2026.
[1090] Chaofan Zhang, Peng Hao, Xiaoge Cao, Xiaoshuai Hao, Shaowei Cui, and Shuo Wang. Vtla:
Vision-tactile-language-action model with preference learning for insertion manipulation.
arXiv preprint arXiv:2505.09577, 2025.
[1091] Dantong Niu, Zhuoyang Liu, Zekai Wang, Boning Shao, Zhao-Heng Yin, Anirudh Pai, Yuvan
Sharma, Stefano Saravalle, Ruijie Zheng, Jing Wang, et al. T-rex: Tactile-reactive dexterous
manipulation. arXiv preprint arXiv:2606.17055, 2026.
[1092] Chengbo Yuan, Zicheng Zhang, Mingjie Zhou, Wendi Chen, Yi Wang, Zhuoyang Liu, Dantong
Niu, Shuo Wang, Hui Zhang, Wenkang Zhang, et al. Ftp-1: A generalist foundation tactile
policy across tactile sensors for contact-rich manipulation. arXiv preprint arXiv:2606.13102,
2026.
[1093] Niklas Funk, Changqi Chen, Tim Schneider, Georgia Chalvatzaki, Roberto Calandra, and Jan
Peters. On the importance of tactile sensing for imitation learning: A case study on robotic
match lighting. In Proceedings of the IEEE International Conference on Robotics and Automation
with Wearables (ICRAW), April 2025.
[1094] Zifan Zhao, Siddhant Haldar, Jinda Cui, and Lerrel Pinto. Touch begins where vision ends:
Generalizable policies for contact-rich manipulation. In Second Workshop on Out-of-Distribution
Generalization in Robotics at RSS 2025, 2025.
[1095] Petar Kormushev, Sylvain Calinon, and Darwin G Caldwell. Imitation learning of positional
and force skills demonstrated via kinesthetic teaching and haptic input. Advanced Robotics,
25(5):581–603, 2011.
[1096] Tsuyoshi Adachi, Kazuki Fujimoto, Sho Sakaino, and Toshiaki Tsuji. Imitation learning for
object manipulation based on position/force information using bilateral control. In 2018
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 3648–3653.
IEEE, 2018.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1097] Mark Edmonds, Feng Gao, Xu Xie, Hangxin Liu, Siyuan Qi, Yixin Zhu, Brandon Rothrock, and
Song-Chun Zhu. Feeling the force: Integrating force and pose for fluent discovery through
imitation learning to open medicine bottles. In 2017 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 3530–3537. IEEE, 2017.
[1098] Yan Wang, Cristian C Beltran-Hernandez, Weiwei Wan, and Kensuke Harada.
Robotic
imitation of human assembly skills using hybrid trajectory and force learning. In 2021 IEEE
international conference on robotics and automation (ICRA), pages 11278–11284. IEEE, 2021.
[1099] Kelin Li, Digby Chappell, and Nicolas Rojas. Immersive demonstrations are the key to imitation
learning. In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages
5071–5077. IEEE, 2023.
[1100] Zihao He, Hongjie Fang, Jingjing Chen, Hao-Shu Fang, and Cewu Lu. Foar: Force-aware
reactive policy for contact-rich robotic manipulation. IEEE Robotics and Automation Letters,
2025.
[1101] Zongzheng Zhang, Haobo Xu, Zhuo Yang, Chenghao Yue, Zehao Lin, Huan-ang Gao, Ziwei
Wang, and Hao Zhao. Ta-vla: Elucidating the design space of torque-aware vision-language-
action models. In Conference on Robot Learning, 2025.
[1102] Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan
Huang, Yan Song, Panpan Cai, et al. Forcevla: Enhancing vla models with a force-aware moe
for contact-rich manipulation. In Conference on Robot Learning, 2026.
[1103] Ruiteng Zhao, Wenshuo Wang, Yicheng Ma, Xiaocong Li, Francis EH Tay, Marcelo H Ang Jr,
and Haiyue Zhu. Fd-vla: Force-distilled vision-language-action model for contact-rich manip-
ulation. In 2026 IEEE International Conference on Robotics and Automation (ICRA), 2026.
[1104] Maximilian Du, Olivia Y Lee, Suraj Nair, and Chelsea Finn. Play it by ear: Learning skills
amidst occlusion through audio-visual imitation learning. In Robotics: Science and Systems,
2022.
[1105] Hao Li, Yizhi Zhang, Junzhe Zhu, Shaoxiong Wang, Michelle A Lee, Huazhe Xu, Edward
Adelson, Li Fei-Fei, Ruohan Gao, and Jiajun Wu. See, hear, and feel: Smart sensory fusion
for robotic manipulation. In Conference on Robot Learning, pages 1368–1378. PMLR, 2023.
[1106] Zeyi Liu, Cheng Chi, Eric Cousineau, Naveen Kuppuswamy, Benjamin Burchfiel, and Shu-
ran Song. Maniwav: Learning robot manipulation from in-the-wild audio-visual data. In
Conference on Robot Learning, pages 947–962. PMLR, 2025.
[1107] Ruoxuan Feng, Di Hu, Wenke Ma, and Xuelong Li. Play to the score: Stage-guided dynamic
multi-sensory fusion for robotic manipulation. In Conference on Robot Learning, pages 340–
363. PMLR, 2025.
[1108] Wei Zhao, Pengxiang Ding, Min Zhang, Zhefei Gong, Shuanghao Bai, Han Zhao, and Donglin
Wang. Vlas: Vision-language-action model with speech instructions for customized robot
manipulation. International Conference on Learning Representations (ICLR), 2025.
[1109] Siyin Wang, Wenyi Yu, Xianzhao Chen, Xiaohai Tian, Jun Zhang, Lu Lu, Yuxuan Wang, and
Chao Zhang. End-to-end listen, look, speak and act. In International Conference on Learning
Representations, volume 2026, pages 66804–66829, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1110] Heyu Guo, Shanmu Wang, Ruichun Ma, Shiqi Jiang, Yasaman Ghasempour, Omid Abari,
Baining Guo, and Lili Qiu. Omnivla: Physically-grounded multimodal vla with unified multi-
sensor perception for robotic manipulation. In 2026 IEEE International Conference on Robotics
and Automation (ICRA), 2026.
[1111] Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, and Kaiwei Wang. E-vla: Event-augmented
vision-language-action model for dark and blurred scenes. arXiv preprint arXiv:2604.04834,
2026.
[1112] Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan
Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, et al. Forceband: Learning forceful manipulation
with semg. arXiv preprint arXiv:2606.26093, 2026.
[1113] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr Dollár, and Ross Girshick. Masked
autoencoders are scalable vision learners. In Proceedings of the IEEE/CVF conference on
computer vision and pattern recognition, pages 16000–16009, 2022.
[1114] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. Imagenet: A large-
scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern
recognition, pages 248–255. Ieee, 2009.
[1115] Simone Parisi, Aravind Rajeswaran, Senthil Purushwalkam, and Abhinav Gupta. The unsur-
prising effectiveness of pre-trained vision models for control. In international conference on
machine learning, pages 17359–17371. PMLR, 2022.
[1116] Jinghuan Shang, Karl Schmeckpeper, Brandon B May, Maria Vittoria Minniti, Tarik Kelestemur,
David Watkins, and Laura Herlant. Theia: Distilling diverse vision foundation models for
robot learning. In Conference on Robot Learning, pages 724–748. PMLR, 2025.
[1117] Yixiao Wang, Mingxiao Huo, Zhixuan Liang, Yushi Du, Lingfeng Sun, Haotian Lin, Jinghuan
Shang, Chensheng Peng, Mohit Bansal, Mingyu Ding, et al. Ver: Vision expert transformer for
robot learning via foundation distillation and dynamic routing. In International Conference
on Learning Representations, volume 2026, pages 155122–155148, 2026.
[1118] Taekyung Kim, Dongyoon Han, Byeongho Heo, Jeongeun Park, and Sangdoo Yun. Token
bottleneck: One token to remember dynamics. Advances in Neural Information Processing
Systems, 38:107455–107479, 2025.
[1119] Wei-Di Chang, Francois Hogan, Scott Fujimoto, David Meger, and Gregory Dudek. General-
izable imitation learning through pre-trained representations. In 2025 IEEE International
Conference on Robotics and Automation (ICRA), pages 1–8. IEEE, 2025.
[1120] Jia Zeng, Qingwen Bu, Bangjun Wang, Wenke Xia, Li Chen, Hao Dong, Haoming Song, Dong
Wang, Di Hu, Ping Luo, et al. Learning manipulation by predicting interaction. In Robotics:
Science and Systems, 2024.
[1121] Mohan Kumar Srirama, Sudeep Dasari, Shikhar Bahl, and Abhinav Gupta. Hrp: Human
affordances for robotic pre-training. In Robotics: Science and Systems, 2024.
[1122] Puhao Li, Tengyu Liu, Yuyang Li, Muzhi Han, Haoran Geng, Shu Wang, Yixin Zhu, Song-Chun
Zhu, and Siyuan Huang. Ag2manip: Learning novel manipulation skills with agent-agnostic
visual and action representations. In 2024 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 573–580. IEEE, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1123] Ilija Radosavovic, Tete Xiao, Stephen James, Pieter Abbeel, Jitendra Malik, and Trevor Darrell.
Real-world robot learning with masked visual pre-training. In Conference on Robot Learning,
pages 416–426. PMLR, 2023.
[1124] Ruijie Zheng, Yongyuan Liang, Xiyao Wang, Shuang Ma, Hal Daumé III, Huazhe Xu, John
Langford, Praveen Palanisamy, Kalyan Shankar Basu, and Furong Huang. Premier-taco: Pre-
training multitask representation via temporal action-driven contrastive loss. In International
Conference on Machine Learning, 2024.
[1125] Guangqi Jiang, Yifei Sun, Tao Huang, Huanyu Li, Yongyuan Liang, and Huazhe Xu. Robots
pre-train robots: Manipulation-centric robotic representation from large-scale robot datasets.
In The Thirteenth International Conference on Learning Representations, 2025.
[1126] Chaoran Zhu, Hengyi Wang, Yik Lung Pang, and Changjae Oh. Lava-man: Learning visual
action representations for robot manipulation. In Proceedings of the 9th Conference on Robot
Learning (CoRL), pages 5506–5525, 2025.
[1127] Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, and Gang Hua. Dynarend: Learning
3d dynamics via masked future rendering for robotic manipulation. Advances in Neural
Information Processing Systems, 38:77292–77318, 2025.
[1128] Jiahua Dong, Yunze Man, Pavel Tokmakov, and Yu-Xiong Wang. Capturing visual environment
structure correlates with control performance.
In International Conference on Learning
Representations, volume 2026, pages 35435–35462, 2026.
[1129] Ashley Edwards, Himanshu Sahni, Yannick Schroecker, and Charles Isbell. Imitating latent
policies from observation. In International conference on machine learning, pages 1755–1763.
PMLR, 2019.
[1130] Dominik Schmidt and Minqi Jiang. Learning to act without actions. In The Twelfth Interna-
tional Conference on Learning Representations, 2024.
[1131] Seungjae Lee, Yibin Wang, Haritheja Etukuru, H Jin Kim, Nur Muhammad Mahi Shafiul-
lah, and Lerrel Pinto. Behavior generation with latent actions. In Proceedings of the 41st
International Conference on Machine Learning, pages 26991–27008, 2024.
[1132] Kun Wu, Yichen Zhu, Jinming Li, Junjie Wen, Ning Liu, Zhiyuan Xu, and Jian Tang. Discrete
policy: Learning disentangled action space for multi-task robotic manipulation. In 2025 IEEE
International Conference on Robotics and Automation (ICRA), pages 8811–8818. IEEE, 2025.
[1133] Hao Li, Qi Lv, Rui Shao, Xiang Deng, Yinchuan Li, Jianye HAO, and Liqiang Nie. Star:
Learning diverse robot skill abstractions through rotation-augmented vector quantization. In
Forty-second International Conference on Machine Learning, 2025.
[1134] Yi Chen, Yuying Ge, Weiliang Tang, Yizhuo Li, Yixiao Ge, Mingyu Ding, Ying Shan, and Xihui
Liu. Moto: Latent motion token as the bridging language for learning robot manipulation
from videos. In 2025 IEEE/CVF International Conference on Computer Vision (ICCV), pages
19752–19763. IEEE, 2025.
[1135] Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Se June Joo, Jianwei Yang, Baolin Peng, Ajay
Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, et al. Latent action pretraining from
videos. In The Thirteenth International Conference on Learning Representations, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1136] Joel Jang, Seonghyeon Ye, Zongyu Lin, Jiannan Xiang, Johan Bjorck, Yu Fang, Fengyuan
Hu, Spencer Huang, Kaushil Kundalia, Yen-Chen Lin, Lo"ic Magne, Ajay Mandlekar, Avnish
Narayan, You Liang Tan, Guanzhi Wang, Jing Wang, Qi Wang, Yinzhen Xu, Xiaohui Zeng,
Kaiyuan Zheng, Ruijie Zheng, Ming-Yu Liu, Luke Zettlemoyer, Dieter Fox, Jan Kautz, Scott
Reed, Yuke Zhu, and Linxi Fan. Dreamgen: Unlocking generalization in robot learning
through video world models. In Proceedings of the 9th Conference on Robot Learning (CoRL),
pages 5170–5194, 2025.
[1137] Chen Wang, Linxi Fan, Jiankai Sun, Ruohan Zhang, Li Fei-Fei, Danfei Xu, Yuke Zhu, and
Anima Anandkumar. Mimicplay: Long-horizon imitation learning by watching human play.
In Conference on Robot Learning, pages 201–221. PMLR, 2023.
[1138] Anthony Liang, Pavel Czempin, Matthew Hong, Yutai Zhou, Erdem Biyik, and Stephen Tu.
Clam: Continuous latent action models for robot learning from unlabeled demonstrations.
arXiv preprint arXiv:2505.04999, 2025.
[1139] Jiange Yang, Yansong Shi, Haoyi Zhu, Mingyu Liu, Kaijing Ma, Yating Wang, Gangshan Wu,
Tong He, and Limin Wang. Como: Learning continuous latent motion from internet videos
for scalable robot learning. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 42352–42363, 2026.
[1140] Ruijie Zheng, Jing Wang, Scott Reed, Johan Bjorck, Yu Fang, Fengyuan Hu, Joel Jang, Kaushil
Kundalia, Zongyu Lin, Loic Magne, et al. FLARE: Robot learning with implicit world modeling.
In 9th Annual Conference on Robot Learning, 2025.
[1141] Erik Bauer, Elvis Nava, and Robert K. Katzschmann.
Latent action diffusion for cross-
embodiment manipulation.
In CoRL 2025 Workshop Dexterous Manipulation: Learning
and Control with Diverse Modalities, 2025.
[1142] Jianxin Bi, Kelvin Lim, Kaiqi Chen, Yifei Huang, and Harold Soh. Imitation learning with lim-
ited actions via diffusion planners and deep koopman controllers. In 2025 IEEE International
Conference on Robotics and Automation (ICRA), pages 4861–4868. IEEE, 2025.
[1143] Yuhang Huang, Jiazhao Zhang, Shilong Zou, Xinwang Liu, Ruizhen Hu, and Kai Xu. Ladi-wm:
A latent diffusion-based world model for predictive manipulation. In Proceedings of the 9th
Conference on Robot Learning (CoRL), pages 1726–1743, 2025.
[1144] Yunhai Han, Mandy Xie, Ye Zhao, and Harish Ravichandar. On the utility of koopman
operator theory in learning dexterous manipulation skills. In Conference on Robot Learning,
pages 106–126. PMLR, 2023.
[1145] Hongyi Chen, Abulikemu Abuduweili, Aviral Agrawal, Yunhai Han, Harish Ravichandar,
Changliu Liu, and Jeffrey Ichnowski. Korol: Learning visualizable object feature with koopman
operator rollout for manipulation. In CoRL, 2024.
[1146] Mengjiao Sherry Yang, Dale Schuurmans, Pieter Abbeel, and Ofir Nachum. Chain of thought
imitation with procedure cloning. In Advances in Neural Information Processing Systems,
volume 35, pages 36366–36381, 2022.
[1147] Vivek Myers, Andre Wang He, Kuan Fang, Homer Rich Walke, Philippe Hansen-Estruch,
Ching-An Cheng, Mihai Jalobeanu, Andrey Kolobov, Anca Dragan, and Sergey Levine. Goal
representations for instruction following: A semi-supervised language interface to control. In
Conference on Robot Learning, pages 3894–3908. PMLR, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1148] Xiaoyu Chen, Junliang Guo, Tianyu He, Chuheng Zhang, Pushi Zhang, Derek Cathera Yang,
Li Zhao, and Jiang Bian. Igor: Image-goal representations are the atomic control units for
foundation models in embodied ai. arXiv preprint arXiv:2411.00785, 2024.
[1149] Ryoga Oishi, Sho Sakaino, and Toshiaki Tsuji. Imitation learning based on disentangled
representation learning of behavioral characteristics. In Proceedings of the 9th Conference on
Robot Learning (CoRL), pages 4625–4640, 2025.
[1150] Ruizhe Liu, Pei Zhou, Qian Luo, Li Sun, Jun Cen, Yibing Song, and Yanchao Yang. Himacon:
Discovering hierarchical manipulation concepts from unlabeled multi-modal data. Advances
in Neural Information Processing Systems, 38, 2025.
[1151] Vedant Gupta, Haotian Fu, Calvin Luo, Yiding Jiang, and George Konidaris.
Learning
parameterized skills from demonstrations. Advances in Neural Information Processing Systems,
38:37721–37746, 2025.
[1152] Jiangran Lyu, Ziming Li, Xuesong Shi, Chaoyi Xu, Yizhou Wang, and He Wang. Dywa:
Dynamics-adaptive world action model for generalizable non-prehensile manipulation. In
ICRA 2025 Workshop: Beyond Pick and Place, 2025.
[1153] Tony Z Zhao, Vikash Kumar, Sergey Levine, and Chelsea Finn. Learning fine-grained bimanual
manipulation with low-cost hardware. In Robotics: Science and Systems, 2023.
[1154] Thanpimon Buamanee, Masato Kobayashi, Yuki Uranishi, and Haruo Takemura. Bi-act:
Bilateral control-based imitation learning via action chunking with transformer. In 2024 IEEE
International Conference on Advanced Intelligent Mechatronics (AIM), pages 410–415. IEEE,
2024.
[1155] Andrew Choong-Won Lee, Ian Chuang, Ling-Yuan Chen, and Iman Soltani. Interact: Inter-
dependency aware action chunking with hierarchical attention transformers for bimanual
manipulation. In 8th Annual Conference on Robot Learning, 2024.
[1156] Kelin Li, Shubham M Wagh, Nitish Sharma, Saksham Bhadani, Wei Chen, Chang Liu, and
Petar Kormushev. Haptic-act: Bridging human intuition with compliant robotic manipulation
via immersive vr. In 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems
(IROS), pages 1084–1091. IEEE, 2025.
[1157] Tony Z. Zhao, Jonathan Tompson, Danny Driess, Pete Florence, Seyed Kamyar Seyed
Ghasemipour, Chelsea Finn, and Ayzaan Wahid. Aloha unleashed: A simple recipe for
robot dexterity. In 8th Annual Conference on Robot Learning, 2024.
[1158] Zhenyu Pan, Haozheng Luo, Manling Li, and Han Liu. Chain-of-action: Faithful and multi-
modal question answering through large language models. In International Conference on
Learning Representations, volume 2025, pages 63920–63939, 2025.
[1159] Qiyang Li, Zhiyuan Paul Zhou, and Sergey Levine. Reinforcement learning with action
chunking. Advances in Neural Information Processing Systems, 38:55518–55553, 2025.
[1160] Yue Su, Xinyu Zhan, Hongjie Fang, Han Xue, Hao-Shu Fang, Yong-Lu Li, Cewu Lu, and Lixin
Yang. Dense policy: Bidirectional autoregressive learning of actions. In 2025 IEEE/CVF
International Conference on Computer Vision (ICCV), pages 14486–14495. IEEE, 2025.
[1161] Zhenyang Liu, Yikai Wang, Kuanning Wang, Longfei Liang, Xiangyang Xue, and Yanwei Fu.
Spatial-temporal aware visuomotor diffusion policy learning. In 2025 IEEE/CVF International
Conference on Computer Vision (ICCV), pages 1–10. IEEE, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1162] Yiyang Lu, Yufeng Tian, Zhecheng Yuan, Xianbang Wang, Pu Hua, Zhengrong Xue, and
Huazhe Xu. H3dp: Triply-hierarchical diffusion policy for visuomotor learning. In International
Conference on Learning Representations, volume 2026, pages 13237–13261, 2026.
[1163] Minjie Zhu, Yichen Zhu, Jinming Li, Junjie Wen, Zhiyuan Xu, Ning Liu, Ran Cheng, Chaomin
Shen, Yaxin Peng, Feifei Feng, et al. Scaling diffusion policy in transformer to 1 billion
parameters for robotic manipulation. In 2025 IEEE International Conference on Robotics and
Automation (ICRA), pages 10838–10845. IEEE, 2025.
[1164] Songming Liu, Lingxuan Wu, Bangguo Li, Hengkai Tan, Huayu Chen, Zhengyi Wang, Ke Xu,
Hang Su, and Jun Zhu. Rdt-1b: a diffusion foundation model for bimanual manipulation.
In International Conference on Learning Representations, volume 2025, pages 29982–30009,
2025.
[1165] Zhendong Wang, Max Li, Ajay Mandlekar, Zhenjia Xu, Jiaojiao Fan, Yashraj Narang, Linxi Fan,
Yuke Zhu, Yogesh Balaji, Mingyuan Zhou, Ming-Yu Liu, and Yu Zeng. One-step diffusion policy:
Fast visuomotor policies via diffusion distillation. In Proceedings of the 42nd International
Conference on Machine Learning (ICML), pages 63399–63416, 2025.
[1166] Yixiao Wang, Yifei Zhang, Mingxiao Huo, Thomas Tian, Xiang Zhang, Yichen Xie, Chenfeng
Xu, Pengliang Ji, Wei Zhan, Mingyu Ding, et al. Sparse diffusion policy: A sparse, reusable,
and flexible policy for robot learning. In Conference on Robot Learning, pages 649–665. PMLR,
2025.
[1167] David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, and
Adam Santoro. Mixture-of-depths: Dynamically allocating compute in transformer-based
language models. arXiv preprint arXiv:2404.02258, 2024.
[1168] Jingyun Yang, Ziang Cao, Congyue Deng, Rika Antonova, Shuran Song, and Jeannette Bohg.
Equibot: Sim (3)-equivariant diffusion policy for generalizable and data efficient learning. In
Conference on Robot Learning, pages 1048–1068. PMLR, 2025.
[1169] Dian Wang, Stephen Hart, David Surovik, Tarik Kelestemur, Haojie Huang, Haibo Zhao, Mark
Yeatman, Jiuguang Wang, Robin Walters, and Robert Platt. Equivariant diffusion policy. In
Conference on Robot Learning, pages 48–69. PMLR, 2025.
[1170] Yilun Du, Sherry Yang, Bo Dai, Hanjun Dai, Ofir Nachum, Josh Tenenbaum, Dale Schuurmans,
and Pieter Abbeel. Learning universal policies via text-guided video generation. Advances in
neural information processing systems, 36:9156–9172, 2023.
[1171] Shuang Li, Yihuai Gao, Dorsa Sadigh, and Shuran Song. Unified video action model. In
Robotics: Science and Systems, 2025.
[1172] Allen Z Ren, Justin Lidard, Lars Lien Ankile, Anthony Simeonov, Pulkit Agrawal, Anirudha
Majumdar, Benjamin Burchfiel, Hongkai Dai, and Max Simchowitz. Diffusion policy policy
optimization. In CoRL 2024 Workshop on Mastering Robot Manipulation in a World of Abundant
Data, 2024.
[1173] Amber Xie, Oleh Rybkin, Dorsa Sadigh, and Chelsea Finn. Latent diffusion planning for
imitation learning. In Proceedings of the 42nd International Conference on Machine Learning
(ICML), pages 68710–68724, 2025.
[1174] Yue Su, Xinyu Zhan, Hongjie Fang, Yong-Lu Li, Cewu Lu, and Lixin Yang. Motion before
action: Diffusing object motion as manipulation condition. IEEE Robotics and Automation
Letters, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1175] Marcel Torne Villasevil, Andy Tang, Yuejiang Liu, and Chelsea Finn. Learning long-context
diffusion policies via past-token prediction. In 9th Annual Conference on Robot Learning,
2025.
[1176] Yipu Chen, Haotian Xue, and Yongxin Chen. Diffusion policy attacker: Crafting adversarial
attacks for diffusion-based policies. In Advances in Neural Information Processing Systems,
volume 37, pages 119614–119637, 2024.
[1177] Xixi Hu, Qiang Liu, Xingchao Liu, and Bo Liu. Adaflow: Imitation learning with variance-
adaptive flow-based policies. Advances in Neural Information Processing Systems, 37:138836–
138858, 2024.
[1178] Xiaogang Jia, Atalay Donat, Xi Huang, Xuan Zhao, Denis Blessing, Hongyi Zhou, Hanyi
Zhang, Han A. Wang, Qian Wang, Rudolf Lioutikov, and Gerhard Neumann. X-IL: Exploring
the design space of imitation learning policies. In 7th Robot Learning Workshop: Towards
Robots with Human-Level Abilities, 2025.
[1179] Sunshine Jiang, Xiaolin Fang, Nicholas Roy, Tomás Lozano-Pérez, Leslie Pack Kaelbling, and
Siddharth Ancha. Streaming flow policy: Simplifying diffusion/flow-matching policies by
treating action trajectories as flow trajectories. In Proceedings of the 9th Conference on Robot
Learning (CoRL), pages 238–257, 2025.
[1180] Hongzhe Bi, Lingxuan Wu, Tianwei Lin, Hengkai Tan, Zhizhong Su, Hang Su, and Jun Zhu.
H-rdt: Human manipulation enhanced bimanual robotic manipulation. In Proceedings of the
AAAI Conference on Artificial Intelligence, volume 40, pages 18135–18143, 2026.
[1181] Xuanran Zhai and Ce Hao. Vfp: Variational flow-matching policy for multi-modal robot
manipulation. In 2026 IEEE International Conference on Robotics and Automation (ICRA),
2026.
[1182] Ge Yan, Jiyue Zhu, Yuquan Deng, Shiqi Yang, Ri-Zhao Qiu, Xuxin Cheng, Marius Memmel,
Ranjay Krishna, Ankit Goyal, Xiaolong Wang, and Dieter Fox. Maniflow: A general robot
manipulation policy via consistency flow training. In Proceedings of the 9th Conference on
Robot Learning (CoRL), pages 2268–2293, 2025.
[1183] Juyi Sheng, Ziyi Wang, Peiming Li, and Mengyuan Liu.
Mp1: Meanflow tames policy
learning in 1-step for robotic manipulation. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 40, pages 18532–18539, 2026.
[1184] Jindou Jia, Gen Li, Xiangyu Chen, Tuo An, Yuxuan Hu, Jingliang Li, Xinying Guo, and Jianfei
Yang. Action-to-action flow matching. In Robotics: Science and Systems, 2026.
[1185] Eugenio Chisari, Nick Heppert, Max Argus, Tim Welschehold, Thomas Brox, and Abhinav
Valada. Learning robotic manipulation policies from point clouds with conditional flow
matching. In 8th Annual Conference on Robot Learning, 2024.
[1186] Qinglun Zhang, Zhen Liu, Haoqiang Fan, Guanghui Liu, Bing Zeng, and Shuaicheng Liu.
Flowpolicy: Enabling fast and robust 3d flow-based policy via consistency flow matching for
robot manipulation. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39,
pages 14754–14762, 2025.
[1187] Fan Zhang and Michael Gienger. Affordance-based robot manipulation with flow matching.
arXiv preprint arXiv:2409.01083, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1188] Sen Wang, Le Wang, Sanping Zhou, Jingyi Tian, Jiayi Li, Haowen Sun, and Wei Tang.
Flowram: Grounding flow matching policy with region-aware mamba framework for robotic
manipulation. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages
12176–12186, 2025.
[1189] Xiaogang Jia, Qian Wang, Atalay Donat, Bowen Xing, Ge Li, Hongyi Zhou, Onur Celik, Denis
Blessing, Rudolf Lioutikov, and Gerhard Neumann. Mail: Improving imitation learning with
selective state space models. In 8th Annual Conference on Robot Learning, 2024.
[1190] Yulin Zhou, Yuankai Lin, Fanzhe Peng, Jiahui Chen, Kaiji Huang, Hua Yang, and Zhouping
Yin. Mtil: Encoding full history with mamba for temporal imitation learning. IEEE Robotics
and Automation Letters, 2025.
[1191] Toshiaki Tsuji. Mamba as a motion encoder for robotic imitation learning. IEEE Access, 2025.
[1192] Zhixing Hou, Maoxu Gao, Hang Yu, Mengyu Yang, Di Zhu, and Chio-In Ieong. Sdp: spiking
diffusion policy for robotic manipulation with learnable channel-wise membrane thresholds.
In Chinese Conference on Pattern Recognition and Computer Vision (PRCV), pages 312–327.
Springer, 2025.
[1193] Qianhao Wang, Yinqian Sun, Enmeng Lu, Qian Zhang, and Yi Zeng. Brain-inspired action
generation with spiking transformer diffusion policy model. In International Conference on
Brain Inspired Cognitive Systems, pages 229–238. Springer, 2024.
[1194] Liwen Zhang, Dong Zhou, Shibo Shao, Zihao Su, and Guanghui Sun. Multimodal spiking
neural network for space robotic manipulation. arXiv preprint arXiv:2508.07287, 2025.
[1195] Liwen Zhang, Heng Deng, and Guanghui Sun. Fully spiking actor-critic neural network for
robotic manipulation. arXiv preprint arXiv:2508.12038, 2025.
[1196] Haojie Huang, Owen Howell, Dian Wang, Xupeng Zhu, Robert Platt, and Robin Walters.
Fourier transporter: Bi-equivariant robotic manipulation in 3d. In International Conference
on Learning Representations, volume 2024, pages 40733–40754, 2024.
[1197] Yiming Zhong, Yumeng Liu, Chuyang Xiao, Zemin Yang, Youzhuo Wang, Yufei Zhu, Ye Shi,
Yujing Sun, Xinge Zhu, and Yuexin Ma. Freqpolicy: Frequency autoregressive visuomotor
policy with continuous tokens. Advances in Neural Information Processing Systems, 38:56493–
56526, 2025.
[1198] Hao Huang, Shuaihang Yuan, Geeta Chandra Raju Bethala, Congcong Wen, Anthony Tzes,
and Yi Fang. Wavelet policy: Lifting scheme for policy learning in long-horizon tasks. In 2025
IEEE/CVF International Conference on Computer Vision (ICCV), pages 12349–12359. IEEE,
2025.
[1199] Geonhyup Lee, Yeongjin Lee, Kangmin Kim, Seongju Lee, Sangjun Noh, Seunghyeok Back,
and Kyoobin Lee. Manipforce: Force-guided policy learning with frequency-aware represen-
tation for contact-rich manipulation. In 2026 IEEE International Conference on Robotics and
Automation (ICRA), 2026.
[1200] Karl Pertsch, Kyle Stachowicz, Brian Ichter, Danny Driess, Suraj Nair, Quan Vuong, Oier Mees,
Chelsea Finn, and Sergey Levine. Fast: Efficient action tokenization for vision-language-action
models. arXiv preprint arXiv:2501.09747, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1201] Kunyun Wang, Yuhang Zheng, Yupeng Zheng, Jieru Zhao, and Wenchao Ding. Learning high-
frequency continuous action chunks in latent space. In Forty-third International Conference
on Machine Learning, 2026.
[1202] Bing-Cheng Chuang, I-Hsuan Chu, Bor-Jiun Lin, YuanFu Yang, Min Sun, and Chun-Yi Lee.
The lie we tell: Correcting the euclidean fallacy in vision language action policies via score
matching on tangent space. In Forty-third International Conference on Machine Learning,
2026.
[1203] Fan Yang, Peiguang Jing, Kaihua Qu, Ningyuan Zhao, and Yuting Su. Abpolicy: Asynchronous
b-spline flow policy for real-time and smooth robotic manipulation. In 2026 IEEE International
Conference on Robotics and Automation (ICRA), 2026.
[1204] Yuxuan Gao, Yedong Shen, Shiqi Zhang, Wenhao Yu, Yifan Duan, Jiajia Wu, Jiajun Deng,
Yanyong Zhang, et al. Drift-based policy optimization: Native one-step policy learning for
online robot control. arXiv preprint arXiv:2604.03540, 2026.
[1205] Zemin Yang, Yaoyu He, Yiming Zhong, Yuhao Zhang, Xinge Zhu, Yao Mu, Qingqiu Huang,
and Yuexin Ma. Implicit drifting policy: One-step action generation via conditional expert
geometry. arXiv preprint arXiv:2606.01098, 2026.
[1206] Huayi Zhou, Ruixiang Wang, Yunxin Tai, Yueci Deng, Guiliang Liu, and Kui Jia. You only
teach once: Learn one-shot bimanual robotic manipulation from video demonstrations. In
Robotics: Science and Systems, 2025.
[1207] Chaoyi Pan, Giridharan Anantharaman, Nai-Chieh Huang, Claire Jin, Daniel Pfrommer,
Chenyang Yuan, Frank Permenter, Guannan Qu, Nicholas Boffi, Guanya Shi, et al. Much ado
about noising: Dispelling the myths of generative robotic control. In International Conference
on Learning Representations, volume 2026, pages 90575–90614, 2026.
[1208] Dechen Gao, Boqi Zhao, Andrew Lee, Ian Chuang, Hanchu Zhou, Hang Wang, Zhe Zhao,
Junshan Zhang, and Iman Soltani. Vita: Vision-to-action flow matching policy. In International
Conference on Learning Representations, volume 2026, pages 100903–100933, 2026.
[1209] Md Tanvir Islam, Sai Navaneet Peddapalli, Sangmoon Lee, and Sangtae Ahn. Sureflow:
State-space uncertainty-aware residual flow matching for robust robot manipulation. In 2026
IEEE/RSJ international conference on intelligent robots and systems (IROS), 2026.
[1210] Sarah Young, Dhiraj Gandhi, Shubham Tulsiani, Abhinav Gupta, Pieter Abbeel, and Lerrel
Pinto. Visual imitation made easy. In Conference on Robot learning, pages 1992–2005. PMLR,
2021.
[1211] Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk, Hao Su, Xiaolong Wang, Yu-Wei Chao,
and Dieter Fox. Anyteleop: A general vision-based dexterous robot arm-hand teleoperation
system. In Robotics: Science and Systems, 2023.
[1212] Philipp Wu, Yide Shentu, Zhongke Yi, Xingyu Lin, and Pieter Abbeel. Gello: A general,
low-cost, and intuitive teleoperation framework for robot manipulators. In 2024 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 12156–12163. IEEE,
2024.
[1213] Aadhithya Iyer, Zhuoran Peng, Yinlong Dai, Irmak Guzey, Siddhant Haldar, Soumith Chintala,
and Lerrel Pinto. Open teach: A versatile teleoperation system for robotic manipulation. In
Conference on Robot Learning, pages 2372–2395. PMLR, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1214] Heecheol Kim, Yoshiyuki Ohmura, Akihiko Nagakubo, and Yasuo Kuniyoshi. Training robots
without robots: deep imitation learning for master-to-robot policy transfer. IEEE Robotics and
Automation Letters, 8(5):2906–2913, 2023.
[1215] Masato Kobayashi, Thanpimon Buamanee, and Takumi Kobayashi. Alpha-𝛼and bi-act are
all you need: Importance of position and force information/control for imitation learning of
unimanual and bimanual robotic manipulation with low-cost system. IEEE Access, 2025.
[1216] Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia, Shiqi Yang, Ruihan Yang, Xiaojuan Qi, and
Xiaolong Wang. Bunny-visionpro: Real-time bimanual dexterous teleoperation for imitation
learning. In 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS),
pages 12248–12255. IEEE, 2025.
[1217] Longyan Wu, Checheng Yu, Jieji Ren, Li Chen, Yufei Jiang, Ran Huang, Guoying Gu, and
Hongyang Li. Freetacman: Robot-free visuo-tactile data collection system for contact-rich
manipulation. In 2026 IEEE International Conference on Robotics and Automation (ICRA),
2026.
[1218] Tianhao Zhang, Zoe McCarthy, Owen Jow, Dennis Lee, Xi Chen, Ken Goldberg, and Pieter
Abbeel. Deep imitation learning for complex manipulation tasks from virtual reality tele-
operation. In 2018 IEEE international conference on robotics and automation (ICRA), pages
5628–5635. Ieee, 2018.
[1219] Simar Kareer, Dhruv Patel, Ryan Punamiya, Pranay Mathur, Shuo Cheng, Chen Wang, Judy
Hoffman, and Danfei Xu. Egomimic: Scaling imitation learning via egocentric video. In 2025
IEEE International Conference on Robotics and Automation (ICRA), pages 13226–13233. IEEE,
2025.
[1220] Sirui Chen, Chen Wang, Kaden Nguyen, Li Fei-Fei, and C Karen Liu. Arcap: Collecting
high-quality human demonstrations for robot learning with augmented reality feedback. In
2025 IEEE International Conference on Robotics and Automation (ICRA), pages 8291–8298.
IEEE, 2025.
[1221] Ian Chuang, Andrew Lee, Dechen Gao, Mahdi Naddaf, and Iman Soltani. Active vision might
be all you need: Exploring active vision in bimanual robotic manipulation. In CoRL 2024
Workshop on Whole-body Control and Bimanual Manipulation: Applications in Humanoids and
Beyond, 2024.
[1222] Hongjie Fang, Hao-Shu Fang, Yiming Wang, Jieji Ren, Jingjing Chen, Ruo Zhang, Weiming
Wang, and Cewu Lu. Airexo: Low-cost exoskeletons for learning whole-arm manipulation in
the wild. In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages
15031–15038. IEEE, 2024.
[1223] Chen Wang, Haochen Shi, Weizhuo Wang, Ruohan Zhang, Li Fei-Fei, and Karen Liu. Dexcap:
Scalable and portable mocap data collection system for dexterous manipulation. In RSS 2024
Workshop: Data Generation for Robotics, 2024.
[1224] Mengda Xu, Han Zhang, Yifan Hou, Zhenjia Xu, Linxi Fan, Manuela Veloso, and Shuran
Song. Dexumi: Using human hand as the universal manipulation interface for dexterous
manipulation. In 3rd RSS Workshop on Dexterous Manipulation: Learning and Control with
Diverse Data, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1225] Zilin Si, Kevin Lee Zhang, Zeynep Temel, and Oliver Kroemer. Tilde: Teleoperation for
dexterous in-hand manipulation learning with a deltahand. In 2nd Workshop on Dexterous
Manipulation: Design, Perception and Control (RSS), 2024.
[1226] Shivin Dass, Wensi Ai, Yuqian Jiang, Samik Singh, Jiaheng Hu, Ruohan Zhang, Peter Stone,
Ben Abbatematteo, and Roberto Martín-Martín. Telemoma: A modular and versatile teleop-
eration system for mobile manipulation. In RSS 2024 Workshop: Data Generation for Robotics,
2024.
[1227] Yuhao Lin, Yi-Lin Wei, Haoran Liao, Mu Lin, Chengyi Xing, Hao Li, Dandan Zhang, Mark
Cutkosky, and Wei-Shi Zheng. Typetele: Releasing dexterity in teleoperation by dexterous
manipulation types. In Proceedings of the 9th Conference on Robot Learning (CoRL), pages
4975–4993, 2025.
[1228] Ryan Hoque, Ajay Mandlekar, Caelan Garrett, Ken Goldberg, and Dieter Fox. Intervengen:
Interventional data generation for robust and data-efficient robot imitation learning. In 2024
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 2840–2846.
IEEE, 2024.
[1229] Xiaomeng Xu, Yifan Hou, Zeyi Liu, and Shuran Song. Compliant residual dagger: Improving
real-world contact-rich manipulation with human corrections. Advances in Neural Information
Processing Systems, 38:139559–139581, 2025.
[1230] Huy Ha, Pete Florence, and Shuran Song. Scaling up and distilling down: Language-guided
robot skill acquisition. In Conference on Robot Learning, pages 3766–3777. PMLR, 2023.
[1231] Jiafei Duan, Wentao Yuan, Wilbert Pumacay, Yi Ru Wang, Kiana Ehsani, Dieter Fox, and
Ranjay Krishna. Manipulate-anything: Automating real-world robots using vision-language
models. In Conference on Robot Learning, pages 5326–5350. PMLR, 2025.
[1232] Zhiyuan Zhou, Pranav Atreya, Abraham Lee, Homer Rich Walke, Oier Mees, and Sergey
Levine. Autonomous improvement of instruction following skills via foundation models. In
Conference on Robot Learning, pages 4805–4825. PMLR, 2025.
[1233] Ajay Mandlekar, Soroush Nasiriany, Bowen Wen, Iretiayo Akinola, Yashraj Narang, Linxi Fan,
Yuke Zhu, and Dieter Fox. Mimicgen: A data generation system for scalable robot learning
using human demonstrations. In Conference on Robot Learning, pages 1820–1864. PMLR,
2023.
[1234] Zhenyu Jiang, Yuqi Xie, Kevin Lin, Zhenjia Xu, Weikang Wan, Ajay Mandlekar, Linxi Fan, and
Yuke Zhu. Dexmimicgen: Automated data generation for bimanual dexterous manipulation
via imitation learning. In CoRL Workshop on Learning Robot Fine and Dexterous Manipulation:
Perception and Control, 2024.
[1235] Caelan Reed Garrett, Ajay Mandlekar, Bowen Wen, and Dieter Fox. Skillmimicgen: Automated
demonstration generation for efficient skill learning and deployment. In Conference on Robot
Learning, pages 2750–2790. PMLR, 2025.
[1236] Zhengrong Xue, Shuying Deng, Zhenyang Chen, Yixuan Wang, Zhecheng Yuan, and Huazhe
Xu. Demogen: Synthetic demonstration generation for data-efficient visuomotor policy
learning. In Robotics: Science and Systems, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1237] Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang,
Qinxi Yu, Xiaolong Wang, Phillip Isola, and Ge Yang. Lucid-xr: An extended-reality data
engine for robotic manipulation. In Proceedings of the 9th Conference on Robot Learning
(CoRL), pages 5151–5169, 2025.
[1238] Lujie Yang, HJ Suh, Tong Zhao, Bernhard Paus Graesdal, Tarik Kelestemur, Jiuguang Wang,
Tao Pang, and Russ Tedrake. Physics-driven data generation for contact-rich manipulation
via trajectory optimization. In Robotics: Science and Systems, 2025.
[1239] Kevin Lin, Varun Ragunath, Andrew McAlinden, Aaditya Prasad, Jimmy Wu, Yuke Zhu, and
Jeannette Bohg. Constraint-preserving data generation for visuomotor policy learning. In
Conference on Robot Learning, 2025.
[1240] Chengshu Li, Mengdi Xu, Arpit Bahety, Hang Yin, Yunfan Jiang, Huang Huang, Josiah Wong,
Sujay Garlanka, Cem Gokmen, Ruohan Zhang, et al. Momagen: Generating demonstrations
under soft and hard constraints for multi-step bimanual mobile manipulation. In International
Conference on Learning Representations, volume 2026, pages 112425–112446, 2026.
[1241] Konstantinos Bousmalis, Giulia Vezzani, Dushyant Rao, Coline Manon Devin, Alex X Lee,
Maria Bauza Villalonga, Todor Davchev, Yuxiang Zhou, Agrim Gupta, Akhil Raju, et al.
Robocat: A self-improving generalist agent for robotic manipulation. Transactions on Machine
Learning Research, 2023.
[1242] Kefei Zhu, Fengshuo Bai, YuanHao Xiang, Yishuai Cai, Xinglin Chen, Ruochong Li, Xingtao
Wang, Hao Dong, Yaodong Yang, Xiaopeng Fan, et al. Dexflywheel: A scalable and self-
improving data generation framework for dexterous manipulation.
Advances in Neural
Information Processing Systems, 38:4236–4265, 2025.
[1243] Michael Jae-Yoon Chung, Maxwell Forbes, Maya Cakmak, and Rajesh PN Rao. Accelerating
imitation learning through crowdsourcing. In 2014 IEEE International Conference on Robotics
and Automation (ICRA), pages 4777–4784. IEEE, 2014.
[1244] Ajay Mandlekar, Yuke Zhu, Animesh Garg, Jonathan Booher, Max Spero, Albert Tung, Julian
Gao, John Emmons, Anchit Gupta, Emre Orbay, et al. Roboturk: A crowdsourcing platform
for robotic skill learning through imitation. In Conference on Robot Learning, pages 879–893.
PMLR, 2018.
[1245] Louise David, Eliana Vassena, and Erik Bijleveld. The unpleasantness of thinking: A meta-
analytic review of the association between mental effort and negative affect. Psychological
Bulletin, 2024.
[1246] Albert Tung, Josiah Wong, Ajay Mandlekar, Roberto Martín-Martín, Yuke Zhu, Li Fei-Fei, and
Silvio Savarese. Learning multi-arm manipulation through collaborative teleoperation. In
2021 IEEE International Conference on Robotics and Automation (ICRA), pages 9212–9219.
IEEE, 2021.
[1247] Jiafei Duan, Yi Ru Wang, Mohit Shridhar, Dieter Fox, and Ranjay Krishna. Ar2-d2: Training a
robot without a robot. In Conference on Robot Learning, pages 2838–2848. PMLR, 2023.
[1248] Vincent Liu, Ademi Adeniji, Haotian Zhan, Siddhant Haldar, Raunaq Bhirangi, Pieter
Abbeel, and Lerrel Pinto.
Egozero: Robot learning from smart glasses.
arXiv preprint
arXiv:2505.20290, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1249] Ayush Agarwal, Ansh Gandhi, Jeremy A Collins, Omar Rayyan, Aryan Sarswat, Ranjani
Koushik, Masoud Moghani, Ajay Mandlekar, and Animesh Garg. Cobalt: Crowdsourcing
robot learning via cloud-based teleoperation with smartphones. In 2026 IEEE International
Conference on Robotics and Automation (ICRA), 2026.
[1250] Kanishk Gandhi, Siddharth Karamcheti, Madeline Liao, and Dorsa Sadigh. Eliciting compatible
demonstrations for multi-human imitation learning. In Conference on Robot Learning, pages
1981–1991. PMLR, 2023.
[1251] Ray Chen Zheng, Kaizhe Hu, Zhecheng Yuan, Boyuan Chen, and Huazhe Xu. Extraneousness-
aware imitation learning. In 2023 IEEE International Conference on Robotics and Automation
(ICRA), pages 2973–2979. IEEE, 2023.
[1252] Suneel Belkhale, Yuchen Cui, and Dorsa Sadigh. Data quality in imitation learning. Advances
in neural information processing systems, 36:80375–80395, 2023.
[1253] Sudeep Dasari, Mohan Kumar Srirama, Unnat Jain, and Abhinav Gupta. An unbiased look at
datasets for visuo-motor pre-training. In Conference on Robot Learning, pages 1183–1198.
PMLR, 2023.
[1254] Sachit Kuhar, Shuo Cheng, Shivang Chopra, Matthew Bronars, and Danfei Xu. Learning to
discern: Imitating heterogeneous human demonstrations with preference and representation
learning. In Conference on Robot Learning, pages 1437–1449. PMLR, 2023.
[1255] Sheng Yue, Jiani Liu, Xingyuan Hua, Ju Ren, Sen Lin, Junshan Zhang, and Yaoxue Zhang. How
to leverage diverse demonstrations in offline imitation learning. In International Conference
on Machine Learning, pages 58037–58067. PMLR, 2024.
[1256] Joey Hejna, Chethan Anand Bhateja, Yichen Jiang, Karl Pertsch, and Dorsa Sadigh. Remix:
Optimizing data mixtures for large scale imitation learning. In Conference on Robot Learning,
pages 145–164. PMLR, 2025.
[1257] Vaibhav Saxena, Matthew Bronars, Nadun Ranawaka Arachchige, Kuancheng Wang, Woo Chul
Shin, Soroush Nasiriany, Ajay Mandlekar, and Danfei Xu. What matters in learning from
large-scale datasets for robot manipulation. In The Thirteenth International Conference on
Learning Representations, 2025.
[1258] Christopher Agia, Rohan Sinha, Jingyun Yang, Rika Antonova, Marco Pavone, Haruki
Nishimura, Masha Itkina, and Jeannette Bohg. Cupid: Curating data your robot loves
with influence functions. In Proceedings of the 9th Conference on Robot Learning (CoRL), pages
2907–2932, 2025.
[1259] Jyothish Pari, Nur Muhammad Mahi Shafiullah, Sridhar Pandian Arunachalam, and Lerrel
Pinto. The surprising effectiveness of representation learning for visual imitation. In 18th
Robotics: Science and Systems, RSS 2022. MIT Press Journals, 2022.
[1260] Soroush Nasiriany, Tian Gao, Ajay Mandlekar, and Yuke Zhu. Learning and retrieval from prior
data for skill-based imitation learning. In Conference on Robot Learning, pages 2181–2204.
PMLR, 2023.
[1261] Maximilian Du, Suraj Nair, Dorsa Sadigh, and Chelsea Finn. Behavior retrieval: Few-shot
imitation learning by querying unlabeled datasets. In Robotics: Science and Systems, 2023.
[1262] Norman Di Palo and Edward Johns. On the effectiveness of retrieval, alignment, and replay
in manipulation. IEEE Robotics and Automation Letters, 9(3):2032–2039, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1263] Norman Di Palo and Edward Johns. Dinobot: Robot manipulation via retrieval and align-
ment with vision foundation models. In 2024 IEEE International Conference on Robotics and
Automation (ICRA), pages 2798–2805. IEEE, 2024.
[1264] Yichen Zhu, Zhicai Ou, Xiaofeng Mou, and Jian Tang. Retrieval-augmented embodied agents.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
17985–17995, 2024.
[1265] Zhao-Heng Yin and Pieter Abbeel. Offline imitation learning through graph search and
retrieval. In Robotics: Science and Systems, 2024.
[1266] Li-Heng Lin, Yuchen Cui, Amber Xie, Tianyu Hua, and Dorsa Sadigh. Flowretrieval: Flow-
guided data retrieval for few-shot imitation learning. In Conference on Robot Learning, pages
4084–4099. PMLR, 2025.
[1267] Marius Memmel, Jacob Berg, Bingqing Chen, Abhishek Gupta, and Jonathan Francis. Strap:
Robot sub-trajectory retrieval for augmented policy learning. In The Thirteenth International
Conference on Learning Representations, 2025.
[1268] Sateesh Kumar, Shivin Dass, Georgios Pavlakos, and Roberto Martín-Martín. Collage: Adaptive
fusion-based retrieval for augmented policy learning. In Conference on Robot Learning. PMLR,
2025.
[1269] Ted Xiao, Harris Chan, Pierre Sermanet, Ayzaan Wahid, Anthony Brohan, Karol Hausman,
Sergey Levine, and Jonathan Tompson. Robotic skill acquisition via instruction augmentation
with vision-language models. In Robotics: Science and Systems, 2023.
[1270] Jesse Zhang, Karl Pertsch, Jiahui Zhang, and Joseph J Lim. Sprint: Scalable policy pre-training
via language instruction relabeling. In 2024 IEEE International Conference on Robotics and
Automation (ICRA), pages 9168–9175. IEEE, 2024.
[1271] Nils Blank, Moritz Reuss, Marcel Rühle, Ömer Erdinç Yağmurlu, Fabian Wenzel, Oier Mees,
and Rudolf Lioutikov. Scaling robot policy learning via zero-shot labeling with foundation
models. In Conference on Robot Learning, pages 4158–4187. PMLR, 2025.
[1272] Norman Di Palo, Leonard Hasenclever, Jan Humplik, and Arunkumar Byravan. Diffusion
augmented agents: A framework for efficient exploration and transfer learning. In Conference
on Lifelong Learning Agents, pages 268–284. PMLR, 2025.
[1273] Jingjing Chen, Hongjie Fang, Hao-Shu Fang, and Cewu Lu. Towards effective utilization
of mixed-quality demonstrations in robotic manipulation via segment-level selection and
optimization. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages
16884–16891. IEEE, 2025.
[1274] Yiming Ding, Carlos Florensa, Pieter Abbeel, and Mariano Phielipp. Goal-conditioned imitation
learning. In Advances in neural information processing systems, volume 32, 2019.
[1275] Zexu Sun, Bowei He, Jinxin Liu, Xu Chen, Chen Ma, and Shuai Zhang. Offline imitation
learning with variational counterfactual reasoning. Advances in Neural Information Processing
Systems, 36:43729–43741, 2023.
[1276] Peter Mitrano and Dmitry Berenson. Data augmentation for manipulation. In Robotics:
Science and Systems, 2022.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1277] Qiang Wang, Robert McCarthy, David Cordova Bulens, Francisco Roldan Sanchez, Kevin
McGuinness, Noel E O’Connor, and Stephen J Redmond. Identifying expert behavior in offline
training datasets improves behavioral cloning of robotic manipulation policies. IEEE Robotics
and Automation Letters, 9(2):1294–1301, 2023.
[1278] Mingxi Jia, Dian Wang, Guanang Su, David Klee, Xupeng Zhu, Robin Walters, and Robert
Platt. Seil: Simulation-augmented equivariant imitation learning. In 2023 IEEE International
Conference on Robotics and Automation (ICRA), pages 1845–1851. IEEE, 2023.
[1279] Zoey Chen, Sho Kiami, Abhishek Gupta, and Vikash Kumar. Genaug: Retargeting behaviors
to unseen situations via generative augmentation. In Robotics: Science and Systems, 2023.
[1280] Lawrence Yunliang Chen, Chenfeng Xu, Karthik Dharmarajan, Richard Cheng, Kurt Keutzer,
Masayoshi Tomizuka, Quan Vuong, and Ken Goldberg. Rovi-aug: Robot and viewpoint
augmentation for cross-embodiment robot learning. In Conference on Robot Learning, pages
209–233. PMLR, 2025.
[1281] Tao Tang, Likui Zhang, Youpeng Wen, Kaidong Zhang, Jia-Wang Bian, Xia Zhou, Tianyi Yan,
Kun Zhan, Peng Jia, Hefeng Wu, Liang Lin, and Xiaodan Liang. Robopearls: Editable video
simulation for robot manipulation. In Proceedings of the IEEE/CVF International Conference
on Computer Vision, 2025.
[1282] Tianhe Yu, Ted Xiao, Austin Stone, Jonathan Tompson, Anthony Brohan, Su Wang, Jaspiar
Singh, Clayton Tan, Jodilyn Peralta, Brian Ichter, et al. Scaling robot learning with semantically
imagined experience. In Robotics: Science and Systems, 2023.
[1283] Xiaoyu Zhang, Matthew Chang, Pranav Kumar, and Saurabh Gupta. Diffusion meets dagger:
Supercharging eye-in-hand imitation learning. In Robotics: Science and Systems, 2024.
[1284] Stephen Tian, Blake Wulfe, Kyle Sargent, Katherine Liu, Sergey Zakharov, Vitor Campagnolo
Guizilini, and Jiajun Wu. View-invariant policy learning via zero-shot novel view synthesis.
In Conference on Robot Learning, pages 1173–1193. PMLR, 2025.
[1285] Masato Kobayashi, Thanpimon Buamanee, and Yuki Uranishi. Dabi: Evaluation of data
augmentation methods using downsampling in bilateral control-based imitation learning
with images. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages
16892–16898. IEEE, 2025.
[1286] Yannick Schroecker, Mel Vecerik, and Jon Scholz. Generative predecessor models for sample-
efficient imitation learning. In International Conference on Learning Representations, 2019.
[1287] Norman Di Palo and Edward Johns. Safari: Safe and active robot imitation learning with
imagination. arXiv preprint arXiv:2011.09586, 2020.
[1288] Hongxiang Zhao, Xingchen Liu, Mutian Xu, Yiming Hao, Weikai Chen, and Xiaoguang Han.
Taste-rob: Advancing video generation of task-oriented hand-object interaction for general-
izable robotic manipulation. In Proceedings of the Computer Vision and Pattern Recognition
Conference, pages 27683–27693, 2025.
[1289] Sha Luo, Hamidreza Kasaei, and Lambert Schomaker. Self-imitation learning by planning. In
2021 IEEE International Conference on Robotics and Automation (ICRA), pages 4823–4829.
IEEE, 2021.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1290] Hao Shen, Weikang Wan, and He Wang. Learning category-level generalizable object manip-
ulation policy via generative adversarial self-imitation learning from demonstrations. IEEE
Robotics and Automation Letters, 7(4):11166–11173, 2022.
[1291] Avi Singh, Eric Jang, Alexander Irpan, Daniel Kappler, Murtaza Dalal, Sergey Levinev, Mohi
Khansari, and Chelsea Finn. Scalable multi-task imitation learning with autonomous im-
provement. In 2020 IEEE International Conference on Robotics and Automation (ICRA), pages
2167–2173. IEEE, 2020.
[1292] Lars Ankile, Anthony Simeonov, Idan Shenfeld, and Pulkit Agrawal. Juicer: Data-efficient im-
itation learning for robotic assembly. In 2024 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 5096–5103. IEEE, 2024.
[1293] Sung-Wook Lee, Xuhui Kang, and Yen-Ling Kuo. Diff-dagger: Uncertainty estimation with
diffusion policy for robotic manipulation. In 2025 IEEE International Conference on Robotics
and Automation (ICRA), pages 4845–4852. IEEE, 2025.
[1294] Mark Beliaev, Andy Shih, Stefano Ermon, Dorsa Sadigh, and Ramtin Pedarsani. Imitation
learning by estimating expertise of demonstrators. In International Conference on Machine
Learning, pages 1732–1748. PMLR, 2022.
[1295] Kei Takahashi, Hikaru Sasaki, and Takamitsu Matsubara. Feasibility-aware imitation learn-
ing from observations through a hand-mounted demonstration interface. In 2025 IEEE
International Conference on Robotics and Automation (ICRA), pages 7822–7828. IEEE, 2025.
[1296] Tung M Luu, Donghoon Lee, Younghwan Lee, and Chang D Yoo. Policy learning from large
vision-language model feedback without reward modeling. In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS). IEEE, 2025.
[1297] Xinhai Li, Jialin Li, Ziheng Zhang, Rui Zhang, Fan Jia, Tiancai Wang, Haoqiang Fan, Kuo-Kun
Tseng, and Ruiping Wang. Robogsim: A real2sim2real robotic gaussian splatting simulator.
arXiv preprint arXiv:2411.11839, 2024.
[1298] Shengliang Deng, Mi Yan, Songlin Wei, Haixin Ma, Yuxin Yang, Jiayi Chen, Zhiqi Zhang,
Taoyu Yang, Xuheng Zhang, Wenhao Zhang, et al. Graspvla: a grasping foundation model
pre-trained on billion-scale synthetic action data. In Conference on Robot Learning, 2025.
[1299] Jensen Gao, Annie Xie, Ted Xiao, Chelsea Finn, and Dorsa Sadigh. Efficient data collection
for robotic manipulation via compositional generalization. In Robotics: Science and Systems,
2024.
[1300] Weikang Wan, Yifeng Zhu, Rutav Shah, and Yuke Zhu. Lotus: Continual imitation learning
for robot manipulation through unsupervised skill discovery. In 2024 IEEE International
Conference on Robotics and Automation (ICRA), pages 537–544. IEEE, 2024.
[1301] Mengda Xu, Zhenjia Xu, Cheng Chi, Manuela Veloso, and Shuran Song.
Xskill: Cross
embodiment skill discovery. In Conference on robot learning, pages 3536–3555. PMLR, 2023.
[1302] Jonathan Yang, Catherine Glossop, Arjun Bhorkar, Dhruv Shah, Quan Vuong, Chelsea Finn,
Dorsa Sadigh, and Sergey Levine. Pushing the limits of cross-embodiment learning for
manipulation and navigation. In Robotics: Science and Systems, 2024.
[1303] Lawrence Yunliang Chen, Kush Hari, Karthik Dharmarajan, Chenfeng Xu, Quan Vuong, and
Ken Goldberg. Mirage: Cross-embodiment zero-shot policy transfer with cross-painting. In
Robotics: Science and Systems, 2024.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1304] Jiangran Lyu, Yuxing Chen, Tao Du, Feng Zhu, Huiquan Liu, Yizhou Wang, and He Wang.
Scissorbot: Learning generalizable scissor skill for paper cutting via simulation, imitation,
and sim2real. In Conference on Robot Learning, pages 3379–3394. PMLR, 2025.
[1305] Xiaoyu Chen, Jiachen Hu, Chi Jin, Lihong Li, and Liwei Wang. Understanding domain
randomization for sim-to-real transfer. In International Conference on Learning Representations,
2022.
[1306] Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, and Pieter Abbeel.
Domain randomization for transferring deep neural networks from simulation to the real
world. In 2017 IEEE/RSJ international conference on intelligent robots and systems (IROS),
pages 23–30. IEEE, 2017.
[1307] Jonathan Tremblay, Aayush Prakash, David Acuna, Mark Brophy, Varun Jampani, Cem Anil,
Thang To, Eric Cameracci, Shaad Boochoon, and Stan Birchfield. Training deep networks
with synthetic data: Bridging the reality gap by domain randomization. In Proceedings of the
IEEE conference on computer vision and pattern recognition workshops, pages 969–977, 2018.
[1308] Xinyi Ren, Jianlan Luo, Eugen Solowjow, Juan Aparicio Ojea, Abhishek Gupta, Aviv Tamar,
and Pieter Abbeel. Domain randomization for active pose estimation. In 2019 International
Conference on Robotics and Automation (ICRA), pages 7228–7234. IEEE, 2019.
[1309] Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, and Pieter Abbeel. Sim-to-real
transfer of robotic control with dynamics randomization. In 2018 IEEE international conference
on robotics and automation (ICRA), pages 3803–3810. IEEE, 2018.
[1310] Guiliang Liu, Yueci Deng, Runyi Zhao, Huayi Zhou, Jian Chen, Jietao Chen, Ruiyan Xu,
Yunxin Tai, and Kui Jia. Dexscale: Automating data scaling for sim2real generalizable robot
control. In Forty-second International Conference on Machine Learning, 2025.
[1311] Josip Josifovski, Shangding Gu, Mohammadhossein Malmir, Haoliang Huang, Sayantan
Auddy, Nicolás Navarro-Guerrero, Costas Spanos, and Alois Knoll. Safe continual domain
adaptation after sim2real transfer of reinforcement learning policies in robotics. arXiv preprint
arXiv:2503.10949, 2025.
[1312] Albert Yu, Adeline Foote, Raymond Mooney, and Roberto Martín-Martín. Natural language
can help bridge the sim2real gap. In Robotics: Science and Systems, 2024.
[1313] Abhiram Maddukuri, Zhenyu Jiang, Lawrence Yunliang Chen, Soroush Nasiriany, Yuqi Xie,
Yu Fang, Wenqi Huang, Zu Wang, Zhenjia Xu, Nikita Chernyadev, et al. Sim-and-real co-
training: A simple recipe for vision-based robotic manipulation. In Robotics: Science and
Systems, 2025.
[1314] Shuo Cheng, Liqian Ma, Zhenyang Chen, Ajay Mandlekar, Caelan Garrett, and Danfei Xu.
Generalizable domain adaptation for sim-and-real policy co-training. Advances in Neural
Information Processing Systems, 38:11905–11933, 2025.
[1315] Marcel Torne, Anthony Simeonov, Zechu Li, April Chan, Tao Chen, Abhishek Gupta, and
Pulkit Agrawal. Reconciling reality through simulation: A real-to-sim-to-real approach for
robust manipulation. In Robotics: Science and Systems, 2024.
[1316] Justin Yu, Letian Fu, Huang Huang, Karim El-Refai, Rares Andrei Ambrus, Richard Cheng,
Muhammad Zubair Irshad, and Ken Goldberg. Real2render2real: Scaling robot data without
dynamics simulation or robot hardware. In Proceedings of the 9th Conference on Robot Learning
(CoRL), pages 547–577, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1317] Yujie Zhao, Hongwei Fan, Di Chen, Shengcong Chen, Liliang Chen, Xiaoqi Li, Guanghui Ren,
and Hao Dong. Real2edit2real: Generating robotic demonstrations via a 3d control interface.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages
23106–23116, 2026.
[1318] Chenrui Tie, Yue Chen, Ruihai Wu, Boxuan Dong, Zeyi Li, Chongkai Gao, and Hao Dong. Et-
seed: Efficient trajectory-level se (3) equivariant diffusion policy. In International Conference
on Learning Representations, volume 2025, pages 60114–60132, 2025.
[1319] Qinglun Zhang, Shen Cheng, Tian Dan, Haoqiang Fan, Guanghui Liu, and Shuaicheng Liu.
Efficient hybrid se(3)-equivariant visuomotor flow policy via spherical harmonics for robot
manipulation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pages 27989–27998, 2026.
[1320] Haoyu Xiong, Xiaomeng Xu, Jimmy Wu, Yifan Hou, Jeannette Bohg, and Shuran Song. Vision
in action: Learning active perception from human demonstrations. In Proceedings of the 9th
Conference on Robot Learning (CoRL), pages 5450–5463, 2025.
[1321] Mengzhen Liu, Enshen Zhou, Cheng Chi, Yi Han, Shanyu Rong, Liming Chen, Pengwei
Wang, Zhongyuan Wang, and Shanghang Zhang. Sapave: Towards active perception and
manipulation in vision-language action models for robotics. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition (CVPR), pages 37164–37174, 2026.
[1322] Shutong Jin, Lezhong Wang, Ben Temming, and Florian T Pokorny. Physically-based lighting
generation for robotic manipulation. arXiv preprint arXiv:2508.01442, 2025.
[1323] Annie Xie, Lisa Lee, Ted Xiao, and Chelsea Finn. Decomposing the generalization gap in
imitation learning for visual robotic manipulation. In 2024 IEEE International Conference on
Robotics and Automation (ICRA), pages 3153–3160. IEEE, 2024.
[1324] Zhecheng Yuan, Tianming Wei, Shuiqi Cheng, Gu Zhang, Yuanpei Chen, and Huazhe Xu.
Learning to manipulate anywhere: A visual generalizable framework for reinforcement
learning. In 8th Annual Conference on Robot Learning, 2024.
[1325] Zhao-Heng Yin, Yang Gao, and Qifeng Chen. Spatial generalization of visual imitation
learning with position-invariant regularization. In RSS 2023 Workshop on Symmetries in
Robot Learning, 2023.
[1326] Shuo Yang, Wei Zhang, Weizhi Lu, Hesheng Wang, and Yibin Li.
Cross-context visual
imitation learning from demonstrations. In 2020 IEEE International Conference on Robotics
and Automation (ICRA), pages 5467–5473. IEEE, 2020.
[1327] Zhifeng Qian, Mingyu You, Hongjun Zhou, Xuanhui Xu, and Bin He. Robot learning from
human demonstrations with inconsistent contexts. Robotics and Autonomous Systems, 166:
104466, 2023.
[1328] Alexandre Chenu, Nicolas Perrin-Gilbert, and Olivier Sigaud. Divide & conquer imitation
learning. In 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS),
pages 8630–8637. IEEE, 2022.
[1329] Youngwoon Lee, Joseph J Lim, Anima Anandkumar, and Yuke Zhu. Adversarial skill chaining
for long-horizon robot manipulation via terminal state regularization. In Conference on Robot
Learning, pages 406–416. PMLR, 2022.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1330] Yifeng Zhu, Peter Stone, and Yuke Zhu.
Bottom-up skill discovery from unsegmented
demonstrations for long-horizon robot manipulation. IEEE Robotics and Automation Letters, 7
(2):4126–4133, 2022.
[1331] Suneel Belkhale, Yuchen Cui, and Dorsa Sadigh. Hydra: Hybrid robot actions for imitation
learning. In Conference on Robot Learning, pages 2113–2133. PMLR, 2023.
[1332] Christopher Agia, Toki Migimatsu, Jiajun Wu, and Jeannette Bohg. Stap: Sequencing task-
agnostic policies. In 2023 IEEE International Conference on Robotics and Automation (ICRA),
pages 7951–7958. IEEE, 2023.
[1333] Jesse Zhang, Jiahui Zhang, Karl Pertsch, Ziyi Liu, Xiang Ren, Minsuk Chang, Shao-Hua Sun,
and Joseph Lim. Bootstrap your own skills: Learning to solve new tasks with large language
model guidance. In 7th Annual Conference on Robot Learning, 2023.
[1334] Weiyu Liu, Neil Nie, Ruohan Zhang, Jiayuan Mao, and Jiajun Wu. Learning compositional
behaviors from demonstration and language. In 8th Annual Conference on Robot Learning,
2024.
[1335] Tong Mu, Yihao Liu, and Mehran Armand. Look before you leap: Using serialized state
machine for language conditioned robotic manipulation. In 2025 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 8096–8102. IEEE, 2025.
[1336] Vivek Myers, Chunyuan Zheng, Oier Mees, Kuan Fang, and Sergey Levine. Policy adaptation
via language optimization: Decomposing tasks for few-shot imitation. In 8th Annual Conference
on Robot Learning, 2024.
[1337] Murtaza Dalal, Min Liu, Walter Talbott, Chen Chen, Deepak Pathak, Jian Zhang, and Russ
Salakhutdinov. Local policies enable zero-shot long-horizon manipulation. In 2nd CoRL
Workshop on Learning Effective Abstractions for Planning, 2024.
[1338] Zhenyang Lin, Yurou Chen, and Zhiyong Liu. Hierarchical human-to-robot imitation learning
for long-horizon tasks via cross-domain skill alignment. In 2024 IEEE International Conference
on Robotics and Automation (ICRA), pages 2783–2790. IEEE, 2024.
[1339] Priya Sundaresan, Hengyuan Hu, Quan Vuong, Jeannette Bohg, and Dorsa Sadigh. What’s
the move? hybrid imitation learning via salient points. In International Conference on Learning
Representations, volume 2025, pages 51806–51821, 2025.
[1340] Xiaofeng Mao, Gabriele Giudici, Claudio Coppola, Kaspar Althoefer, Ildar Farkhatdinov, Zhibin
Li, and Lorenzo Jamone. Dexskills: Skill segmentation using haptic data for learning au-
tonomous long-horizon robotic manipulation tasks. In 2024 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS), pages 5104–5111. IEEE, 2024.
[1341] Eleftherios Triantafyllidis, Fernando Acero, Zhaocheng Liu, and Zhibin Li. Hybrid hierarchical
learning for solving complex sequential tasks using the robotic manipulation network roman.
Nature Machine Intelligence, 5(9):991–1005, 2023.
[1342] Ajay Kumar Tanwani, Andy Yan, Jonathan Lee, Sylvain Calinon, and Ken Goldberg. Sequential
robot imitation learning from observations. The International Journal of Robotics Research, 40
(10-11):1306–1325, 2021.
[1343] Bohan Wu, Feng Xu, Zhanpeng He, Abhi Gupta, and Peter K Allen. Squirl: Robust and
efficient learning from video demonstration of long-horizon robotic manipulation tasks. In
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
9720–9727. IEEE, 2020.
[1344] Xiaoshuai Chen, Wei Chen, Dongmyoung Lee, Yukun Ge, Nicolas Rojas, and Petar Kormushev.
A backbone for long-horizon robot task understanding. IEEE Robotics and Automation Letters,
2025.
[1345] Zixuan Chen, Jing Huo, Yangtao Chen, and Yang Gao. Robohorizon: An llm-assisted multi-
view world model for long-horizon robotic manipulation. arXiv preprint arXiv:2501.06605,
2025.
[1346] Jinrong Yang, Kexun Chen, Zhuoling Li, Shengkai Wu, Yong Zhao, Liangliang Ren, Wenqiu
Luo, Chaohui Shang, Meiyu Zhi, Linfeng Gao, et al. Bootstrapping imitation learning for long-
horizon manipulation via hierarchical data collection space. arXiv preprint arXiv:2505.17389,
2025.
[1347] Renhao Wang, Jiayuan Mao, Joy Hsu, Hang Zhao, Jiajun Wu, and Yang Gao. Programmatically
grounded, compositionally generalizable robotic manipulation. In The Eleventh International
Conference on Learning Representations, 2023.
[1348] Allan Zhou, Vikash Kumar, Chelsea Finn, and Aravind Rajeswaran. Policy architectures for
compositional generalization in control. In Deep Reinforcement Learning Workshop NeurIPS
2022, 2022.
[1349] Hanzhi Chen, Boyang Sun, Anran Zhang, Marc Pollefeys, and Stefan Leutenegger. Vidbot:
Learning generalizable 3d actions from in-the-wild 2d human videos for zero-shot robotic
manipulation. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages
27661–27672, 2025.
[1350] Eugene Valassakis, Georgios Papagiannis, Norman Di Palo, and Edward Johns. Demonstrate
once, imitate immediately (dome): Learning visual servoing for one-shot imitation learning.
In 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages
8614–8621. IEEE, 2022.
[1351] Aayush Jain, Philip Long, Valeria Villani, John D Kelleher, and Maria Chiara Leva. Cobt:
Collaborative programming of behaviour trees from one demonstration for robot manipulation.
In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 12993–12999.
IEEE, 2024.
[1352] Nick Heppert, Max Argus, Tim Welschehold, Thomas Brox, and Abhinav Valada. Ditto: Demon-
stration imitation by trajectory transformation. In 2024 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 7565–7572. IEEE, 2024.
[1353] Tianyu Li, Sunan Sun, Shubhodeep Shiv Aditya, and Nadia Figueroa. Elastic motion policy:
An adaptive dynamical system for robust and efficient one-shot imitation learning. In 2025
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 9846–9853.
IEEE, 2025.
[1354] Yu Ren, Yang Cong, Ronghan Chen, and Jiahao Long. Learning generalizable 3d manipulation
with 10 demonstrations. In 7th Annual Conference on Robot Learning, 2023.
[1355] Mingchen Song, Xiang Deng, Guoqiang Zhong, Qi Lv, Jia Wan, Yinchuan Li, Jianye Hao,
and Weili Guan. Few-shot vision-language action-incremental policy learning. arXiv preprint
arXiv:2504.15517, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1356] Stephen James, Michael Bloesch, and Andrew J Davison. Task-embedded control networks
for few-shot imitation learning. In Conference on robot learning, pages 783–795. PMLR, 2018.
[1357] Francesco Di Felice, Salvatore D’Avella, Alberto Remus, Paolo Tripicchio, and Carlo Alberto
Avizzano. One-shot imitation learning with graph neural networks for pick-and-place manip-
ulation tasks. IEEE Robotics and Automation Letters, 8(9):5926–5933, 2023.
[1358] Xinyu Zhang and Abdeslam Boularias. One-shot imitation learning with invariance matching
for robotic manipulation. In Robotics: Science and Systems, 2024.
[1359] Zhenshan Bing, Alexander Koch, Xiangtong Yao, Kai Huang, and Alois Knoll.
Meta-
reinforcement learning via language instructions. In 2023 International Conference on Robotics
and Automation (ICRA), 2023.
[1360] Siddhant Haldar, Jyothish Pari, Anant Rai, and Lerrel Pinto. Teach a robot to fish: Versatile
imitation from one minute of demonstrations. In Robotics: Science and Systems, 2023.
[1361] Ondrej Biza, Skye Thompson, Kishore Reddy Pagidi, Abhinav Kumar, Elise van der Pol, Robin
Walters, Thomas Kipf, Jan-Willem van de Meent, Lawson L. S. Wong, and Robert Platt. One-
shot imitation learning via interaction warping. In Proceedings of the 7th Conference on Robot
Learning (CoRL), pages 2519–2536, 2023.
[1362] Yuanqi Yao, Siao Liu, Haoming Song, Delin Qu, Qizhi Chen, Yan Ding, Bin Zhao, Zhigang
Wang, Xuelong Li, and Dong Wang. Think small, act big: Primitive prompt learning for
lifelong robot manipulation. In Proceedings of the Computer Vision and Pattern Recognition
Conference, pages 22573–22583, 2025.
[1363] Kaushik Roy, Akila Dissanayakc, Brendan Tidd, and Pcyman Moghadam. M2distill: Multi-
modal distillation for lifelong imitation learning. In 2025 IEEE International Conference on
Robotics and Automation (ICRA), pages 1429–1435. IEEE, 2025.
[1364] Chongkai Gao, Haichuan Gao, Shangqi Guo, Tianren Zhang, and Feng Chen. Cril: Continual
robot imitation learning via generative and prediction model. In 2021 IEEE/RSJ International
Conference on Intelligent Robots and Systems (IROS), pages 6747–5754. IEEE, 2021.
[1365] Yuheng Lei, Sitong Mao, Shunbo Zhou, Hongyuan Zhang, Xuelong Li, and Ping Luo. Dy-
namic mixture of progressive parameter-efficient expert library for lifelong robot learning.
Transactions on Machine Learning Research, 2026. ISSN 2835-8856.
[1366] Zexin Zheng, Jia-Feng Cai, Xiao-Ming Wu, Yi-Lin Wei, Yu-Ming Tang, Ancong Wu, and Wei-
Shi Zheng. imanip: Skill-incremental learning for robotic manipulation. In 2025 IEEE/CVF
International Conference on Computer Vision (ICCV), pages 13890–13900. IEEE, 2025.
[1367] Daehee Lee, Dongsu Lee, TaeYoon Kwack, Wonje Choi, and Honguk Woo. Policy compatible
skill incremental learning via lazy learning interface. Advances in Neural Information Processing
Systems, 38:129000–129039, 2025.
[1368] Tyler Ga Wei Lum, Olivia Y. Lee, Karen Liu, and Jeannette Bohg. Crossing the human-robot
embodiment gap with sim-to-real rl using one human demonstration. In Proceedings of the
9th Conference on Robot Learning (CoRL), pages 4418–4441, 2025.
[1369] Prithwish Dan, Kushal Kedia, Angela Chao, Edward Duan, Maximus Adrian Pace, Wei-Chiu
Ma, and Sanjiban Choudhury. X-sim: Cross-embodiment learning via real-to-sim-to-real. In
Proceedings of the 9th Conference on Robot Learning (CoRL), pages 816–833, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1370] Yangcen Liu, Woo Chul Shin, Yunhai Han, Zhenyang Chen, Harish Ravichandar, and Danfei
Xu. Immimic: Cross-domain imitation from human videos via mapping and interpolation. In
Proceedings of the 9th Conference on Robot Learning (CoRL), pages 834–858, 2025.
[1371] Ryan Punamiya, Dhruv Patel, Patcharapong Aphiwetsa, Pranav Kuppili, Lawrence Zhu, Simar
Kareer, Judy Hoffman, and Danfei Xu. Egobridge: Domain adaptation for generalizable
imitation from egocentric human data. In Advances in Neural Information Processing Systems
(NeurIPS), volume 38, pages 47092–47122, 2025.
[1372] Tianyu Wang, Dwait Bhatt, Xiaolong Wang, and Nikolay Atanasov. Cross-embodiment robot
manipulation skill transfer using latent space alignment. arXiv preprint arXiv:2406.01968,
2024.
[1373] Yifan Zhou, Shubham Sonawani, Mariano Phielipp, Simon Stepputtis, and Heni Amor. Modu-
larity through attention: Efficient training and transfer of language-conditioned policies for
robot manipulation. In Conference on Robot Learning, pages 1684–1695. PMLR, 2023.
[1374] Ria Doshi, Homer Rich Walke, Oier Mees, Sudeep Dasari, and Sergey Levine. Scaling cross-
embodied learning: One policy for manipulation, navigation, locomotion and aviation. In
Conference on Robot Learning, pages 496–512. PMLR, 2025.
[1375] Guanxing Lu, Tengbo Yu, Haoyuan Deng, Season Si Chen, Yansong Tang, and Ziwei Wang.
Anybimanual: Transferring unimanual policy for general bimanual manipulation. In Proceed-
ings of the ieee/cvf international conference on computer vision, 2025.
[1376] Mingyo Seo, H Andy Park, Shenli Yuan, Yuke Zhu, and Luis Sentis. Legato: Cross-embodiment
imitation using a grasping tool. IEEE Robotics and Automation Letters, 2025.
[1377] Tong Wu, Shoujie Li, Junhao Gong, Changqing Guo, Xingting Li, Shilong Mu, and Wenbo
Ding. Cei: A unified interface for cross-embodiment visuomotor policy learning in 3d space.
IEEE Robotics and Automation Letters, 2026.
[1378] Huajie Tan, Xiaoshuai Hao, Cheng Chi, Minglan Lin, Yaoxu Lyu, Mingyu Cao, Dong Liang,
Zhuo Chen, Mengsi Lyu, Cheng Peng, et al. Roboos: A hierarchical embodied framework for
cross-embodiment and multi-agent collaboration. arXiv preprint arXiv:2505.03673, 2025.
[1379] Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting
Li, Yu Zhang, Pan Zhou, Hechang Chen, et al. Agentic robot: A brain-inspired framework for
vision-language-action models in embodied agents. arXiv preprint arXiv:2505.23450, 2025.
[1380] Han Zhao, Jiaxuan Zhang, Wenxuan Song, Pengxiang Ding, and Donglin Wang. Vla2:
Empowering vision-language-action models with an agentic framework for unseen concept
manipulation. arXiv preprint arXiv:2510.14902, 2025.
[1381] Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, Furong Huang,
and Jiayuan Mao. Guava: An effective and universal harness for embodied manipulation.
arXiv preprint arXiv:2606.18363, 2026.
[1382] Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu,
Yuchen Yan, Jiyuan Liu, Wenhao Tang, et al. Harness vla: Steering frozen vlas into reliable
manipulation primitives via memory-guided agents. arXiv preprint arXiv:2607.08448, 2026.
[1383] Zhuoran Li, Zhiyang Li, Kaijun Zhou, and Jinyu Gu. Soma: Strategic orchestration and
memory-augmented system for vision-language-action model robustness via in-context adap-
tation. arXiv preprint arXiv:2603.24060, 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1384] Xu Huang, Weixin Mao, Yinhao Li, Hua Chen, and Jiabao Zhao. Long-term memory for
vla-based agents in open-world task execution. arXiv preprint arXiv:2604.15671, 2026.
[1385] Ruofan Jin and Zaixi Zhang. Agentic-vla: Efficient online adaptation for vision-language-
action models. arXiv preprint arXiv:2605.22896, 2026.
[1386] Daphne Chen, Archit Ritesh Jain, Eric Goossen, Emma Romig, Michael Murray, Nick Walker,
and Maya Cakmak. A few words go a long way: Language guided robot policy synthesis.
arXiv preprint arXiv:2607.23784, 2026.
[1387] Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian Fu, Haoru Xue, Jalen Lu, Yi Yang,
Cunxi Dai, Zi Wang, et al. Enpire: Agentic robot policy self-improvement in the real world.
arXiv preprint arXiv:2606.19980, 2026.
[1388] Ruiying Li, Yunlang Zhou, YuYao Zhu, Kylin Chen, Jingyuan Wang, Sukai Wang, Kongtao
Hu, Minhui Yu, Bowen Jiang, Zhan Su, et al. Roboclaw: An agentic framework for scalable
long-horizon robotic tasks. In European conference on computer vision, 2026.
[1389] Yang Liu, Weixing Chen, Xinshuai Song, Tao Pu, Siwen Mo, Yongjie Bai, Zihao Chen, Qianran
Sun, Liruo Zhong, Ying Shen, et al.
Phyagentos: A self-evolving operating system for
embodied agents with decoupled cognitive planning and physical execution. arXiv preprint
arXiv:2607.16636, 2026.
[1390] Yi-Xiang He, Lan Wei, Haoming Cen, Jian-Jian Jiang, Zhuohao Li, Guanxing Lu, Yihan
Yang, Dandan Zhang, and Wei-Shi Zheng. A closed-loop multi-agent framework for robust
multi-robot manipulation. arXiv preprint arXiv:2607.06990, 2026.
[1391] Claudia Pérez-D’Arpino and Julie A Shah. Fast target prediction of human reaching motion
for cooperative human-robot manipulation tasks using time series classification. In 2015 IEEE
international conference on robotics and automation (ICRA), pages 6175–6182. IEEE, 2015.
[1392] Dongjun Lee, Juheon Choi, Dong Kyu Shin, Sinjae Kang, and Kimin Lee. Hierarchical policies
from verbal and egocentric human signals for natural human-robot interaction. arXiv preprint
arXiv:2606.10276, 2026.
[1393] Yuzhi Lai, Shenghai Yuan, Peizheng Li, and Andreas Zell. Sticky-glance: Robust intent
recognition for human robot collaboration via single-glance. arXiv e-prints, pages arXiv–2603,
2026.
[1394] Jiurun Song, Xiao Liang, and Minghui Zheng. Tatic: Task-aware temporal learning for human
intent inference from physical corrections in human-robot collaboration. arXiv preprint
arXiv:2603.11077, 2026.
[1395] Debasmita Ghose, Oz Gitelson, Ryan Jin, Grace Abawe, Marynel Vázquez, and Brian Scassel-
lati. I’ve changed my mind: Robots adapting to changing human goals during collaboration.
IEEE Robotics and Automation Letters, 11(2):1490–1497, 2025.
[1396] Debasmita Ghose, Oz Gitelson, Marynel Vázquez, and Brian Scassellati. Open-ended goal
inference through actions and language for human-robot collaboration. In Proceedings of the
21st ACM/IEEE International Conference on Human-Robot Interaction, pages 68–77, 2026.
[1397] Yuedi Zhang, Shuanghao Bai, Wanqi Zhou, Haoran Zhang, Qi Zhang, Zhirong Luan, and
Badong Chen. Assistance without interruption: A benchmark and llm-based framework for
non-intrusive human-robot assistance. In 2026 IEEE/RSJ international conference on intelligent
robots and systems (IROS), 2026.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1398] Ashesh Jain, Shikhar Sharma, Thorsten Joachims, and Ashutosh Saxena. Learning preferences
for manipulation tasks from online coactive feedback. The International Journal of Robotics
Research, 34(10):1296–1313, 2015.
[1399] Allen Z. Ren, Anushri Dixit, Alexandra Bodrova, Sumeet Singh, Stephen Tu, Noah Brown,
Peng Xu, Leila Takayama, Fei Xia, Jake Varley, Zhenjia Xu, Dorsa Sadigh, Andy Zeng, and
Anirudha Majumdar. Robots that ask for help: Uncertainty alignment for large language
model planners. In Proceedings of the 7th Conference on Robot Learning (CoRL), pages 661–682,
2023.
[1400] Jakob Thumm, Christopher Agia, Marco Pavone, and Matthias Althoff. Text2interaction:
Establishing safe and preferable human-robot interaction. In 8th Annual Conference on Robot
Learning, 2024.
[1401] Ran Tian, Yilin Wu, Chenfeng Xu, Masayoshi Tomizuka, Jitendra Malik, and Andrea Bajcsy.
Maximizing alignment with minimal feedback: Efficiently learning rewards for visuomotor
robot policy alignment. arXiv preprint arXiv:2412.04835, 2024.
[1402] Shaid Hasan, Breenice Lee, Sujan Sarker, and Tariq Iqbal. M2hri: An llm-driven multi-
modal multi-agent framework for personalized human-robot interaction. arXiv preprint
arXiv:2604.11975, 2026.
[1403] Junxiang Wang, Xinwen Xu, Tiancheng Wu, Julian Millan, Nir Pechuk, and Zackory Erickson.
Generative simulation for policy learning in physical human-robot interaction. arXiv preprint
arXiv:2604.08664, 2026.
[1404] Yincong Chen, Ranpeng Qiu, Zihao Li, Yanan Zhou, Guoqiang Ren, and Weiming Zhi. Robots
that collaborate: Sequential asymmetric imitation for learning coupled robot policies. arXiv
preprint arXiv:2606.16490, 2026.
[1405] Chaoran Zhang, Chenhao Zhang, Zhaobo Xu, Qinghongbing Xie, Jinliang Hou, Pingfa Feng,
and Long Zeng. Embodied intelligent industrial robotics: Framework and techniques. Journal
of Manufacturing Systems, 88:158–189, 2026.
[1406] Roya Firoozi, Johnathan Tucker, Stephen Tian, Anirudha Majumdar, Jiankai Sun, Weiyu Liu,
Yuke Zhu, Shuran Song, Ashish Kapoor, Karol Hausman, et al. Foundation models in robotics:
Applications, challenges, and the future. The International Journal of Robotics Research, 44
(5):701–739, 2025.
[1407] Jian Zhao, Yunlong Lian, Andy M Tyrrell, Michael Gienger, and Jihong Zhu. Bimanual robot-
assisted dressing: A spherical coordinate-based strategy for tight-fitting garments. In 2025
IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 3328–3335.
IEEE, 2025.
[1408] Wenhai Liu, Junbo Wang, Yiming Wang, Weiming Wang, and Cewu Lu. Forcemimic: Force-
centric imitation learning with force-motion capture system for contact-rich manipulation. In
2025 IEEE International Conference on Robotics and Automation (ICRA), pages 1105–1112.
IEEE, 2025.
[1409] Priya Sundaresan, Jiajun Wu, and Dorsa Sadigh. Learning sequential acquisition policies for
robot-assisted feeding. In Conference on Robot Learning, pages 1282–1299. PMLR, 2023.
[1410] Haonan Chen, Yilong Niu, Kaiwen Hong, Shuijing Liu, Yixuan Wang, Yunzhu Li, and Kather-
ine Rose Driggs-Campbell.
Predicting object interactions with behavior primitives: An
application in stowing tasks. In 7th Annual Conference on Robot Learning, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1411] Ivan Kapelyukh, Vitalis Vosylius, and Edward Johns. Dall-e-bot: Introducing web-scale
diffusion models to robotics. IEEE Robotics and Automation Letters, 8(7):3956–3963, 2023.
[1412] Chao Tang, Anxing Xiao, Yuhong Deng, Tianrun Hu, Wenlong Dong, Hanbo Zhang, David Hsu,
and Hong Zhang. Functo: Function-centric one-shot imitation learning for tool manipulation.
arXiv preprint arXiv:2502.11744, 2025.
[1413] Chung Hee Kim, Abhisesh Silwal, and George Kantor. Autonomous robotic pepper harvesting:
Imitation learning in unstructured agricultural environments. IEEE Robotics and Automation
Letters, 2025.
[1414] Lun Li and Hamidreza Kasaei. Enhanced view planning for robotic harvesting: Tackling
occlusions with imitation learning. In 2025 IEEE International Conference on Robotics and
Automation (ICRA), pages 13146–13152. IEEE, 2025.
[1415] Dominic Guri, Moonyoung Lee, Oliver Kroemer, and George Kantor. Hefty: A modular reconfig-
urable robot for advancing robot manipulation in agriculture. arXiv preprint arXiv:2402.18710,
2024.
[1416] Favour Adetunji, Abhiram Karukayil, Pranjal Samant, Sheena Shabana, Finny Varghese, Ujjwal
Upadhyay, Raj A Yadav, A Partridge, Elizabeth Pendleton, Ruth Plant, et al. Vision-based
manipulation of transparent plastic bags in industrial setups. Frontiers in Robotics and AI, 12:
1506290, 2025.
[1417] Andreas Dömel, Simon Kriegel, Michael Kassecker, Manuel Brucker, Tim Bodenmüller, and
Michael Suppa. Toward fully autonomous mobile manipulation for industrial environments.
International Journal of Advanced Robotic Systems, 14(4):1729881417718588, 2017.
[1418] Peter Buš and Zhiyong Dong. Deepcraft: imitation learning method in a cointelligent design
to production process to deliver architectural scenarios. Architectural Intelligence, 3(1):12,
2024.
[1419] Daniyal Maroufi, Xinyuan Huang, Yash Kulkarni, Omid Rezayof, Susheela Sharma, Vaibhav
Goggela, Jordan P Amadio, Mohsen Khadem, and Farshid Alambeigi. S3d: A spatial steer-
able surgical drilling framework for robotic spinal fixation procedures. In 2025 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 2156–2162. IEEE,
2025.
[1420] Xiting He, Mingwu Su, Xinqi Jiang, Long Bai, and Hongliang Ren.
Capsdt: Diffusion-
transformer for capsule robot manipulation. In 2025 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), pages 414–419. IEEE, 2025.
[1421] Kevin Angers, Kourosh Darvish, Naruki Yoshikawa, Sargol Okhovatian, Dawn Bannerman, Ilya
Yakavets, Florian Shkurti, Alán Aspuru-Guzik, and Milica Radisic. Roboculture: A robotics
platform for automated biological experimentation. arXiv preprint arXiv:2505.14941, 2025.
[1422] Ashutosh Mishra, Shreya Santra, Hazal Gozbasi, Kentaro Uno, and Kazuya Yoshida. Enhancing
autonomous manipulator control with human-in-loop for uncertain assembly environments.
In 2025 IEEE 21st International Conference on Automation Science and Engineering (CASE),
pages 527–532. IEEE, 2025.
[1423] Xiaoming Wang and Zhiguo Gong. Style generation in robot calligraphy with deep generative
adversarial networks. arXiv preprint arXiv:2312.09673, 2023.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1424] Yves-Simon Zeulner, Sandeep Selvaraj, and Roberto Calandra. Learning to play piano in the
real world. arXiv preprint arXiv:2503.15481, 2025.
[1425] Tianying Wang, Wei Qi Toh, Hao Zhang, Xiuchao Sui, Shaohua Li, Yong Liu, and Wei Jing.
Robocodraw: Robotic avatar drawing with gan-based style transfer and time-efficient path
optimization. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages
10402–10409, 2020.
[1426] Yuntao Ma, Andrei Cramariuc, Farbod Farshidian, and Marco Hutter. Learning coordinated
badminton skills for legged manipulators. Science Robotics, 10(102):eadu3922, 2025.
[1427] Hao Wang, Chengkai Hou, Xianglong Li, Yankai Fu, Chenxuan Li, Ning Chen, Gaole Dai,
Jiaming Liu, Tiejun Huang, and Shanghang Zhang. Spikepingpong: Spike vision-based
fast-slow pingpong robot system. In International Conference on Learning Representations,
volume 2026, pages 21636–21660, 2026.
[1428] Zackory Erickson, Henry M Clever, Vamsee Gangaram, Greg Turk, C Karen Liu, and Charles C
Kemp. Multidimensional capacitive sensing for robot-assisted dressing and bathing. In 2019
IEEE 16th International Conference on Rehabilitation Robotics (ICORR), pages 224–231. IEEE,
2019.
[1429] Rui Liu, Amisha Bhaskar, and Pratap Tokekar. Adaptive visual imitation learning for robotic
assisted feeding across varied bowl configurations and food types. In ICRA2024 Workshop on
Cooking Robotics: Perception and Motion Planning, 2024.
[1430] Ze Fu, Pinhao Song, Yutong Hu, and Renaud Detry. Tasc: Task-aware shared control for
teleoperated manipulation. arXiv preprint arXiv:2509.10416, 2025.
[1431] Rishabh Madan, Jiawei Lin, Mahika Goel, Angchen Xie, Xiaoyu Liang, Marcus Lee, Justin
Guo, Pranav N Thakkar, Rohan Banerjee, Jose Barreiros, et al. Prioritouch: Adapting to user
contact preferences for whole-arm physical human-robot interaction. In Conference on Robot
Learning, 2025.
[1432] Shutong Jin, Ruiyu Wang, Kuangyi Chen, and Florian T Pokorny. Paca: Perspective-aware
cross-attention representation for zero-shot scene rearrangement. In 2025 IEEE/CVF Winter
Conference on Applications of Computer Vision (WACV), pages 6559–6569. IEEE, 2025.
[1433] Haonan Chang, Kai Gao, Kowndinya Boyalakuntla, Alex Lee, Baichuan Huang, Jingjin Yu,
and Abdeslam Boularias. Lgmcts: Language-guided monte-carlo tree search for executable
semantic object rearrangement. In 2024 IEEE/RSJ International Conference on Intelligent
Robots and Systems (IROS), pages 13607–13612. IEEE, 2024.
[1434] Yan Ding, Xiaohan Zhang, Chris Paxton, and Shiqi Zhang. Task and motion planning with
large language models for object rearrangement. In 2023 IEEE/RSJ International Conference
on Intelligent Robots and Systems (IROS), pages 2086–2092. IEEE, 2023.
[1435] Chunru Lin, Haotian Yuan, Yian Wang, Xiaowen Qiu, Tsun-Hsuan Johnson Wang, Minghao
Guo, Bohan Wang, Yashraj Narang, Dieter Fox, and Chuang Gan. Robotsmith: Genera-
tive robotic tool design for acquisition of complex manipulation skills. Advances in Neural
Information Processing Systems, 38:110290–110319, 2025.
[1436] Haonan Chen, Cheng Zhu, Yunzhu Li, and Katherine Driggs-Campbell. Tool-as-interface:
Learning robot policies from human tool usage through imitation learning. arXiv preprint
arXiv:2504.04612, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1437] Allen Z Ren, Bharat Govil, Tsung-Yen Yang, Karthik R Narasimhan, and Anirudha Majumdar.
Leveraging language for accelerated learning of tool manipulation. In Conference on Robot
Learning, pages 1531–1541. PMLR, 2023.
[1438] Nitesh Subedi, Hsin-Jung Yang, Devesh K Jha, and Soumik Sarkar. Find the fruit: Designing
a zero-shot sim2real deep rl planner for occlusion aware plant manipulation. arXiv preprint
arXiv:2505.16547, 2025.
[1439] Amirreza Davar, Zhengtong Xu, Siavash Mahmoudi, Pouya Sohrabipour, Chaitanya Pallerla,
Yu She, Wan Shou, Philip Glen Crandall, and Dongyi Wang. Chicgrasp: Imitation-learning-
based customized dual-jaw gripper control for manipulation of delicate, irregular bio-products.
Advanced Robotics Research, page e202500149, 2025.
[1440] Nidhi Homey Parayil, Thierry Peynot, and Chris Lehnert. Rice: Reactive interaction controller
for cluttered canopy environment. In 2026 IEEE International Conference on Robotics and
Automation (ICRA), 2026.
[1441] Selma Kchir, Saadia Dhouib, Jérémie Tatibouet, Baptiste Gradoussoff, and Max Da Silva
Simoes. Robotml for industrial robots: Design and simulation of manipulation scenarios. In
2016 IEEE 21st International Conference on Emerging Technologies and Factory Automation
(ETFA), pages 1–8. IEEE, 2016.
[1442] Junzheng Li, Dong Pang, Yu Zheng, Xinping Guan, and Xinyi Le. A flexible manufacturing
assembly system with deep reinforcement learning. Control Engineering Practice, 118:104957,
2022.
[1443] Yu Tian, Ruoyi Hao, Yiming Huang, Dihong Xie, Catherine Po Ling Chan, Jason Ying Kuen
Chan, and Hongliang Ren.
Learning to perform low-contact autonomous nasotracheal
intubation by recurrent action-confidence chunking with transformer. In 2025 IEEE/RSJ
International Conference on Intelligent Robots and Systems (IROS), pages 11233–11239. IEEE,
2025.
[1444] Ji Woong Kim, Tony Z Zhao, Samuel Schmidgall, Anton Deguet, Marin Kobilarov, Chelsea
Finn, and Axel Krieger. Surgical robot transformer (srt): Imitation learning for surgical tasks.
In Conference on Robot Learning, pages 130–144. PMLR, 2025.
[1445] Ji Woong Kim, Juo-Tung Chen, Pascal Hansen, Lucy Xiaoyang Shi, Antony Goldenberg,
Samuel Schmidgall, Paul Maria Scheikl, Anton Deguet, Brandon M White, De Ru Tsai, et al.
Srt-h: A hierarchical framework for autonomous surgery via language-conditioned imitation
learning. Science robotics, 10(104):eadt5254, 2025.
[1446] Yunke Ao, Masoud Moghani, Mayank Mittal, Manish Prajapat, Luohong Wu, Frederic Giraud,
Fabio Carrillo, Andreas Krause, and Philipp Fürnstahl. Sonogym: High performance simula-
tion for challenging surgical tasks with robotic ultrasound. Advances in Neural Information
Processing Systems, 38, 2025.
[1447] Ryoya Mori, Tadayoshi Aoyama, Taisuke Kobayashi, Kazuya Sakamoto, Masaru Takeuchi,
and Yasuhisa Hasegawa. Real-time spatiotemporal assistance for micromanipulation using
imitation learning. IEEE Robotics and Automation Letters, 9(4):3506–3513, 2024.
[1448] Tao Song, Man Luo, Xiaolong Zhang, Linjiang Chen, Yan Huang, Jiaqi Cao, Qing Zhu, Daobin
Liu, Baicheng Zhang, Gang Zou, et al. A multiagent-driven robotic ai chemist enabling
autonomous chemical research on demand. Journal of the American Chemical Society, 147
(15):12534–12545, 2025.
Towards a Unified Understanding of Robot Manipulation: A Comprehensive Survey
[1449] RB Shyam, Zhou Hao, Umberto Montanaro, and Gerhard Neumann. Imitation learning for
autonomous trajectory learning of robot arms in space. arXiv preprint arXiv:2008.04007,
2020.
[1450] Rui Li, Zixuan Hu, Wenxi Qu, Jinouwen Zhang, Zhenfei Yin, Sha Zhang, Xuantuo Huang,
Hanqing Wang, Tai Wang, Jiangmiao Pang, et al. Labutopia: High-fidelity simulation and
hierarchical benchmark for scientific embodied agents.
Advances in Neural Information
Processing Systems, 38, 2025.
[1451] Yi Zhao, Le Chen, Jan Schneider, Quankai Gao, Juho Kannala, Bernhard Schölkopf, Joni
Pajarinen, and Dieter Büchler. Rp1m: A large-scale motion dataset for piano playing with
bi-manual dexterous robot hands. In Conference on Robot Learning, pages 5184–5203. PMLR,
2025.
[1452] Fangping Xie, Pierre Le Meur, and Charith Fernando. End-to-end manipulator calligraphy
planning via variational imitation learning. arXiv preprint arXiv:2304.02801, 2023.
[1453] Jonas Tebbe, Lukas Krauch, Yapeng Gao, and Andreas Zell. Sample-efficient reinforcement
learning in robotic table tennis. In 2021 IEEE international conference on robotics and automa-
tion (ICRA), pages 4171–4178. IEEE, 2021.
[1454] Shuanghao Bai, Wenxuan Song, Jiayi Chen, Yuheng Ji, Zhide Zhong, Jin Yang, Han Zhao,
Wanqi Zhou, Zhe Li, Pengxiang Ding, et al. Embodied robot manipulation in the era of
foundation models: Planning and learning perspectives. arXiv preprint arXiv:2512.22983,
2025.
