<div align="center">

<h1>脉冲神经网络精选 — 时间线版</h1>

<p><em>用时间顺序讲完整个脉冲神经网络领域 — 最新在前。</em><br>
<sub>主题版 <a href="README.zh-CN.md">Hub</a> 的时间线姊妹篇</sub></p>

<p><a href="TIMELINE.md">English</a> &nbsp;·&nbsp; <a href="TIMELINE.zh-CN.md"><b>中文</b></a> &nbsp;|&nbsp; <a href="README.zh-CN.md">主题版 (中文)</a> &nbsp;·&nbsp; <a href="README.md">Thematic Hub (EN)</a></p>

<p><b>536</b> 篇成果（225 篇精选注释 + 311 篇索引） &nbsp;·&nbsp; <b>44</b> 项里程碑 &nbsp;·&nbsp; <b>1943–2026</b></p>

</div>

---

## 如何阅读本页

这是 [脉冲神经网络精选 Hub](README.zh-CN.md) 的**时间线视图**。Hub 按*主题*组织；本页把整个领域按**年份倒序**铺开——让你顺着时间看清它是怎么一步步走过来的，就像 [TheBrainLab 的时间线](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) 那样。

每个年份分**两层**：

- **精选** — Hub 中 **225** 篇带深度注释的条目。每条都有一句*为什么重要*、一个可跳回主题章节的标签（如 `训练方法`、`神经形态硬件`），**★ = 领域里程碑**。
- **当年全量索引** — 可折叠列表，收录另外 **311** 篇论文，来自 [TheBrainLab](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks) 并已与精选去重，让当年的会议产出更完整（标题 · 会议 · 链接）。

> **自动生成** — 请勿手工编辑本文件。精选条目请加到 [README.zh-CN.md](README.zh-CN.md)，刷新[索引快照](tools/data/thebrainlab-snapshot.md)后运行 `python tools/build_timeline.py`。会议索引部分来自 [TheBrainLab/Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks)，特此致谢。

---

## 逐年论文量

```
2026  ███████████████                69
2025  ██████████████████████████████ 135
2024  ███████████████████████        105
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
<summary><b>当年另有 62 篇</b> — 会议索引，来自 TheBrainLab</summary>

- Robustify Spiking Neural Networks via Dominant Singular Deflation under Heterogeneous Training Vulnerability (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10010693)]
- A Brain-Inspired Gating Mechanism Unlocks Robust Computation in Spiking Neural Networks (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011430)]
- Training Deep Normalization-Free Spiking Neural Networks with Lateral Inhibition. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009258)]
- 3DSMT: A Hybrid Spiking Mamba-Transformer for Point Cloud Analysis. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10010096)]
- Time Is All It Takes: Spike-Retiming Attacks on Event-Driven Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10008650)]
- Cannistraci-Hebb Training on Ultra-Sparse Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007264)]
- CaRe-BN: Precise Moving Statistics for Stabilizing Spiking Neural Networks in Reinforcement Learning. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011021)]
- Otters: An Energy-Efficient Spiking Transformer via Optical Time-to-First-Spike Encoding. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007423)]
- Online Pseudo-Zeroth-Order Training of Neuromorphic Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011366)]
- SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011088)]
- Breaking Gradient Temporal Collinearity for Robust Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10006881)]
- Random Spiking Neural Networks are Stable and Spectrally Simple. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009762)]
- Many Eyes, One Mind: Temporal Multi-Perspective and Progressive Distillation for Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009850)]
- Robust Selective Activation with Randomized Temporal K-Winner-Take-All in Spiking Neural Networks for Continual Learning. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10006915)]
- Beyond Linear Processing: Dendritic Bilinear Integration in Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011474)]
- Spiking Discrepancy Transformer for Point Cloud Analysis. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10011321)]
- PredNext: Explicit Cross-View Temporal Prediction for Unsupervised Learning in Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10010014)]
- Difference Predictive Coding for Training Spiking Neural Networks. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007923)]
- Fractional-Order Spiking Neural Network. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009869)]
- SpikeGen: Decoupled “Rods and Cones” Visual Representation Processing with Latent Generative Framework. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009062)]
- Biologically Plausible Learning via Bidirectional Spike-Based Distillation. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009918)]
- Distribution-Aware Multi-Granularity Phase Coding: Towards Lower Conversion Error for Spike-Driven Large Language Models. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007555)]
- SpikeStereoNet: A Brain-Inspired Framework for Stereo Depth Estimation from Spike Streams. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10007680)]
- SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10008450)]
- Spike-based Digital Brain: a novel fundamental model for brain activity analysis. (**ICLR 2026**) [[paper](https://iclr.cc/virtual/2026/poster/10009923)]
- Activation-wise Propagation: A One-Timestep Strategy for Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37187)]
- SpikingIR: A Novel Converted Spiking Neural Network for Efficient Image Restoration (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37769)]
- A Closer Look at Knowledge Distillation in Spiking Neural Network Training (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37769)]
- Optimization Method for Surrogate Function in Spiking Neural Networks Based on Membrane Potential Distribution (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39769)]
- Parallel Training Time-to-First-Spike Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37149)]
- HardF-SNN: Hardware-Friendly Quantization for Spiking Neural Networks with Efficient Integer-Arithmetic-Only Inference (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37174)]
- SpikCommander: A High-performance Spiking Transformer with Multi-view Learning for Efficient Speech Command Recognition (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37194)]
- Timestep-Compressed Attack on Spiking Neural Networks Through Timestep-Level Backpropagation (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37479)]
- Firing Bits Where It Matters: Spiking-Guided Just Recognizable Distortion Modeling for Machine-Centric Video Coding (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38935)]
- MPD-SGR: Robust Spiking Neural Networks with Membrane Potential Distribution-Driven Surrogate Gradient Regularization (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37166)]
- Training-Free ANN-to-SNN Conversion for High-Performance Spiking Transformers (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37195)]
- I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37179)]
- S³: Spiking Neurons as an Isolating Segmenter for Brain Signal Decoding (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38869)]
- TDSNNs: Competitive Topographic Deep Spiking Neural Networks for Visual Cortex Modeling (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37208)]
- Temporal Dynamics Enhancer for Directly Trained Spiking Object Detectors (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37178)]
- Spiking Heterogeneous Graph Attention Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39068)]
- Oligodendrocyte-Driven Spiking Neural Model (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39306)]
- HLML-SNN：Fast Continual Learning in Spiking Neural Networks Achieved via Hebbian Learning-Driven Meta-Learning (**AAAI 2026**)
- DS-ATGO: Dual-Stage Synergistic Learning via Forward Adaptive Threshold and Backward Gradient Optimization for Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37165)]
- Pseudo-Spiking Neurons: A Noise-Based Training Framework for Heterogeneous-Latency Spiking Neural Networks (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40086)]
- Spatial-Frequency Spiking Neural Network for Underwater Object Detection (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39109)]
- SFedHIFI: Fire Rate-Based Heterogeneous Information Fusion for Spiking Federated Learning (**AAAI 2026**)
- Dynamic Weight Adaptation in Spiking Neural Networks Inspired by Biological Homeostasis (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40146)]
- GT-SNT: A Linear-Time Transformer for Large-Scale Graphs via Spiking Node Tokenization (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38667)]
- Exploring the Potentials of Spiking Neural Networks for Image Deraining (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37295)]
- Spiking-Aided Neural Architecture for Efficient and Robust WiFi Sensing (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39589)]
- Stabilizing Spiking Neurons Through Biologically Inspired Polarization (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39435)]
- Spike Stream Memory Transfer for Dynamic Scene Reconstruction (**AAAI 2026**)
- LAS: Loss-less ANN-SNN Conversion for Fully Spike-Driven Large Language Models (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37151)]
- Spike Imaging Velocimetry: Dense Motion Estimation of Fluids Using Spike Streams (**AAAI 2026**)
- BulletTime4D: Towards High Spatio-Temporal Resolution Dynamic Scene Rendering via Spike-Guided Stereo Vision (**AAAI 2026**)
- Robust Noise Modeling for Spike Camera via Time-Interval Quantification and Spike-DSLR Multimodal Dataset in Low-Light Imaging (**AAAI 2026**)
- Generalized Threshold Optimization with Harmony Multi-Threshold Neurons for Accurate ANN-to-SNN Conversion (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37206)]
- HypoxSpike: Ternary Spiking Neural Network for Opioid Overdose Detection (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/41237)]
- Bi-Spectrum Distillation: Addressing Spectral Mismatch in ANN-SNN Knowledge Transfer (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40085)]
- Towards Training-Free and Accurate ANN-to-SNN Conversion via Activation-Aware Redistribution (**AAAI 2026**) [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37148)]
- Spiking neural networks with fatigue spike-timing-dependent plasticity learning using hybrid memristor arrays (**Nature Electronics, 2026**) [[paper](https://www.nature.com/articles/s41928-025-01554-4)]

</details>

### 2025

**精选**

- [`脉冲大模型`](README.zh-CN.md#5--脉冲大模型与-llm) ★ · SpikingBrain: Spiking Brain-inspired Large Models (**arXiv 2025**). \[[paper](https://arxiv.org/abs/2509.05276)\]\[[code](https://github.com/BICLab/SpikingBrain-7B)\]
  > 中科院自动化所（李国齐、徐波）的类脑脉冲大模型（7B 线性 / 76B 混合 MoE），自适应脉冲编码，4M 长上下文首字延迟提速百倍，并在国产（沐曦 MetaX）GPU 上训练。
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
<summary><b>当年另有 126 篇</b> — 会议索引，来自 TheBrainLab</summary>

- Neuromorphic computing paradigms enhance robustness through spiking neural networks (**Nature Communications, 2025**) [[paper](https://www.nature.com/articles/s41467-025-65197-x)][[code](https://github.com/DingJianhao/SNNEnhancingRobustness)]
- A spiking artificial neuron based on one diffusive memristor, one transistor and one resistor (**Nature Electronics, 2025**) [[paper](https://www.nature.com/articles/s41928-025-01488-x)][[code](https://github.com/GnohzZ/Brain-Dynamics-Modeling-Acceleration)]
- A biologically inspired artificial neuron with intrinsic plasticity based on monolayer molybdenum disulfide (**Nature Electronics, 2025**) [[paper](https://www.nature.com/articles/s41928-025-01433-y)]
- Modeling macroscopic brain dynamics with brain-inspired computing architecture (**Nature Communications, 2025**) [[paper](https://www.nature.com/articles/s41467-025-64470-3)]
- A frugal Spiking Neural Network for unsupervised multivariate temporal pattern classification and multichannel spike sorting (**Nature Communications, 2025**) [[paper](https://www.nature.com/articles/s41467-025-64231-2)][[code](https://codeocean.com/capsule/9829487/tree)]
- Efficient and robust temporal processing with neural oscillations modulated spiking neural networks (**Nature Communications, 2025**) [[paper](https://www.nature.com/articles/s41467-025-63771-x)][[code](https://github.com/YinsongYan/Rhythm-SNN)]
- Covariant spatio-temporal receptive fields for spiking neural networks (**Nature Communications, 2025**) [[paper](https://www.nature.com/articles/s41467-025-63493-0)][[code](https://github.com/jegp/nrf)]
- A multisynaptic spiking neuron for simultaneously encoding spatial and temporal dynamics in spiking neural networks (**Nature Communications, 2025**) [[paper](https://doi.org/10.1038/s41467-025-62251-6)][[code](https://github.com/fanliangwei/Multisynaptic-spiking-neurons)]
- Advancing spatio-temporal processing through adaptation in spiking neural networks (**Nature Communications, 2025**) [[paper](https://www.nature.com/articles/s41467-025-60878-z)][[code](https://github.com/IGITUGraz/SE-adlif)]
- Topology optimization of random memristors for input-aware dynamic SNN (**Science Advances, 2025**) [[paper](https://www.science.org/doi/10.1126/sciadv.ads5340)][[code](https://github.com/bo-wang-up/PRIME)]
- Fully memristive spiking neural network for energy-efficient graph learning (**Science Advances, 2025**) [[paper](https://www.science.org/doi/10.1126/sciadv.adv2312)]
- Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=oGmROC4e4W)] [[code](https://github.com/korneelf1/SpikingCrazyflie)]
- Toward Relative Positional Encoding in Spiking Transformers (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=MDWJlTWZHH)] [[code](https://github.com/microsoft/SeqSNN)]
- High Dynamic Range Imaging with Time-Encoding Spike Camera (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=flIdch9eTf)] [[code](https://github.com/zkzhu123/TESC)]
- Bipolar Self-attention for Spiking Transformers (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=nG45z7lJ7D)] [[code](https://openreview.net/attachment?id=nG45z7lJ7D&name=supplementary_material)]
- Spike-timing-dependent Hebbian learning as noisy gradient descent (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=YTbLri0siT)]
- Spike-RetinexFormer: Rethinking Low-light Image Enhancement with Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=8W8SRZIpJP)]
- SPACE: SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=Di0RasgbQ6)] [[code](https://github.com/ethanxyluo/SPACE)]
- MI-TRQR: Mutual Information-Based Temporal Redundancy Quantification and Reduction for Energy-Efficient Spiking Neural Networks (**Neurips  2025**) [[paper](https://openreview.net/pdf?id=NRqGpUAjV9)] [[code](https://github.com/dfxue/MI-TRQR)]
- Spik-NeRF: Spiking Neural Networks for Neural Radiance Fields (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=047VzZEpnu)]
- Dendritic Resonate-and-Fire Neuron for Effective and Efficient Long Sequence Modeling (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=ywzGKDStrm)] [[code](https://openreview.net/attachment?id=ywzGKDStrm&name=supplementary_material)]
- Spiking Neural Networks Need High-Frequency Information (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=owNPAl7LNK)] [[code](https://github.com/bic-L/MaxFormer)]
- Activity Pruning for Efficient Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=zjOXZEXQKZ)] [[code](https://github.com/putshua/Activity-Pruning-SNN)]
- Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=4q5ZYP0ynu)] [[code](https://github.com/PengXue0812/Multiplication-Free-Parallelizable-Spiking-Neurons-with-Efficient-Spatio-Temporal-Dynamics)]
- SpikingVTG: A Spiking Detection Transformer for Video Temporal Grounding (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=SkhF3cuyev)] [[code](https://openreview.net/attachment?id=SkhF3cuyev&name=supplementary_material)]
- S$^2$M-Former: Spiking Symmetric Mixing Branchformer for Brain Auditory Attention Detection (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=WtMuGdHvh6)] [[code](https://github.com/JackieWang9811/S2M-Former)]
- Local-Global Coupling Spiking Graph Transformer for Brain Disorders Diagnosis from Two Perspectives (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=kkhRTTmXFV)]
- A Scalable, Causal, and Energy Efficient Framework for Neural Decoding with Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=oAbaGU9N1X)] [[code](https://spikachu-bci.github.io/)]
- Spiking Meets Attention: Efficient Remote Sensing Image Super-Resolution with Attention Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=VaE33hkqmg)] [[code](https://github.com/XY-boy/SpikeSR)]
- Adaptive Fission: Post-training Encoding for Low-latency Spike Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=2zZzdAMyYi)] [[code](https://github.com/JiangYizhou16/Adaptive-Fission)]
- S$^2$NN: Sub-bit Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=hFsCuVc1cB)] [[code](https://openreview.net/attachment?id=hFsCuVc1cB&name=supplementary_material)]
- Seemingly Redundant Modules Enhance Robust Odor Learning in Fruit Flies (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=d6WUTRJqP3)] [[code](https://github.com/L-0cean/Fly-SNN)]
- Fully Spiking Neural Networks for Unified Frame-Event Object Tracking (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=FooiwsnEH9)] [[code](https://github.com/Noctis-A/SpikeFET)]
- Enhanced Self-Distillation Framework for Efficient Spiking Neural Network Training (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=dpmMg6aK1D)] [[code](openreview.net/pdf?id=dpmMg6aK1D)]
- Learning the Plasticity: Plasticity-Driven Learning Framework in Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=fllsm01JWS)]
- HetSyn: Versatile Timescale Integration in Spiking Neural Networks via Heterogeneous Synapses (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=YYz4fumVed)] [[code](https://github.com/dzcgood/HetSyn)]
- Unveiling the Spatial-temporal Effective Receptive Fields of Spiking Neural Networks (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=tYnJC5ba6j)] [[code](https://github.com/EricZhang1412/Spatial-temporal-ERF)]
- Brain-like Variational Inference (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=573IcLusXq)] [[code](https://github.com/hadivafaii/IterativeVAE)]
- Proxy Target: Bridging the Gap Between Discrete Spiking Neural Networks and Continuous Control (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=RRBve5GwjS)] [[code](openreview.net/pdf?id=RRBve5GwjS)]
- Synergy Between the Strong and the Weak: Spiking Neural Networks are Inherently Self-Distillers (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=BrmR69AhUg)]
- Spike4DGS: Towards High-Speed Dynamic Scene Recontruction with 4D Gaussian Splatting via a Spike Camera Array (**Neurips 2025**) [[paper](https://openreview.net/pdf?id=V5efEA8nIr)] [[code](https://github.com/Qinghongye/Spike4DGS)]
- Toward End-to-End Bearing Fault Diagnosis for Industrial Scenarios with Spiking Neural Networks (**KDD 2025**) [[paper](https://doi.org/10.48550/arXiv.2408.11067)][[code](https://github.com/yqding326/MRA-SNN)]
- DSF-Net: Dynamic Sparse Fusion of Event-RGB via Spike-Triggered Attention for High-Speed Detection (**ACM MM 2025**)
- ESOD: Event-Based Small Object Detection (**ACM MM 2025**)
- E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event Cameras (**ACM MM 2025**)
- Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics (**ACM MM 2025**)
- Signal-SGN: A Spiking Graph Convolutional Network for Skeleton Action Recognition via Learning Temporal-Frequency Dynamics (**ACM MM 2025**)
- SGM-Transformer: Rethinking Gradient Information Loss and Compensation in Spiking Neural Networks (**ACM MM 2025**)
- Advanced SpikingYOLOX: Extending Spiking Neural Network on Object Detection with Spike-based Partial Self-Attention and 2D-Spiking Transformer (**ACM MM 2025**)
- Spiking Neural Networks with Temporal Attention-Guided Adaptive Fusion for imbalanced Multi-modal Learning (**ACM MM 2025**)
- Temporal-coded Spiking Transformer (**ACM MM 2025**)
- ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1849)]
- Robust Unfolding Network for HDR Imaging with Modulo Cameras (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1986)]
- SpikeDiff: Zero-shot High-Quality Video Reconstruction from Chromatic Spike Camera and Sub-millisecond Spike Streams (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1181)]
- Noise-Modeled Diffusion Models for Low-Light Spike Image Restoration (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1467)]
- Efficient Spiking Point Mamba for Point Cloud Analysis (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/2271)]
- SpikePack: Enhanced Information Flow in Spiking Neural Networks with High Hardware Compatibility (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/345)]
- SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition (**ICCV 2025**) [[paper](https://iccv.thecvf.com/virtual/2025/poster/1753)]
- Adaptive Gradient Learning for Spiking Neural Networks by Exploiting Membrane Potential Dynamics (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7783.pdf)]
- ILIF: Temporal Inhibitory Leaky Integrate-and-Fire Neuron for Overactivation in Spiking Neural Networks (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/4566.pdf)]
- Neuromorphic Sequential Arena: A Benchmark for Neuromorphic Temporal Processing (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7408.pdf)]
- MSVIT: Improving Spiking Vision Transformer Using Multi-scale Attention Fusion (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7378.pdf)]
- A Fast and Accurate ANN-SNN Conversion Algorithm with Negative Spikes (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/6149.pdf)]
- ECC-SNN: Cost-Effective Edge-Cloud Collaboration for Spiking Neural Networks (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/3167.pdf)]
- Cost-Effective On-Device Sequential Recommendation with Spiking Neural Networks (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/3150.pdf)]
- SCNNs: Spike-based Coupling Neural Networks for Understanding Structural-Functional Relationships in the Human Brain (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1337.pdf)]
- Exploiting Label Skewness for Spiking Neural Networks in Federated Learning (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1298.pdf)]
- Binary Event-Driven Spiking Transformer (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1206.pdf)]
- Tackling Long-Tailed Data Challenges in Spiking Neural Networks via Heterogeneous Knowledge Distillation (**IJCAI 2025**) [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/787.pdf)]
- SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and $\mathcal{O}(T)$ Complexity (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.10352)]
- Efficient ANN-SNN Conversion with Error Compensation Learning (**ICML 2025**) [[paper](https://www.arxiv.org/abs/2506.01968)]
- Differential Coding for Training-Free ANN-to-SNN Conversion (**ICML 2025**) [[paper](https://arxiv.org/abs/2503.00301)]
- Efficient Logit-based Knowledge Distillation of Deep Spiking Neural Networks for Full-Range Timestep Deployment (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44825)]
- ReverB-SNN: Reversing Bit of the Weight and Activation for Spiking Neural Networks (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/43640)]
- TTFSFormer: A TTFS-based Lossless Conversion of Spiking Transformer (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44159)]
- BSO: Binary Spiking Online Optimization (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/45087)]
- Delay-DSGN: A Dynamic Spiking Graph Neural Network with Delay Mechanisms for Evolving Graph (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/43816)]
- TS-SNN: Temporal Shift Module for Spiking Neural Networks (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.04165)]
- SpikF: Spiking Fourier Network for Efficient Long-term Prediction (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/46411)]
- Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning (**ICML 2025**) [[paper](https://arxiv.org/pdf/2505.07921)]
- Faster and Stronger: When ANN-SNN Conversion Meets Parallel Spiking Calculation (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44986)]
- Efficient Parallel Training Methods for Spiking Neural Networks with Constant Time Complexity (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/45776)]
- Training High Performance Spiking Neural Networks by Temporal Model Calibration (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/44216)]
- Temporal Misalignment in ANN-SNN Conversion and Its Mitigation via Probabilistic Spiking Neurons (**ICML 2025**) [[paper](https://icml.cc/virtual/2025/poster/45627)]
- Time to Spike? Understanding the Representational Power of Spiking Neural Networks in Discrete Time (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.18023)]
- Hybrid Spiking Vision Transformer for Object Detection with Event Cameras (**ICML 2025**) [[paper](https://arxiv.org/abs/2505.07715)]
- EventGPT: Event Stream Understanding with Multimodal Large Language Models (**CVPR 2025**) [[paper](https://arxiv.org/pdf/2412.00832)] [[code](https://github.com/XduSyL/EventGPT)]
- Spk2SRImgNet: Super-Resolve Dynamic Scene from Spike Stream via Motion Aligned Collaborative Filtering (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33079)]
- Decision SpikeFormer: Spike-Driven Transformer for Decision Making (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/32864)]
- Self-Supervised Learning for Color Spike Camera Reconstruction (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/34093)]
- USP-Gaussian: Unifying Spike-based Image Reconstruction, Pose Correction and Gaussian Splatting (**CVPR 2025**) [[paper](https://arxiv.org/abs/2411.10504)]
- VISTREAM: Improving Computation Efficiency of Visual Perception Streaming via Law-of-Charge-Conservation Inspired Spiking Neural Network (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/34908)]
- Efficient ANN-Guided Distillation: Aligning Rate-based Features of Spiking Neural Networks through Hybrid Block-wise Replacement (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.16572)]
- Spiking Transformer: Introducing Accurate Addition-Only Spiking Self-Attention for Transformer (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.00226)]
- Brain-Inspired Spiking Neural Networks for Energy-Efficient Object Detection (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33275)]
- Temporal Separation with Entropy Regularization for Knowledge Distillation in Spiking Neural Networks (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.03144)]
- STAA-SNN: Spatial-Temporal Attention Aggregator for Spiking Neural Networks (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.02689)]
- Towards Effective and Sparse Adversarial Attack on Spiking Neural Networks via Breaking Invisible Surrogate Gradients (**CVPR 2025**) [[paper](https://arxiv.org/abs/2503.03272)]
- Rethinking Spiking Self-Attention Mechanism: Implementing α-XNOR Similarity Calculation in Spiking Transformers (**CVPR 2025**) [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33850)]
- Quantized Spike-driven Transformer (**ICLR 2025**) [[paper](https://openreview.net/forum?id=5J9B7Sb8rO)]
- Rethinking Spiking Neural Networks from an Ensemble Learning Perspective (**ICLR 2025**) [[paper](https://openreview.net/forum?id=ZyknpOQwkT)]
- DeepTAGE: Deep Temporal-Aligned Gradient Enhancement for Optimizing Spiking Neural Networks (**ICLR 2025**) [[paper](https://openreview.net/forum?id=drPDukdY3t)]
- QP-SNN: Quantized and Pruned Spiking Neural Networks (**ICLR 2025**) [[paper](https://openreview.net/forum?id=MiPyle6Jef)]
- Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness (**ICLR 2025**) [[paper](https://openreview.net/forum?id=9HsfTgflT7)]
- P-SpikeSSM: Harnessing Probabilistic Spiking State Space Models for Long-Range Dependency Tasks (**ICLR 2025**) [[paper](https://openreview.net/forum?id=Sf4ep9Udjf)]
- TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting (**ICLR 2025**) [[paper](https://openreview.net/forum?id=rDe9yQQYKt)]
- Improving the Sparse Structure Learning of Spiking Neural Networks from the View of Compression Efficiency (**ICLR 2025**) [[paper](https://openreview.net/forum?id=gcouwCx7dG)]
- Spiking Vision Transformer with Saccadic Attention (**ICLR 2025**) [[paper](https://openreview.net/forum?id=qzZsz6MuEq)]
- SpikeGS: Reconstruct 3D scene captured by a fast moving bio-inspired camera (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2407.03771v2)]
- Rethinking High-speed Image Reconstruction Framework with Spike Camera (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2501.04477)] [[code](https://github.com/chenkang455/SpikeCLIP)]
- Spiking Point Transformer for Point Cloud Classification (**AAAI 2025**)
- Efficient 3D Recognition with Event-driven Spike Sparse Convolution (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.07360)] [[code](https://github.com/bollossom/e-3dsnn)]
- GRSN: Gated Recurrent Spiking Neurons for POMDPs and MARL (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2404.15597)]
- EventZoom: A Progressive Approach to Event-Based Data Augmentation for Enhanced Neuromorphic Vision (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2405.18880)]
- Leveraging Asynchronous Spiking Neural Networks for Ultra Efficient Event-Based Visual Processing (**AAAI 2025**)
- CREST: An Efficient Conjointly-trained Spike-driven Framework for Event-based Object Detection Exploiting Spatiotemporal Dynamics  (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.12525)] [[code](https://github.com/shen-aoyu/CREST/)]
- UCF-Crime-DVS: A Novel Event-Based Dataset for Video Anomaly Detection with Spiking Neural Networks (**AAAI 2025**)
- SpikingSSMs: Learning Long Sequences with Sparse and Parallel Spiking State Space Models (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2408.14909)][[code](https://github.com/shenshuaijie/SDN
- Advancing Spiking Neural Networks towards Multiscale Spatiotemporal Interaction Learning (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2405.13672)]
- SpikingYOLOX: Improved YOLOX Object Detection with Fast Fourier Convolution and Spiking Neural Networks(**AAAI 2025**)
- ALADE-SNN: Adaptive Logit Alignment in Dynamically Expandable Spiking Neural Networks for Class Incremental Learning (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.12696)]
- Efficient Spike-driven Transformer For High-performance Image Segmentation (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2412.14587)] [[code](https://github.com/BICLab/Spike2Former)]
- Towards Accurate Binary Spiking Neural Networks: Learning with Adaptive Gradient Modulation Mechanism (**AAAI 2025**)
- Adaptive Calibration: A Unified Conversion Framework of Spiking Neural Networks (**AAAI 2025**)
- Towards More Discriminative Feature Learning in SNNs with Temporal-Self-Erasing Supervision (**AAAI 2025**)
- FSTA-SNN: Frequency-based Spatial-Temporal Attention Module for Spiking Neural Networks (**AAAI 2025**) [[paper](https://arxiv.org/pdf/2501.14744)] [[code](https://github.com/yukairong/FSTA-SNN)]

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
<summary><b>当年另有 72 篇</b> — 会议索引，来自 TheBrainLab</summary>

- Direct Training High-Performance Deep Spiking Neural Networks: A Review of Theories and Methods (**Frontiers in Neuroscience 2024**) [[paper](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1383844/full)] [[arxiv](https://arxiv.org/abs/2405.04289v2)]
- SpikedAttention: Training-Free and Fully Spike-Driven Transformer-to-SNN Conversion with Winner-Oriented Spike Shift for Softmax Operation (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=fs28jccJj5)]
- Spiking Graph Neural Network on Riemannian Manifolds (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=VKt0K3iOmO)]
- Rethinking the Dynamics of Spiking Neural Networks (**NeurIPS 2024**) [[paper](https://neurips.cc/virtual/2024/poster/96543)]
- Long-Range Feedback Spiking Network Captures Dynamic and Static Representations of the Visual Cortex under Movie Stimuli (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=bxDok3uaK6)] [[code](https://github.com/Grasshlw/SNN-Neural-Similarity-Movie)]
- Take A Shortcut Back: Mitigating the Gradient Vanishing for Training Spiking Neural Networks (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=xjyU6zmZD7)]
- Advancing Training Efficiency of Deep Spiking Neural Networks through Rate-based Backpropagation (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2410.11488)] [[code](https://github.com/Tab-ct/rate-based-backpropagation)]
- Latent Diffusion for Neural Spiking Data (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=ZX6CEo1Wtv)]
- Exact Gradients for Stochastic Spiking Neural Networks Driven by Rough Signals  (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=mCWZj7pa0M)]
- Spatio-Temporal Interactive Learning for Efficient Image Reconstruction of Spiking Cameras  (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=S4ZqnMywcM)]
- Slack-Free Spiking Neural Network Formulation for Hypergraph Minimum Vertex Cover (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=4A5IQEjG8c)]
- EnOF: Training Accurate Spiking Neural Networks via Enhancing the Output Feature Representation (**NeurIPS 2024**) [[paper](https://openreview.net/pdf/5a4dfaf8dc6861efa8e8356b3bd86743ab98838d.pdf)]
- Spiking Token Mixer: A event-driven friendly Former structure for spiking neural networks (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=iYcY7KAkSy)] [[code](https://github.com/brain-intelligence-lab/STMixer_demo)]
- SpGesture: Source-Free Domain-adaptive sEMG-based Gesture Recognition with Jaccard Attentive Spiking Neural Network (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2405.14398)] [[code](https://github.com/guoweiyu/SpGesture/)]
- Spiking Transformer with Experts Mixture (**NeurIPS 2024**) [[paper](https://openreview.net/pdf/35a5bc54de368426f66605d8e3f447638863888a.pdf)]
- FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor (**NeurIPS 2024**) [[paper](https://openreview.net/pdf?id=TuCQdBo4NC)] [[code](https://github.com/zju-bmi-lab/FEEL_SNN)]
- Spiking Neural Network as Adaptive Event Stream Slicer (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2410.02249)]
- Advancing Spiking Neural Networks for Sequential Modeling with Central Pattern Generators (**NeurIPS 2024**) [[paper](https://arxiv.org/abs/2405.14362)] [[code](https://github.com/microsoft/SeqSNN)]
- Q-SNNs: Quantized Spiking Neural Networks (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3681186)]
- RSC-SNN: Exploring the Trade-off Between Adversarial Robustness and Accuracy in Spiking Neural Networks via Randomized Smoothing Coding (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3680639)] [[code](https://github.com/KemingWu/RSC-SNN)]
- Reversing Structural Pattern Learning with Biologically Inspired Knowledge Distillation for Spiking Neural Networks (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/pdf/10.1145/3664647.3680655)]
- Towards High-performance Spiking Transformers from ANN to SNN Conversion (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3680620)] [[code](https://github.com/h-z-h-cell/Transformer-to-SNN-ECMT)]
- Towards Low-latency Event-based Visual Recognition with Hybrid Step-wise Distillation Spiking Neural Networks (**ACM MM 2024**) [[paper](https://dl.acm.org/doi/10.1145/3664647.3680832)] [[code](https://github.com/hsw0929/HSD)]
- Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection (**ECCV 2024**) [[paper](https://arxiv.org/pdf/2407.20708)] [[code](https://github.com/BICLab/SpikeYOLO)]
- Spiking Wavelet Transformer (**ECCV 2024**) [[paper](https://arxiv.org/pdf/2403.11138)] [[code](https://github.com/bic-L/Spiking-Wavelet-Transformer)]
- Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05068.pdf)] [[code](https://github.com/kiritozc/MPIS-SNNs)]
- Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08133.pdf)]
- BKDSNN: Enhancing the Performance of Learning-based Spiking Neural Networks Training with Blurred Knowledge Distillation (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06649.pdf)] [[code](https://github.com/Intelligent-Computing-Research-Group/BKDSNN)]
- Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09164.pdf)]
- EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07766.pdf)] [[code](https://github.com/Windere/EAS-SNN)]
- Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction (**ECCV 2024**) [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05843.pdf)]
- EC-SNN: Splitting Deep Spiking Neural Networks on Edge Devices (**IJCAI 2024**) [[code](https://github.com/AmazingDD/EC-SNN)]
- One-step Spiking Transformer with a Linear Complexity (**IJCAI 2024**)
- Learning a Spiking Neural Network for Efficient Image Deraining (**IJCAI 2024**) [[code](https://github.com/MingTian99/ESDNet)]
- LitE-SNN: Designing Lightweight and Efficient Spiking Neural Network through Spatial-Temporal Compressive Network Search and Joint Optimization (**IJCAI 2024**) [[paper](https://arxiv.org/pdf/2401.14652)]
- Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/35073)]
- Towards efficient deep spiking neural networks construction with spiking activity based pruning (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33505)]
- Autaptic Synaptic Circuit Enhances Spatio-temporal Predictive Learning of Spiking Neural Networks (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33269)]
- Robust Stable Spiking Neural Networks (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33217)]
- NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks  (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33481)]
- High-Performance Temporal Reversible Spiking Neural Networks with $O(L)$ Training Memory and $O(1)$ Inference Cost (**ICML 2024**) [[paper](https://arxiv.org/pdf/2405.16466)]
- Towards Efficient Spiking Transformer: a Token Sparsification Framework for Training and Inference Acceleration (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/32674)]
- Sign Gradient Descent-based Neuronal Dynamics: ANN-to-SNN Conversion Beyond ReLU Network (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/33242)]
- Enhancing Adversarial Robustness in SNNs with Sparse Gradients (**ICML 2024**) [[paper](https://icml.cc/virtual/2024/poster/34066)]
- Are Conventional SNNs Really Efficient? A Perspective from Network Quantization  (**CVPR 2024**) [[paper](https://arxiv.org/pdf/2311.10802)]
- SFOD: Spiking Fusion Object Detector (**CVPR 2024**) [[paper](https://arxiv.org/pdf/2403.15192)] [[code](https://github.com/yimeng-fan/SFOD)]
- SGLFormer: Spiking Global-Local-Fusion Transformer with high performance (**Frontiers in Neuroscience 2024**) [[paper](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1371290/full)] [[code](https://github.com/ZhangHanN1/SGLFormer)]
- Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework  (**ICLR 2024**) [[paper](https://openreview.net/forum?id=eoSeaK4QJo&referrer=%5Bthe%20profile%20of%20Zecheng%20Hao%5D(%2Fprofile%3Fid%3D~Zecheng_Hao1))]
- Online Stabilization of Spiking Neural Networks  (**ICLR 2024**) [[paper](https://openreview.net/forum?id=CIj1CVbkpr)]
- SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition (**ICLR 2024**) [[paper](https://arxiv.org/pdf/2310.07189.pdf)]
- Spatio-Temporal Approximation: A Training-Free SNN Conversion for Transformers  (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=XrunSYwoLr)]
- Sparse Spiking Neural Network: Exploiting Heterogeneity in Timescales for Pruning Recurrent SNN (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=0jsfesDZDq)]
- Threaten Spiking Neural Networks through Combining Rate and Temporal Information (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=xv8iGxENyI)] [[code](https://github.com/hzc1208/HART_Attack)]
- TAB: Temporal Accumulated Batch Normalization in Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/forum?id=k1wlmtPGLq&noteId=p5M9gOLAOf)]
- Certified Adversarial Robustness for Rate Encoded Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/forum?id=5bNYf0CqxY)]
- Bayesian Bi-clustering of Neural Spiking Activity with Latent Structures (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=ZYm1Ql6udy)]
- Adaptive deep spiking neural network with global-local learning via balanced excitatory and inhibitory mechanism (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=wpnlc2ONu0)]
- Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks (**ICLR 2024**) [[paper](https://arxiv.org/pdf/2402.11984.pdf)] [[code](https://github.com/pkuxmq/HLOP-SNN)]
- A Progressive Training Framework for Spiking Neural Networks with Learnable Multi-hierarchical Model (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=g52tgL8jy6)] [[code](https://github.com/hzc1208/STBP_LMH)]
- LMUFormer: Low Complexity Yet Powerful Spiking Model With Legendre Memory Units (**ICLR 2024**) [[paper](https://arxiv.org/pdf/2402.04882.pdf)] [[code](https://github.com/zeyuliu1037/LMUFormer)]
- Spike-driven Transformer V2: Meta Spiking Neural Network Architecture Inspiring the Design of Next-generation Neuromorphic Chips (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=1SIBN5Xyw7)] [[code](https://github.com/BICLab/Spike-Driven-Transformer-V2)]
- Can we get the best of both Binary Neural Networks and Spiking Neural Networks for Efficient Computer Vision? (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=lGUyAuuTYZ)] [[code](https://github.com/godatta/Ultra-Low-Latency-SNN)]
- A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks (**ICLR 2024**) [[paper](https://openreview.net/pdf?id=LnLySuf1vp)] [[code](https://github.com/EdisonLeeeee/SpikeGCL)]
- Ternary Spike: Learning Ternary Spikes for Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2312.06372.pdf)] [[code](https://github.com/yfguo91/Ternary-Spike)]
- Memory-Efficient Reversible Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2312.07922.pdf)] [[code](https://github.com/mi804/RevSNN)]
- Gated Attention Coding for Training High-performance and Efficient Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2308.06582.pdf)]
- Shrinking Your TimeStep: Towards Low-Latency Neuromorphic Object Recognition with Spiking Neural Networks (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2401.01912.pdf)]
- An Efficient Knowledge Transfer Strategy for Spiking Neural Networks from Static to Event Domain (**AAAI 2024**) [[paper](https://arxiv.org/pdf/2303.13077.pdf)] [[code](https://github.com/Brain-Cog-Lab/Transfer-for-DVS)]
- Brain-Inspired Spiking Neural Networks for Industrial Fault Diagnosis: A Survey, Challenges, and Opportunities [[paper](https://doi.org/10.48550/arXiv.2401.02429)]
- Scalable MatMul-free Language Modeling [[paper](https://arxiv.org/pdf/2406.02528)] [[code](https://github.com/ridgerchu/matmulfreellm)]
- SpikeNAS: A Fast Memory-Aware Neural Architecture Search Framework for Spiking Neural Network Systems [[paper](https://arxiv.org/pdf/2402.11322.pdf)]
- Astrocyte-Enabled Advancements in Spiking Neural Networks for Large Language Modeling [[paper](https://arxiv.org/pdf/2312.07625v2.pdf)]

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
<summary><b>当年另有 38 篇</b> — 会议索引，来自 TheBrainLab</summary>

- Direct Learning-Based Deep Spiking Neural Networks: A Review (**Frontiers in Neuroscience 2023**) [[paper](https://arxiv.org/pdf/2305.19725.pdf)]
- Time series prediction and anomaly detection with recurrent spiking neural networks (**IJCNN 2023**) [[paper](https://ieeexplore.ieee.org/abstract/document/10191614)]
- SpikingJelly: An open-source machine learning infrastructure platform for spike-based intelligence (**Science Advances 2023**) [[paper](https://www.science.org/doi/10.1126/sciadv.adi1480)] [[code](https://github.com/fangwei123456/spikingjelly)]
- Parallel Spiking Neurons with High Efficiency and Long-term Dependencies Learning Ability (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2304.12760)] [[code](https://github.com/fangwei123456/Parallel-Spiking-Neuron)]
- Temporal Conditioning Spiking Latent Variable Models of the Neural Response to Natural Visual Scenes (**NeurIPS 2023**) [[paper](https://arxiv.org/pdf/2306.12045.pdf)]
- SEENN: Towards Temporal Spiking Early Exit Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=mbaN0Y0QTw)]
- EICIL: Joint Excitatory Inhibitory Cycle Iteration Learning for Deep Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=OMDgOjdqoZ)]
- Addressing the speed-accuracy simulation trade-off for adaptive spiking neurons (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=Ht79ZTVMsn)]
- Enhancing Adaptive History Reserving by Spiking Convolutional Block Attention Module in Recurrent Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=aGZp61S9Lj)]
- Trial matching: capturing variability with data-constrained spiking neural networks (**NeurIPS 2023**) [[paper](https://arxiv.org/abs/2306.03603)]
- Evolving Connectivity for Recurrent Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://arxiv.org/pdf/2305.17650.pdf)]
- SparseProp: Efficient Event-Based Simulation and Training of Sparse Recurrent Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=yzZbwQPkmP)]
- Exploring Loss Functions for Time-based Training Strategy in Spiking Neural Networks (**NeurIPS 2023**) [[paper](https://openreview.net/pdf?id=8IvW2k5VeA)]
- Unleashing the Potential of Spiking Neural Networks with Dynamic Confidence (**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Unleashing_the_Potential_of_Spiking_Neural_Networks_with_Dynamic_Confidence_ICCV_2023_paper.pdf)]
- Inherent Redundancy in Spiking Neural Networks	(**ICCV 2023**) [[paper](https://arxiv.org/abs/2308.08227)]
- Temporal-Coded Spiking Neural Networks with Dynamic Firing Threshold: Learning with Event-Driven Backpropagation (**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wei_Temporal-Coded_Spiking_Neural_Networks_with_Dynamic_Firing_Threshold_Learning_with_ICCV_2023_paper.pdf)]
- Efficient Converted Spiking Neural Network for 3D and 2D Classification	(**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Lan_Efficient_Converted_Spiking_Neural_Network_for_3D_and_2D_Classification_ICCV_2023_paper.pdf)]
- SSF: Accelerating Training of Spiking Neural Networks with Stabilized Spiking Flow (**ICCV 2023**) [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_SSF_Accelerating_Training_of_Spiking_Neural_Networks_with_Stabilized_Spiking_ICCV_2023_paper.pdf)]
- Spatial-Temporal Self-Attention for Asynchronous Spiking Neural Networks (**IJCAI 2023**) [[paper](https://www.ijcai.org/proceedings/2023/0344.pdf)]
- Learnable Surrogate Gradient for Direct Training Spiking Neural Networks (**IJCAI 2023**) [[paper](https://www.ijcai.org/proceedings/2023/0335.pdf)]
- Enhancing Efficient Continual Learning with Dynamic Structure Development of Spiking Neural Networks (**IJCAI 2023**) [[paper](https://www.ijcai.org/proceedings/2023/0334.pdf)]
- Adaptive Smoothing Gradient Learning for Spiking Neural Networks (**ICML 2023**) [[paper](https://openreview.net/pdf?id=GdkwSGTpbC)]
- Surrogate Module Learning: Reduce the Gradient Error Accumulation in Training Spiking Neural Networks (**ICML 2023**) [[paper](https://openreview.net/pdf?id=zRkz4duLKp)] [[code](https://github.com/brain-intelligence-lab/surrogate_module_learning)]
- Rate Gradient Approximation Attack Threats Deep Spiking Neural Networks (**CVPR 2023**) [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Bu_Rate_Gradient_Approximation_Attack_Threats_Deep_Spiking_Neural_Networks_CVPR_2023_paper.pdf)]
- Constructing Deep Spiking Neural Networks from Artificial Neural Networks with Knowledge Distillation (**CVPR 2023**) [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Xu_Constructing_Deep_Spiking_Neural_Networks_From_Artificial_Neural_Networks_With_CVPR_2023_paper.pdf)]
- Heterogeneous neuronal and synaptic dynamics for spike-efficient unsupervised learning: Theory and design principles (**ICLR 2023**) [[paper](https://arxiv.org/pdf/2302.11618.pdf)]
- A Unified Framework of Soft Threshold Pruning (**ICLR 2023**) [[paper](https://openreview.net/forum?id=cCFqcrq0d8)] [[code](https://github.com/Yanqi-Chen/LATS)]
- Reducing ANN-SNN Conversion Error through Residual Membrane Potential (**AAAI 2023**) [[paper](https://arxiv.org/abs/2302.02091)] [[code](https://github.com/hzc1208/ANN2SNN_SRP)]
- Deep Spiking Neural Networks with High Representation Similarity Model Visual Pathways of Macaque and Mouse (**AAAI 2023**) [[paper](https://arxiv.org/abs/2303.06060)]
- ESL-SNNs: An Evolutionary Structure Learning Strategy for Spiking Neural Networks (**AAAI 2023**) [[paper](https://arxiv.org/pdf/2306.03693.pdf)]
- Exploring Temporal Information Dynamics in Spiking Neural Networks (**AAAI 2023**) [[paper](https://arxiv.org/pdf/2211.14406.pdf)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Exploring-Temporal-Information-Dynamics-in-Spiking-Neural-Networks)]
- Complex Dynamic Neurons Improved Spiking Transformer Network for Efficient Automatic Speech Recognition(**AAAI 2023**) [[paper](https://arxiv.org/pdf/2302.01194.pdf)]
- Spikingformer: Spike-driven Residual Learning for Transformer-based Spiking Neural Network [[paper](https://arxiv.org/abs/2304.11954)] [[code](https://github.com/zhouchenlin2096/Spikingformer)]
- Enhancing the Performance of Transformer-based Spiking Neural Networks by Improved Downsampling with Precise Gradient Backpropagation [[paper](https://arxiv.org/abs/2305.05954)] [[code](https://github.com/zhouchenlin2096/Spikingformer-CML)]
- Training Full Spike Neural Networks via Auxiliary Accumulation Pathway [[paper](https://arxiv.org/pdf/2301.11929.pdf)]
- MSS-DepthNet: Depth Prediction with Multi-Step Spiking Neural Network [[paper](https://arxiv.org/abs/2211.12156)]
- Auto-Spikformer: Spikformer Architecture Search [[paper](https://arxiv.org/pdf/2306.00807.pdf)]
- Advancing Spiking Neural Networks Towards Deep Residual Learning [[paper](https://arxiv.org/pdf/2112.08954.pdf)]

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
<summary><b>当年另有 9 篇</b> — 会议索引，来自 TheBrainLab</summary>

- Neuromorphic Data Augmentation for Training Spiking Neural Networks [[paper](https://arxiv.org/abs/2203.06145)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/NDA_SNN)]
- State Transition of Dendritic Spines Improves Learning of Sparse Spiking Neural Networks [[paper](https://proceedings.mlr.press/v162/chen22ac.html)] [[code](https://github.com/Yanqi-Chen/STDS)]
- Exploring Lottery Ticket Hypothesis in Spiking Neural Networks [[paper](https://arxiv.org/abs/2207.01382)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Exploring-Lottery-Ticket-Hypothesis-in-SNNs)]
- A calibratable sensory neuron based on epitaxial VO2 for spike-based neuromorphic multisensory system [[paper](https://www.nature.com/articles/s41467-022-31747-w)] [[code](https://github.com/billyuanpku96/SNN-for-sensory-neuron)]
- Training Spiking Neural Networks with Event-driven Backpropagation [[paper](https://openreview.net/forum?id=d4JmP1T45WE)] [[code](https://github.com/zhuyaoyu/SNN-event-driven-learning)]
- Training Spiking Neural Networks with Local Tandem Learning (**NeurIPS 2022**) [[paper](https://arxiv.org/pdf/2210.04532.pdf)]
- Biologically Inspired Dynamic Thresholds for Spiking Neural Networks (**NeurIPS 2022**) [[paper](https://arxiv.org/pdf/2206.04426.pdf)]
- Optimal Conversion of Conventional Artificial Neural Networks to Spiking Neural Networks (**ICLR 2022**) [[paper](https://arxiv.org/pdf/2103.00476.pdf)] [[code](https://github.com/Jackn0/snn_optimal_conversion_pipeline)]
- Multi-Level Firing with Spiking DS-ResNet: Enabling Better and Deeper Directly-Trained Spiking Neural Networks (**IJCAI 2022**) [[paper](https://arxiv.org/pdf/2210.06386.pdf)]

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
<summary><b>当年另有 4 篇</b> — 会议索引，来自 TheBrainLab</summary>

- Spiking Deep Residual Network [[paper](https://arxiv.org/pdf/1805.01352.pdf)]
- Pruning of Deep Spiking Neural Networks through Gradient Rewiring [[paper](https://arxiv.org/abs/2105.04916)] [[code](https://github.com/Yanqi-Chen/Gradient-Rewiring)]
- Optimal ANN-SNN Conversion for Fast and Accurate Inference in Deep Spiking Neural Networks [[paper](https://arxiv.org/pdf/2105.11654)] [[code](https://github.com/DingJianhao/OptSNNConvertion-RNL-RIL)]
- Training Spiking Neural Networks with Accumulated Spiking Flow (**AAAI 2021**) [[paper](https://arxiv.org/pdf/2011.05280.pdf)]

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

<sub>精选条目自动提取自 <a href="README.zh-CN.md">README.zh-CN.md</a> · 会议索引来自 <a href="https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks">TheBrainLab</a> · 由 <a href="tools/build_timeline.py">tools/build_timeline.py</a> 生成。</sub><br>
<sub>如果本项目对你有帮助，欢迎 Star 并 <a href="README.zh-CN.md#引用">引用</a>。</sub>
</div>
