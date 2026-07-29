<div align="center">

<h1>脉冲神经网络精选 — 时间线版</h1>

<p><em>用时间顺序讲完整个脉冲神经网络领域 — 最新在前。</em><br>
<sub>主题版 <a href="README.zh-CN.md">Hub</a> 的时间线姊妹篇</sub></p>

<p><a href="TIMELINE.md">English</a> &nbsp;·&nbsp; <a href="TIMELINE.zh-CN.md"><b>中文</b></a> &nbsp;|&nbsp; <a href="README.zh-CN.md">主题版 (中文)</a> &nbsp;·&nbsp; <a href="README.md">Thematic Hub (EN)</a></p>

<p><b>568</b> 篇成果，篇篇有一句话说明（225 篇精选 + 343 篇索引） &nbsp;·&nbsp; <b>44</b> 项里程碑 &nbsp;·&nbsp; <b>1943–2026</b></p>

</div>

---

## 如何阅读本页

这是 [脉冲神经网络精选 Hub](README.zh-CN.md) 的**时间线视图**。Hub 按*主题*组织；本页把整个领域按**年份倒序**铺开——让你顺着时间看清它是怎么一步步走过来的。

每个年份分**两层**：

- **精选** — Hub 中 **225** 篇带深度注释的条目。每条都有一句*为什么重要*、一个可跳回主题章节的标签（如 `训练方法`、`神经形态硬件`），**★ = 领域里程碑**。
- **当年全量索引** — 可折叠列表，收录当年主要会议与期刊的另外 **343** 篇论文，并已与精选去重，让当年的产出更完整；每篇同样配一句话说明它做了什么，方便快速扫读。

> **自动生成** — 请勿手工编辑本文件。精选条目请加到 [README.zh-CN.md](README.zh-CN.md)，索引条目请加到[全量索引](tools/data/conference-index.md)，然后运行 `python tools/build_timeline.py`。

---

## 逐年论文量

```
2026  ███████████████████████        102
2025  ██████████████████████████████ 134
2024  ████████████████████████       105
2023  ███████████████                67
2022  █████████                      41
2021  ███████                        30
2020  ████                           17
2019  ██                             8
2018  ███                            14
2017  █                              6
2016  █                              3
2015  █                              6
2014  █                              4
2013  █                              2
2011  █                              4
2010  █                              2
≤2009 █████                          23
```

<sub>2018 年代理梯度的突破与 2023 年脉冲 Transformer 浪潮，是图中两级明显的跃升。</sub>

---

## 跳转到年份

[2026](#2026) · [2025](#2025) · [2024](#2024) · [2023](#2023) · [2022](#2022) · [2021](#2021) · [2020](#2020) · [2019](#2019) · [2018](#2018) · [2017](#2017) · [2016](#2016) · [2015](#2015) · [2014](#2014) · [2013](#2013) · [2011](#2011) · [2010](#2010) · [2008](#2008) · [2007](#2007) · [2006](#2006) · [2005](#2005) · [2004](#2004) · [2003](#2003) · [2002](#2002) · [2001](#2001) · [2000](#2000) · [1999](#1999) · [1998](#1998) · [1997](#1997) · [1991](#1991) · [1990](#1990) · [1952](#1952) · [1943](#1943)

---

## 脉冲 Transformer 与大模型时代  <sub>(2023–2026)</sub>

### 2026

**精选**

- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) ★ · SpikingBrain: Spiking Brain-inspired Large Models (**TMLR 2026**). \[[paper](https://arxiv.org/abs/2509.05276)\]\[[code](https://github.com/BICLab/SpikingBrain-7B)\]
  > 中科院自动化所（李国齐、徐波）的类脑脉冲大模型（7B 线性 / 76B 混合 MoE），自适应脉冲编码，4M 长上下文首字延迟提速百倍，并在国产（沐曦 MetaX）GPU 上训练。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Advancing Spatiotemporal Representations in SNNs via Parametric Invertible Transformation (PIT) (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=3JwNXQzxll)\]\[[code](https://github.com/YinsongYan/ICLR26)\]
  > 将可逆变换与神经元动力学共轭结合，并校正代理梯度失配，扩展二值脉冲可用的时空表征空间。
- [`训练方法`](README.zh-CN.md#3--训练方法) · TP-Spikformer: Token Pruned Spiking Transformer (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=L5llQD0nMf)\]
  > 在多个脉冲 Transformer 家族中免训练剪除低信息 token，在保持竞争性精度的同时降低存储与计算开销。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Towards Lossless Memory-efficient Training of SNNs via Gradient Checkpointing and Spike Compression (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=nrBJ0Uvj7c)\]\[[code](https://github.com/AllenYolk/snn-gradient-checkpointing)\]
  > 将自适应时空梯度检查点与无损二值脉冲压缩结合，训练内存最多降低 8 倍且不损失精度。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spikingformer: A Key Foundation Model for Spiking Neural Networks (**AAAI 2026**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37207)\]\[[code](https://github.com/TheBrainLab/Spikingformer)\]
  > 用全脉冲（膜电位）残差取代 Spikformer 的非脉冲连接，消除整数-浮点乘法，更契合硬件。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Neural Dynamics Self-Attention for Spiking Transformers (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=jJedqisfOt)\]
  > 引入局部感受野偏置，并以充电—发放—复位动力学实现注意力，推理时无需显式存储注意力矩阵。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikingBrain2.0: Brain-Inspired Foundation Models for Efficient Long-Context and Cross-Platform Inference (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2604.22575)\]
  > 扩展至 5B 语言/视觉语言模型，引入双空间稀疏注意力与 INT8 脉冲/FP8 双路径，支持千万级 token 及 GPU 或神经形态推理。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Robust Spiking Neural Networks Against Adversarial Attacks (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=qTqAL2t8Aa)\]
  > 将阈值邻近神经元识别为主要攻击面，并以阈值感知优化保护膜电位安全裕量。

<details>
<summary><b>当年另有 94 篇</b> — 当年全量索引，每篇一句话</summary>

- A highly energy-efficient multi-core neuromorphic architecture for training deep spiking neural networks (**Nature Communications 2026**) [[paper](https://www.nature.com/articles/s41467-026-70586-x)]
  > 在每个核内设置三种专用计算引擎，让神经形态芯片能在端侧直接反向传播训练深度脉冲网络，并在 FPGA 上以 20 核验证，涵盖联邦学习场景。
- Robustify Spiking Neural Networks via Dominant Singular Deflation under Heterogeneous Training Vulnerability (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10010693)]
  > 正交投影剔除 BPTT 梯度的主奇异分量，压低 Hessian 谱半径，避免单次异分布反向传播导致网络崩溃。
- A Brain-Inspired Gating Mechanism Unlocks Robust Computation in Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011430)]
  > 让膜电导随神经元活动演化，为 LIF 引入类生物门控，选择性过滤输入并抑制噪声，提升 SHD 等时序任务的鲁棒性。
- Training Deep Normalization-Free Spiking Neural Networks with Lateral Inhibition (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009258)]
  > 将每层拆分为兴奋性与抑制性神经元群，用减性与除性侧抑制取代归一化层，配合专门初始化与梯度解耦稳定深层训练。
- 3DSMT: A Hybrid Spiking Mamba-Transformer for Point Cloud Analysis (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10010096)]
  > 将 Spiking Local Offset Attention 与脉冲 Mamba 模块结合，兼顾点云局部几何细节与线性复杂度的全局建模，降低能耗。
- Time Is All It Takes: Spike-Retiming Attacks on Event-Driven Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10008650)]
  > 在抖动、总延迟与篡改数量预算下仅平移已有脉冲时刻，保持发放数与发放率不变，揭示现有防御忽视的时间维攻击面。
- Cannistraci-Hebb Training on Ultra-Sparse Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007264)]
  > 以脉冲相关性初始化拓扑，并用 Cannistraci-Hebb 网络自动机预测突触再生，在超稀疏连接下削减突触操作与神经形态硬件能耗。
- CaRe-BN: Precise Moving Statistics for Stabilizing Spiking Neural Networks in Reinforcement Learning (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011021)]
  > 用置信度自适应策略更新 BN 滑动统计量并加入重校准，缓解强化学习中分布漂移导致的脉冲策略训练不稳，且不增加推理开销。
- Otters: An Energy-Efficient Spiking Transformer via Optical Time-to-First-Spike Encoding (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007423)]
  > 让氧化铟光电突触的自然衰减直接完成 TTFS 时间加权，省去数字运算，并配套量化 ANN 到 SNN 的转换算法支撑 Transformer。
- Online Pseudo-Zeroth-Order Training of Neuromorphic Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011366)]
  > 以单次带噪前向传播加自上而下的直接反馈取代空间反向传播，并用动量反馈连接抑制方差，更契合片上在线训练。
- SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011088)]
  > 调节发放阈值使多数神经元保持稳定发放、少数快速适应，再以零阶优化与子空间投影支撑端侧小样本类增量学习。
- Breaking Gradient Temporal Collinearity for Robust Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10006881)]
  > 以梯度时间共线性刻画各时间步梯度方向的一致性，并在直接编码输入层加入参数化正交核解相关，弥补直接编码的鲁棒性短板。
- Random Spiking Neural Networks are Stable and Spectrally Simple (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009762)]
  > 借助布尔函数的傅里叶分析刻画离散时间 LIF 分类器，证明宽随机网络的频谱集中于低频，因而对输入扰动天然稳定。
- Many Eyes, One Mind: Temporal Multi-Perspective and Progressive Distillation for Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009850)]
  > 为每个时间步提供掩码加权的教师特征以形成不同时序视角，并让截断预测逐步对齐全长预测，使早停推理同样可靠。
- Robust Selective Activation with Randomized Temporal K-Winner-Take-All in Spiking Neural Networks for Continual Learning (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10006915)]
  > 以脉冲迹相关性配合随机 top-k 竞争取代基于发放率的 K-WTA 选择激活神经元，降低任务表征重叠并增强对时间扰动的鲁棒性。
- Beyond Linear Processing: Dendritic Bilinear Integration in Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011474)]
  > 在 LIF 神经元中引入源自神经生理实验的双线性树突整合规则，使单个神经元即可捕捉输入相关性并完成非线性分类。
- Spiking Discrepancy Transformer for Point Cloud Analysis (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011321)]
  > 通过脉冲特征之间的差异构建注意力，兼顾中心-邻域局部几何与宏观脉冲强度统计，把脉冲 Transformer 扩展到三维点云。
- PredNext: Explicit Cross-View Temporal Prediction for Unsupervised Learning in Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10010014)]
  > 跨视角预测未来时间步与视频片段，为 SNN 提供无监督训练信号，提升时序特征一致性，并在 UCF101、HMDB51、MiniKinetics 上建立基准。
- Difference Predictive Coding for Training Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007923)]
  > 把预测编码层间传递的稠密浮点误差换成稀疏三值脉冲并配自适应阈值，实现局部学习，层间数据搬运降低两个数量级以上。
- Fractional-Order Spiking Neural Network (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009869)]
  > 用分数阶微分方程取代一阶膜电位动力学，使神经元具备长程非马尔可夫记忆，在能耗相当的前提下提升抗噪能力，并开源工具箱。
- SpikeGen: Decoupled “Rods and Cones” Visual Representation Processing with Latent Generative Framework (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009062)]
  > 仿照视杆-视锥分工，在潜空间生成模型中融合脉冲相机与 RGB 流，互补脉冲的空间稀疏与 RGB 的时间稀疏，覆盖去模糊、重建与新视角合成。
- Biologically Plausible Learning via Bidirectional Spike-Based Distillation (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009918)]
  > 联合训练前馈与反向两个脉冲网络，让感知决策与刺激重建互为编码转换，无需传递带正负号的误差信号。
- Distribution-Aware Multi-Granularity Phase Coding: Towards Lower Conversion Error for Spike-Driven Large Language Models (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007555)]
  > 以带多个可学习基的多粒度相位编码按隐层激活分布分配离散值，降低 ANN-to-SNN 转换误差；仅训练神经元即可转换 LLaMA，无需微调权重。
- SpikeStereoNet: A Brain-Inspired Framework for Stereo Depth Estimation from Spike Streams (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007680)]
  > 直接从双视角原始脉冲流估计立体深度，用循环脉冲网络模块迭代细化结果，并配套发布合成与真实的稠密深度标注数据集。
- SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10008450)]
  > 将脉冲相机的快速球体检测与较慢的脉冲神经校准相结合，并用模仿学习训练击球策略，实现高速乒乓球的精准落点控制。
- Spike-based Digital Brain: a novel fundamental model for brain activity analysis (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009923)]
  > 把 fMRI 时间序列编码为脉冲序列，学习锚点脑区与目标脑区之间的时序驱动关系，同时支持活动预测、疾病分类与有效连接推断。
- Activation-wise Propagation: A One-Timestep Strategy for Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37187)]
  > 让膜电位在空间相邻神经元之间传递以取代逐时间步迭代，将推理压缩到单个时间步，适用于点云与事件流网络。
- SpikingIR: A Novel Converted Spiking Neural Network for Efficient Image Restoration (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37769)]
  > 把图像复原网络转换为 SNN：将离散脉冲输出映射回连续像素空间，并回收残余膜电位，减少转换中的信息损失。
- A Closer Look at Knowledge Distillation in Spiking Neural Network Training (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37175)]
  > 用显著性加权的教师激活图对齐学生的脉冲激活图，并以高斯噪声平滑稀疏 logits，弥合 ANN 与 SNN 输出的连续-离散差异。
- Optimization Method for Surrogate Function in Spiking Neural Networks Based on Membrane Potential Distribution (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39769)]
  > 依据膜电位分布自适应调整代理梯度的宽度，并引入 KL 散度正则与离散化误差校正，稳定深层 SNN 训练中的梯度传播。
- Parallel Training Time-to-First-Spike Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37149)]
  > 推导可并行的前向与反向传播公式，使 TTFS（首次脉冲时间编码）网络能在 GPU 上并行训练，并改用基于膜电位的输出解码与渐进时间步训练。
- HardF-SNN: Hardware-Friendly Quantization for Spiking Neural Networks with Efficient Integer-Arithmetic-Only Inference (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37174)]
  > 将批归一化折叠为移位运算并采用比例化共享尺度量化，使脉冲推理全程只用整数运算，并在 FPGA 加速器上完成部署验证。
- SpikCommander: A High-performance Spiking Transformer with Multi-view Learning for Efficient Speech Command Recognition (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37194)]
  > 在全脉冲驱动 Transformer 中融合多视角时序感知脉冲注意力与上下文精修通道 MLP，以更少参数提升 SHD、SSC、GSC 上的语音命令识别。
- Timestep-Compressed Attack on Spiking Neural Networks Through Timestep-Level Backpropagation (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37479)]
  > 按单个时间步反向传播以支持提前停止，并复用预先计算的膜电位预热阶段，降低对脉冲神经网络发起梯度攻击所需的时延。
- Firing Bits Where It Matters: Spiking-Guided Just Recognizable Distortion Modeling for Machine-Centric Video Coding (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38935)]
  > 用脉冲网络将视频帧分解为空间结构、通道交互与时间模式以预测 QP 图，抑制机器视觉冗余，把码率优先分配给任务关键内容。
- MPD-SGR: Robust Spiking Neural Networks with Membrane Potential Distribution-Driven Surrogate Gradient Regularization (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37166)]
  > 通过正则化减少落在代理梯度有效区间内的膜电位比例，削弱输入扰动的可利用梯度通路，提升 SNN 的对抗鲁棒性。
- Training-Free ANN-to-SNN Conversion for High-Performance Spiking Transformers (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37195)]
  > 用多基指数衰减脉冲神经元近似 Transformer 中的各类非线性运算，无需修改权重或微调即可转换 ViT、RoBERTa、GPT-2 等预训练模型。
- I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37179)]
  > 用并行卷积模拟微眼跳，将静态图像实时转换为事件流，缓解事件数据稀缺，支持先合成预训练再在真实数据上微调。
- S³: Spiking Neurons as an Isolating Segmenter for Brain Signal Decoding (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38869)]
  > 借助脉冲神经元的复位机制自适应切分脑信号，并以随机贪心搜索生成分段伪标签，规避分段与任务性能之间的梯度阻断。
- TDSNNs: Competitive Topographic Deep Spiking Neural Networks for Visual Cortex Modeling (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37208)]
  > 为脉冲网络加入时空约束损失，复现灵长类视觉皮层的拓扑组织，ImageNet top-1 精度不降，而拓扑 ANN TopoNet 约掉 3 个点。
- Temporal Dynamics Enhancer for Directly Trained Spiking Object Detectors (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37178)]
  > 用脉冲编码器打破各时间步输入雷同，以时序相关性做注意力门控，并用脉冲驱动注意力将其能耗降到常规注意力的一小部分。
- Spiking Heterogeneous Graph Attention Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39068)]
  > 以共享参数的单层图卷积聚合元路径邻居并做语义级注意力，再用脉冲编码得到 1-bit 异质图表示，降低内存与推理开销。
- Oligodendrocyte-Driven Spiking Neural Model (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39306)]
  > 为脉冲神经元配上少突胶质细胞单元进行双向调制，丰富脉冲表达的多样性并提升发放精度，使微弱脉冲不再被淹没。
- HLML-SNN：Fast Continual Learning in Spiking Neural Networks Achieved via Hebbian Learning-Driven Meta-Learning (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39942)]
  > 将持续学习拆为样本级 Hebbian 快速适应与任务级元学习的权重固化两个阶段，模仿皮层-海马的记忆转移，抑制灾难性遗忘。
- DS-ATGO: Dual-Stage Synergistic Learning via Forward Adaptive Threshold and Backward Gradient Optimization for Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37165)]
  > 前向按各时间步的膜电位动态自适应调节阈值，后向同步优化代理梯度，均衡各层发放率，让深层神经元也能拿到梯度。
- Pseudo-Spiking Neurons: A Noise-Based Training Framework for Heterogeneous-Latency Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40086)]
  > 用可学习噪声模拟脉冲的截断与量化，把每个神经元的时间步数变成可反传优化的参数，无需 BPTT 即可训练异构延迟网络。
- Spatial-Frequency Spiking Neural Network for Underwater Object Detection (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39109)]
  > 在脉冲模块中融合空域与频域特征，强化浑浊水下的边缘与纹理，并把 YOLOX 由 ANN 转换为 SNN，实现低功耗水下目标检测。
- SFedHIFI: Fire Rate-Based Heterogeneous Information Fusion for Spiking Federated Learning (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39787)]
  > 按通道分解权重让资源受限客户端只训练更窄的 SNN，再基于发放率跨宽度融合信息，使异构客户端能在联邦学习中统一聚合。
- Dynamic Weight Adaptation in Spiking Neural Networks Inspired by Biological Homeostasis (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40146)]
  > 把 BCM 稳态理论引入脉冲网络，在运行中实时调整权重以稳定神经元活动，无需微调即可改善退化条件下的避障与连续控制。
- GT-SNT: A Linear-Time Transformer for Large-Scale Graphs via Spiking Node Tokenization (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38667)]
  > 以多步特征传播后的脉冲计数作为节点 token，免去预定义码本，并通过 node-to-token 注意力把全局聚合降到线性复杂度。
- Exploring the Potentials of Spiking Neural Networks for Image Deraining (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37295)]
  > 为 LIF 神经元补上空间上下文以缓解频域饱和，再做脉冲分解增强与多尺度表示，图像去雨能耗仅为已有 SNN 方法的 13%。
- Spiking-Aided Neural Architecture for Efficient and Robust WiFi Sensing (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39589)]
  > 将抗噪的脉冲神经元与常规 ANN 特征提取器结合用于 WiFi 室内感知，缓解多径衰落干扰并加快训练收敛。
- Stabilizing Spiking Neurons Through Biologically Inspired Polarization (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39435)]
  > 以解析式膜动力学刻画去极化、复极化与超极化，把膜电位约束在合理区间，稳定深层网络梯度，无需可学习门控与代理梯度调参。
- Spike Stream Memory Transfer for Dynamic Scene Reconstruction (**AAAI 2026**)
  > 借鉴视觉记忆机制，将此前推断的光强与运动信息前传，扩展脉冲流的长时感知范围，并抑制片段间与片段内的运动模糊。
- LAS: Loss-less ANN-SNN Conversion for Fully Spike-Driven Large Language Models (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37151)]
  > 用两类新神经元处理激活离群值与非线性算子，并配以脉冲等价的 Transformer 组件，把预训练 LLM 无损转换为全脉冲驱动模型。
- Spike Imaging Velocimetry: Dense Motion Estimation of Fluids Using Spike Streams (**AAAI 2026**)
  > 以细节保持的分层变换、图编码器与多尺度细化，从脉冲相机流估计复杂流场的稠密速度场，并发布带标注的粒子成像数据集。
- BulletTime4D: Towards High Spatio-Temporal Resolution Dynamic Scene Rendering via Spike-Guided Stereo Vision (**AAAI 2026**)
  > 将脉冲相机与双目 RGB 相机联合，用多时间尺度形变表示融合低频时空特征与高频帧间运动，提升动态场景渲染的时空分辨率。
- Robust Noise Modeling for Spike Camera via Time-Interval Quantification and Spike-DSLR Multimodal Dataset in Low-Light Imaging (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37252)]
  > 借鉴传统相机曝光时间提出时间间隔量化以精确刻画脉冲相机噪声，并发布首个脉冲-DSLR 对齐数据集，低光重建 PSNR 提升逾 1.6 dB。
- Generalized Threshold Optimization with Harmony Multi-Threshold Neurons for Accurate ANN-to-SNN Conversion (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37206)]
  > 让神经元单步发放多次脉冲以释放残余膜电位，并给出可迁移到多种神经元变体的通用阈值优化，减少 ANN 转 SNN 所需时间步。
- HypoxSpike: Ternary Spiking Neural Network for Opioid Overdose Detection (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/41237)]
  > 用三值脉冲网络融合运动、呼吸与血氧信号，在肩戴式低功耗设备上分级识别低氧血症，降低误报率并修正脉搏血氧的肤色偏差。
- Bi-Spectrum Distillation: Addressing Spectral Mismatch in ANN-SNN Knowledge Transfer (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40085)]
  > 针对脉冲网络的低通特性导致的频谱失配，用可学习滤波器在特征层补回高频细节，并在 logits 层蒸馏教师输出的高频分量。
- Towards Training-Free and Accurate ANN-to-SNN Conversion via Activation-Aware Redistribution (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37148)]
  > 将免训练转换误差归因于分布失配，为自适应 IF 神经元引入逐通道参数以校准发放率，几乎零开销地适配 Transformer 主干。
- S3Net: Spatiotemporally Separated Sparse Network for Neuromorphic Vision Processing (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/42467)]
  > 用空间与时间分离的稀疏算子处理事件数据，在保持异步、稀疏计算的同时不牺牲任务精度。
- Ultralight Polarity-Split Neuromorphic SNN for Event-Stream Super-Resolution (**AAAI 2026**) [[paper](https://arxiv.org/abs/2508.03244)]
  > 让正负极性事件分别走同一脉冲网络的两条前向路径，并用可学习权重平衡时间、空间与极性一致性，把事件超分辨压缩成可嵌入相机的轻量模块。
- SDTrack: A Baseline for Event-based Tracking via Spiking Neural Networks (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shan_SDTrack_A_Baseline_for_Event-based_Tracking_via_Spiking_Neural_Networks_CVPR_2026_paper.html)][[arxiv](https://arxiv.org/abs/2503.08703)]
  > 用全局轨迹提示把事件流聚合成事件帧，再交由全脉冲驱动的 Transformer 主干跟踪，端到端运行，无需数据增强与后处理。
- Spk2VidNet: A Hierarchical Recurrent Architecture for High-Fidelity Video Reconstruction from Long Spike-Camera Streams (**CVPR 2026**) [[paper](https://cvpr.thecvf.com/virtual/2026/poster/38367)]
  > 从低分辨率脉冲流重建高保真视频：联合估计并互相修正帧间运动，按多尺度相似度融合特征，并用分段训练在显存受限下建模长时依赖。
- Towards Reliable Evaluation of Adversarial Robustness for Spiking Neural Networks (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_Towards_Reliable_Evaluation_of_Adversarial_Robustness_for_Spiking_Neural_Networks_CVPR_2026_paper.pdf)][[code](https://github.com/craree/ASSG-SNNs-Robustness-Evaluation)]
  > 在攻击迭代中按输入分布自适应调整代理梯度形状，并配合自适应步长的 PGD 变体，揭示现有脉冲网络的对抗鲁棒性被明显高估。
- Rethinking SNN Online Training and Deployment: Gradient-Coherent Learning via Hybrid-Driven LIF Model (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Hao_Rethinking_SNN_Online_Training_and_Deployment_Gradient-Coherent_Learning_via_Hybrid-Driven_CVPR_2026_paper.pdf)][[code](https://github.com/hzc1208/HD_LIF)]
  > 在发放阈值上下区间采用不同的脉冲计算规则，分离时间维梯度并缓解代理梯度错配，让在线训练既省显存又不牺牲推理精度。
- Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks (**CVPR 2026**) [[paper](https://arxiv.org/abs/2603.11676)]
  > 用硬件友好的按位与运算提取稳定脉冲骨架，牵引各时间步的噪声脉冲图向其收敛，再注入幅度感知噪声以保持扰动下的预测一致性。
- Reconstructing Spiking Neural Networks Using a Single Neuron with Autapses (**CVPR 2026**) [[paper](https://cvpr.thecvf.com/virtual/2026/poster/37109)]
  > 用带时延自突触的单个神经元重建整张网络：靠内部时间状态动态重构，模拟储备池、多层感知机与卷积层，大幅降低计算开销。
- Brain-Inspired Multimodal Spiking Neural Network for Image-Text Retrieval (**CVPR 2026**) [[paper](https://arxiv.org/abs/2603.26787)][[code](https://github.com/zxt6174/CMSF)]
  > 在脉冲层面融合图像与文本特征，再把融合表示作为软监督反哺单模态脉冲嵌入，仅用两个时间步即可实现有竞争力的检索。
- SpikeTrack: A Spike-driven Framework for Efficient Visual Tracking (**CVPR 2026**) [[paper](https://arxiv.org/abs/2602.23963)][[code](https://github.com/faicaiwawa/SpikeTrack)]
  > 以非对称时间步扩展与分支间单向信息流做 RGB 跟踪，并循环查询由模板初始化的紧凑记忆模块，逐步强化对目标的辨识。
- Temporal Representation Enhancement (TRE): Learning to Forget Dominant Patterns for Enhanced Temporal Spiking Features (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Temporal_Representation_Enhancement_TRE_Learning_to_Forget_Dominant_Patterns_for_CVPR_2026_paper.pdf)]
  > 抑制在各时间步反复出现的主导模式，迫使网络转而编码互补的时间线索，在不增加推理开销的前提下丰富脉冲动态。
- Temporal Interaction in Spiking Transformers with Multi-Delay Mixer (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Temporal_Interaction_in_Spiking_Transformers_with_Multi-Delay_Mixer_CVPR_2026_paper.pdf)]
  > 在脉冲自注意力中混合多种突触延迟上的激活，让信息在时间步之间交互，而非各时间步彼此独立地处理。
- Spike-driven Discrete Aggregation for Event-based Object Detection (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Spike-driven_Discrete_Aggregation_for_Event-based_Object_Detection_CVPR_2026_paper.pdf)]
  > 端到端学习如何采样并聚合原始事件为离散脉冲表示，替代手工设定的事件窗口，供循环脉冲检测器直接使用。
- Dynamic-Static Decomposition for Novel View Synthesis of Dynamic Scenes with Spiking Neurons (**CVPR 2026**) [[paper](https://openaccess.thecvf.com/content/CVPR2026/html/Dai_Dynamic-Static_Decomposition_for_Novel_View_Synthesis_of_Dynamic_CVPR_2026_paper.html)]
  > 将动态内容与静态背景分离，分别用脉冲神经元建模，避免动态场景的新视角合成把两者混为一体。
- On the Role of Temporal Granularity in the Robustness of Spiking Neural Networks (**CVPR 2026**)
  > 系统研究时间离散粒度如何影响脉冲网络的鲁棒性，把时间步分辨率视作可调的设计变量而非固定开销。
- SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks (**ICML 2026**) [[paper](https://icml.cc/virtual/2026/poster/63548)][[arxiv](https://arxiv.org/abs/2606.27807)]
  > 把视觉-语言-动作模型整条链路脉冲化：事件驱动视觉编码器、脉冲多模态大模型与群体编码策略头，面向低功耗具身导航与控制。
- SVL: Spike-based Vision-language Pretraining for Efficient 3D Open-world Understanding (**ICML 2026**) [[paper](https://arxiv.org/abs/2505.17674)][[code](https://github.com/bollossom/SVL)]
  > 通过点云、图像与文本的三元对比对齐预训练脉冲 3D 主干，再把语言分支重参数化移除，使推理保持脉冲驱动且轻量。
- UltraLIF: Fully Differentiable Spiking Neural Networks via Ultradiscretization and Max-Plus Algebra (**ICML 2026**) [[paper](https://icml.cc/virtual/2026/poster/64130)]
  > 用超离散化取代代理梯度：log-sum-exp 软阈值随可学习温度退火逼近真实发放，使脉冲网络前后向一致、真正可微。
- SpikeNet: Sparse Spike-Driven Mask Vector Transformer for Energy-Efficient and Stable Spiking Point Cloud Processing (**ICML 2026**) [[paper](https://icml.cc/virtual/2026/poster/66082)]
  > 用二值脉冲掩码把注意力对齐到点云的稀疏性，免除 softmax 与乘法运算，并配合动态稀疏残差结构完成点云分类与分割。
- Bio-Vision-Inspired Spiking Neural Networks for Object Detection with Event Cameras (**ICML 2026**) [[paper](https://icml.cc/virtual/2026/poster/64518)]
  > 引入具备噪声过滤能力的神经元、类视网膜的事件-脉冲表示，以及模拟皮层双向通路的多尺度网络，面向事件相机目标检测。
- TEFormer: Structured Bidirectional Temporal Enhancement Modeling in Spiking Transformers (**ICML 2026**) [[paper](https://arxiv.org/abs/2601.18274)][[code](https://github.com/Fancyssc/TEFormer)]
  > 在注意力模块做前向时间融合、在 MLP 中以门控循环做反向聚合，为脉冲 Transformer 提供双向时序建模，且对编码方式不敏感。
- Plug-and-Play Spiking Operators: Breaking the Nonlinearity Bottleneck in Spiking Transformers (**ICML 2026**) [[paper](https://arxiv.org/abs/2605.20289)]
  > 把 Transformer 的非线性拆解为除法、指数与范数三种基元，用 LIF 神经元群配合移位缩放实现，使 ANN-to-SNN 转换免微调地覆盖 softmax 与归一化。
- Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks (**ICML 2026**) [[paper](https://arxiv.org/abs/2603.13283)]
  > 用并行关联扫描一次处理多个输入脉冲，同时保留精确的硬复位动力学，并以可微求解器直接算出脉冲时刻，无需时间分箱。
- A2SG: Adaptive and Asymmetric Surrogate Gradients for Training Deep Spiking Neural Networks (**ICML 2026**) [[paper](https://arxiv.org/abs/2606.11236)][[code](https://github.com/KIST-NCL/A2SG)]
  > 在时空维度自适应调整代理梯度窗口，并让膜电位更高的神经元获得更大梯度，把梯度波动的降低与更平坦的极小值联系起来。
- Frequency Matching in Spiking Neural Networks for mmWave Sensing (**ICML 2026**) [[paper](https://arxiv.org/abs/2605.09983)]
  > 把 LIF 动力学视作低通滤波器，按毫米波信号中判别信息所处的频段来匹配设定膜电位衰减系数。
- Event2Vec: Processing Neuromorphic Events Directly by Representations in Vector Space (**ICML 2026**) [[paper](https://arxiv.org/abs/2504.15371)][[code](https://github.com/Intelligent-Computing-Lab-Panda/event2vec)]
  > 仿照 word2vec 把原始神经形态事件嵌入向量空间，让 Transformer 直接处理稀疏异步事件流，而不必先稠密化为帧。
- SAFformer: Improving Spiking Transformer via Active Predictive Filtering (**IJCAI 2026**) [[paper](https://arxiv.org/abs/2605.08270)]
  > 把预测编码引入脉冲 Transformer：主动抑制可预测的输入信号，把算力集中到显著特征上，而非被动响应全部输入。
- Intrinsically Stable Spiking Neural Networks: Overcoming the Performance Barrier in the Absence of Batch Normalization (**ECCV 2026**) [[paper](https://arxiv.org/abs/2606.31695)]
  > 把无归一化脉冲网络的性能崩塌归因于发放率灾难性衰减，改用可离线折叠进静态权重的权重标准化与残差改造，消除推理期乘法。
- A First Exploration of Neuromorphic OT-CFM for Multi-Speaker VSR (**ECCV 2026**) [[paper](https://arxiv.org/abs/2606.31225)]
  > 先把视频转成事件流做唇读，再切分出单说话人片段，并用最优传输条件流匹配在潜空间走直线轨迹，推理仅需两步 ODE。
- SNNTracker: Online High-Speed Multi-Object Tracking With Spike Camera (**TPAMI 2026**) [[paper](https://ieeexplore.ieee.org/document/11165142/)]
  > 直接在脉冲相机流上做多目标跟踪：用动态神经场注意力检测目标，再以胜者为王模块结合在线 STDP 学习轨迹，全程无需先重建图像。
- DSNeRF: Dynamic View Synthesis for Ultra-Fast Scenes From Continuous Spike Streams (**TPAMI 2026**) [[paper](https://pubmed.ncbi.nlm.nih.gov/41570103/)]
  > 把像素射线到脉冲的生成过程写入 NeRF 训练，用积分发放层刻画传感器噪声，并以运动引导的脉冲层处理动态场景，实现超高速场景的新视角合成。
- Spiking neural networks with fatigue spike-timing-dependent plasticity learning using hybrid memristor arrays (**Nature Electronics 2026**) [[paper](https://www.nature.com/articles/s41928-025-01554-4)]
  > 将动态忆阻器的固有疲劳特性与非易失 1T1R 单元配对，使单个突触同时承载短时与长时记忆，在硬件上实现 fatigue-STDP 的无监督在线学习。

</details>

### 2025

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) · Backpropagation-Free Spiking Neural Networks with the Forward-Forward Algorithm (**arXiv 2025**). \[[paper](https://arxiv.org/abs/2502.20411)\]
  > 将 Hinton 的 Forward-Forward（两次对比性前向、逐层局部目标）搬到脉冲神经元。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Scaling Spike-driven Transformer with Efficient Spike Firing Approximation (V3) (**IEEE TPAMI 2025**). \[[paper](https://arxiv.org/abs/2411.16061)\]\[[code](https://github.com/BICLab/Spike-Driven-Transformer-V3)\]
  > 用整数训练+脉冲推理（脉冲发放近似）与脉冲 MAE，把 SNN 扩展到 ImageNet 86.2%。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spiking Transformer with Spatial-Temporal Attention (STAtten) (**CVPR 2025**). \[[paper](https://arxiv.org/abs/2409.19764)\]\[[code](https://github.com/Intelligent-Computing-Lab-Panda/STAtten)\]
  > 提出分块的时空联合注意力，在与纯空间注意力相同复杂度下融合时序信息。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · Sorbet: A Neuromorphic Hardware-Compatible Transformer-Based Spiking Language Model (**ICML 2025**). \[[paper](https://arxiv.org/abs/2409.15298)\]
  > 用移位型 PTsoftmax 与 BSPN 替代 softmax 和层归一化，得到硬件友好的脉冲语言模型，在 GLUE 上相比 BERT 节能约 27 倍。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikeCLIP: A Contrastive Language-Image Pretrained Spiking Neural Network (**Neural Networks 2025**). \[[paper](https://arxiv.org/abs/2310.06488)\]\[[code](https://github.com/Lvchangze/SpikeCLIP)\]
  > 脉冲版 CLIP *多模态* 模型，在脉冲空间对齐图文表征，把 SNN 拓展到视觉-语言。
- [`应用`](README.zh-CN.md#7--应用) · Spike2Former: Efficient Spiking Transformer for High-Performance Image Segmentation (**AAAI 2025**). \[[paper](https://arxiv.org/abs/2412.14587)\]\[[code](https://github.com/BICLab/Spike2Former)\]
  > 基于归一化整数神经元的脉冲版 Mask2Former，在 ADE20K 等分割任务上刷新 SNN 最优（+12.7% mIoU）。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · On the Privacy Risks of Spiking Neural Networks: A Membership Inference Analysis (**UAI 2025**). \[[paper](https://arxiv.org/abs/2502.13191)\]
  > 证明 SNN 的成员推断隐私风险与 ANN 相当，且泄露随时间步 T 增大。
- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) · Spiking Neural Networks: A Theoretical Framework for Universal Approximation and Training (**arXiv 2025**). \[[paper](https://arxiv.org/abs/2509.21920)\]
  > 证明基于 LIF 的 SNN 可用脉冲时刻编码目标值，对紧域上任意连续函数做通用逼近。

<details>
<summary><b>当年另有 126 篇</b> — 当年全量索引，每篇一句话</summary>

- Neuromorphic computing paradigms enhance robustness through spiking neural networks (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-65197-x)][[code](https://github.com/DingJianhao/SNNEnhancingRobustness)]
  > 把任务关键信息前置到脉冲编码序列的早期，并采用提前退出解码忽略后段扰动，使脉冲神经网络的对抗鲁棒性超过传统 ANN。
- A spiking artificial neuron based on one diffusive memristor, one transistor and one resistor (**Nature Electronics 2025**) [[paper](https://www.nature.com/articles/s41928-025-01488-x)][[code](https://github.com/GnohzZ/Brain-Dynamics-Modeling-Acceleration)]
  > 用扩散型忆阻器、晶体管与电阻堆叠出单晶体管面积的神经元，具备阈值发放、不应期、随机性与内在可塑性，每脉冲能耗低至皮焦级。
- A biologically inspired artificial neuron with intrinsic plasticity based on monolayer molybdenum disulfide (**Nature Electronics 2025**) [[paper](https://www.nature.com/articles/s41928-025-01433-y)]
  > 以晶圆级单层 MoS2 的 DRAM 单元加反相器构成积分发放神经元，通过调制膜电位模拟内在可塑性与人眼明暗视觉适应。
- Modeling macroscopic brain dynamics with brain-inspired computing architecture (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-64470-3)]
  > 用面向动力学的量化与分层并行映射，将宏观脑动力学模型以低精度部署到类脑芯片和 GPU，在保持功能保真度的同时大幅加速仿真。
- A frugal Spiking Neural Network for unsupervised multivariate temporal pattern classification and multichannel spike sorting (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-64231-2)][[code](https://codeocean.com/capsule/9829487/tree)]
  > 在单层脉冲网络中联合 STDP、短时可塑性与内在可塑性，全无监督地在线聚类多变量时序模式，并用于语音特征与多通道 spike sorting。
- Efficient and robust temporal processing with neural oscillations modulated spiking neural networks (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-63771-x)][[code](https://github.com/YinsongYan/Rhythm-SNN)]
  > 用异质振荡信号调制脉冲神经元，使其只在各自的周期窗口内活跃，降低发放率并提升长时序处理能力与抗噪鲁棒性。
- Covariant spatio-temporal receptive fields for spiking neural networks (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-63493-0)][[code](https://github.com/jegp/nrf)]
  > 用仿射高斯核与漏积分动力学构造时空感受野，对仿射与时间尺度变换保持协变，并作为先验改善事件相机上的脉冲网络训练。
- A multisynaptic spiking neuron for simultaneously encoding spatial and temporal dynamics in spiking neural networks (**Nature Communications 2025**) [[paper](https://doi.org/10.1038/s41467-025-62251-6)][[code](https://github.com/fanliangwei/Multisynaptic-spiking-neurons)]
  > 让同一轴突在突触后神经元上建立多个不同阈值的突触，使发放率编码空间强度、脉冲时刻编码时间动态，并把 LIF 与 ReLU 纳为特例。
- Advancing spatio-temporal processing through adaptation in spiking neural networks (**Nature Communications 2025**) [[paper](https://www.nature.com/articles/s41467-025-60878-z)][[code](https://github.com/IGITUGraz/SE-adlif)]
  > 把自适应 LIF 的不稳定性归因于前向 Euler 离散化，改用辛 Euler 更新以拓宽可用参数范围，并在事件式时序基准上提升精度。
- Topology optimization of random memristors for input-aware dynamic SNN (**Science Advances 2025**) [[paper](https://www.science.org/doi/10.1126/sciadv.ads5340)][[code](https://github.com/bo-wang-up/PRIME)]
  > 受结构可塑性启发剪枝随机忆阻 SNN 的拓扑以吸收器件编程随机性，并按输入难度提前停止推理，在存内计算宏上降低延迟与能耗。
- Fully memristive spiking neural network for energy-efficient graph learning (**Science Advances 2025**) [[paper](https://www.science.org/doi/10.1126/sciadv.adv2312)]
  > 用 RRAM 突触与 NbOx 阈值开关神经元让脉冲并行传播求最短路径，替代算术搜索，并以非线性权重映射补偿神经元非线性以支撑大规模图。
- Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=oGmROC4e4W)] [[code](https://github.com/korneelf1/SpikingCrazyflie)]
  > 调度代理梯度斜率以平衡梯度幅值与方向一致性，并用特权引导策略热启动脉冲策略，使有状态强化学习可用于无人机位置控制。
- Toward Relative Positional Encoding in Spiking Transformers (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=MDWJlTWZHH)] [[code](https://github.com/microsoft/SeqSNN)]
  > 用格雷码编码相对距离，使偏移为 2 的幂时汉明距离恒定；并给出将对数距离矩阵直接融入脉冲注意力图的 Log-PE，支持二维图块。
- High Dynamic Range Imaging with Time-Encoding Spike Camera (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=flIdch9eTf)] [[code](https://github.com/zkzhu123/TESC)]
  > 改用高频计时信号的周期数记录脉冲溢出时刻，替代逐次计数，以更少比特位宽扩展 spike camera 的动态范围。
- Bipolar Self-attention for Spiking Transformers (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=nG45z7lJ7D)] [[code](https://openreview.net/attachment?id=nG45z7lJ7D&name=supplementary_material)]
  > 用三值矩阵乘法建模 Query 与 Key 的同极性与异极性膜电位交互，并以移位式 Softmax 近似 Shiftmax 部分恢复注意力行随机性，全程保持脉冲驱动。
- Spike-timing-dependent Hebbian learning as noisy gradient descent (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=YTbLri0siT)]
  > 把 Hebbian 型 STDP 规则改写为概率单纯形上的含噪梯度下降，证明其最终选出活动最强的突触前神经元，并揭示与镜像下降的联系。
- Spike-RetinexFormer: Rethinking Low-light Image Enhancement with Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=8W8SRZIpJP)]
  > 用脉冲算子在 Transformer 架构中重建 Retinex 分解流程，在参数量相当、理论能耗与访存更低的情况下逼近 ANN 的低光增强画质。
- SPACE: SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=Di0RasgbQ6)] [[code](https://github.com/ethanxyluo/SPACE)]
  > 最大化单个测试样本各增强视图间的脉冲发放行为一致性，无需源数据即可让 SNN 在测试时适应分布偏移。
- MI-TRQR: Mutual Information-Based Temporal Redundancy Quantification and Reduction for Energy-Efficient Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=NRqGpUAjV9)] [[code](https://github.com/dfxue/MI-TRQR)]
  > 度量不同时间步脉冲特征在像素级与全局尺度上的互信息冗余，再用概率掩码剔除冗余脉冲，无需额外参数即可提升稀疏度。
- Spik-NeRF: Spiking Neural Networks for Neural Radiance Fields (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=047VzZEpnu)]
  > 改用三值脉冲神经元提升 NeRF 渲染中的信息容量，推理时重参数化以保持无乘法事件驱动，并借 ANN 教师蒸馏补齐画质。
- Dendritic Resonate-and-Fire Neuron for Effective and Efficient Long Sequence Modeling (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=ywzGKDStrm)] [[code](https://openreview.net/attachment?id=ywzGKDStrm&name=supplementary_material)]
  > 把谐振-发放神经元拆成编码不同频段的多条树突分支，并在胞体引入随发放历史自适应的阈值，延长记忆跨度并保持脉冲稀疏。
- Spiking Neural Networks Need High-Frequency Information (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=owNPAl7LNK)] [[code](https://github.com/bic-L/MaxFormer)]
  > 指出脉冲神经元本质上是低通滤波器，并用 patch embedding 中的额外最大池化与浅层深度卷积替代自注意力，补回被抑制的高频信息。
- Activity Pruning for Efficient Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=zjOXZEXQKZ)] [[code](https://github.com/putshua/Activity-Pruning-SNN)]
  > 改用 AT-LIF 神经元并自适应调整阈值，稳定稀疏训练的同时压低平均发放率与突触操作数，可与权重剪枝叠加。
- Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=4q5ZYP0ynu)] [[code](https://github.com/PengXue0812/Multiplication-Free-Parallelizable-Spiking-Neurons-with-Efficient-Spatio-Temporal-Dynamics)]
  > 用逐通道卷积增强并行脉冲神经元的表达力，以锯齿状膨胀降低所需阶数，并以移位运算取代乘法，兼顾训练速度与硬件开销。
- SpikingVTG: A Spiking Detection Transformer for Video Temporal Grounding (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=SkhF3cuyev)] [[code](https://openreview.net/attachment?id=SkhF3cuyev&name=supplementary_material)]
  > 用显著性反馈门控在多模态脉冲检测 Transformer 中放大相关视频片段，借平衡点隐式微分实现免 BPTT 训练，并从非脉冲教师蒸馏。
- S²M-Former: Spiking Symmetric Mixing Branchformer for Brain Auditory Attention Detection (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=WtMuGdHvh6)] [[code](https://github.com/JackieWang9811/S2M-Former)]
  > 用镜像对称的空间与频率双分支及脉冲驱动 token-channel 混合器解码 EEG 听觉注意，并以一维 token 序列取代三维运算压缩参数与能耗。
- Local-Global Coupling Spiking Graph Transformer for Brain Disorders Diagnosis from Two Perspectives (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=kkhRTTmXFV)]
  > 耦合局部受限的脉冲群体动力学与全局优化的图卷积，从脑区间连接拓扑与脑区异常发放率两个视角刻画脑疾病特征。
- A Scalable, Causal, and Energy Efficient Framework for Neural Decoding with Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=oAbaGU9N1X)] [[code](https://spikachu-bci.github.io/)]
  > 将分箱脉冲投影到共享隐空间，由因果脉冲模块提取特征，实现低功耗实时脑机接口解码，并可少样本迁移到新会话与新个体。
- Spiking Meets Attention: Efficient Remote Sensing Image Super-Resolution with Attention Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=VaE33hkqmg)] [[code](https://github.com/XY-boy/SpikeSR)]
  > 用推断的注意力权重调制膜电位，联合建模时间与通道维度并利用遥感影像的全局自相似性，实现高效超分辨率重建。
- Adaptive Fission: Post-training Encoding for Low-latency Spike Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=2zZzdAMyYi)] [[code](https://github.com/JiangYizhou16/Adaptive-Fission)]
  > 训练后将高敏感神经元裂分为不同尺度与阈值的神经元组，作为 population coding 的推广，无需微调即可降低率编码 SNN 的时间步与延迟。
- S²NN: Sub-bit Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=hFsCuVc1cB)] [[code](https://openreview.net/attachment?id=hFsCuVc1cB&name=supplementary_material)]
  > 借助二值 SNN 卷积核的聚类规律把权重压缩到一比特以下，并用离群点感知量化 OS-Quant 校正码字选择偏差，降低存储与算力需求。
- Seemingly Redundant Modules Enhance Robust Odor Learning in Fruit Flies (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=d6WUTRJqP3)] [[code](https://github.com/L-0cean/Fly-SNN)]
  > 用果蝇嗅觉环路模型拆解侧抑制与脉冲频率适应的分工：前者仅在中低噪声下有益，后者在各噪声水平都能提升气味辨别。
- Fully Spiking Neural Networks for Unified Frame-Event Object Tracking (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=FooiwsnEH9)] [[code](https://github.com/Noctis-A/SpikeFET)]
  > 在全脉冲框架内融合图像帧与事件流，卷积局部特征与 Transformer 全局建模并行，并用随机拼块模块消除卷积填充带来的位置偏置。
- Enhanced Self-Distillation Framework for Efficient Spiking Neural Network Training (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=dpmMg6aK1D)] [[code](openreview.net/pdf?id=dpmMg6aK1D)]
  > 把中间层发放率投影到轻量 ANN 分支做自蒸馏，并结合基于发放率的反传，剔除不可靠教师信号，避免 BPTT 随时间步线性增长的开销。
- Learning the Plasticity: Plasticity-Driven Learning Framework in Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=fllsm01JWS)]
  > 训练突触可塑性规则而非固定权重，重构功能性与突触前依赖可塑性，使脉冲网络在线适应动态环境，提升工作记忆与多任务能力。
- HetSyn: Versatile Timescale Integration in Spiking Neural Networks via Heterogeneous Synapses (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=YYz4fumVed)] [[code](https://github.com/dzcgood/HetSyn)]
  > 为每个突触赋予独立时间常数，把时间积分从膜电位转移到突触电流，使单一 LIF 变体覆盖多种时间尺度，并增强噪声鲁棒性与工作记忆。
- Unveiling the Spatial-temporal Effective Receptive Fields of Spiking Neural Networks (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=tYnJC5ba6j)] [[code](https://github.com/EricZhang1412/Spatial-temporal-ERF)]
  > 提出时空有效感受野指标，揭示脉冲 Transformer 缺乏全局时空感受野，并用 MLPixer 与 SRB 两种通道混合模块在浅层扩大感受野，改善检测与分割。
- Brain-like Variational Inference (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=573IcLusXq)] [[code](https://github.com/hadivafaii/IterativeVAE)]
  > 从自由能的自然梯度推导推断动力学，得到循环脉冲 VAE：用膜电位迭代更新取代摊销编码器，并以整数脉冲计数表示，便于硬件实现。
- Proxy Target: Bridging the Gap Between Discrete Spiking Neural Networks and Continuous Control (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=RRBve5GwjS)] [[code](openreview.net/pdf?id=RRBve5GwjS)]
  > 引入连续可微的代理网络提供平滑目标更新，化解目标网络软更新与脉冲离散动力学的冲突，代理仅用于训练，部署无额外开销。
- Synergy Between the Strong and the Weak: Spiking Neural Networks are Inherently Self-Distillers (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=BrmR69AhUg)]
  > 把 SNN 每个时间步视作一个子模型并按置信度分强弱，双向自蒸馏（强教弱、弱教强），无需外部教师即可提升精度与对抗鲁棒性。
- Spike4DGS: Towards High-Speed Dynamic Scene Recontruction with 4D Gaussian Splatting via a Spike Camera Array (**NeurIPS 2025**) [[paper](https://openreview.net/pdf?id=V5efEA8nIr)] [[code](https://github.com/Qinghongye/Spike4DGS)]
  > 用多视角脉冲相机阵列拍摄高速动态场景，从连续脉冲流中恢复稠密点云与相机位姿，为 4D Gaussian Splatting 提供初始化，并配套合成与真实数据集。
- Toward End-to-End Bearing Fault Diagnosis for Industrial Scenarios with Spiking Neural Networks (**KDD 2025**) [[paper](https://doi.org/10.48550/arXiv.2408.11067)][[code](https://github.com/yqding326/MRA-SNN)]
  > 用多尺度注意力将原始振动信号直接编码为时空脉冲，免去预处理，再以脉冲残差注意力增强稀疏特征，实现端到端轴承故障诊断。
- DSF-Net: Dynamic Sparse Fusion of Event-RGB via Spike-Triggered Attention for High-Speed Detection (**ACM MM 2025**)
  > 以脉冲触发的动态稀疏注意力筛选并融合 Event 与 RGB 的判别性特征，并发布面向高速目标检测的大规模双模态基准数据集。
- ESOD: Event-Based Small Object Detection (**ACM MM 2025**)
  > 在主干中聚合稀疏事件特征，再由粗到细的可变形检测头逐级细化，弥补小目标的判别信息缺失，并采集真实场景的事件基准。
- E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event Cameras (**ACM MM 2025**)
  > 仅用多视角事件流驱动 4D 高斯泼溅，通过事件初始化、时间自适应切片与强度重要性剪枝抑制漂浮伪影，重建高速与低光动态场景。
- Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics (**ACM MM 2025**)
  > 通过脉冲触发的阈值动态在发放后短暂抬高阈值，为 LIF 神经元引入不应期，抑制过度兴奋与异常输入干扰，几乎不增开销。
- Signal-SGN: A Spiking Graph Convolutional Network for Skeleton Action Recognition via Learning Temporal-Frequency Dynamics (**ACM MM 2025**)
  > 把骨架序列的时间维当作脉冲时间步，联合一维脉冲图卷积、频域脉冲卷积与多尺度小波融合建模时频动态，以低能耗完成动作识别。
- SGM-Transformer: Rethinking Gradient Information Loss and Compensation in Spiking Neural Networks (**ACM MM 2025**)
  > 用 MCLIF 神经元从时间与空间双维度补偿反向传播中损失的梯度，并以 QK Memory 嵌入时序特征，让脉冲注意力跨时间步复用信息。
- Advanced SpikingYOLOX: Extending Spiking Neural Network on Object Detection with Spike-based Partial Self-Attention and 2D-Spiking Transformer (**ACM MM 2025**)
  > 在主干最深层引入基于脉冲的部分自注意力与二维脉冲 Transformer，并重新分配 Q/K/V 上的脉冲层位置，提升 SNN 目标检测精度。
- Spiking Neural Networks with Temporal Attention-Guided Adaptive Fusion for imbalanced Multi-modal Learning (**ACM MM 2025**)
  > 在每个时间步为融合后的脉冲特征打上跨模态注意力权重，并据此调节各模态学习率，缓解多模态 SNN 中的模态失衡与时间错位。
- Temporal-coded Spiking Transformer (**ACM MM 2025**)
  > 改造批归一化与残差连接以适配 TTFS 时间编码，并构建时间编码脉冲注意力，使 Transformer 以单次脉冲的发放时刻而非发放率承载信息。
- ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1849)]
  > 用 SNN 分支提取事件运动特征、ANN 分支处理色彩，并由神经元配置模块按跨模态特征动态调参，使脉冲集中于模糊区域完成去模糊。
- Robust Unfolding Network for HDR Imaging with Modulo Cameras (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1986)]
  > 将取模相机的 HDR 重建改写到图像梯度域，把优化过程展开为网络，并用脉冲神经元模块施加可学习稀疏先验，模型轻量且更鲁棒。
- SpikeDiff: Zero-shot High-Quality Video Reconstruction from Chromatic Spike Camera and Sub-millisecond Spike Streams (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1181)]
  > 把脉冲相机的成像物理约束注入预训练扩散模型的采样过程，无需领域训练数据即可从彩色脉冲流零样本重建高时间分辨率视频。
- Noise-Modeled Diffusion Models for Low-Light Spike Image Restoration (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1467)]
  > 把低光下脉冲成像的噪声退化直接建模为扩散前向过程，并以区域掩码、暗电流图与脉冲密度作为条件引导反向采样，复原脉冲图像。
- Efficient Spiking Point Mamba for Point Cloud Analysis (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/2271)]
  > 将 Mamba 状态空间模块引入 3D 脉冲网络，配合分层动态编码与非对称 SNN-ANN 预训练，弥补以往 3D SNN 难以建模长程依赖的缺陷。
- SpikePack: Enhanced Information Flow in Spiking Neural Networks with High Hardware Compatibility (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/345)]
  > 重构 LIF 神经元以减少时间依赖带来的信息损失，同时保留复位与漏电积分，实现 O(1) 复杂度、GPU 并行与近乎无损的 ANN-SNN 转换。
- SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1753)]
  > 在脉冲注意力中引入侧抑制机制，增强对相关 token 的关注并压制无关上下文，纠正沿用模拟 Transformer 注意力造成的注意力错配。
- Adaptive Gradient Learning for Spiking Neural Networks by Exploiting Membrane Potential Dynamics (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7783.pdf)]
  > 将代理梯度的形状与各时间步的膜电位分布动态绑定，抵消归一化层引起的电位漂移，缓解梯度消失并支持低时延推理。
- ILIF: Temporal Inhibitory Leaky Integrate-and-Fire Neuron for Overactivation in Spiking Neural Networks (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/4566.pdf)]
  > 引入分别作用于膜电位与电流的两个耦合抑制单元，在抑制过度发放、降低发放率的同时避免窄代理梯度带来的梯度消失。
- Neuromorphic Sequential Arena: A Benchmark for Neuromorphic Temporal Processing (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7408.pdf)]
  > 汇集七项跨多时间尺度的真实时序任务，从任务性能、训练速度、内存占用与能耗四方面统一评测各类脉冲神经元模型与网络架构。
- MSVIT: Improving Spiking Vision Transformer Using Multi-scale Attention Fusion (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7378.pdf)]
  > 用多尺度脉冲注意力融合替换单一尺度的注意力块，使脉冲驱动 Transformer 能跨图像尺度提取特征，缓解 SNN 与 ANN Transformer 的性能差距。
- A Fast and Accurate ANN-SNN Conversion Algorithm with Negative Spikes (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/6149.pdf)]
  > 引入可发放负脉冲的神经元，使 Leaky ReLU 网络也能快速转换为 SNN，并用基于激活值方差的阈值优化与跨层联合校准抑制误差累积。
- ECC-SNN: Cost-Effective Edge-Cloud Collaboration for Spiking Neural Networks (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/3167.pdf)]
  > 通过 ANN-SNN 联合训练把推理负载从云端下放到边缘脉冲模型，并以端侧增量学习适应环境变化，降低通信开销、能耗与时延。
- Cost-Effective On-Device Sequential Recommendation with Spiking Neural Networks (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/3150.pdf)]
  > 把稠密的物品嵌入编码为稀疏脉冲表示，并用脉冲滤波模块提取时序模式，使序列推荐能在内存与能耗受限的端侧设备上运行。
- SCNNs: Spike-based Coupling Neural Networks for Understanding Structural-Functional Relationships in the Human Brain (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1337.pdf)]
  > 用脉冲神经元分别刻画 fMRI 时序的功能特征与结构网络的空间特征，借助突触与神经元滤波效应量化结构-功能耦合，用于脑疾病识别。
- Exploiting Label Skewness for Spiking Neural Networks in Federated Learning (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1298.pdf)]
  > 在客户端内校准各标签的学习权重，并在客户端之间做知识蒸馏补偿缺失类别，抑制标签倾斜导致的本地 SNN 模型漂移。
- Binary Event-Driven Spiking Transformer (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1206.pdf)]
  > 将脉冲 Transformer 的权重与注意力图同时二值化为 1 bit，再用可逆框架与互信息增强蒸馏对齐全精度模型，弥补二值化的精度损失。
- Tackling Long-Tailed Data Challenges in Spiking Neural Networks via Heterogeneous Knowledge Distillation (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/787.pdf)]
  > 以训练充分的 CNN 作为异构教师，对脉冲 Transformer 同时做跨层特征与全局预测的多粒度蒸馏，缓解长尾数据下头部与尾部类别的分布偏差。
- SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and O(T) Complexity (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.10352)]
  > 把实值注意力改造为脉冲驱动的 Hamming 注意力，并筛选最优时空注意力方案，使视频任务的时间复杂度保持线性，可用于姿态跟踪与分割。
- Efficient ANN-SNN Conversion with Error Compensation Learning (**ICML 2025**) [[paper](https://www.arxiv.org/abs/2506.01968)]
  > 以可学习阈值裁剪、双阈值神经元和膜电位初始化分别抑制截断、量化与不均匀三类转换误差，把推理压缩到两个时间步。
- Differential Coding for Training-Free ANN-to-SNN Conversion (**ICML 2025**) [[paper](https://arxiv.org/abs/2503.00301)]
  > 在 ANN-to-SNN 转换中传递发放率的变化量而非发放率本身，并按激活分布迭代整定阈值，减少脉冲数与能耗。
- Efficient Logit-based Knowledge Distillation of Deep Spiking Neural Networks for Full-Range Timestep Deployment (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44825)]
  > 通过时空解耦的 logit 蒸馏让 SNN 在所有时间步上的隐式子模型同时收敛，一次训练即可任意调整推理时间步而无需重训。
- ReverB-SNN: Reversing Bit of the Weight and Activation for Spiking Neural Networks (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/43640)]
  > 将二值化对象由激活换成权重，保留实值脉冲激活并给二值权重加可学习幅度因子，在无乘法前提下提升信息容量。
- TTFSFormer: A TTFS-based Lossless Conversion of Spiking Transformer (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44159)]
  > 重新设计 TTFS 神经元以扩展表示范围并处理 Transformer 中的非线性层，实现每神经元至多发放一次脉冲的理论无损转换。
- BSO: Binary Spiking Online Optimization (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/45087)]
  > 以梯度动量与权重乘积超过阈值触发的翻转信号在线更新二值脉冲网络，省去潜权重存储，并给出按时间步自适应调阈的变体。
- Delay-DSGN: A Dynamic Spiking Graph Neural Network with Delay Mechanisms for Evolving Graph (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/43816)]
  > 为动态脉冲图网络加入可学习传播延迟，用可调中心的高斯核生成节点级延迟表示，使历史信息影响未来时间步的节点表征。
- TS-SNN: Temporal Shift Module for Spiking Neural Networks (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.04165)]
  > 通过时间维度的移位操作在单个时间步内融合过去、当前与未来的脉冲特征，并用残差防止信息丢失，仅新增一个可学习参数。
- SpikF: Spiking Fourier Network for Efficient Long-term Prediction (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/46411)]
  > 将长序列切分为 patch 并在频域上做选择性筛选，构建无注意力的脉冲预测网络，以更低能耗捕捉长程时间依赖。
- Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning (**ICML 2025**) [[paper](https://arxiv.org/pdf/2505.07921)]
  > 用自特征提取与交叉特征对比两个模块细化表征，并以 InfoNCE 与时间高效训练损失优化脉冲序列动态，提升低功耗小样本分类。
- Faster and Stronger: When ANN-SNN Conversion Meets Parallel Spiking Calculation (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44986)]
  > 把并行脉冲神经元各时间步与累积发放率建立数学映射，配合分布感知误差校准，在超低延迟下支持更一般激活函数的转换。
- Efficient Parallel Training Methods for Spiking Neural Networks with Constant Time Complexity (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/45776)]
  > 把 LIF 神经元改写为不动点迭代形式并行求解所有时间步，在不改网络结构的前提下将训练时间复杂度从 O(T) 降为常数。
- Training High Performance Spiking Neural Networks by Temporal Model Calibration (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44216)]
  > 从梯度视角出发，按时间步对 logit 梯度做重缩放以提升时间异质性，使直接训练的 SNN 各时间步输出更具多样性并提升精度。
- Temporal Misalignment in ANN-SNN Conversion and Its Mitigation via Probabilistic Spiking Neurons (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/45627)]
  > 指出 ANN-SNN 转换中的时间错位现象（层间脉冲随机重排反而提升精度），并据此引入两阶段概率脉冲神经元改进转换效果。
- Time to Spike? Understanding the Representational Power of Spiking Neural Networks in Discrete Time (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.18023)]
  > 证明离散时间 LIF 网络实现多面体区域上的分段常值函数，并量化时间步数与深度对输入空间划分复杂度及逼近规模的影响。
- Hybrid Spiking Vision Transformer for Object Detection with Event Cameras (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.07715)]
  > 将事件相机目标检测拆分为空间与时间两条特征提取支路构成混合脉冲 Transformer，并公开一个保护隐私的跌倒检测事件数据集。
- EventGPT: Event Stream Understanding with Multimodal Large Language Models (**CVPR 2025**) [[paper](https://arxiv.org/pdf/2412.00832)] [[code](https://github.com/XduSyL/EventGPT)]
  > 通过时空聚合器与事件-语言适配器把事件流接入预训练大语言模型，并以 RGB 图文预热、合成与真实指令数据三阶段训练。
- Spk2SRImgNet: Super-Resolve Dynamic Scene from Spike Stream via Motion Aligned Collaborative Filtering (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33079)]
  > 沿运动轨迹从相邻时刻聚合相似特征做协同滤波，抑制脉冲流波动，从低分辨率脉冲相机数据重建高分辨率高速场景图像。
- Decision SpikeFormer: Spike-Driven Transformer for Decision Making (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/32864)]
  > 以时间型与位置型脉冲自注意力把脉冲驱动 Transformer 用于离线强化学习序列建模，捕捉视觉类脉冲注意力忽略的轨迹依赖。
- Self-Supervised Learning for Color Spike Camera Reconstruction (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/34093)]
  > 利用颜色通道间的运动一致性联合估计运动，沿轨迹补全 Bayer 缺失像素，再以自监督掩码脉冲编码器抑制量化噪声。
- USP-Gaussian: Unifying Spike-based Image Reconstruction, Pose Correction and Gaussian Splatting (**CVPR 2025**) [[paper](https://arxiv.org/abs/2411.10504)]
  > 把脉冲流图像重建、相机位姿校正与 3D Gaussian Splatting 统一为端到端联合迭代优化，消除级联流程中的误差累积。
- VISTREAM: Improving Computation Efficiency of Visual Perception Streaming via Law-of-Charge-Conservation Inspired Spiking Neural Network (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/34908)]
  > 仅编码相邻帧的差分并借助 ST-BIF 神经元的电荷守恒性质免去膜电位重置，在等价于 ANN 精度的前提下降低流式感知的计算量。
- Efficient ANN-Guided Distillation: Aligning Rate-based Features of Spiking Neural Networks through Hybrid Block-wise Replacement (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.16572)]
  > 逐块把 ANN 模块替换为脉冲模块，用中间混合模型渐进对齐发放率特征，并自然支持基于发放率的反向传播完成蒸馏。
- Spiking Transformer: Introducing Accurate Addition-Only Spiking Self-Attention for Transformer (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.00226)]
  > 在自注意力中混用二值、三值与 ReLU 脉冲神经元，去掉 softmax 与缩放操作，使计算仅含加法并弥补纯二值化的精度损失。
- Brain-Inspired Spiking Neural Networks for Energy-Efficient Object Detection (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33275)]
  > 以含脉冲卷积神经元的视神经核团模块增强深层特征提取，构建可直接训练的多尺度脉冲检测器，兼顾可解释性与低功耗。
- Temporal Separation with Entropy Regularization for Knowledge Distillation in Spiking Neural Networks (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.03144)]
  > 在各时间步分别对 logits 做蒸馏而非只用时间平均输出，并引入熵正则稳定优化，提升脉冲学生网络的蒸馏效果。
- STAA-SNN: Spatial-Temporal Attention Aggregator for Spiking Neural Networks (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.02689)]
  > 融合脉冲驱动自注意力、时间位置编码与步间注意力，并用时间步随机丢弃跳出局部最优，以更少时间步捕获时空依赖。
- Towards Effective and Sparse Adversarial Attack on Spiking Neural Networks via Breaking Invisible Surrogate Gradients (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.03272)]
  > 针对代理梯度不可见的推理模型，由膜电位分布反推代理梯度，并用生成-削减范式稀疏化扰动，攻击事件相机的二值动态图像。
- Rethinking Spiking Self-Attention Mechanism: Implementing α-XNOR Similarity Calculation in Spiking Transformers (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33850)]
  > 用 α-XNOR 相似度替代点积计算 Q-K 相关性，为成对非脉冲赋予权重 α，弥补脉冲序列稀疏带来的信息缺失。
- Quantized Spike-driven Transformer (**ICLR 2025**) [[paper](https://openreview.net/forum?id=5J9B7Sb8rO)]
  > 把量化脉冲驱动注意力的退化归因于脉冲分布双峰化，用信息增强 LIF 神经元与细粒度蒸馏对齐全精度教师，兼顾精度与低功耗。
- Rethinking Spiking Neural Networks from an Ensemble Learning Perspective (**ICLR 2025**) [[paper](https://openreview.net/forum?id=ZyknpOQwkT)]
  > 把各时间步视作共享参数的子网络集成，通过平滑初始膜电位并让相邻时间步互相引导，缓解训练不稳定与时间维梯度消失。
- DeepTAGE: Deep Temporal-Aligned Gradient Enhancement for Optimizing Spiking Neural Networks (**ICLR 2025**) [[paper](https://openreview.net/forum?id=drPDukdY3t)]
  > 按各时间步的膜电位分布自适应调整代理梯度，并在网络阶段与时间步两个维度施加深监督，抑制梯度消失且不增加推理开销。
- QP-SNN: Quantized and Pruned Spiking Neural Networks (**ICLR 2025**) [[paper](https://openreview.net/forum?id=MiPyle6Jef)]
  > 重缩放权重使均匀量化充分利用比特位宽，并按时空脉冲活动的奇异值识别冗余卷积核做结构化剪枝，面向边缘端部署。
- Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness (**ICLR 2025**) [[paper](https://openreview.net/forum?id=9HsfTgflT7)]
  > 训练时为网络各阶段随机分配时间步数，使同一模型在推理阶段可跨时间步泛化，并能部署到时钟驱动与事件驱动硬件。
- P-SpikeSSM: Harnessing Probabilistic Spiking State Space Models for Long-Range Dependency Tasks (**ICLR 2025**) [[paper](https://openreview.net/forum?id=Sf4ep9Udjf)]
  > 以随机脉冲采样取代串行 LIF 动力学并嵌入状态空间模型，使训练可并行化，在长程序列任务上保持稀疏发放。
- TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting (**ICLR 2025**) [[paper](https://openreview.net/forum?id=rDe9yQQYKt)]
  > 把脉冲神经元拆为树突与胞体双腔室分别处理不同频段，并直接向胞体注入电流减少信息损失，提升时序预测精度与鲁棒性。
- Improving the Sparse Structure Learning of Spiking Neural Networks from the View of Compression Efficiency (**ICLR 2025**) [[paper](https://openreview.net/forum?id=gcouwCx7dG)]
  > 先用 PQ 指数评估当前稀疏子网络的可压缩程度，据此自适应确定连接重连比例，再执行动态剪枝与再生长，提高稀疏 SNN 的压缩效率。
- Spiking Vision Transformer with Saccadic Attention (**ICLR 2025**) [[paper](https://openreview.net/forum?id=qzZsz6MuEq)]
  > 借鉴眼跳机制，用脉冲分布而非点积衡量 Q-K 空间相关性，并加入时间交互模块，使脉冲注意力复杂度随 token 数线性增长。
- SpikeGS: Reconstruct 3D scene captured by a fast moving bio-inspired camera (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2407.03771v2)]
  > 将脉冲流接入 3D Gaussian Splatting，以累积光栅化与区间监督从高时间分辨率但缺纹理的脉冲流中重建几何与纹理，克服快速运动模糊。
- Rethinking High-speed Image Reconstruction Framework with Spike Camera (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2501.04477)] [[code](https://github.com/chenkang455/SpikeCLIP)]
  > 借助 CLIP 的图文对齐，用场景文本描述与非配对高质量图像替代合成数据监督脉冲重建，改善真实低光场景下的纹理与亮度。
- Spiking Point Transformer for Point Cloud Classification (**AAAI 2025**)
  > 以队列驱动的采样直接编码在每个时间步保留最有效的支撑点，把脉冲 Transformer 从二维图像推广到三维点云分类。
- Efficient 3D Recognition with Event-driven Spike Sparse Convolution (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.07360)] [[code](https://github.com/bollossom/e-3dsnn)]
  > 用脉冲体素编码把点云转为稀疏脉冲序列，再以脉冲稀疏卷积提特征，得到可同时做分类、检测与分割的事件驱动三维骨干网络。
- GRSN: Gated Recurrent Spiking Neurons for POMDPs and MARL (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2404.15597)]
  > 用脉冲神经元的单步更新累积历史状态以对齐 RL 时序，并引入门控增强记忆，在 POMDP 与多智能体协作上以约一半功耗接近 RNN。
- EventZoom: A Progressive Approach to Event-Based Data Augmentation for Enhanced Neuromorphic Vision (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2405.18880)]
  > 通过渐进缩放与平移把变换样本嵌入原始事件流，避免裁剪造成的空间信息丢失与时间中断，保持稀疏性与高动态范围。
- Leveraging Asynchronous Spiking Neural Networks for Ultra Efficient Event-Based Visual Processing (**AAAI 2025**)
  > 逐事件异步处理并动态演化图表示，配合脉冲神经元实现低延迟与高稀疏，能耗较帧式方法低若干数量级，精度相当。
- CREST: An Efficient Conjointly-trained Spike-driven Framework for Event-based Object Detection Exploiting Spatiotemporal Dynamics (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.12525)] [[code](https://github.com/shen-aoyu/CREST/)]
  > 以联合学习规则缓解深层 SNN 的梯度消失并支持双运行模式，配合多尺度时空事件整合器与 ST-IoU 损失完成全脉冲事件目标检测。
- UCF-Crime-DVS: A Novel Event-Based Dataset for Video Anomaly Detection with Spiking Neural Networks (**AAAI 2025**)
  > 把 UCF-Crime 监控视频转为 DVS 事件流，构建首个事件相机视频异常检测基准，并配套多尺度脉冲融合网络 MSF 作为基线。
- SpikingSSMs: Learning Long Sequences with Sparse and Parallel Spiking State Space Models (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2408.14909)][[code](https://github.com/shenshuaijie/SDN
  > 将树突启发的神经元动力学分层融入状态空间模型，并用轻量代理网络预测复位后膜电位，化解事件驱动与并行计算的冲突。
- Advancing Spiking Neural Networks towards Multiscale Spatiotemporal Interaction Learning (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2405.13672)]
  > 用脉冲多尺度注意力捕捉事件数据的时空交互，并以注意力权重驱动的 ZoneOut 伪集成正则化，缩小非 Transformer 架构 SNN 与 ANN 的差距。
- SpikingYOLOX: Improved YOLOX Object Detection with Fast Fourier Convolution and Spiking Neural Networks(**AAAI 2025**)
  > 在 YOLOX 中引入可发放三值的带符号脉冲神经元以增强深层特征，并用快速傅里叶卷积提供全局感受野，把 SNN 推向目标检测任务。
- ALADE-SNN: Adaptive Logit Alignment in Dynamically Expandable Spiking Neural Networks for Class Incremental Learning (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.12696)]
  > 按任务动态扩展 SNN 结构，用自适应 logit 对齐平衡新旧任务特征，训练时抑制旧特征到新类的映射权重，缓解类增量学习中的偏置与过拟合。
- Efficient Spike-driven Transformer For High-performance Image Segmentation (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.14587)] [[code](https://github.com/BICLab/Spike2Former)]
  > 定位并改造导致脉冲发放骤降的分割架构模块，引入归一化整数脉冲神经元稳定复杂 SNN 的训练，提升语义分割 mIoU。
- Towards Accurate Binary Spiking Neural Networks: Learning with Adaptive Gradient Modulation Mechanism (**AAAI 2025**)
  > 将权重符号频繁翻转诊断为二值脉冲神经网络训练的主要障碍，通过自适应调制梯度加以抑制，加快收敛并提升精度。
- Adaptive Calibration: A Unified Conversion Framework of Spiking Neural Networks (**AAAI 2025**)
  > 以逐层自适应发放的神经元降低 ANN-to-SNN 转换误差，再通过敏感度引导的脉冲压缩与输入自适应时间步，削减能耗和延迟。
- Towards More Discriminative Feature Learning in SNNs with Temporal-Self-Erasing Supervision (**AAAI 2025**)
  > 训练时自适应擦除各时间步预测中的高激活区域，迫使网络关注被忽略的弱激活线索，提升特征判别力与多时间步推理效果。
- FSTA-SNN: Frequency-based Spatial-Temporal Attention Module for Spiking Neural Networks (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2501.14744)] [[code](https://github.com/yukairong/FSTA-SNN)]
  > 利用浅层偏重竖直、深层偏重水平变化且各时间步差异微小的观察，以频域时空注意力抑制冗余脉冲特征，降低发放率。

</details>

### 2024

**精选**

- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) ★ · SpikeGPT: Generative Pre-trained Language Model with Spiking Neural Networks (**TMLR 2024**). \[[paper](https://arxiv.org/abs/2302.13939)\]\[[code](https://github.com/ridgerchu/SpikeGPT)\]
  > 首个大型生成式脉冲语言模型（最高 2.6 亿参数），将注意力线性化，运算量降低约 20 倍。
- [`应用`](README.zh-CN.md#7--应用) ★ · Fully Neuromorphic Vision and Control for Autonomous Drone Flight (**Science Robotics 2024**). \[[paper](https://www.science.org/doi/10.1126/scirobotics.adi0591)\]
  > 端到端"事件相机→SNN→控制"闭环，完全在神经形态硬件上驱动真实四旋翼飞行，是里程碑式的真机演示。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · TC-LIF: A Two-Compartment Spiking Neuron Model for Long-Term Sequential Modelling (**AAAI 2024**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/29625)\]\[[code](https://github.com/ZhangShimin1/TC-LIF)\]
  > 胞体-树突双腔室神经元，专为在长时间间隔上传播梯度而设计。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks (**ICML 2024**). \[[paper](https://proceedings.mlr.press/v235/huang24n.html)\]\[[code](https://github.com/HuuYuLong/Complementary-LIF)\]
  > 无超参的互补型神经元，开辟额外反传路径以缓解时间维梯度消失。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · Temporal Dendritic Heterogeneity Incorporated with SNNs for Learning Multi-Timescale Dynamics (DH-LIF) (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-023-44614-z)\]
  > 多树突分支神经元，各分支时间常数可学习，捕捉多时间尺度动态。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Training Spiking Neural Networks via Augmented Direct Feedback Alignment (**NeurIPS 2024**). \[[paper](https://arxiv.org/abs/2409.07776)\]
  > 用随机投影的直接反馈对齐（aDFA）无梯度训练 SNN，避免权重传输问题，更贴近生物与硬件。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Advancing Spiking Neural Networks Toward Deep Residual Learning (MS-ResNet) (**IEEE TNNLS 2024**). \[[paper](https://arxiv.org/abs/2112.08954)\]\[[code](https://github.com/Ariande1/MS-ResNet)\]
  > 提出膜电位（预激活）捷径，保持全脉冲计算与梯度范数守恒，把直接训练的 SNN 拓展到 482 层。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spike-driven Transformer V2 (Meta-SpikeFormer) (**ICLR 2024**). \[[paper](https://arxiv.org/abs/2404.03663)\]\[[code](https://github.com/BICLab/Spike-Driven-Transformer-V2)\]
  > 统一分类、检测与分割的元脉冲骨干（ImageNet 80%），为下一代神经形态芯片设计提供范式。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spikformer V2: Join the High-Accuracy Club on ImageNet with an SNN Ticket (**arXiv 2024**). \[[paper](https://arxiv.org/abs/2401.02020)\]
  > 引入脉冲卷积 Stem 与自监督预训练，是最早在 ImageNet 上突破 80% 的 SNN 之一。
- [`网络结构`](README.zh-CN.md#4--网络架构) · QKFormer: Hierarchical Spiking Transformer using Q-K Attention (**NeurIPS 2024**). \[[paper](https://arxiv.org/abs/2403.16552)\]\[[code](https://github.com/zhouchenlin2096/QKFormer)\]
  > 线性复杂度的二值 Q-K 注意力与层级金字塔，首次让直接训练 SNN 在 ImageNet 上超过 85%。
- [`网络结构`](README.zh-CN.md#4--网络架构) · SpikingResformer: Bridging ResNet and Vision Transformer in SNNs (**CVPR 2024**). \[[paper](https://arxiv.org/abs/2403.14302)\]\[[code](https://github.com/xyshi2000/SpikingResformer)\]
  > 将 ResNet 多阶段骨干与双脉冲自注意力 DSSA 结合，以更少参数与更低能耗取得高精度。
- [`网络结构`](README.zh-CN.md#4--网络架构) · TIM: An Efficient Temporal Interaction Module for Spiking Transformer (**IJCAI 2024**). \[[paper](https://arxiv.org/abs/2401.11687)\]
  > 轻量卷积模块，把前一时间步信息注入注意力矩阵，增强脉冲 Transformer 的时序建模。
- [`网络结构`](README.zh-CN.md#4--网络架构) · A Graph is Worth 1-bit Spikes: Graph Contrastive Learning Meets SNNs (SpikeGCL) (**ICLR 2024**). \[[paper](https://arxiv.org/abs/2305.19306)\]\[[code](https://github.com/EdisonLeeeee/SpikeGCL)\]
  > 用脉冲图对比学习得到 1-bit 二值图表示，约 32 倍存储压缩且精度可比。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Dynamic Spiking Graph Neural Networks (Dy-SIGN) (**AAAI 2024**). \[[paper](https://arxiv.org/abs/2401.05373)\]
  > 针对动态脉冲图网络的信息损失，提出隐式微分与信息补偿方案。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spiking Denoising Diffusion Probabilistic Models (SDDPM) (**WACV 2024**). \[[paper](https://arxiv.org/abs/2306.17046)\]\[[code](https://github.com/SageCao1125/SDDPM)\]
  > 用脉冲 U-Net 骨干把扩散模型引入 SNN，采样质量（FID）媲美甚至超过 ANN 版 DDPM。
- [`网络结构`](README.zh-CN.md#4--网络架构) · SDiT: Spiking Diffusion Model with Transformer (**arXiv 2024**). \[[paper](https://arxiv.org/abs/2402.11588)\]
  > 用脉冲 Transformer 替代 U-Net 的脉冲扩散模型，实现更高质量、更低成本的图像生成。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spiking Generative Adversarial Network with Attention Scoring Decoding (**Neural Networks 2024**). \[[paper](https://arxiv.org/abs/2305.10246)\]
  > 为脉冲 GAN 加入注意力打分解码器，从脉冲特征生成更高保真度图像。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikingBERT: Distilling BERT to Train Spiking Language Models Using Implicit Differentiation (**AAAI 2024**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/28975)\]
  > 受生物启发的脉冲 BERT，用平衡态脉冲发放率的隐式微分训练，把 SNN 带入自然语言理解。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms (**ICML 2024**). \[[paper](https://arxiv.org/abs/2406.03287)\]\[[code](https://github.com/Xingrun-Xing/SpikeLM)\]
  > 提出弹性双向脉冲机制，首次用全脉冲模型统一处理判别式与生成式语言任务。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikeLLM: Scaling up SNNs to Large Language Models via Saliency-Based Spiking (**arXiv 2024**). \[[paper](https://arxiv.org/abs/2407.04752)\]
  > 首个 7B–70B 规模的脉冲大模型，用广义 IF 神经元与显著性脉冲超越量化基线。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN (**ICML 2024**). \[[paper](https://arxiv.org/abs/2406.03470)\]\[[code](https://github.com/Intelligent-Computing-Research-Group/SpikeZIP-TF)\]
  > 将量化 Transformer 无损转换为 SNN，在视觉与语言上把与 ANN 的精度差距抹平。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Darwin3: A Large-Scale Neuromorphic Chip with a Novel ISA and On-Chip Learning (**National Science Review 2024**). \[[paper](https://arxiv.org/abs/2312.17582)\]
  > 浙大潘纲团队的大规模数字类脑芯片，具专用 10 指令集与片上学习，单芯片可支持约 235 万神经元。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Intel Hala Point — 1.15B-neuron Loihi 2 system (**Intel 2024**). \[[link](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system)\]
  > 集成 1152 颗 Loihi 2 → 11.5 亿神经元、1280 亿突触、14 万核，约 2.6 kW；Intel 在 2024 年发布时称其为全球最大神经形态系统。
- [`应用`](README.zh-CN.md#7--应用) · SpikePoint: An Efficient Point-based SNN for Event-Camera Action Recognition (**ICLR 2024**). \[[paper](https://arxiv.org/abs/2310.07189)\]
  > 直接处理原始事件点云（不转帧），用约 ANN 0.3% 的参数取得动作识别最佳性能。
- [`应用`](README.zh-CN.md#7--应用) · Integer-Valued Training and Spike-Driven Inference SNN for Object Detection (SpikeYOLO) (**ECCV 2024**). \[[paper](https://arxiv.org/abs/2407.20708)\]\[[code](https://github.com/BICLab/SpikeYOLO)\]
  > ECCV 最佳论文候选，训练用整数、推理用脉冲，在 COCO/Gen1 上大幅提升 SNN 检测精度。
- [`应用`](README.zh-CN.md#7--应用) · Accurate and Efficient Event-Based Semantic Segmentation Using Adaptive Spiking Encoder-Decoder (**IEEE TNNLS 2024**). \[[paper](https://arxiv.org/abs/2304.11857)\]
  > 深层脉冲编解码网络，实现事件流上准确且低功耗的语义分割。
- [`应用`](README.zh-CN.md#7--应用) · Autonomous Driving with Spiking Neural Networks (SAD) (**NeurIPS 2024**). \[[paper](https://arxiv.org/abs/2405.19687)\]\[[code](https://github.com/ridgerchu/SAD)\]
  > 首个端到端全脉冲自动驾驶系统（感知-预测-规划），在 nuScenes 上取得有竞争力的表现。
- [`应用`](README.zh-CN.md#7--应用) · VPRTempo: A Fast Temporally-Encoded SNN for Visual Place Recognition (**ICRA 2024**). \[[paper](https://arxiv.org/abs/2309.10225)\]\[[code](https://github.com/QVPR/VPRTempo)\]
  > 时间编码的 SNN 视觉地点识别，分钟级训练、CPU 上 >50Hz，可作 SLAM 闭环/定位模块。
- [`应用`](README.zh-CN.md#7--应用) · Fully Spiking Actor Network with Intra-Layer Connections for Reinforcement Learning (**IEEE TNNLS 2024**). \[[paper](https://arxiv.org/abs/2401.05444)\]
  > 完全脉冲的 actor（无浮点矩阵乘），用非脉冲中间神经元电压与层内连接，可直接部署到神经形态芯片。
- [`应用`](README.zh-CN.md#7--应用) · Learning Delays in SNNs using Dilated Convolutions with Learnable Spacings (**ICLR 2024**). \[[paper](https://openreview.net/forum?id=4r2ybzJnmN)\]\[[code](https://github.com/Thvnvtos/SNN-delays)\]
  > 用带可学习间距的膨胀卷积学习突触延迟，在 SHD/SSC 脉冲音频基准上取得最佳。
- [`应用`](README.zh-CN.md#7--应用) · Efficient and Effective Time-Series Forecasting with Spiking Neural Networks (**ICML 2024**). \[[paper](https://arxiv.org/abs/2402.01533)\]\[[code](https://github.com/microsoft/SeqSNN)\]
  > 提出带专门时间编码的脉冲框架，使 SNN 在时间序列预测上具备竞争力。
- [`应用`](README.zh-CN.md#7--应用) · An Efficient Intrusion Detection Model Based on Convolutional Spiking Neural Network (**Scientific Reports 2024**). \[[paper](https://www.nature.com/articles/s41598-024-57691-x)\]
  > 用卷积 SNN 做网络入侵检测，借助脉冲稀疏性高效识别异常与攻击。
- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) · On the Intrinsic Structures of Spiking Neural Networks (**JMLR 2024**). \[[paper](https://jmlr.org/papers/volume25/23-1526/23-1526.pdf)\]
  > 从理论上分析脉冲特有结构（时序复位、阈值）如何塑造 SNN 的逼近与泛化能力。

<details>
<summary><b>当年另有 72 篇</b> — 当年全量索引，每篇一句话</summary>

- Direct Training High-Performance Deep Spiking Neural Networks: A Review of Theories and Methods (**Frontiers in Neuroscience 2024**) [[paper](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1383844/full)] [[arxiv](https://arxiv.org/abs/2405.04289v2)]
  > 系统梳理基于代理梯度的直接训练路线：脉冲神经元模型、残差与 Transformer 架构、软件框架、神经形态硬件及应用与趋势。
- SpikedAttention: Training-Free and Fully Spike-Driven Transformer-to-SNN Conversion with Winner-Oriented Spike Shift for Softmax Operation (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=fs28jccJj5)]
  > 免训练地把已训练好的 Swin Transformer 与 BERT 转换为全脉冲驱动 SNN，用 winner-oriented 脉冲移位实现 softmax，无需改动注意力结构。
- Spiking Graph Neural Network on Riemannian Manifolds (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=VKt0K3iOmO)]
  > 在测地完备的黎曼流形上定义脉冲神经元，以流形微分取代 BPTT，既保留图的结构几何又缓解高时延问题。
- Rethinking the Dynamics of Spiking Neural Networks (**NeurIPS 2024**) [[paper](https://neurips.cc/virtual/2024/poster/96543)]
  > 将初始膜电位设为可学习参数，解锁零初值无法产生的放电模式，并配合末时间步读出与标签平滑 TET 损失重整优化目标。
- Long-Range Feedback Spiking Network Captures Dynamic and Static Representations of the Visual Cortex under Movie Stimuli (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=bxDok3uaK6)] [[code](https://github.com/Grasshlw/SNN-Neural-Similarity-Movie)]
  > 在脉冲网络中引入跨脑区的长程自上而下反馈，对小鼠视觉皮层在长时程电影刺激下的动态与静态表征相似度更高。
- Take A Shortcut Back: Mitigating the Gradient Vanishing for Training Spiking Neural Networks (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=xjyU6zmZD7)]
  > 让梯度从损失直达浅层，缓解代理梯度在深层脉冲网络中的消失问题，并按训练轮次动态调节捷径与主路径的权重比例。
- Advancing Training Efficiency of Deep Spiking Neural Networks through Rate-based Backpropagation (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2410.11488)] [[code](https://github.com/Tab-ct/rate-based-backpropagation)]
  > 以平均发放率而非逐时间步的时序导数做反向传播，精简 BPTT 计算图以降低训练显存与算力，同时保持与 BPTT 相当的精度。
- Latent Diffusion for Neural Spiking Data (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=ZX6CEo1Wtv)]
  > 用带 S4 层的自编码器把离散脉冲记录压成连续隐空间，再在其上训练条件扩散模型，生成可变长度、行为条件化的群体放电数据。
- Exact Gradients for Stochastic Spiking Neural Networks Driven by Rough Signals (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=mCWZj7pa0M)]
  > 以粗糙路径理论将随机脉冲网络建模为带事件跳变的随机微分方程，导出轨迹与放电时刻的精确梯度，配套可自动微分求解器。
- Spatio-Temporal Interactive Learning for Efficient Image Reconstruction of Spiking Cameras (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=S4ZqnMywcM)]
  > 从脉冲相机的二值脉冲流重建图像时，将帧间运动对齐与帧内特征滤波以由粗到细的方式交互进行，替代逐步串行的重建流水线。
- Slack-Free Spiking Neural Network Formulation for Hypergraph Minimum Vertex Cover (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=4A5IQEjG8c)]
  > 求解超图最小顶点覆盖时绕开 QUBO 重构与松弛变量，改用额外脉冲神经元做约束检查与修正，在神经形态硬件上稳定收敛到可行解。
- EnOF: Training Accurate Spiking Neural Networks via Enhancing the Output Feature Representation (**NeurIPS 2024**) [[paper](https://openreview.net/pdf/5a4dfaf8dc6861efa8e8356b3bd86743ab98838d.pdf)]
  > 把最后一层 LIF 换成 ReLU，以极小额外开销得到全精度输出特征，并用 KL 散度蒸馏损失将其与 ANN 教师特征对齐。
- Spiking Token Mixer: A event-driven friendly Former structure for spiking neural networks (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=iYcY7KAkSy)] [[code](https://github.com/brain-intelligence-lab/STMixer_demo)]
  > 仅用卷积、全连接与残差通路搭出类 Transformer 的 token 混合结构，去掉两个脉冲矩阵相乘，使网络可部署到事件驱动异步芯片。
- SpGesture: Source-Free Domain-adaptive sEMG-based Gesture Recognition with Jaccard Attentive Spiking Neural Network (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2405.14398)] [[code](https://github.com/guoweiyu/SpGesture/)]
  > 把膜电位当作记忆列表，将无源域自适应引入脉冲神经网络，并用脉冲 Jaccard 注意力提升 sEMG 手势识别对分布漂移的鲁棒性。
- Spiking Transformer with Experts Mixture (**NeurIPS 2024**) [[paper](https://openreview.net/pdf/35a5bc54de368426f66605d8e3f447638863888a.pdf)]
  > 让专家与路由器都输出脉冲序列，二者逐元素相乘即得到动态稀疏的条件计算，从而把混合专家机制以脉冲驱动方式引入脉冲 Transformer。
- FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=TuCQdBo4NC)] [[code](https://github.com/zju-bmi-lab/FEEL_SNN)]
  > 在不同时间步编码不同频段的输入，并让各神经元自行进化膜电位泄漏因子，在保留原始信息的同时抑制不同频段噪声。
- Spiking Neural Network as Adaptive Event Stream Slicer (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2410.02249)]
  > 用低功耗脉冲网络自适应决定事件流的切分时刻，以位置感知损失调制神经元状态，并借下游 ANN 的反馈更新切分策略。
- Advancing Spiking Neural Networks for Sequential Modeling with Central Pattern Generators (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2405.14362)] [[code](https://github.com/microsoft/SeqSNN)]
  > 从中枢模式发生器的膜电位动力学导出脉冲形式的位置编码，证明正弦编码只是其特解，使脉冲网络可胜任时序预测与文本分类。
- Q-SNNs: Quantized Spiking Neural Networks (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3681186)]
  > 同时量化突触权重与膜电位，并用受信息熵启发的权重-脉冲双重调节弥补压缩损失，压缩模型体积以适配低功耗边缘设备。
- RSC-SNN: Exploring the Trade-off Between Adversarial Robustness and Accuracy in Spiking Neural Networks via Randomized Smoothing Coding (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3680639)] [[code](https://github.com/KemingWu/RSC-SNN)]
  > 把脉冲网络的对抗鲁棒性归因于 Poisson 编码，论证其与随机平滑等价，并通过调节编码噪声在鲁棒性与精度之间取舍。
- Reversing Structural Pattern Learning with Biologically Inspired Knowledge Distillation for Spiking Neural Networks (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/pdf/10.1145/3664647.3680655)]
  > 用进化式规则从零构建脉冲网络拓扑，将反向知识蒸馏与连接剪枝结合，训练中动态调整突触连接以削减结构冗余。
- Towards High-performance Spiking Transformers from ANN to SNN Conversion (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3680620)] [[code](https://github.com/h-z-h-cell/Transformer-to-SNN-ECMT)]
  > 用期望补偿模块借助此前时间步的输出还原非线性模块的期望值，再以多阈值神经元与并行参数归一化压缩转换所需时间步。
- Towards Low-latency Event-based Visual Recognition with Hybrid Step-wise Distillation Spiking Neural Networks (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3680832)] [[code](https://github.com/hsw0929/HSD)]
  > 解耦事件帧数量与脉冲网络时间步：训练阶段用更多事件帧、推理阶段用更少，并以逐时间步蒸馏对齐各步输出分布以降低延迟。
- Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection (**ECCV 2024**) [[paper](https://arxiv.org/pdf/2407.20708)] [[code](https://github.com/BICLab/SpikeYOLO)]
  > 将 YOLO 精简为元 SNN 模块，训练时激活整数值、推理时靠扩展虚拟时间步回到脉冲驱动，缓解膜电位量化误差对检测的影响。
- Spiking Wavelet Transformer (**ECCV 2024**) [[paper](https://arxiv.org/pdf/2403.11138)] [[code](https://github.com/bic-L/Spiking-Wavelet-Transformer)]
  > 以稀疏小波 token 混合器取代自注意力，配合卷积与逐点分支并引入负脉冲动力学，在无乘法的脉冲驱动下捕捉边缘等高频成分。
- Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05068.pdf)] [[code](https://github.com/kiritozc/MPIS-SNNs)]
  > 借鉴平衡模型训练脉冲网络：前向让多条融合的并行隐式流同时收敛到平衡点，反向仅需单时间步模拟，免去存储大量激活值。
- Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08133.pdf)]
  > 依据膜电位梯度、阈值回溯梯度与放电效率自适应调节发放行为，使神经元在事件相机输入波动下保持稳态，同时降低功耗。
- BKDSNN: Enhancing the Performance of Learning-based Spiking Neural Networks Training with Blurred Knowledge Distillation (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06649.pdf)] [[code](https://github.com/Intelligent-Computing-Research-Group/BKDSNN)]
  > 对末层前的 SNN 特征图随机模糊以复原并模仿 ANN 教师特征，并与 logits 蒸馏结合，缩小代理梯度训练带来的精度差距。
- Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09164.pdf)]
  > 将三值事件取值松弛为概率采样，在稀疏范数约束下直接对原始事件流做定向对抗攻击，暴露栅格化之前环节的安全隐患。
- EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07766.pdf)] [[code](https://github.com/Windere/EAS-SNN)]
  > 用带时序记忆的循环卷积 SNN 端到端学习事件采样策略，并以残差膜电位 Dropout 与脉冲感知训练稳定膜电位分布，所需参数与时间步更少。
- Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05843.pdf)]
  > 把事件体素逐层编码为脉冲隐表示，以网络深度逼近迭代收缩阈值算法的不动点，再经 U 形脉冲解码器重建灰度视频，提升能效。
- EC-SNN: Splitting Deep Spiking Neural Networks on Edge Devices (**IJCAI 2024**) [[code](https://github.com/AmazingDD/EC-SNN)]
  > 结合通道剪枝把深层 SNN 切分为若干子模型，分布到多台边缘设备并行执行，在保持精度的同时降低单设备时延与能耗。
- One-step Spiking Transformer with a Linear Complexity (**IJCAI 2024**)
  > 通过时域压缩与补偿模块把时间步降到 1，并用脉冲线性变换替代浮点注意力运算，将复杂度与浮点乘加开销降到线性。
- Learning a Spiking Neural Network for Efficient Image Deraining (**IJCAI 2024**) [[code](https://github.com/MingTian99/ESDNet)]
  > 利用雨纹像素触发更强脉冲响应的特性，在脉冲残差块中以注意力调制膜电位，缓解二值激活信息损失，并以代理梯度直接训练。
- LitE-SNN: Designing Lightweight and Efficient Spiking Neural Network through Spatial-Temporal Compressive Network Search and Joint Optimization (**IJCAI 2024**) [[paper](https://arxiv.org/pdf/2401.14652)]
  > 把剪枝、混合精度量化与时间步数目一并纳入自动架构搜索空间，在计算开销约束下联合优化网络结构与时空压缩策略。
- Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/35073)]
  > 借助突触延迟把关系属性编码进脉冲发放时刻，以稀疏事件驱动的动力学把知识图谱推理表述为神经化的路径计算。
- Towards efficient deep spiking neural networks construction with spiking activity based pruning (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33505)]
  > 以卷积核的脉冲发放活跃度作为结构化剪枝依据，在训练中动态剪除并再生通道，使稀疏结构随任务自适应调整而非一次定死。
- Autaptic Synaptic Circuit Enhances Spatio-temporal Predictive Learning of Spiking Neural Networks (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33269)]
  > 借鉴自突触环路，在脉冲神经元中引入两条可学习的自反馈通路，增强时间记忆与空间协同，并缓解梯度消失问题。
- Robust Stable Spiking Neural Networks (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33217)]
  > 从非线性系统稳定性视角刻画膜电位扰动动力学，并改造 LIF 神经元以抑制扰动幅度，提升 SNN 在噪声与对抗攻击下的鲁棒性。
- NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33481)]
  > 以在线的前向时间学习替代 BPTT 展开，将梯度拆为空间项与源自神经元动力学的时间项，免去逐时间步保存中间状态。
- High-Performance Temporal Reversible Spiking Neural Networks with O(L) Training Memory and O(1) Inference Cost (**ICML 2024**) [[paper](https://arxiv.org/pdf/2405.16466)]
  > 关闭多数脉冲神经元的时间动力学，仅在少数神经元间构建时间可逆交互，训练无需缓存各时间步激活，推理开销与时间步解耦。
- Towards Efficient Spiking Transformer: a Token Sparsification Framework for Training and Inference Acceleration (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/32674)]
  > 用逐时间步的锚点 token 统一筛选重要 token，并对注意力图做时间步内与跨时间步对齐，加速脉冲 Transformer 训练并降低能耗。
- Sign Gradient Descent-based Neuronal Dynamics: ANN-to-SNN Conversion Beyond ReLU Network (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33242)]
  > 将积分发放动力学解释为次梯度优化，据此设计 signGD 神经元以逼近 ReLU 之外的非线性，在低时间步下完成 ConvNeXt、MLP-Mixer、ResMLP 的转换。
- Enhancing Adversarial Robustness in SNNs with Sparse Gradients (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/34066)]
  > 揭示随机扰动与对抗扰动的鲁棒性差距受输入梯度稀疏度约束，据此正则化梯度稀疏度来训练，图像与事件相机数据均适用。
- Are Conventional SNNs Really Efficient? A Perspective from Network Quantization (**CVPR 2024**) [[paper](https://arxiv.org/pdf/2311.10802)]
  > 把时间步等同于激活量化位宽，用 Bit Budget 取代 SynOps 估算能耗，并指出把预算投向脉冲模式与权重量化比拉长时间步更划算。
- SFOD: Spiking Fusion Object Detector (**CVPR 2024**) [[paper](https://arxiv.org/pdf/2403.15192)] [[code](https://github.com/yimeng-fan/SFOD)]
  > 在脉冲主干中首次融合多尺度特征图用于事件相机目标检测，并配套优化脉冲解码策略与损失函数，在 GEN1 数据集上验证。
- SGLFormer: Spiking Global-Local-Fusion Transformer with high performance (**Frontiers in Neuroscience 2024**) [[paper](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1371290/full)] [[code](https://github.com/ZhangHanN1/SGLFormer)]
  > 将卷积式局部提取与全局脉冲 Transformer 块交替堆叠，修复 maxpooling 处的梯度回传阻塞，并在分类头以时空块聚合空间与时间特征。
- Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework (**ICLR 2024**) [[paper](https://openreview.net/forum?id=eoSeaK4QJo&referrer=%5Bthe%20profile%20of%20Zecheng%20Hao%5D(%2Fprofile%3Fid%3D~Zecheng_Hao1))]
  > 把非结构化权重剪枝与非结构化神经元剪枝结合，同时利用突触与神经元两级稀疏，直接减少神经形态硬件上的突触运算量。
- Online Stabilization of Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/forum?id=CIj1CVbkpr)]
  > 为省内存的在线训练补上批归一化式收益：用在线脉冲重归一化对齐训练与测试参数，并用阈值稳定器稳定发放率。
- SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition (**ICLR 2024**) [[paper](https://arxiv.org/pdf/2310.07189.pdf)]
  > 直接以点云形式处理原始事件流而非转成帧，保留事件相机的稀疏性，并用单阶段结构同时提取全局与局部特征。
- Spatio-Temporal Approximation: A Training-Free SNN Conversion for Transformers (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=XrunSYwoLr)]
  > 免训练地把预训练 Transformer 转为 SNN：用通用群算子在空间维近似非线性，用时间校正自注意力层估计并修正脉冲乘法。
- Sparse Spiking Neural Network: Exploiting Heterogeneity in Timescales for Pruning Recurrent SNN (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=0jsfesDZDq)]
  > 在任务训练之前就对随机初始化的循环 SNN 剪枝，以 Lyapunov 指数与谱图稀疏化保证剪枝后稳定，得到异质时间尺度的稀疏网络。
- Threaten Spiking Neural Networks through Combining Rate and Temporal Information (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=xv8iGxENyI)] [[code](https://github.com/hzc1208/HART_Attack)]
  > 先分别量化 SNN 中保留的发放率信息与时间信息，再把两者融合为可动态调节配比的混合对抗扰动，暴露更强的攻击面。
- TAB: Temporal Accumulated Batch Normalization in Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/forum?id=k1wlmtPGLq&noteId=p5M9gOLAOf)]
  > 用截至当前时间步的累积统计量做批归一化，使其与膜电位的累积动态对齐，缓解直接训练中沿时间维的协变量偏移。
- Certified Adversarial Robustness for Rate Encoded Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/forum?id=5bNYf0CqxY)]
  > 把发放率编码等价视作随机平滑，从而给出脉冲分类器在 l1 范数扰动下的可证明鲁棒性界，并配套面向率编码的对抗训练算法。
- Bayesian Bi-clustering of Neural Spiking Activity with Latent Structures (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=ZYm1Ql6udy)]
  > 用非参数贝叶斯模型对多脑区放电数据做神经元与时段的双向聚类，神经元簇由潜在轨迹界定，时段由同步局部线性动力学界定。
- Adaptive deep spiking neural network with global-local learning via balanced excitatory and inhibitory mechanism (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=wpnlc2ONu0)]
  > 用兴奋-抑制机制动态调节网络连接度，并据此在局部学习与全局学习之间切换，兼顾全局学习的精度与局部学习的低能耗。
- Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks (**ICLR 2024**) [[paper](https://arxiv.org/pdf/2402.11984.pdf)] [[code](https://github.com/pkuxmq/HLOP-SNN)]
  > 在侧向连接上用 Hebbian/反 Hebbian 学习提取活动迹的主子空间，再把权重更新投影到其正交方向，以近乎无遗忘的方式持续学习新任务。
- A Progressive Training Framework for Spiking Neural Networks with Learnable Multi-hierarchical Model (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=g52tgL8jy6)] [[code](https://github.com/hzc1208/STBP_LMH)]
  > 以可学习的膜相关因子推广 LIF 神经元，动态调节历史与当前信息的提取比例，并给出涵盖混合训练与时间切片在线训练的渐进式方案。
- LMUFormer: Low Complexity Yet Powerful Spiking Model With Legendre Memory Units (**ICLR 2024**) [[paper](https://arxiv.org/pdf/2402.04882.pdf)] [[code](https://github.com/zeyuliu1037/LMUFormer)]
  > 为 Legendre Memory Unit 加入卷积式 patch 嵌入与卷积通道混合器，并给出脉冲版本，在保持流式推理的同时逼近 Transformer 的序列建模精度。
- Spike-driven Transformer V2: Meta Spiking Neural Network Architecture Inspiring the Design of Next-generation Neuromorphic Chips (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=1SIBN5Xyw7)] [[code](https://github.com/BICLab/Spike-Driven-Transformer-V2)]
  > 把 Spike-driven Transformer 抽象为元架构，网络中只保留稀疏加法，用一个直接训练的骨干同时支撑分类、检测与分割，并为神经形态芯片设计提供参照。
- Can we get the best of both Binary Neural Networks and Spiking Neural Networks for Efficient Computer Vision? (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=lGUyAuuTYZ)] [[code](https://github.com/godatta/Ultra-Low-Latency-SNN)]
  > 以单极性二值激活把 SNN 的稀疏性与 BNN 的精度结合起来，去掉时间维度，从而避免多时间步带来的延迟与能耗。
- A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=LnLySuf1vp)] [[code](https://github.com/EdisonLeeeee/SpikeGCL)]
  > 将图节点编码为稀疏的 1-bit 脉冲表示用于对比学习，并以分块训练缓解梯度消失，在压缩存储的同时保持与全精度相当的表达能力。
- Ternary Spike: Learning Ternary Spikes for Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2312.06372.pdf)] [[code](https://github.com/yfguo91/Ternary-Spike)]
  > 把二值脉冲扩展为三值脉冲以提升信息容量且仍然免乘法，逐层学习脉冲幅值，并在推理时通过重参数化还原为标准三值形式。
- Memory-Efficient Reversible Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2312.07922.pdf)] [[code](https://github.com/mi804/RevSNN)]
  > 将可逆结构沿时间维度扩展，反向过程中重算中间激活与膜电位而非保存，使训练显存不随网络深度增长。
- Gated Attention Coding for Training High-performance and Efficient Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2308.06582.pdf)]
  > 用多维门控注意力前端取代直接编码，增强输入的时间动态，同时保持主干网络的脉冲驱动特性，便于神经形态硬件部署。
- Shrinking Your TimeStep: Towards Low-Latency Neuromorphic Object Recognition with Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2401.01912.pdf)]
  > 将网络分阶段并逐级缩减时间步以降低推理延迟，用时序变换模块平滑改变时间尺度，并加入多个早期分类器稳定代理梯度训练。
- An Efficient Knowledge Transfer Strategy for Spiking Neural Networks from Static to Event Domain (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2303.13077.pdf)] [[code](https://github.com/Brain-Cog-Lab/Transfer-for-DVS)]
  > 用域对齐损失加逐时间步事件特征的时空正则缩小静态图像与事件数据的分布差异，并以滑动策略逐步把图像输入替换为事件流。
- Brain-Inspired Spiking Neural Networks for Industrial Fault Diagnosis: A Survey, Challenges, and Opportunities [[paper](https://doi.org/10.48550/arXiv.2401.02429)]
  > 系统梳理脉冲神经网络在工业故障诊断中的应用，涵盖神经元与编码基础、现有诊断模型，并归纳该方向落地面临的挑战与机会。
- Scalable MatMul-free Language Modeling [[paper](https://arxiv.org/pdf/2406.02528)] [[code](https://github.com/ridgerchu/matmulfreellm)]
  > 从注意力与前馈层中彻底移除矩阵乘法，在最高 2.7B 参数规模上保持性能，大幅降低推理显存，并可映射到多芯片神经形态系统。
- SpikeNAS: A Fast Memory-Aware Neural Architecture Search Framework for Spiking Neural Network Systems [[paper](https://arxiv.org/pdf/2402.11322.pdf)]
  > 在给定内存预算下搜索 SNN 结构：先分析各类算子对精度的影响，再配合快速搜索与量化，缩短面向嵌入式部署的搜索时间。
- Astrocyte-Enabled Advancements in Spiking Neural Networks for Large Language Modeling [[paper](https://arxiv.org/pdf/2312.07625v2.pdf)]
  > 为脉冲单元耦合基于三方突触的星形胶质细胞调制状态，增强长时程依赖与记忆保持，在语言生成中兼顾低延迟与低内存占用。

</details>

### 2023

**精选**

- [`网络结构`](README.zh-CN.md#4--网络架构) ★ · Spikformer: When Spiking Neural Network Meets Transformer (**ICLR 2023**). \[[paper](https://arxiv.org/abs/2209.15425)\]\[[code](https://github.com/ZK-Zhou/spikformer)\]
  > 提出无 softmax 的脉冲自注意力 SSA（Q/K/V 皆为脉冲），是首个直接构建的脉冲视觉 Transformer。
- [`网络结构`](README.zh-CN.md#4--网络架构) ★ · Spike-driven Transformer (**NeurIPS 2023**). \[[paper](https://arxiv.org/abs/2307.01694)\]\[[code](https://github.com/BICLab/Spike-Driven-Transformer)\]
  > 纯脉冲驱动 Transformer，自注意力仅用掩码与稀疏加法（线性复杂度），注意力能耗降低最多 87 倍。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · DIET-SNN: Direct Input Encoding with Leakage and Threshold Optimization (**IEEE TNNLS 2023**). \[[paper](https://arxiv.org/abs/2008.03658)\]
  > 直接输入模拟像素并端到端学习泄漏与阈值，推广了"直接输入编码"范式。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · KLIF: An Optimized Spiking Neuron Unit for Tuning Surrogate Gradient Slope and Membrane Potential (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2302.09238)\]
  > 引入可学习缩放因子，训练中动态调整代理梯度曲线的斜率与宽度。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · Parallel Spiking Neurons with High Efficiency and Ability to Learn Long-Term Dependencies (PSN) (**NeurIPS 2023**). \[[paper](https://arxiv.org/abs/2304.12760)\]\[[code](https://github.com/fangwei123456/Parallel-Spiking-Neuron)\]
  > 去除复位以将神经元动力学改写为可并行形式，加速训练并学习长时依赖。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Bridging the Gap Between ANNs and SNNs by Calibrating Offset Spikes (**ICLR 2023**). \[[paper](https://arxiv.org/abs/2302.10685)\]
  > 指出"多发/少发一个脉冲"的偏移是转换残余误差主因，通过平移初始膜电位加以校正。
- [`训练方法`](README.zh-CN.md#3--训练方法) · A Unified Optimization Framework of ANN-SNN Conversion (**ICML 2023**). \[[paper](https://proceedings.mlr.press/v202/jiang23a.html)\]\[[code](https://github.com/HaiyanJiang/SNN_Conversion_unified)\]
  > 用 SlipReLU 统一"性能损失"与"转换误差"两种视角，首次实现单步可用的高性能转换。
- [`训练方法`](README.zh-CN.md#3--训练方法) · RMP-Loss: Regularizing Membrane Potential Distribution for Spiking Neural Networks (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2308.06787)\]
  > 加入正则损失把膜电位向脉冲取值聚拢，直接减小量化误差，几乎不增加推理开销。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Surrogate Module Learning: Reduce Gradient Error Accumulation in Training SNNs (**ICML 2023**). \[[paper](https://proceedings.mlr.press/v202/deng23d.html)\]
  > 引入替代模块搭建"捷径"回传更准的梯度，抑制逐层累积的梯度误差。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Towards Memory- and Time-Efficient Backpropagation for Training SNNs (SLTT) (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2302.14311)\]\[[code](https://github.com/qymeng94/SLTT)\]
  > 发现时间维反传贡献很小，剪掉这些路径使显存降 70% 以上、训练时间降 50% 以上。
- [`训练方法`](README.zh-CN.md#3--训练方法) · A Tandem Learning Rule for Effective Training and Rapid Inference of Deep SNNs (**IEEE TNNLS 2023**). \[[paper](https://arxiv.org/abs/1907.01167)\]\[[code](https://github.com/deepspike/tandem_learning)\]
  > 让 ANN 与 SNN 共享权重"串联"训练，用 ANN 传梯度、SNN 数脉冲，大幅降低推理开销。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Constructing Deep SNNs from ANNs with Knowledge Distillation (**CVPR 2023**). \[[paper](https://arxiv.org/abs/2304.05627)\]
  > 用 ANN 作教师，把特征与响应知识蒸馏到 SNN 学生，避免从零训练脉冲网络的高成本。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Membrane Potential Batch Normalization for Spiking Neural Networks (MPBN) (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2308.08359)\]\[[code](https://github.com/yfguo91/MPBN)\]
  > 在发放函数前对膜电位再加一层 BN，并通过重参数化折叠进阈值，推理零额外开销。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Masked Spiking Transformer (**ICCV 2023**). \[[paper](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_Masked_Spiking_Transformer_ICCV_2023_paper.html)\]\[[code](https://github.com/bic-L/Masked-Spiking-Transformer)\]
  > 基于 ANN-SNN 转换的 Transformer，用随机脉冲掩码剪除冗余脉冲，降能耗且不掉精度。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Attention Spiking Neural Networks (MA-SNN) (**IEEE TPAMI 2023**). \[[paper](https://arxiv.org/abs/2209.13929)\]\[[code](https://github.com/BICLab/Attention-SNN)\]
  > 提出多维（时间/通道/空间）注意力调制膜电位，实现更稀疏发放与更高精度。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Scaling Up Dynamic Graph Representation Learning via Spiking Neural Networks (SpikeNet) (**AAAI 2023**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/26034)\]\[[code](https://github.com/EdisonLeeeee/SpikeNet)\]
  > 用脉冲神经元替代 RNN，把动态图表示学习低成本扩展到百万级节点。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · Spiking Convolutional Neural Networks for Text Classification (**ICLR 2023**). \[[paper](https://openreview.net/forum?id=pgU3k7QXuz0)\]\[[code](https://github.com/Lvchangze/snn)\]
  > 用"转换+微调"把词向量编码为脉冲，文本分类逼近 ANN，且对抗鲁棒性更强。
- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) · SpikeBERT: A Language Spikformer Learned from BERT with Knowledge Distillation (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2308.15122)\]\[[code](https://github.com/Lvchangze/SpikeBERT)\]
  > 两阶段从 BERT 蒸馏到 Spikformer，在中英文文本分类上逼近 BERT 且能耗大幅降低。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · SENECA: Building a Fully Digital Neuromorphic Processor (**Front. Neurosci. 2023**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2023.1187252/full)\]
  > imec 的 RISC-V + 循环缓冲混合架构，在可编程性与效率间取得平衡，支持端侧学习。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · IBM NorthPole: Neural Inference at the Frontier of Energy, Space, and Time (**Science 2023**). \[[paper](https://www.science.org/doi/10.1126/science.adh1174)\]
  > IBM 存算一体类脑推理芯片，消除片外内存（严格说非脉冲，但为神经形态领域标志性架构）。
- [`应用`](README.zh-CN.md#7--应用) · Spiking PointNet: Spiking Neural Networks for Point Clouds (**NeurIPS 2023**). \[[paper](https://arxiv.org/abs/2310.06232)\]\[[code](https://github.com/DayongRen/Spiking-PointNet)\]
  > 首个用于三维点云的 SNN，用"少训练多推理"范式甚至超过对应的 ANN。
- [`应用`](README.zh-CN.md#7--应用) · Deep Directly-Trained Spiking Neural Networks for Object Detection (EMS-YOLO) (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2307.11411)\]\[[code](https://github.com/BICLab/EMS-YOLO)\]
  > 首个"直接训练"（非转换）的深层 SNN 检测器，用全脉冲残差块仅 4 个时间步逼近 ANN 精度。
- [`应用`](README.zh-CN.md#7--应用) · Adaptive-SpikeNet: Event-Based Optical Flow with Learnable Neuronal Dynamics (**ICRA 2023**). \[[paper](https://arxiv.org/abs/2209.11741)\]
  > 全脉冲光流网络，用可学习的神经元动力学解决脉冲消失问题，超过同等规模 ANN。
- [`应用`](README.zh-CN.md#7--应用) · Event-Based Human Pose Tracking by Spiking Spatiotemporal Transformer (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2303.09681)\]
  > 全脉冲时空 Transformer，从事件流做三维人体姿态跟踪，利用时间稀疏性提升效率。
- [`应用`](README.zh-CN.md#7--应用) · Deep Multi-Threshold Spiking-UNet for Image Processing (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2307.10974)\]\[[code](https://github.com/SNNresearch/Spiking-UNet)\]
  > 多阈值神经元的脉冲 U-Net，配合"转换+微调"流程，在分割/去噪上推理时间降约 90%。
- [`应用`](README.zh-CN.md#7--应用) · Neuromorphic Control of a Simulated 7-DOF Arm using Loihi (**Neuromorphic Comput. Eng. 2023**). \[[paper](https://iopscience.iop.org/article/10.1088/2634-4386/acb286)\]
  > 基于神经工程框架的全脉冲控制器，在 Loihi 上对 7 自由度机械臂做操作空间的位姿控制。
- [`应用`](README.zh-CN.md#7--应用) · A Convolutional Spiking Neural Network with Adaptive Coding for Motor-Imagery Classification (**Neurocomputing 2023**). \[[paper](https://www.sciencedirect.com/science/article/abs/pii/S0925231223005933)\]
  > 将带自适应脉冲编码的卷积 SNN 用于脑机接口的运动想象 EEG 解码。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · HoSNN: Adversarially-Robust Homeostatic SNNs with Adaptive Firing Thresholds (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2308.10373)\]
  > 用自适应阈值的稳态神经元自我镇定扰动，无需对抗训练即提升鲁棒性。
- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) · Expressivity of Spiking Neural Networks (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2308.08218)\]
  > 证明积分放电脉冲神经元的线性区域数随输入维度指数增长，表达力超过 ReLU 神经元。

<details>
<summary><b>当年另有 38 篇</b> — 当年全量索引，每篇一句话</summary>

- Direct Learning-Based Deep Spiking Neural Networks: A Review (**Frontiers in Neuroscience 2023**) [[paper](https://arxiv.org/pdf/2305.19725.pdf)]
  > 综述基于代理梯度的深层脉冲神经网络直接训练工作，按精度提升、效率提升与时序动态利用三条脉络归类，并梳理各自的开放挑战。
- Time series prediction and anomaly detection with recurrent spiking neural networks (**IJCNN 2023**) [[paper](https://ieeexplore.ieee.org/abstract/document/10191614)]
  > 为稀疏循环脉冲网络配套专门的编解码机制，实现时间序列预测与无监督异常检测，并给出可公平比较的计算开销核算方法。
- SpikingJelly: An open-source machine learning infrastructure platform for spike-based intelligence (**Science Advances 2023**) [[paper](https://www.science.org/doi/10.1126/sciadv.adi1480)] [[code](https://github.com/fangwei123456/spikingjelly)]
  > 将神经形态数据集预处理、建模、训练到芯片部署整合为全栈框架，借助多级继承与代码生成使深层 SNN 训练提速 11 倍。
- Parallel Spiking Neurons with High Efficiency and Long-term Dependencies Learning Ability (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2304.12760)] [[code](https://github.com/fangwei123456/Parallel-Spiking-Neuron)]
  > 去掉复位机制，将膜电位动态改写为非迭代形式以在时间步上并行仿真，并用 masked 与 sliding 变体适配逐步推理与变长序列。
- Temporal Conditioning Spiking Latent Variable Models of the Neural Response to Natural Visual Scenes (**NeurIPS 2023**) [[paper](https://arxiv.org/pdf/2306.12045.pdf)]
  > 以脉冲隐变量直接生成可与记录对齐的脉冲序列来建模自然视觉场景下的神经响应，用时间条件化操作取代固定时间滤波器。
- SEENN: Towards Temporal Spiking Early Exit Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=mbaN0Y0QTw)]
  > 把时间步数视为随输入而变的量：一种变体按置信度阈值提前退出，另一种用强化学习决定步数，降低平均推理时间步。
- EICIL: Joint Excitatory Inhibitory Cycle Iteration Learning for Deep Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=OMDgOjdqoZ)]
  > 将兴奋与抑制两种神经元行为嵌入同一循环迭代训练框架，扩展脉冲神经元的表示空间，让深层 SNN 的训练更贴近生物信号传递。
- Addressing the speed-accuracy simulation trade-off for adaptive spiking neurons (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=Ht79ZTVMsn)]
  > 重新推导 ALIF 神经元的递推结构以缩短串行依赖，使小离散步长下训练提速 50 倍以上，并能亚毫秒精度拟合真实皮层记录。
- Enhancing Adaptive History Reserving by Spiking Convolutional Block Attention Module in Recurrent Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=aGZp61S9Lj)]
  > 在循环脉冲网络中嵌入脉冲卷积块注意力模块 SCBAM，选择性调用空间与时间历史信息，在手势与时序数据上以更小内存取得更高精度。
- Trial matching: capturing variability with data-constrained spiking neural networks (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2306.03603)]
  > 用最优传输度量生成试次与真实试次的分布差异，将大型循环脉冲网络拟合到多脑区皮层记录，复现试次间变异并预测下颌运动。
- Evolving Connectivity for Recurrent Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://arxiv.org/pdf/2305.17650.pdf)]
  > 把权重训练改为对连接概率分布的搜索，用自然演化策略免梯度优化，得到稀疏布尔连接、硬件友好的 RSNN，可完成 17 自由度人形运动。
- SparseProp: Efficient Event-Based Simulation and Training of Sparse Recurrent Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=yzZbwQPkmP)]
  > 利用网络稀疏性以事件驱动方式惰性更新神经元状态，把每个脉冲的前向与反向开销从 O(N) 降到 O(log N)，支持精确仿真与 BPTT 训练。
- Exploring Loss Functions for Time-based Training Strategy in Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=8IvW2k5VeA)]
  > 把基于发放率的损失函数映射为基于时间的形式，并从理论上说明提供足够正向整体梯度的损失更利于时间编码的异步训练。
- Unleashing the Potential of Spiking Neural Networks with Dynamic Confidence (**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Unleashing_the_Potential_of_Spiking_Neural_Networks_with_Dynamic_Confidence_ICCV_2023_paper.pdf)]
  > 从脉冲网络的时序输出中解码置信度，为每个样本动态决定何时提前终止推理，在运行时按需削减时间步与延迟。
- Inherent Redundancy in Spiking Neural Networks	(**ICCV 2023**) [[paper](https://arxiv.org/abs/2308.08227)]
  > 把冗余噪声脉冲归因于脉冲网络的时空不变性，并用一对空间注意力子模块调整膜电位分布，有效降低发放率。
- Temporal-Coded Spiking Neural Networks with Dynamic Firing Threshold: Learning with Event-Driven Backpropagation (**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wei_Temporal-Coded_Spiking_Neural_Networks_with_Dynamic_Firing_Threshold_Learning_with_ICCV_2023_paper.pdf)]
  > 针对 TTFS 编码中脉冲过稀与因果集难求的问题引入动态发放阈值，使深层时间编码脉冲网络可用事件驱动方式直接训练。
- Efficient Converted Spiking Neural Network for 3D and 2D Classification	(**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Lan_Efficient_Converted_Spiking_Neural_Network_for_3D_and_2D_Classification_ICCV_2023_paper.pdf)]
  > 根据神经元激活状态自适应调整阈值并扩大脉冲输出范围，让 ANN 到 SNN 的转换在很少的时间步内同时适用于点云与图像分类。
- SSF: Accelerating Training of Spiking Neural Networks with Stabilized Spiking Flow (**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_SSF_Accelerating_Training_of_Spiking_Neural_Networks_with_Stabilized_Spiking_ICCV_2023_paper.pdf)]
  > 把每个神经元的输入输出在时间维上求平均得到稳定量，再经二者的映射关系直接回传梯度，摆脱时间纠缠带来的训练耗时。
- Spatial-Temporal Self-Attention for Asynchronous Spiking Neural Networks (**IJCAI 2023**) [[paper](https://www.ijcai.org/proceedings/2023/0344.pdf)]
  > 在时间与空间维度上联合计算特征依赖并加入时空相对位置偏置，使注意力不破坏脉冲网络的异步事件驱动传输特性。
- Learnable Surrogate Gradient for Direct Training Spiking Neural Networks (**IJCAI 2023**) [[paper](https://www.ijcai.org/proceedings/2023/0335.pdf)]
  > 通过可训练的衰减因子把代理梯度的宽度与膜电位分布挂钩，训练中自动调节宽度，缓解梯度消失与梯度失配。
- Enhancing Efficient Continual Learning with Dynamic Structure Development of Spiking Neural Networks (**IJCAI 2023**) [[paper](https://www.ijcai.org/proceedings/2023/0334.pdf)]
  > 为每个新任务动态生长神经元并剪除冗余单元，通过共享重叠结构复用旧知识，无需为每个任务维护子网络掩码。
- Adaptive Smoothing Gradient Learning for Spiking Neural Networks (**ICML 2023**) [[paper](https://openreview.net/pdf?id=GdkwSGTpbC)]
  > 将代理梯度的松弛程度设为可学习参数并注入随机脉冲噪声，让平滑的原型网络逐步演化为真正的 SNN，从而消除平滑误差。
- Surrogate Module Learning: Reduce the Gradient Error Accumulation in Training Spiking Neural Networks (**ICML 2023**) [[paper](https://openreview.net/pdf?id=zRkz4duLKp)] [[code](https://github.com/brain-intelligence-lab/surrogate_module_learning)]
  > 为深层 SNN 挂载代理模块以构建反传捷径，并用专门损失联合训练，抑制代理梯度误差在层间的逐层放大。
- Rate Gradient Approximation Attack Threats Deep Spiking Neural Networks (**CVPR 2023**) [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Bu_Rate_Gradient_Approximation_Attack_Threats_Deep_Spiking_Neural_Networks_CVPR_2023_paper.pdf)]
  > 利用 SNN 层间以发放率编码通信的特性来近似梯度并构造对抗攻击，可推广到不同 LIF 泄漏参数与输入编码，并有时间维扩展增强。
- Constructing Deep Spiking Neural Networks from Artificial Neural Networks with Knowledge Distillation (**CVPR 2023**) [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Xu_Constructing_Deep_Spiking_Neural_Networks_From_Artificial_Neural_Networks_With_CVPR_2023_paper.pdf)]
  > 以 ANN 为教师、SNN 为学生做联合训练与蒸馏，迁移丰富的特征信息，避开在不可导脉冲上从零训练深层网络。
- Heterogeneous neuronal and synaptic dynamics for spike-efficient unsupervised learning: Theory and design principles (**ICLR 2023**) [[paper](https://arxiv.org/pdf/2302.11618.pdf)]
  > 借助贝叶斯优化使神经元积分/弛豫与 STDP 动力学异质化，理论证明异质性可提升循环 SNN 的记忆容量并降低发放量。
- A Unified Framework of Soft Threshold Pruning (**ICLR 2023**) [[paper](https://openreview.net/forum?id=cCFqcrq0d8)] [[code](https://github.com/Yanqi-Chen/LATS)]
  > 将软阈值剪枝重构为求解隐式 L1 问题的 ISTA 过程，据此推出与学习率同步变化的阈值调度器，改善稀疏度与精度的权衡。
- Reducing ANN-SNN Conversion Error through Residual Membrane Potential (**AAAI 2023**) [[paper](https://arxiv.org/abs/2302.02091)] [[code](https://github.com/hzc1208/ANN2SNN_SRP)]
  > 将脉冲到达时序不同所致的不均匀误差分为四类，并用残差膜电位加以校正，使 ANN-SNN 转换在极少时间步下仍保持精度。
- Deep Spiking Neural Networks with High Representation Similarity Model Visual Pathways of Macaque and Mouse (**AAAI 2023**) [[paper](https://arxiv.org/abs/2303.06060)]
  > 在三种相似性度量下将深层 SNN 与 CNN、ViT 同猕猴和小鼠的神经记录对比，发现脉冲模型与生物视觉层级的表征更接近。
- ESL-SNNs: An Evolutionary Structure Learning Strategy for Spiking Neural Networks (**AAAI 2023**) [[paper](https://arxiv.org/pdf/2306.03693.pdf)]
  > 在训练过程中动态剪除并重新生长突触连接、始终保持结构稀疏度，实现从零训练稀疏 SNN，而非训练完成后再压缩。
- Exploring Temporal Information Dynamics in Spiking Neural Networks (**AAAI 2023**) [[paper](https://arxiv.org/pdf/2211.14406.pdf)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Exploring-Temporal-Information-Dynamics-in-Spiking-Neural-Networks)]
  > 用权重的 Fisher 信息量化各时间步的信息分布，揭示训练后信息向早期时间步集中的现象，并据此设计迭代剪枝准则。
- Complex Dynamic Neurons Improved Spiking Transformer Network for Efficient Automatic Speech Recognition(**AAAI 2023**) [[paper](https://arxiv.org/pdf/2302.01194.pdf)]
  > 在脉冲 Transformer 的序列输出后接入四类比 LIF 更复杂的神经元动力学，降低语音识别的音素错误率与计算开销，并提升鲁棒性。
- Spikingformer: Spike-driven Residual Learning for Transformer-based Spiking Neural Network [[paper](https://arxiv.org/abs/2304.11954)] [[code](https://github.com/zhouchenlin2096/Spikingformer)]
  > 将膜电位残差与脉冲自注意力融合，使骨干各层保持脉冲驱动，消除 Spikformer 残差结构残留的整数-浮点乘法，便于神经形态部署。
- Enhancing the Performance of Transformer-based Spiking Neural Networks by Improved Downsampling with Precise Gradient Backpropagation [[paper](https://arxiv.org/abs/2305.05954)] [[code](https://github.com/zhouchenlin2096/Spikingformer-CML)]
  > 把下采样模块重排为 ConvBN-MaxPooling-LIF，消除梯度反传的失真，在静态图像与神经形态数据集上均超过 Spikingformer 的精度。
- Training Full Spike Neural Networks via Auxiliary Accumulation Pathway [[paper](https://arxiv.org/pdf/2301.11929.pdf)]
  > 为全脉冲残差网络并联一条可拆卸的累积支路，补偿二值脉冲前传与反传中的信息损失，推理时移除以保持纯脉冲运算。
- MSS-DepthNet: Depth Prediction with Multi-Step Spiking Neural Network [[paper](https://arxiv.org/abs/2211.12156)]
  > 为事件相机深度估计重新设计脉冲残差块，并加入多维注意力与专用事件流编码，在 MVSEC 上超过同规模 ANN 且计算更省。
- Auto-Spikformer: Spikformer Architecture Search [[paper](https://arxiv.org/pdf/2306.00807.pdf)]
  > 用一次性超网搜索 Spikformer 的通道与模块配置，并进化优化脉冲神经元参数，以精度-能耗联合适应度剔除冗余、降低推理能耗。
- Advancing Spiking Neural Networks Towards Deep Residual Learning [[paper](https://arxiv.org/pdf/2112.08954.pdf)]
  > 让残差捷径走膜电位而非脉冲，并用块动力学等距理论证明梯度范数相等，把直接训练的 SNN 深度扩展到 482 层而不退化。

</details>

---

## 深度脉冲网络时代 — 代理梯度走向深层  <sub>(2018–2022)</sub>

### 2022

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Optimal ANN-SNN Conversion for High-Accuracy and Ultra-Low-Latency SNNs (QCFS) (**ICLR 2022**). \[[paper](https://arxiv.org/abs/2303.04347)\]\[[code](https://github.com/putshua/ANN_SNN_QCFS)\]
  > 训练 ANN 时用 QCFS 激活来贴合脉冲量化特性，仅需 4 步即可高精度。
- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Temporal Efficient Training of SNNs via Gradient Re-weighting (TET) (**ICLR 2022**). \[[paper](https://arxiv.org/abs/2202.11946)\]\[[code](https://github.com/Gus-Lab/temporal_efficient_training)\]
  > 对每个时间步都加监督损失以弥补替代梯度的"动量损失"，收敛更平坦、泛化更好，已成常用技巧。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks (**NeurIPS 2022**). \[[paper](https://openreview.net/forum?id=UmFSx2c4ubT)\]\[[code](https://github.com/Ikarosy/Gated-LIF)\]
  > 用可学习门控融合多种生物特性，扩大单个神经元的表达空间。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Optimized Potential Initialization for Low-Latency Spiking Neural Networks (**AAAI 2022**). \[[paper](https://arxiv.org/abs/2202.01440)\]
  > 把初始膜电位设为半阈值能最小化转换误差，使 SNN 在 32 步以内也高精度。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Training High-Performance Low-Latency SNNs by Differentiation on Spike Representation (DSR) (**CVPR 2022**). \[[paper](https://arxiv.org/abs/2205.00459)\]\[[code](https://github.com/qymeng94/DSR)\]
  > 把脉冲的发放率表示看成次可微映射并对其求导训练，绕开不可微问题，低延迟高精度。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Online Training Through Time for Spiking Neural Networks (OTTT) (**NeurIPS 2022**). \[[paper](https://arxiv.org/abs/2210.04195)\]\[[code](https://github.com/pkuxmq/OTTT-SNN)\]
  > 常数显存、无需展开时间的在线训练法，梯度呈三因子 Hebbian 形式，利于片上学习。
- [`训练方法`](README.zh-CN.md#3--训练方法) · RecDis-SNN: Rectifying Membrane Potential Distribution for Directly Training SNNs (**CVPR 2022**). \[[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Guo_RecDis-SNN_Rectifying_Membrane_Potential_Distribution_for_Directly_Training_Spiking_Neural_CVPR_2022_paper.html)\]
  > 用膜电位分布损失矫正分布偏移，缓解退化、饱和与梯度失配。
- [`训练方法`](README.zh-CN.md#3--训练方法) · IM-Loss: Information Maximization Loss for Spiking Neural Networks (**NeurIPS 2022**). \[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/010c5ba0cafc743fece8be02e7adb8dd-Abstract-Conference.html)\]\[[code](https://github.com/yfguo91/IM-Loss-Information-Maximization-Loss-for-Spiking-Neural-Networks)\]
  > 以最大化脉冲所携带的信息熵为目标，减小 0/1 量化造成的信息损失。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Real Spike: Learning Real-valued Spikes for Spiking Neural Networks (**ECCV 2022**). \[[paper](https://arxiv.org/abs/2210.06686)\]\[[code](https://github.com/yfguo91/Real-Spike)\]
  > 训练时用实值脉冲增强表达、推理时重参数化折回二值脉冲，精度提升而不增加推理成本。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Towards Ultra-Low-Latency SNNs for Vision and Sequential Tasks Using Temporal Pruning (**ECCV 2022**). \[[paper](https://doi.org/10.1007/978-3-031-20083-0_42)\]
  > 在训练中逐步"剪时间步"，把 SNN 推向单步推理，极致压缩延迟与能耗。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Temporal Effective Batch Normalization in Spiking Neural Networks (TEBN) (**NeurIPS 2022**). \[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/de2ad3ed44ee4e675b3be42aa0b615d0-Abstract-Conference.html)\]\[[code](https://github.com/ChaotengDuan/TEBN)\]
  > 为每个时间步用不同可学习权重重标定输入，平滑时序分布与优化曲面。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spiking Graph Convolutional Networks (SpikingGCN) (**IJCAI 2022**). \[[paper](https://arxiv.org/abs/2205.02767)\]\[[code](https://github.com/ZulunZhu/SpikingGCN)\]
  > 端到端地把图卷积编码为脉冲序列，为节点/图任务带来节能的 SNN 推理。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spiking-GAN: A Spiking Generative Adversarial Network Using Time-To-First-Spike Coding (**IJCNN 2022**). \[[paper](https://arxiv.org/abs/2106.15420)\]
  > 首个脉冲 GAN，用首脉冲时间编码与时域反传训练，实现超低能耗生成。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Fully Spiking Variational Autoencoder (FSVAE) (**AAAI 2022**). \[[paper](https://arxiv.org/abs/2110.00375)\]
  > 首个全脉冲变分自编码器，把隐变量采样为自回归伯努利脉冲序列，端到端以脉冲生成图像。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Neural Architecture Search for Spiking Neural Networks (SNASNet) (**ECCV 2022**). \[[paper](https://arxiv.org/abs/2201.10355)\]\[[code](https://github.com/Intelligent-Computing-Lab-Panda/Neural-Architecture-Search-for-Spiking-Neural-Networks)\]
  > 免训练 NAS，用初始化时的脉冲激活多样性选架构，并引入时序反馈连接。
- [`网络结构`](README.zh-CN.md#4--网络架构) · AutoSNN: Towards Energy-Efficient Spiking Neural Networks (**ICML 2022**). \[[paper](https://arxiv.org/abs/2201.12738)\]\[[code](https://github.com/nabk89/AutoSNN)\]
  > 脉冲感知的架构搜索，用同时兼顾精度与脉冲数的适应度，得到更准更省能的 SNN。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Differentiable Hierarchical and Surrogate Gradient Search for SNNs (SpikeDHS) (**NeurIPS 2022**). \[[paper](https://openreview.net/forum?id=Lr2Z85cdvB)\]\[[code](https://github.com/Huawei-BIC/SpikeDHS)\]
  > 可微地联合搜索单元/层结构与替代梯度函数。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · ReckOn: A 28 nm Sub-mm² Task-Agnostic Spiking Recurrent Neural Network Processor Enabling On-Chip Learning over Second-Long Timescales (**IEEE ISSCC 2022**). \[[paper](https://arxiv.org/abs/2208.09759)\]
  > Frenkel 与 Indiveri 的芯片以 e-prop 式片上学习，在秒级时间尺度上学习时序任务，功耗亚毫瓦。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · The BrainScaleS-2 Accelerated Neuromorphic System with Hybrid Plasticity (**Front. Neurosci. 2022**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2022.795876/full)\]
  > 将连续时间模拟神经元/突触电路与嵌入式 SIMD 处理器耦合，支持灵活的片上混合可塑性。
- [`应用`](README.zh-CN.md#7--应用) · Fusion-FlowNet: Energy-Efficient Optical Flow via Sensor Fusion and Spiking-Analog Networks (**ICRA 2022**). \[[paper](https://arxiv.org/abs/2103.10592)\]
  > 在脉冲-模拟混合网络中融合帧与事件，用更少参数与能耗估计稠密光流。
- [`应用`](README.zh-CN.md#7--应用) · StereoSpike: Depth Learning with a Spiking Neural Network (**IEEE Access 2022**). \[[paper](https://arxiv.org/abs/2109.13751)\]\[[code](https://github.com/urancon/StereoSpike)\]
  > 首个用全脉冲网络求解大规模稠密深度回归（双目事件），泛化甚至优于 ANN 版本。
- [`应用`](README.zh-CN.md#7--应用) · Event-Based Video Reconstruction via Potential-Assisted SNN (EVSNN) (**CVPR 2022**). \[[paper](https://arxiv.org/abs/2201.10943)\]\[[code](https://github.com/LinZhu111/EVSNN)\]
  > 首个用全 SNN 从事件重建灰度视频的框架，比 ANN 版高效约 19 倍。
- [`应用`](README.zh-CN.md#7--应用) · Spiking Transformers for Event-Based Single Object Tracking (STNet) (**CVPR 2022**). \[[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Zhang_Spiking_Transformers_for_Event-Based_Single_Object_Tracking_CVPR_2022_paper.html)\]
  > 将 Transformer（空间）与 SNN（时间）结合做事件跟踪，在多个事件跟踪数据集上取得最佳。
- [`应用`](README.zh-CN.md#7--应用) · Neuromorphic Adaptive Spiking CPG Towards Bio-Inspired Locomotion of Legged Robots (**Neurocomputing 2022**). \[[paper](https://arxiv.org/abs/2101.09709)\]
  > 在 SpiNNaker 上实现脉冲中枢模式发生器（CPG），依据传感反馈为足式机器人生成自适应步态。
- [`应用`](README.zh-CN.md#7--应用) · Human-Level Control through Directly-Trained Deep Spiking Q-Networks (DSQN) (**IEEE T-Cybernetics 2022**). \[[paper](https://arxiv.org/abs/2201.07211)\]\[[code](https://github.com/AptX395/Deep-Spiking-Q-Networks)\]
  > 直接训练的深层脉冲 Q 网络，以膜电位表示 Q 值，在多数 Atari 游戏上超过 ANN-DQN 且更鲁棒。
- [`应用`](README.zh-CN.md#7--应用) · Multiscale Dynamic Coding Improved Spiking Actor Network for Reinforcement Learning (MDC-SAN) (**AAAI 2022**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/19879)\]
  > 用多尺度动态神经编码改进脉冲 actor，提升连续控制性能。
- [`应用`](README.zh-CN.md#7--应用) · A Surrogate-Gradient Spiking Baseline for Speech Command Recognition (sparch) (**Front. Neurosci. 2022**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2022.865897/full)\]\[[code](https://github.com/idiap/sparch)\]
  > 面向 SHD/SSC/Google 语音命令的强力可复现代理梯度 SNN 基线与工具包。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Benchmarking Neuromorphic Hardware and Its Energy Expenditure (**Front. Neurosci. 2022**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2022.873935/full)\]
  > 提出公平衡量神经形态硬件能耗的方法与指标，揭示 SNN 能效对比中的陷阱。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · SNN-RAT: Robustness-Enhanced SNN through Regularized Adversarial Training (**NeurIPS 2022**). \[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9cf904c86cc5f9ac95646c07d2cfa241-Abstract-Conference.html)\]
  > 为脉冲表示推导 Lipschitz 常数并正则化，做鲁棒性增强的对抗训练。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Toward Robust Spiking Neural Network Against Adversarial Perturbation (**NeurIPS 2022**). \[[paper](https://arxiv.org/abs/2205.01625)\]
  > 提出 S-IBP/S-CROWN，首次将线性松弛验证引入 SNN，给出可认证鲁棒边界。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Adversarial Attacks on Spiking Convolutional Networks for Event-Based Vision (SpikeFool) (**Front. Neurosci. 2022**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2022.1068193/full)\]
  > 提出稀疏梯度攻击 SpikeFool，可在真实事件数据上欺骗脉冲卷积网络。
- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) · PC-SNN: Predictive Coding-Based Local Hebbian Plasticity Learning in SNNs (**arXiv 2022**). \[[paper](https://arxiv.org/abs/2211.15386)\]
  > 用局部 Hebbian 预测编码更新训练 SNN，以近似反传但无需全局误差传播。

<details>
<summary><b>当年另有 9 篇</b> — 当年全量索引，每篇一句话</summary>

- Neuromorphic Data Augmentation for Training Spiking Neural Networks [[paper](https://arxiv.org/abs/2203.06145)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/NDA_SNN)]
  > 把几何图像增广适配到事件数据上，缓解小规模神经形态数据集的过拟合，稳定训练，并首次支持 SNN 的无监督对比学习。
- State Transition of Dendritic Spines Improves Learning of Sparse Spiking Neural Networks [[paper](https://proceedings.mlr.press/v162/chen22ac.html)] [[code](https://github.com/Yanqi-Chen/STDS)]
  > 将权重重参数化为树突棘尺寸，用状态转换实现动态剪枝，并以生长阈值调节剪枝速度，避免训练后期在高稀疏度下崩溃。
- Exploring Lottery Ticket Hypothesis in Spiking Neural Networks [[paper](https://arxiv.org/abs/2207.01382)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Exploring-Lottery-Ticket-Hypothesis-in-SNNs)]
  > 验证深层 SNN 中存在高稀疏度的中奖彩票，并用仅由前几个时间步确定连接的 Early-Time 票，降低迭代幅值剪枝的搜索开销。
- A calibratable sensory neuron based on epitaxial VO2 for spike-based neuromorphic multisensory system [[paper](https://www.nature.com/articles/s41467-022-31747-w)] [[code](https://github.com/billyuanpku96/SNN-for-sensory-neuron)]
  > 用外延 VO2 制作人工感觉神经元，并加入校准电阻与缩放电阻，把光照、温度、压力和曲率统一编码为脉冲，改善器件间与循环间一致性。
- Training Spiking Neural Networks with Event-driven Backpropagation [[paper](https://openreview.net/forum?id=d4JmP1T45WE)] [[code](https://github.com/zhuyaoyu/SNN-event-driven-learning)]
  > 仅在脉冲发放时刻反传梯度而非逐时间步展开，证明全连接与卷积层的梯度和守恒，并用反向卷积核修正梯度的时序错配。
- Training Spiking Neural Networks with Local Tandem Learning (**NeurIPS 2022**) [[paper](https://arxiv.org/pdf/2210.04532.pdf)]
  > 让每层脉冲网络就地模仿预训练 ANN 的中间特征，逐层解耦训练以快速收敛，并支持在混合信号神经形态芯片上做片上校准。
- Biologically Inspired Dynamic Thresholds for Spiking Neural Networks (**NeurIPS 2022**) [[paper](https://arxiv.org/pdf/2206.04426.pdf)]
  > 依据神经元稳态，让阈值随平均膜电位上升、随去极化速率下降而动态调节，在含噪声的机器人避障与控制任务中更稳定。
- Optimal Conversion of Conventional Artificial Neural Networks to Spiking Neural Networks (**ICLR 2022**) [[paper](https://arxiv.org/pdf/2103.00476.pdf)] [[code](https://github.com/Jackn0/snn_optimal_conversion_pipeline)]
  > 把 ANN-SNN 转换误差递归分解为逐层求和，结合阈值平衡与软复位，用约十分之一的仿真时长逼近原 ANN 精度。
- Multi-Level Firing with Spiking DS-ResNet: Enabling Better and Deeper Directly-Trained Spiking Neural Networks (**IJCAI 2022**) [[paper](https://arxiv.org/pdf/2210.06386.pdf)]
  > 将神经元拆成多级发放以改善梯度传播，并用抑制静默的残差块实现离散脉冲恒等映射，缓解深层直训 SNN 的梯度消失与退化。

</details>

### 2021

**精选**

- [`神经元模型`](README.zh-CN.md#2--神经元模型) ★ · Incorporating Learnable Membrane Time Constant to Enhance Learning of SNNs (PLIF) (**ICCV 2021**). \[[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Fang_Incorporating_Learnable_Membrane_Time_Constant_To_Enhance_Learning_of_Spiking_ICCV_2021_paper.html)\]\[[code](https://github.com/fangwei123456/Parametric-Leaky-Integrate-and-Fire-Spiking-Neuron)\]
  > PLIF 让膜时间常数可学习，提升精度并降低对初始化的敏感度。
- [`网络结构`](README.zh-CN.md#4--网络架构) ★ · Deep Residual Learning in Spiking Neural Networks (SEW-ResNet) (**NeurIPS 2021**). \[[paper](https://arxiv.org/abs/2102.04159)\]\[[code](https://github.com/fangwei123456/Spike-Element-Wise-ResNet)\]
  > 脉冲逐元素残差块 SEW 实现恒等映射并克服梯度消失/爆炸，首次直接训练百层以上深度 SNN。
- [`网络结构`](README.zh-CN.md#4--网络架构) ★ · Going Deeper with Directly-Trained Larger SNNs (STBP-tdBN) (**AAAI 2021**). \[[paper](https://arxiv.org/abs/2011.05280)\]
  > 阈值相关的批归一化 tdBN 跨时间步平衡发放率，把直接训练的 SNN 从不足 10 层拓展到 50 层。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Neural Coding in Spiking Neural Networks: A Comparative Study for Robust Neuromorphic Systems (**Front. Neurosci. 2021**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2021.638474/full)\]
  > 系统对比率编码、时间、相位与突发编码在精度与鲁棒性上的表现。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Temporal-Coded Deep Spiking Neural Network with Easy Training and Robust Performance (**AAAI 2021**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/17329)\]
  > 论证非泄漏单脉冲时间编码最利于直接训练且鲁棒的深度 SNN。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Optimized Spiking Neurons Can Classify Images with High Accuracy through Temporal Coding with Two Spikes (FS neurons) (**Nature Machine Intelligence 2021**). \[[paper](https://www.nature.com/articles/s42256-021-00311-4)\]
  > 少脉冲（FS）神经元用约 2 个脉冲即可模拟 ANN 激活，实现高精度、超稀疏的时间编码。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · Neural Heterogeneity Promotes Robust Learning (**Nature Communications 2021**). \[[paper](https://www.nature.com/articles/s41467-021-26022-3)\]
  > 让神经元的时间常数多样且可学习，能提升精度与鲁棒性——为"异质性"提供了有原则的证据。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Optimal Conversion of Conventional ANNs to SNNs (**ICLR 2021**). \[[paper](https://openreview.net/forum?id=FZ1oTwcXchK)\]\[[code](https://github.com/Jackn0/snn_optimal_conversion_pipeline)\]
  > 将转换误差逐层分解，配合发放率归一化激活与最优阈值/偏移，显著缩短仿真步数。
- [`训练方法`](README.zh-CN.md#3--训练方法) · A Free Lunch From ANN: Towards Efficient, Accurate SNN Calibration (**ICML 2021**). \[[paper](https://proceedings.mlr.press/v139/li21d.html)\]\[[code](https://github.com/yhhhli/SNN_Calibration)\]
  > 只需少量样本做逐层"校准"即可修正转换误差，推广到 MobileNet/RegNet 等大模型。
- [`训练方法`](README.zh-CN.md#3--训练方法) · The Remarkable Robustness of Surrogate Gradient Learning for Instilling Complex Function in SNNs (**Neural Computation 2021**). \[[paper](https://doi.org/10.1162/neco_a_01367)\]\[[code](https://github.com/fzenke/randman)\]
  > 系统验证替代函数形状影响不大、但尺度很关键，为如何选替代梯度提供实证指南。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Differentiable Spike: Rethinking Gradient-Descent for Training SNNs (Dspike) (**NeurIPS 2021**). \[[paper](https://proceedings.neurips.cc/paper/2021/hash/c4ca4238a0b923820dcc509a6f75849b-Abstract.html)\]
  > 提出可自适应演化的可微替代函数族 Dspike，训练中更好地逼近真实梯度。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Training Feedback SNNs by Implicit Differentiation on the Equilibrium State (IDE) (**NeurIPS 2021**). \[[paper](https://arxiv.org/abs/2109.14247)\]\[[code](https://github.com/pkuxmq/IDE-FSNN)\]
  > 将反馈 SNN 的平均发放率视为不动点方程，用隐式微分求梯度，显存不随时间步增长。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Sparse Spiking Gradient Descent (**NeurIPS 2021**). \[[paper](https://arxiv.org/abs/2105.08810)\]\[[code](https://github.com/npvoid/SparseSpikingBackprop)\]
  > 利用脉冲的时空稀疏性做稀疏反传，训练最高加速 150 倍、显存降约 85%。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Accurate and Efficient Time-Domain Classification with Adaptive Spiking Recurrent Neural Networks (**Nature Machine Intelligence 2021**). \[[paper](https://doi.org/10.1038/s42256-021-00397-w)\]
  > 自适应脉冲神经元 + 替代梯度循环 SNN，在语音/手势上达 RNN 级精度且计算量低 1–3 个数量级。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Spiking Deep Residual Networks (**IEEE TNNLS 2021**). \[[paper](https://arxiv.org/abs/1805.01352)\]
  > 最早的"脉冲 ResNet"，通过缩放捷径与误差补偿构建首个 40 层以上且精度接近原网络的 SNN。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Revisiting Batch Normalization for Training Low-Latency Deep SNNs from Scratch (BNTT) (**Front. Neurosci. 2021**). \[[paper](https://arxiv.org/abs/2010.01729)\]\[[code](https://github.com/Intelligent-Computing-Lab-Panda/BNTT-Batch-Normalization-Through-Time)\]
  > 沿时间轴解耦 BN 参数（BNTT），捕捉脉冲的时序动态，实现低时延、从零训练。
- [`网络结构`](README.zh-CN.md#4--网络架构) · Temporal-wise Attention Spiking Neural Networks for Event Streams Classification (TA-SNN) (**ICCV 2021**). \[[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Yao_Temporal-Wise_Attention_Spiking_Neural_Networks_for_Event_Streams_Classification_ICCV_2021_paper.html)\]\[[code](https://github.com/BICLab/TA-SNN)\]
  > 引入时间维注意力，衡量并筛除噪声事件帧，是事件数据上里程碑式的注意力 SNN。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Taking Neuromorphic Computing to the Next Level with Loihi 2 (**Intel Tech Brief 2021**). \[[paper](https://www.intel.com/content/www/us/en/research/neuromorphic-computing-loihi-2-technology-brief.html)\]\[[code](https://github.com/lava-nc/lava)\]
  > Loihi 2 引入分级脉冲、可编程神经元微码，7nm 支持百万神经元，并配套开源 Lava。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · μBrain: An Event-Driven and Fully Synthesizable Architecture for SNNs (**Front. Neurosci. 2021**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2021.664208/full)\]
  > 首个无时钟、可完全综合的数字脉冲芯片（40nm、亚百微瓦），实现常开近传感器边缘智能。
- [`应用`](README.zh-CN.md#7--应用) · Self-Supervised Learning of Event-Based Optical Flow with Spiking Neural Networks (**NeurIPS 2021**). \[[paper](https://arxiv.org/abs/2106.01862)\]\[[code](https://github.com/tudelft/ssl_e2vid)\]
  > Hagenaars 等自监督训练深度 SNN 做稠密事件光流，大幅缩小与 ANN 的差距。
- [`应用`](README.zh-CN.md#7--应用) · SpikeMS: Deep Spiking Neural Network for Motion Segmentation (**IEEE/RSJ IROS 2021**). \[[paper](https://arxiv.org/abs/2105.06562)\]
  > 首个用于事件运动分割的深度 SNN，提出时空损失，低功耗且支持增量预测。
- [`应用`](README.zh-CN.md#7--应用) · Neuromorphic Control for Optic-Flow-Based Landing of MAVs using the Loihi Processor (**ICRA 2021**). \[[paper](https://arxiv.org/abs/2011.00534)\]
  > 首个在飞行无人机上完全嵌入 Loihi 的 SNN，用光流散度控制推力实现自主降落。
- [`应用`](README.zh-CN.md#7--应用) · Strategy and Benchmark for Converting Deep Q-Networks to Event-Driven SNNs (**AAAI 2021**). \[[paper](https://arxiv.org/abs/2009.14456)\]
  > 确立了深度 Q 网络到脉冲 DQN 的转换方法与基准，是神经形态深度强化学习的早期里程碑。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · HIRE-SNN: Harnessing the Inherent Robustness of Energy-Efficient Deep SNNs by Training with Crafted Input Noise (**ICCV 2021**). \[[paper](https://arxiv.org/abs/2110.11417)\]
  > 用时序单步输入噪声训练，在保持低延迟能耗下提升 SNN 对抗鲁棒性。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · DVS-Attacks: Adversarial Attacks on Dynamic Vision Sensors for SNNs (**IJCNN 2021**). \[[paper](https://arxiv.org/abs/2107.00415)\]\[[code](https://github.com/albertomarchisio/DVS-Attacks)\]
  > 提出针对事件流的隐蔽攻击（DVS-Gesture 精度掉超 20%），并用 DVS 噪声滤波做部分防御。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Securing Deep SNNs against Adversarial Attacks through Inherent Structural Parameters (**DATE 2021**). \[[paper](https://arxiv.org/abs/2012.05321)\]
  > 研究阈值、泄漏、时间步等结构超参对 SNN 抗攻击能力的调控，并可作为防御手段。

<details>
<summary><b>当年另有 4 篇</b> — 当年全量索引，每篇一句话</summary>

- Spiking Deep Residual Network [[paper](https://arxiv.org/pdf/1805.01352.pdf)]
  > 用专门的捷径转换模型把激活值缩放到对应发放率，并以补偿机制减小离散化误差，将转换所得脉冲 ResNet 推进到 40 层以上。
- Pruning of Deep Spiking Neural Networks through Gradient Rewiring [[paper](https://arxiv.org/abs/2105.04916)] [[code](https://github.com/Yanqi-Chen/Gradient-Rewiring)]
  > 为突触引入统一参数，让剪枝与连接再生在同一梯度下竞争，联合学习连接结构与权重，无需重训练即可揭示深层 SNN 的冗余。
- Optimal ANN-SNN Conversion for Fast and Accurate Inference in Deep Spiking Neural Networks [[paper](https://arxiv.org/pdf/2105.11654)] [[code](https://github.com/DingJianhao/OptSNNConvertion-RNL-RIL)]
  > 用带可学习上界的 Rate Norm Layer 取代源 ANN 中的 ReLU，并拟合激活值与发放率的对应关系，在近乎无损转换的同时缩短推理时间步。
- Training Spiking Neural Networks with Accumulated Spiking Flow (**AAAI 2021**) [[paper](https://arxiv.org/pdf/2011.05280.pdf)]
  > 用时间窗内累积的输入输出脉冲量替代逐时间步展开来计算梯度，并以自适应线性估计刻画神经元动态，降低训练复杂度。

</details>

### 2020

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · A Solution to the Learning Dilemma for Recurrent Networks of Spiking Neurons (e-prop) (**Nature Communications 2020**). \[[paper](https://doi.org/10.1038/s41467-020-17236-y)\]\[[code](https://github.com/IGITUGraz/eligibility_propagation)\]
  > 用局部资格迹配合自上而下的学习信号近似 BPTT，无需时间反传，为神经形态芯片上的在线学习铺路。
- [`应用`](README.zh-CN.md#7--应用) ★ · Spiking-YOLO: Spiking Neural Network for Energy-Efficient Object Detection (**AAAI 2020**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/6787)\]
  > 首个脉冲目标检测器，用逐通道归一化与带符号 IF 神经元，在能耗降低约 280 倍下逼近 Tiny-YOLO。
- [`应用`](README.zh-CN.md#7--应用) ★ · Deep RL with Population-Coded Spiking Neural Network for Continuous Control (PopSAN) (**CoRL 2020**). \[[paper](https://proceedings.mlr.press/v155/tang21a.html)\]\[[code](https://github.com/combra-lab/pop-spiking-deep-rl)\]
  > 用群体编码的脉冲 actor 配合 DDPG 训练，部署到 Loihi 做连续机器人控制，能耗降低约 140 倍。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · T2FSNN: Deep Spiking Neural Networks with Time-to-First-Spike Coding (**DAC 2020**). \[[paper](https://arxiv.org/abs/2003.11741)\]
  > 将首脉冲时间编码引入深度 SNN，配合核阈值与提前发放实现低延迟低能耗。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Temporal Coding in Spiking Neural Networks with Alpha Synaptic Function (**ICASSP 2020**). \[[paper](https://arxiv.org/abs/1907.13223)\]
  > 借助 alpha 型突触响应，实现对精确脉冲时刻的解析反向传播。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Enabling Deep SNNs with Hybrid Conversion and Spike-Timing-Dependent Backpropagation (**ICLR 2020**). \[[paper](https://openreview.net/forum?id=B1xSperKvH)\]\[[code](https://github.com/nitin-rathi/hybrid-snn-conversion)\]
  > 先用转换得到好初始权重，再用脉冲反传微调，把推理时间步数量级式压缩。
- [`训练方法`](README.zh-CN.md#3--训练方法) · RMP-SNN: Residual Membrane Potential Neuron for Deeper, High-Accuracy, Low-Latency SNNs (**CVPR 2020**). \[[paper](https://arxiv.org/abs/2003.01811)\]
  > 用"软复位"保留超阈值的剩余膜电位，消除硬复位带来的转换误差，近乎无损。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Temporal Spike Sequence Learning via Backpropagation for Deep SNNs (TSSL-BP) (**NeurIPS 2020**). \[[paper](https://arxiv.org/abs/2002.10085)\]\[[code](https://github.com/stonezwr/TSSL-BP)\]
  > 将误差分配拆成神经元间与神经元内两类依赖，实现少步数下的高精度时序学习。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · DYNAP-CNN & Speck: Event-Driven Convolutional Neuromorphic Vision Processors (SynSense) (**2020**). \[[paper](https://www.synsense.ai/products/speck-2/)\]\[[code](https://github.com/synsense/sinabs)\]
  > 商用亚毫瓦脉冲卷积处理器（Speck 把 DVS 与 DynapCNN 集成于单芯片），微秒延迟常开事件视觉。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Fully Hardware-Implemented Memristor Convolutional Neural Network (**Nature 2020**). \[[paper](https://www.nature.com/articles/s41586-020-1942-4)\]
  > 清华把八个忆阻交叉阵列集成为完整卷积网络并混合训练，能效超 GPU 百倍。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Deep Learning Incorporating Biologically Inspired Neural Dynamics and In-Memory Computing (**Nature Machine Intelligence 2020**). \[[paper](https://www.nature.com/articles/s42256-020-0187-0)\]
  > Woźniak 等的脉冲神经单元（SNU）把 LIF 动力学引入深度学习层，可部署到存内计算硬件。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · A 1280×720 Back-Illuminated Stacked Temporal-Contrast Event-Based Vision Sensor (**IEEE ISSCC 2020**). \[[paper](https://ieeexplore.ieee.org/document/9063149)\]
  > 索尼/Prophesee 将事件相机做到高清、业界最小像素与超 124dB 高动态，推动商用落地。
- [`应用`](README.zh-CN.md#7--应用) · Spike-FlowNet: Event-Based Optical Flow with Energy-Efficient Hybrid Neural Networks (**ECCV 2020**). \[[paper](https://arxiv.org/abs/2003.06696)\]\[[code](https://github.com/chan8972/Spike-FlowNet)\]
  > SNN-ANN 混合网络，从稀疏事件估计光流，相比纯 ANN 大幅提升效率。
- [`应用`](README.zh-CN.md#7--应用) · Unsupervised Learning of a Hierarchical Spiking Neural Network for Optical Flow Estimation (**IEEE TPAMI 2020**). \[[paper](https://arxiv.org/abs/1807.10936)\]
  > Paredes-Vallés 等用 STDP 训练的层级 SNN 从原始事件学习运动感知，是生物可塑性光流的里程碑。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Rethinking the Performance Comparison Between SNNs and ANNs (**Neural Networks 2020**). \[[paper](https://doi.org/10.1016/j.neunet.2019.09.005)\]
  > 系统比较 SNN 与 ANN 的精度/运算量/能耗，厘清脉冲稀疏性带来的真实收益。
- [`能效与鲁棒`](README.zh-CN.md#8--能耗鲁棒性与安全) · Inherent Adversarial Robustness of Deep SNNs: Discrete Input Encoding and Non-linear Activations (**ECCV 2020**). \[[paper](https://doi.org/10.1007/978-3-030-58526-6_24)\]
  > 泊松离散输入与 LIF 泄漏使 SNN 在（尤其黑盒）梯度攻击下比 ANN 更鲁棒。
- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) · Entropy, Mutual Information, and Systematic Measures of Structured Spiking Neural Networks (**J. Theoretical Biology 2020**). \[[paper](https://www.sciencedirect.com/science/article/abs/pii/S002251932030165X)\]
  > 建立熵/互信息度量，刻画脉冲网络结构与信息流、动力学之间的关系。


### 2019

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Going Deeper in Spiking Neural Networks: VGG and Residual Architectures (**Front. Neurosci. 2019**). \[[paper](https://doi.org/10.3389/fnins.2019.00095)\]
  > 把转换法扩展到深层 VGG-16/ResNet 并首次在 ImageNet 上验证，证明脉冲网络也能做深。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · Towards Artificial General Intelligence with Hybrid Tianjic Chip Architecture (**Nature 2019**). \[[paper](https://www.nature.com/articles/s41586-019-1424-8)\]
  > 清华天机芯在同一可重构众核芯片上融合 ANN 与 SNN，并以自动驾驶自行车惊艳亮相。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Direct Training for Spiking Neural Networks: Faster, Larger, Better (NeuNorm) (**AAAI 2019**). \[[paper](https://arxiv.org/abs/1809.05793)\]
  > 提出神经元归一化 NeuNorm 并改进编码，让 STBP 能训练更大网络。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Bio-Inspired Digit Recognition Using Reward-Modulated STDP in Deep Conv Networks (**Pattern Recognition 2019**). \[[paper](https://arxiv.org/abs/1804.00227)\]\[[code](https://github.com/miladmozafari/SpykeTorch)\]
  > 将无监督 STDP 与奖赏调制 STDP（三因子规则）结合，用类强化信号驱动特征学习。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · SpiNNaker 2: A 10-Million-Core Processor System for Brain Simulation and Machine Learning (**arXiv 2019**). \[[paper](https://arxiv.org/abs/1911.02385)\]
  > 22nm FDSOI 第二代，加入数值加速器与自适应功耗管理，兼顾脑仿真与机器学习。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · ODIN: A 0.086 mm² 12.7 pJ/SOP 64k-Synapse 256-Neuron Online-Learning Digital SNN Processor (**IEEE TBCAS 2019**). \[[paper](https://arxiv.org/abs/1804.07858)\]\[[code](https://github.com/ChFrenkel/ODIN)\]
  > 小巧开源的 28nm 芯片，支持 SDSP 片上学习与 Izhikevich 神经元，突触密度与能耗创纪录。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · MorphIC: A 65-nm Quad-Core Binary-Weight Digital Neuromorphic Processor with Stochastic Online Learning (**IEEE TBCAS 2019**). \[[paper](https://arxiv.org/abs/1904.08513)\]
  > ODIN 的四核后续，用二值权重与随机脉冲驱动可塑性最大化突触密度，面向边缘学习。
- [`应用`](README.zh-CN.md#7--应用) · Benchmarking Keyword Spotting Efficiency on Neuromorphic Hardware (**NICE 2019**). \[[paper](https://arxiv.org/abs/1812.01739)\]
  > 证明 Loihi 上的脉冲关键词唤醒在同等精度下的单次推理能耗优于 CPU/GPU/边缘设备。


### 2018

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Spatio-Temporal Backpropagation for Training High-Performance SNNs (STBP) (**Front. Neurosci. 2018**). \[[paper](https://doi.org/10.3389/fnins.2018.00331)\]\[[code](https://github.com/yjwu17/STBP-for-training-SpikingNN)\]
  > 在空间与时间两个维度展开做 BPTT 并用近似梯度，奠定当今直接训练 SNN 的标准框架。
- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · SLAYER: Spike Layer Error Reassignment in Time (**NeurIPS 2018**). \[[paper](https://papers.nips.cc/paper/7415-slayer-spike-layer-error-reassignment-in-time)\]\[[code](https://github.com/bamsumit/slayerPytorch)\]
  > 用时间信用分配核在时间轴上反传误差，可同时学习权重与轴突延迟。
- [`网络结构`](README.zh-CN.md#4--网络架构) ★ · Long Short-Term Memory and Learning-to-Learn in Networks of Spiking Neurons (LSNN) (**NeurIPS 2018**). \[[paper](https://arxiv.org/abs/1803.09574)\]\[[code](https://github.com/IGITUGraz/LSNN-official)\]
  > 为循环 SNN 引入自适应阈值（ALIF）神经元与"学会学习"，首次让脉冲网络逼近 LSTM 级时序计算力。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · Loihi: A Neuromorphic Manycore Processor with On-Chip Learning (**IEEE Micro 2018**). \[[paper](https://ieeexplore.ieee.org/document/8259423)\]\[[code](https://github.com/lava-nc/lava)\]
  > Intel 14nm、128 核、支持可编程突触学习规则，是片上脉冲学习最具影响力的研究平台。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Deep Neural Networks with Weighted Spikes (**Neurocomputing 2018**). \[[paper](https://doi.org/10.1016/j.neucom.2018.05.087)\]
  > 相位/加权脉冲编码按时间相位赋予脉冲不同权重，降低延迟与发放数。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Conversion of Analog to Spiking Neural Networks Using Sparse Temporal Coding (**IEEE ISCAS 2018**). \[[paper](https://doi.org/10.1109/ISCAS.2018.8351295)\]
  > 基于首脉冲时间的转换，相比率编码大幅减少运算而几乎不损精度。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Supervised Learning Based on Temporal Coding in Spiking Neural Networks (**IEEE TNNLS 2018**). \[[paper](https://doi.org/10.1109/TNNLS.2017.2726060)\]
  > Mostafa 对"首脉冲时刻"做精确梯度下降，是时间编码训练的奠基方法之一。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · Generalized Leaky Integrate-and-Fire Models Classify Multiple Neuron Types (**Nature Communications 2018**). \[[paper](https://www.nature.com/articles/s41467-017-02717-4)\]\[[code](https://github.com/AllenInstitute/GLIF_Teeter_et_al_2018)\]
  > Allen 研究所的数据驱动 GLIF 层级模型，拟合 645 个真实神经元并区分细胞类型。
- [`训练方法`](README.zh-CN.md#3--训练方法) · SuperSpike: Supervised Learning in Multilayer Spiking Neural Networks (**Neural Computation 2018**). \[[paper](https://doi.org/10.1162/neco_a_01086)\]\[[code](https://github.com/fzenke/pub2018superspike)\]
  > 推导出可在线运行的三因子近似梯度规则，把多层 SNN 训练与生物可塑性联系起来。
- [`训练方法`](README.zh-CN.md#3--训练方法) · STDP-Based Spiking Deep Convolutional Neural Networks for Object Recognition (**Neural Networks 2018**). \[[paper](https://doi.org/10.1016/j.neunet.2017.12.005)\]
  > 用 STDP 逐层无监督训练卷积特征并配合时间编码，证明局部可塑性也能学到深层层次化特征。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · DYNAP-SE: A Scalable Multicore Architecture with Heterogeneous Memory for Dynamic Neuromorphic Async Processors (**IEEE TBCAS 2018**). \[[paper](https://doi.org/10.1109/TBCAS.2017.2759700)\]
  > Indiveri 的亚阈值模拟芯片，用异构分层/网格路由解决神经形态芯片的连接扩展难题。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Fully Memristive Neural Networks for Pattern Classification with Unsupervised Learning (**Nature Electronics 2018**). \[[paper](https://www.nature.com/articles/s41928-018-0023-2)\]
  > 把扩散忆阻器 LIF 神经元与非易失忆阻突触集成为全忆阻网络，实现无监督学习。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Equivalent-Accuracy Accelerated Neural-Network Training Using Analogue Memory (**Nature 2018**). \[[paper](https://www.nature.com/articles/s41586-018-0180-5)\]
  > 用相变+电容模拟突触实现与软件同等的训练精度，能效比 GPU 高约两个数量级。
- [`应用`](README.zh-CN.md#7--应用) · EV-FlowNet: Self-Supervised Optical Flow Estimation for Event-Based Cameras (**RSS 2018**). \[[paper](https://arxiv.org/abs/1802.06898)\]\[[code](https://github.com/daniilidis-group/EV-FlowNet)\]
  > 开创性的自监督事件相机光流网络，确立了 MVSEC 评测范式。


---

## 神经形态芯片与早期深度脉冲网络  <sub>(2010–2017)</sub>

### 2017

**精选**

- [`应用`](README.zh-CN.md#7--应用) ★ · A Low Power, Fully Event-Based Gesture Recognition System (**CVPR 2017**). \[[paper](https://openaccess.thecvf.com/content_cvpr_2017/papers/Amir_A_Low_Power_CVPR_2017_paper.pdf)\]
  > IBM 用 DVS 相机加 TrueNorth 芯片实现毫瓦级手势识别，并发布广泛使用的 DVS128 Gesture 数据集。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Conversion of Continuous-Valued Deep Networks to Efficient Event-Driven Networks (**Front. Neurosci. 2017**). \[[paper](https://doi.org/10.3389/fnins.2017.00682)\]\[[code](https://github.com/NeuromorphicProcessorProject/snn_toolbox)\]
  > 给出 BN、最大池化、softmax、偏置的脉冲等价实现，并开源常用的 SNN 工具箱。
- [`训练方法`](README.zh-CN.md#3--训练方法) · Equilibrium Propagation: Bridging Energy-Based Models and Backpropagation (**Front. Comput. Neurosci. 2017**). \[[paper](https://doi.org/10.3389/fncom.2017.00024)\]
  > 用两阶段、仅需局部同类计算的方式获得精确梯度，是反传的生物可行替代方案。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Darwin: A Neuromorphic Hardware Co-Processor Based on SNNs (**J. Systems Architecture 2017**). \[[paper](https://www.sciencedirect.com/science/article/abs/pii/S1383762117300231)\]
  > 中国达尔文芯片（180nm、2048 神经元、可配置突触延迟），早期低功耗嵌入式脉冲协处理器。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Memristors with Diffusive Dynamics as Synaptic Emulators (**Nature Materials 2017**). \[[paper](https://www.nature.com/articles/nmat4756)\]
  > 银纳米颗粒扩散型忆阻器再现类钙离子的短时突触动力学，提供生物学上逼真的模拟突触。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Neuromorphic Computing with Nanoscale Spintronic Oscillators (**Nature 2017**). \[[paper](https://www.nature.com/articles/nature23011)\]
  > 用单个自旋力矩纳米振荡器识别口语数字，开辟自旋电子学作为神经形态载体。


### 2016

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) · Training Deep Spiking Neural Networks Using Backpropagation (**Front. Neurosci. 2016**). \[[paper](https://doi.org/10.3389/fnins.2016.00508)\]
  > 把膜电位当作可微信号、脉冲跳变视为噪声，让标准反传能直接训练深层 SNN。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Convolutional Networks for Fast, Energy-Efficient Neuromorphic Computing (TrueNorth) (**PNAS 2016**). \[[paper](https://www.pnas.org/doi/10.1073/pnas.1604850113)\]
  > 把深度卷积网络映射到 TrueNorth，用几十毫瓦达到接近顶尖精度、1200–2600 fps。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Stochastic Phase-Change Neurons (**Nature Nanotechnology 2016**). \[[paper](https://www.nature.com/articles/nnano.2016.70)\]
  > IBM 用相变器件实现积分-发放人工神经元，其内在随机性支持基于群体的信号表示。


### 2015

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Spiking Deep Convolutional Neural Networks for Energy-Efficient Object Recognition (**IJCV 2015**). \[[paper](https://doi.org/10.1007/s11263-014-0788-3)\]
  > 最早把训练好的 CNN 搬到脉冲网络，用"发放率≈ReLU 激活"开创了 ANN 转 SNN 这条路线。
- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Fast-Classifying, High-Accuracy Spiking Deep Networks Through Weight and Threshold Balancing (**IJCNN 2015**). \[[paper](https://doi.org/10.1109/IJCNN.2015.7280696)\]
  > 提出权重归一化/阈值平衡，让各层发放率不饱和，使转换几乎无损且低延迟。
- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Unsupervised Learning of Digit Recognition Using STDP (**Front. Comput. Neurosci. 2015**). \[[paper](https://doi.org/10.3389/fncom.2015.00099)\]\[[code](https://github.com/peter-u-diehl/stdp-mnist)\]
  > Diehl 与 Cook 用 STDP 加侧向抑制无监督学习 MNIST（约 95%），成为生物可塑性 SNN 的经典基准。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · Training and Operation of an Integrated Neuromorphic Network Based on Metal-Oxide Memristors (**Nature 2015**). \[[paper](https://www.nature.com/articles/nature14441)\]
  > 首个无晶体管忆阻交叉阵列感知机并原位训练，证明集成忆阻神经网络可行。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · ROLLS: A Reconfigurable On-Line Learning Spiking Neuromorphic Processor (256 Neurons, 128k Synapses) (**Front. Neurosci. 2015**). \[[paper](https://doi.org/10.3389/fnins.2015.00141)\]
  > 混合信号芯片，以真实神经元/突触物理特性与脉冲可塑性实现完全片上的在线学习。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Experimental Demonstration and Tolerancing of a Large-Scale Neural Network (165,000 Synapses) Using Phase-Change Memory (**IEEE TED 2015**). \[[paper](https://doi.org/10.1109/TED.2015.2439635)\]
  > IBM 的 Burr 等在真实相变存储硬件上训练 16.5 万突触网络，是大规模存内计算的里程碑。


### 2014

**精选**

- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network (TrueNorth) (**Science 2014**). \[[paper](https://www.science.org/doi/10.1126/science.1254642)\]
  > IBM TrueNorth 用 65 毫瓦集成百万神经元、2.56 亿突触，是大规模数字类脑芯片的里程碑。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · Neurogrid: A Mixed-Analog-Digital Multichip System for Large-Scale Neural Simulations (**Proc. IEEE 2014**). \[[paper](https://doi.org/10.1109/JPROC.2014.2313565)\]
  > Boahen 的 16 核 Neurogrid 用亚阈值模拟电路，以仅 3 瓦实时仿真百万神经元与数十亿突触。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · The SpiNNaker Project (**Proc. IEEE 2014**). \[[paper](https://doi.org/10.1109/JPROC.2014.2304638)\]\[[code](https://github.com/SpiNNakerManchester)\]
  > 曼彻斯特用海量 ARM 核与类脑分组路由，以生物实时速度模拟脉冲网络。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · A 240×180 130 dB 3 μs Latency Global-Shutter Spatiotemporal Vision Sensor (DAVIS) (**IEEE JSSC 2014**). \[[paper](https://doi.org/10.1109/JSSC.2014.2342715)\]
  > 从同一光电二极管同时输出异步 DVS 事件与同步 APS 帧，是最常用的事件相机格式。


### 2013

**精选**

- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) ★ · Predictive Coding of Dynamical Variables in Balanced Spiking Networks (**PLOS Comp. Biol. 2013**). \[[paper](https://doi.org/10.1371/journal.pcbi.1003258)\]
  > 经典理论：平衡脉冲网络仅在降低表征误差时发放，可实现任意线性动力系统。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · SpiNNaker: A 1-W 18-Core System-on-Chip for Massively-Parallel Neural Simulation (**IEEE JSSC 2013**). \[[paper](https://doi.org/10.1109/JSSC.2013.2259038)\]
  > 18 个 ARM 核、1 亿晶体管、1 瓦的 GALS 芯片，是百万核 SpiNNaker 系统的物理基石。


### 2011

**精选**

- [`理论与神经科学`](README.zh-CN.md#9--理论与神经科学) ★ · Neural Dynamics as Sampling: A Model for Stochastic Computation in Recurrent Networks of Spiking Neurons (**PLoS Comput. Biol. 2011**). \[[paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002211)\]
  > Buesing 等证明脉冲网络可通过*采样*完成概率推断，为"脉冲"提供了奠基性的贝叶斯解读。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · A Digital Neurosynaptic Core Using Embedded Crossbar Memory with 45 pJ per Spike in 45 nm (**IEEE CICC 2011**). \[[paper](https://doi.org/10.1109/CICC.2011.6055294)\]
  > Merolla 等的神经突触核，是 IBM TrueNorth 的直接架构前身。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Nanoelectronic Programmable Synapses Based on Phase-Change Materials (**Nano Letters 2011**). \[[paper](https://pubs.acs.org/doi/10.1021/nl201040y)\]
  > 用相变材料的连续电阻变化，以皮焦能耗模拟模拟型突触可塑性（STDP）。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · A QVGA 143 dB Dynamic Range Frame-Free PWM Image Sensor (ATIS) (**IEEE JSSC 2011**). \[[paper](https://doi.org/10.1109/JSSC.2010.2085952)\]
  > 将事件式变化检测与逐像素 PWM 绝对光强编码结合，为事件视觉补上灰度信息。


### 2010

**精选**

- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · Nanoscale Memristor Device as Synapse in Neuromorphic Systems (**Nano Letters 2010**). \[[paper](https://pubs.acs.org/doi/10.1021/nl904092h)\]
  > Jo 与 Lu 的硅忆阻器在单个纳米器件上实验实现 STDP，开启忆阻突触类脑计算。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · A Wafer-Scale Neuromorphic Hardware System for Large-Scale Neural Modeling (BrainScaleS-1) (**IEEE ISCAS 2010**). \[[paper](https://doi.org/10.1109/ISCAS.2010.5536970)\]
  > 海德堡 HICANN 晶圆级系统，以生物 1 万倍速在每片晶圆上仿真约 20 万神经元。


---

## 奠基时代 — 从神经元到学习法则  <sub>(1943–2008)</sub>

### 2008

**精选**

- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · The Missing Memristor Found (**Nature 2008**). \[[paper](https://www.nature.com/articles/nature06932)\]
  > HP 实验室首次物理实现蔡少棠预言的忆阻器，开启了整个忆阻突触领域。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · A 128×128 120 dB 15 μs Latency Asynchronous Temporal Contrast Vision Sensor (DVS) (**IEEE JSSC 2008**). \[[paper](https://doi.org/10.1109/JSSC.2007.914337)\]
  > 动态视觉传感器（DVS），像素在亮度变化时异步发放脉冲，开创事件式/神经形态视觉。
- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Rapid Neural Coding in the Retina with Relative Spike Latencies (**Science 2008**). \[[paper](https://www.science.org/doi/10.1126/science.1149639)\]
  > 生物学证据：相对首脉冲潜伏期能稳健、抗对比度地编码信息。


### 2007

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Unsupervised Learning of Visual Features through Spike-Timing-Dependent Plasticity (**PLoS Comput. Biol. 2007**). \[[paper](https://doi.org/10.1371/journal.pcbi.0030031)\]
  > Masquelier 与 Thorpe 证明 STDP + 延迟编码可自组织出有选择性的视觉特征，是无监督学习的里程碑。
- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · AER EAR: A Matched Silicon Cochlea Pair with Address-Event Representation Interface (**IEEE TCAS-I 2007**). \[[paper](https://doi.org/10.1109/TCSI.2006.887979)\]
  > 双耳硅耳蜗模拟基底膜滤波并输出 AER 脉冲，是听觉版的动态视觉传感器。
- [`应用`](README.zh-CN.md#7--应用) · Improved Spiking Neural Networks for EEG Classification and Epilepsy/Seizure Detection (**Integr. Comput.-Aided Eng. 2007**). \[[paper](https://journals.sagepub.com/doi/10.3233/ICA-2007-14301)\]
  > 将多脉冲 SNN 用于 EEG 癫痫/发作检测的早期里程碑，取得高准确率。


### 2006

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · The Tempotron: A Neuron That Learns Spike Timing-Based Decisions (**Nature Neuroscience 2006**). \[[paper](https://doi.org/10.1038/nn1643)\]
  > Gütig 与 Sompolinsky 的 tempotron——单个神经元即可依据输入脉冲的*时序*学会分类。


### 2005

**精选**

- [`神经元模型`](README.zh-CN.md#2--神经元模型) · Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity (**J. Neurophysiology 2005**). \[[paper](https://doi.org/10.1152/jn.00686.2005)\]
  > AdEx 模型，加入指数发放项与自适应，能精确拟合真实神经元行为。


### 2004

**精选**

- [`神经元模型`](README.zh-CN.md#2--神经元模型) · Which Model to Use for Cortical Spiking Neurons? (**IEEE TNN 2004**). \[[paper](https://doi.org/10.1109/TNN.2004.832719)\]
  > 著名的神经元模型对比图，权衡生物真实性与计算成本，指导选型。


### 2003

**精选**

- [`神经元模型`](README.zh-CN.md#2--神经元模型) ★ · Simple Model of Spiking Neurons (**IEEE TNN 2003**). \[[paper](https://doi.org/10.1109/TNN.2003.820440)\]
  > Izhikevich 双变量模型，以积分-发放的代价再现丰富皮层放电模式。


### 2002

**精选**

- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) ★ · Spiking Neuron Models: Single Neurons, Populations, Plasticity (**Cambridge Univ. Press 2002**). \[[paper](https://doi.org/10.1017/CBO9780511815706)\]
  > Gerstner 与 Kistler 的奠基性教材，统一了 IF、SRM、群体与可塑性理论。
- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Error-Backpropagation in Temporally Encoded Networks of Spiking Neurons (SpikeProp) (**Neurocomputing 2002**). \[[paper](https://doi.org/10.1016/S0925-2312(01)00658-0)\]
  > 为时间编码脉冲神经元推导出首个类反传规则，是所有梯度训练 SNN 方法的鼻祖。
- [`网络结构`](README.zh-CN.md#4--网络架构) ★ · Real-Time Computing Without Stable States (Liquid State Machine) (**Neural Computation 2002**). \[[paper](https://direct.mit.edu/neco/article/14/11/2531/6650)\]
  > 奠基性的液体状态机（储备池计算）——用循环脉冲回路把输入映射到高维可读状态。


### 2001

**精选**

- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) · Spike-Based Strategies for Rapid Processing (**Neural Networks 2001**). \[[paper](https://doi.org/10.1016/S0893-6080(01)00083-1)\]
  > Thorpe 等提出的排序编码，仅凭放电先后顺序即可实现超快识别。
- [`神经元模型`](README.zh-CN.md#2--神经元模型) · A Framework for Spiking Neuron Models: The Spike Response Model (**Handbook of Biol. Physics 2001**). \[[paper](https://www.sciencedirect.com/science/article/pii/S1383812101800154)\]
  > 正式提出脉冲响应模型（SRM），用核函数将积分-发放神经元一般化。


### 2000

**精选**

- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) · Point-to-Point Connectivity Between Neuromorphic Chips Using Address Events (**IEEE TCAS-II 2000**). \[[paper](https://doi.org/10.1109/82.842110)\]
  > Boahen 正式提出地址-事件表示（AER）——如今每颗神经形态芯片都在用的"脉冲即数据包"协议。


### 1999

**精选**

- [`神经元模型`](README.zh-CN.md#2--神经元模型) ★ · Lapicque's Introduction of the Integrate-and-Fire Model Neuron (1907) (**Brain Res. Bull. 1999**). \[[paper](https://doi.org/10.1016/S0361-9230(99)00161-6)\]
  > 考证并追溯了 Lapicque 在 1907 年提出的最初积分-发放神经元。


### 1998

**精选**

- [`训练方法`](README.zh-CN.md#3--训练方法) ★ · Synaptic Modifications in Cultured Hippocampal Neurons: Dependence on Spike Timing... (**J. Neuroscience 1998**). \[[paper](https://doi.org/10.1523/JNEUROSCI.18-24-10464.1998)\]
  > Bi 与 Poo 通过实验量化了脉冲时序依赖可塑性（STDP），是所有局部 SNN 学习规则的生物学根基。


### 1997

**精选**

- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) ★ · Networks of Spiking Neurons: The Third Generation of Neural Network Models (**Neural Networks 1997**). \[[paper](https://doi.org/10.1016/S0893-6080(97)00011-7)\]
  > Maass 的里程碑论文，定义 SNN 为计算能力更强的"第三代神经网络"。


### 1991

**精选**

- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · A Silicon Neuron (**Nature 1991**). \[[paper](https://www.nature.com/articles/354515a0)\]
  > Mahowald 与 Douglas 用模拟 VLSI 复现真实脉冲动力学，是首个"硅神经元"。


### 1990

**精选**

- [`神经形态硬件`](README.zh-CN.md#6--神经形态硬件) ★ · Neuromorphic Electronic Systems (**Proceedings of the IEEE 1990**). \[[paper](https://doi.org/10.1109/5.58356)\]
  > Carver Mead 的开山之作——用模拟 VLSI 模仿神经计算，为整个领域命名。


### 1952

**精选**

- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) ★ · A Quantitative Description of Membrane Current and Its Application to Conduction and Excitation in Nerve (**J. Physiology 1952**). \[[paper](https://doi.org/10.1113/jphysiol.1952.sp004764)\]
  > Hodgkin–Huxley 模型（诺奖成果），是一切生物物理脉冲动力学的基础。


### 1943

**精选**

- [`基础与编码`](README.zh-CN.md#1--基础与神经编码) ★ · A Logical Calculus of the Ideas Immanent in Nervous Activity (**Bull. Math. Biophysics 1943**). \[[paper](https://doi.org/10.1007/BF02478259)\]
  > McCulloch–Pitts 阈值神经元，是人工神经元与脉冲神经元的思想源头。


---

<div align="center">

<sub>精选条目自动提取自 <a href="README.zh-CN.md">README.zh-CN.md</a> · 全量索引来自 <a href="tools/data/conference-index.md">tools/data/conference-index.md</a> · 由 <a href="tools/build_timeline.py">tools/build_timeline.py</a> 生成。</sub><br>
<sub>如果本项目对你有帮助，欢迎 Star 并 <a href="README.zh-CN.md#引用">引用</a>。</sub>
</div>
