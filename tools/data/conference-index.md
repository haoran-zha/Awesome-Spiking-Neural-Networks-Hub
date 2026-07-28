<!--
Full-year SNN conference index, 2021-2026 — the data file behind the "Full-year
index" tier of TIMELINE.md / TIMELINE.zh-CN.md.

Format, per paper:

    - Title (**Venue Year**). [[paper](url)][[code](url)]
      > English one-line summary — mechanism first, then the payoff.
      > zh: 中文一句话摘要——先讲机制，再讲收益。

Both one-liners are required; `python tools/build_timeline.py` warns about any
entry missing one. Keep them verb-initial, and never state a number that is not
in the paper's own abstract. Entries that duplicate a curated README pick are
dropped automatically at build time, so they can stay here.
-->
# Full-year SNN conference index (2021–2026)

Every SNN paper tracked from the year's major venues — title, venue, links, and a
one-line summary in English and 中文. Consumed by `tools/build_timeline.py`.

## Papers

### 2026

**Nature, Science, Cell**

**AAAI, ICLR**
- Robustify Spiking Neural Networks via Dominant Singular Deflation under Heterogeneous Training Vulnerability (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10010693)]
  > Deflates the dominant singular components of BPTT gradients to shrink the Hessian spectral radius, preventing collapse when a single backward pass comes from a shifted distribution.
  > zh: 正交投影剔除 BPTT 梯度的主奇异分量，压低 Hessian 谱半径，避免单次异分布反向传播导致网络崩溃。
- A Brain-Inspired Gating Mechanism Unlocks Robust Computation in Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011430)]
  > Lets membrane conductance evolve with neuronal activity so LIF gains a biological gate, filtering inputs and rejecting disturbances on noisy temporal benchmarks like SHD.
  > zh: 让膜电导随神经元活动演化，为 LIF 引入类生物门控，选择性过滤输入并抑制噪声，提升 SHD 等时序任务的鲁棒性。
- Training Deep Normalization-Free Spiking Neural Networks with Lateral Inhibition (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009258)]
  > Splits each layer into excitatory and inhibitory populations whose subtractive and divisive inhibition replaces normalization, with tailored initialization and gradient decoupling keeping deep training stable.
  > zh: 将每层拆分为兴奋性与抑制性神经元群，用减性与除性侧抑制取代归一化层，配合专门初始化与梯度解耦稳定深层训练。
- 3DSMT: A Hybrid Spiking Mamba-Transformer for Point Cloud Analysis (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10010096)]
  > Pairs a spiking local offset attention module with a spiking Mamba block, capturing point-cloud geometry locally while integrating global context at linear complexity.
  > zh: 将 Spiking Local Offset Attention 与脉冲 Mamba 模块结合，兼顾点云局部几何细节与线性复杂度的全局建模，降低能耗。
- Neural Dynamics Self-Attention for Spiking Transformers (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007889)]
  > Adds a local receptive-field bias and realizes attention through charge-fire-reset dynamics, avoiding explicit attention-matrix storage at inference.
  > zh: 为脉冲注意力引入局部感受野偏置，并用充电-发放-重置动力学计算注意力，推理时无需显式存储注意力矩阵。
- Time Is All It Takes: Spike-Retiming Attacks on Event-Driven Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10008650)]
  > Shifts existing spike times under jitter, delay and tamper budgets while leaving spike counts and rates intact, exposing a temporal attack surface current defenses miss.
  > zh: 在抖动、总延迟与篡改数量预算下仅平移已有脉冲时刻，保持发放数与发放率不变，揭示现有防御忽视的时间维攻击面。
- Cannistraci-Hebb Training on Ultra-Sparse Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007264)]
  > Combines spike-correlation topology initialization with Cannistraci-Hebb link regrowth to grow ultra-sparse connectivity, cutting synaptic operations and energy on neuromorphic hardware.
  > zh: 以脉冲相关性初始化拓扑，并用 Cannistraci-Hebb 网络自动机预测突触再生，在超稀疏连接下削减突触操作与神经形态硬件能耗。
- CaRe-BN: Precise Moving Statistics for Stabilizing Spiking Neural Networks in Reinforcement Learning (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011021)]
  > Updates batch-norm moving statistics with a confidence-guided rule plus a re-calibration step, stabilizing spiking policies under reinforcement learning's shifting data without extra inference cost.
  > zh: 用置信度自适应策略更新 BN 滑动统计量并加入重校准，缓解强化学习中分布漂移导致的脉冲策略训练不稳，且不增加推理开销。
- Otters: An Energy-Efficient Spiking Transformer via Optical Time-to-First-Spike Encoding (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007423)]
  > Implements time-to-first-spike decay in indium-oxide optoelectronic synapses so device physics performs the temporal weighting, paired with a quantized ANN-to-SNN conversion for transformers.
  > zh: 让氧化铟光电突触的自然衰减直接完成 TTFS 时间加权，省去数字运算，并配套量化 ANN 到 SNN 的转换算法支撑 Transformer。
- Online Pseudo-Zeroth-Order Training of Neuromorphic Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011366)]
  > Replaces spatial backpropagation with a single noisy forward pass and direct top-down feedback, using momentum connections to tame variance and keep training on-chip friendly.
  > zh: 以单次带噪前向传播加自上而下的直接反馈取代空间反向传播，并用动量反馈连接抑制方差，更契合片上在线训练。
- SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011088)]
  > Tunes firing thresholds so most neurons spike stably while a subset adapts fast, then combines zeroth-order updates with subspace projection for on-device few-shot class-incremental learning.
  > zh: 调节发放阈值使多数神经元保持稳定发放、少数快速适应，再以零阶优化与子空间投影支撑端侧小样本类增量学习。
- Robust Spiking Neural Networks Against Adversarial Attacks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007241)]
  > Pushes membrane potentials away from threshold via a loss constraint and adds noisy firing, shrinking the pool of threshold-adjacent neurons that adversarial perturbations flip.
  > zh: 在损失中加入约束使膜电位远离阈值，并引入随机发放神经元，减少易被微小扰动翻转的阈值附近神经元，提升对抗鲁棒性。
- TP-Spikformer: Token Pruned Spiking Transformer (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10010064)]
  > Scores tokens by a spatiotemporal information-retaining criterion and early-stops uninformative ones block-wise rather than deleting them, cutting compute training-free across several spiking-Transformer backbones.
  > zh: 用时空信息保留准则评估 token 重要性，对低信息 token 采用块级提前终止而非直接删除，免训练地在多种脉冲 Transformer 上降低计算量。
- Breaking Gradient Temporal Collinearity for Robust Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10006881)]
  > Measures how gradient directions align across time steps, then inserts parametric orthogonal kernels into the direct-encoding input layer to decorrelate them and restore robustness.
  > zh: 以梯度时间共线性刻画各时间步梯度方向的一致性，并在直接编码输入层加入参数化正交核解相关，弥补直接编码的鲁棒性短板。
- Random Spiking Neural Networks are Stable and Spectrally Simple (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009762)]
  > Analyzes discrete-time LIF classifiers with Boolean Fourier tools, showing wide random networks concentrate on low-frequency components and are therefore stable under input perturbations.
  > zh: 借助布尔函数的傅里叶分析刻画离散时间 LIF 分类器，证明宽随机网络的频谱集中于低频，因而对输入扰动天然稳定。
- Many Eyes, One Mind: Temporal Multi-Perspective and Progressive Distillation for Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009850)]
  > Distills from mask-weighted teacher features to give each timestep a distinct temporal perspective, then aligns truncated predictions with the full-length one for reliable early inference.
  > zh: 为每个时间步提供掩码加权的教师特征以形成不同时序视角，并让截断预测逐步对齐全长预测，使早停推理同样可靠。
- Robust Selective Activation with Randomized Temporal K-Winner-Take-All in Spiking Neural Networks for Continual Learning (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10006915)]
  > Selects active neurons by spike-trace relevance with randomized top-k competition instead of firing-rate K-WTA, decorrelating task representations and resisting temporal perturbations during continual learning.
  > zh: 以脉冲迹相关性配合随机 top-k 竞争取代基于发放率的 K-WTA 选择激活神经元，降低任务表征重叠并增强对时间扰动的鲁棒性。
- Towards Lossless Memory-efficient Training of Spiking Neural Networks via Gradient Checkpointing and Spike Compression (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007453)]
  > Combines layer-wise gradient checkpointing with lossless spike compression and profiling-guided checkpoint placement, cutting BPTT memory up to 8x with no accuracy loss and modest slowdown.
  > zh: 将逐层梯度检查点与无损脉冲压缩结合，并按性能剖析调整检查点位置，把 BPTT 训练显存最多降至 1/8 且不损精度。
- Beyond Linear Processing: Dendritic Bilinear Integration in Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011474)]
  > Adds a bilinear dendritic integration term to the LIF neuron so single units capture input correlations and solve nonlinearly separable tasks, propagating correlation structure through depth.
  > zh: 在 LIF 神经元中引入源自神经生理实验的双线性树突整合规则，使单个神经元即可捕捉输入相关性并完成非线性分类。
- Spiking Discrepancy Transformer for Point Cloud Analysis (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011321)]
  > Measures differences between spike features to build attention for 3D point clouds, pairing local centre-neighbour geometry with macroscopic spike-intensity statistics in a hierarchical spiking Transformer.
  > zh: 通过脉冲特征之间的差异构建注意力，兼顾中心-邻域局部几何与宏观脉冲强度统计，把脉冲 Transformer 扩展到三维点云。
- PredNext: Explicit Cross-View Temporal Prediction for Unsupervised Learning in Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10010014)]
  > Trains unsupervised SNNs by predicting future steps and clips across views, improving temporal feature consistency and establishing video benchmarks on UCF101, HMDB51 and MiniKinetics.
  > zh: 跨视角预测未来时间步与视频片段，为 SNN 提供无监督训练信号，提升时序特征一致性，并在 UCF101、HMDB51、MiniKinetics 上建立基准。
- Difference Predictive Coding for Training Spiking Neural Networks (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007923)]
  > Recasts predictive-coding messages as sparse ternary spikes with adaptive threshold schedules, giving local backprop-free training that cuts inter-layer data movement by over two orders of magnitude.
  > zh: 把预测编码层间传递的稠密浮点误差换成稀疏三值脉冲并配自适应阈值，实现局部学习，层间数据搬运降低两个数量级以上。
- Advancing Spatiotemporal Representations in Spiking Neural Networks via Parametric Invertible Transformation (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10011650)]
  > Couples an invertible parametric transform with neuronal dynamics to widen the binary spike representation space, and adds an auxiliary gradient correction term against surrogate-gradient mismatch.
  > zh: 耦合可逆参数化变换与神经元动力学以扩展二值脉冲的表征空间，并引入辅助梯度校正项缓解代理梯度失配与训练振荡。
- Fractional-Order Spiking Neural Network (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009869)]
  > Replaces first-order membrane dynamics with fractional-order differential equations so neurons retain long-range non-Markovian memory, improving noise robustness at comparable energy cost, with an open toolbox.
  > zh: 用分数阶微分方程取代一阶膜电位动力学，使神经元具备长程非马尔可夫记忆，在能耗相当的前提下提升抗噪能力，并开源工具箱。
- SpikeGen: Decoupled “Rods and Cones” Visual Representation Processing with Latent Generative Framework (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009062)]
  > Fuses spike-camera and RGB streams inside a latent generative model, mirroring rod/cone separation to offset spike spatial sparsity and RGB temporal sparsity across deblurring, reconstruction and novel-view synthesis.
  > zh: 仿照视杆-视锥分工，在潜空间生成模型中融合脉冲相机与 RGB 流，互补脉冲的空间稀疏与 RGB 的时间稀疏，覆盖去模糊、重建与新视角合成。
- Biologically Plausible Learning via Bidirectional Spike-Based Distillation (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009918)]
  > Trains a feedforward and a backward spiking network jointly so perception and stimulus recall become mutual code translations, removing any need for signed error signals.
  > zh: 联合训练前馈与反向两个脉冲网络，让感知决策与刺激重建互为编码转换，无需传递带正负号的误差信号。
- Distribution-Aware Multi-Granularity Phase Coding: Towards Lower Conversion Error for Spike-Driven Large Language Models (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007555)]
  > Allocates discrete spike levels to match hidden-layer activation distributions using phase coding with multiple learnable bases, converting LLaMA to spikes by training neurons only, without weight fine-tuning.
  > zh: 以带多个可学习基的多粒度相位编码按隐层激活分布分配离散值，降低 ANN-to-SNN 转换误差；仅训练神经元即可转换 LLaMA，无需微调权重。
- SpikeStereoNet: A Brain-Inspired Framework for Stereo Depth Estimation from Spike Streams (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10007680)]
  > Estimates stereo depth directly from raw dual-view spike streams via a recurrent spiking update module that iteratively refines the estimate, released with synthetic and real densely annotated benchmarks.
  > zh: 直接从双视角原始脉冲流估计立体深度，用循环脉冲网络模块迭代细化结果，并配套发布合成与真实的稠密深度标注数据集。
- SpikePingpong: Spike Vision-based Fast-Slow Pingpong Robot System (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10008450)]
  > Pairs a fast spike-camera detector with a slower spike-oriented calibration stage and imitation-learned striking policies, hitting table-tennis balls into small target zones.
  > zh: 将脉冲相机的快速球体检测与较慢的脉冲神经校准相结合，并用模仿学习训练击球策略，实现高速乒乓球的精准落点控制。
- Spike-based Digital Brain: a novel fundamental model for brain activity analysis (**ICLR 2026**). [[paper](https://iclr.cc/virtual/2026/poster/10009923)]
  > Encodes fMRI time series as spike trains and learns driving relations between anchor and target regions, yielding activity forecasts plus disease classification and effective-connectivity inference.
  > zh: 把 fMRI 时间序列编码为脉冲序列，学习锚点脑区与目标脑区之间的时序驱动关系，同时支持活动预测、疾病分类与有效连接推断。
- Activation-wise Propagation: A One-Timestep Strategy for Spiking Neural Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37187)]
  > Propagates membrane potential across spatially adjacent neurons instead of iterating over timesteps, collapsing inference to a single step for point-cloud and event-stream backbones.
  > zh: 让膜电位在空间相邻神经元之间传递以取代逐时间步迭代，将推理压缩到单个时间步，适用于点云与事件流网络。
- SpikingIR: A Novel Converted Spiking Neural Network for Efficient Image Restoration (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37769)] 
  > Converts image-restoration ANNs into SNNs by mapping discrete spike outputs back to continuous pixel space and reclaiming residual membrane potential, curbing information loss.
  > zh: 把图像复原网络转换为 SNN：将离散脉冲输出映射回连续像素空间，并回收残余膜电位，减少转换中的信息损失。
- A Closer Look at Knowledge Distillation in Spiking Neural Network Training (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37175)] 
  > Aligns the student's spike activation maps with a saliency-scaled teacher map and smooths sparse spiking logits with Gaussian noise, closing the discrete-continuous gap in ANN-to-SNN distillation.
  > zh: 用显著性加权的教师激活图对齐学生的脉冲激活图，并以高斯噪声平滑稀疏 logits，弥合 ANN 与 SNN 输出的连续-离散差异。
- Optimization Method for Surrogate Function in Spiking Neural Networks Based on Membrane Potential Distribution (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39769)] 
  > Fits the surrogate gradient's width to the measured membrane-potential distribution and adds KL regularization plus a discretization-error correction, steadying gradient flow in deep SNN training.
  > zh: 依据膜电位分布自适应调整代理梯度的宽度，并引入 KL 散度正则与离散化误差校正，稳定深层 SNN 训练中的梯度传播。
- Parallel Training Time-to-First-Spike Spiking Neural Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37149)] 
  > Derives closed-form forward and backward equations so time-to-first-spike networks train in parallel on GPUs, and swaps the output decoder for a membrane-potential readout.
  > zh: 推导可并行的前向与反向传播公式，使 TTFS（首次脉冲时间编码）网络能在 GPU 上并行训练，并改用基于膜电位的输出解码与渐进时间步训练。
- HardF-SNN: Hardware-Friendly Quantization for Spiking Neural Networks with Efficient Integer-Arithmetic-Only Inference (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37174)] 
  > Folds batch norm into bit-shifts and rescales shared quantization scales so spiking inference runs on integers alone, validated on an FPGA accelerator.
  > zh: 将批归一化折叠为移位运算并采用比例化共享尺度量化，使脉冲推理全程只用整数运算，并在 FPGA 加速器上完成部署验证。
- SpikCommander: A High-performance Spiking Transformer with Multi-view Learning for Efficient Speech Command Recognition (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37194)] 
  > Combines multi-view temporal-aware spiking attention with a contextual channel MLP in a fully spike-driven transformer, sharpening temporal modeling for speech command recognition on SHD, SSC and GSC.
  > zh: 在全脉冲驱动 Transformer 中融合多视角时序感知脉冲注意力与上下文精修通道 MLP，以更少参数提升 SHD、SSC、GSC 上的语音命令识别。
- Timestep-Compressed Attack on Spiking Neural Networks Through Timestep-Level Backpropagation (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37479)] 
  > Backpropagates adversarial gradients per timestep for early stopping and reuses a precomputed membrane-potential warm-up, cutting the latency of gradient attacks on spiking networks.
  > zh: 按单个时间步反向传播以支持提前停止，并复用预先计算的膜电位预热阶段，降低对脉冲神经网络发起梯度攻击所需的时延。
- Firing Bits Where It Matters: Spiking-Guided Just Recognizable Distortion Modeling for Machine-Centric Video Coding (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38935)] 
  > Predicts per-region quantization parameters with a spiking network that factorizes frames into spatial, channel and temporal components, steering bits toward content that machine vision tasks actually need.
  > zh: 用脉冲网络将视频帧分解为空间结构、通道交互与时间模式以预测 QP 图，抑制机器视觉冗余，把码率优先分配给任务关键内容。
- MPD-SGR: Robust Spiking Neural Networks with Membrane Potential Distribution-Driven Surrogate Gradient Regularization (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37166)] 
  > Regularizes training to push membrane potentials out of the surrogate gradient's non-zero band, shrinking the gradient pathway that adversarial attacks exploit in spiking networks.
  > zh: 通过正则化减少落在代理梯度有效区间内的膜电位比例，削弱输入扰动的可利用梯度通路，提升 SNN 的对抗鲁棒性。
- Training-Free ANN-to-SNN Conversion for High-Performance Spiking Transformers (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37195)] 
  > Approximates Transformer nonlinearities with an exponential-decay, multi-basis spiking neuron, converting pretrained ViT, RoBERTa and GPT-2 weights without any fine-tuning.
  > zh: 用多基指数衰减脉冲神经元近似 Transformer 中的各类非线性运算，无需修改权重或微调即可转换 ViT、RoBERTa、GPT-2 等预训练模型。
- Spikingformer: A Key Foundation Model for Spiking Neural Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37207)] 
  > Merges membrane-shortcut residuals with self-attention to eliminate integer-float multiplications in the backbone, and extends the spike-driven transformer across static, neuromorphic and language benchmarks.
  > zh: 将 MS 残差连接与自注意力融合，消除主干中的整数-浮点乘法，并把全脉冲驱动 Transformer 扩展到静态图像、神经形态数据与语言任务。
- I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37179)] 
  > Converts static images into event streams by simulating microsaccadic eye movement with parallelized convolution, making synthetic pre-training viable when real event data is scarce.
  > zh: 用并行卷积模拟微眼跳，将静态图像实时转换为事件流，缓解事件数据稀缺，支持先合成预训练再在真实数据上微调。
- S³: Spiking Neurons as an Isolating Segmenter for Brain Signal Decoding (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38869)] 
  > Segments brain signals adaptively using spiking neurons' reset dynamics, and derives segmentation pseudo-labels by stochastic-greedy search to circumvent the gradient blockade against task performance.
  > zh: 借助脉冲神经元的复位机制自适应切分脑信号，并以随机贪心搜索生成分段伪标签，规避分段与任务性能之间的梯度阻断。
- TDSNNs: Competitive Topographic Deep Spiking Neural Networks for Visual Cortex Modeling (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37208)] 
  > Imposes a spatio-temporal constraint loss on spiking networks to grow cortex-like topographic maps, holding ImageNet top-1 accuracy where the topographic ANN TopoNet drops about three points.
  > zh: 为脉冲网络加入时空约束损失，复现灵长类视觉皮层的拓扑组织，ImageNet top-1 精度不降，而拓扑 ANN TopoNet 约掉 3 个点。
- Temporal Dynamics Enhancer for Directly Trained Spiking Object Detectors (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37178)] 
  > Diversifies per-timestep inputs with a spiking encoder and gates them by temporal correlation, using spike-driven attention so the added module costs a fraction of conventional attention energy.
  > zh: 用脉冲编码器打破各时间步输入雷同，以时序相关性做注意力门控，并用脉冲驱动注意力将其能耗降到常规注意力的一小部分。
- Spiking Heterogeneous Graph Attention Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39068)] 
  > Aggregates metapath neighbors with a shared single-layer convolution and semantic attention, then spikes the result into 1-bit heterogeneous-graph embeddings that cut memory and inference cost.
  > zh: 以共享参数的单层图卷积聚合元路径邻居并做语义级注意力，再用脉冲编码得到 1-bit 异质图表示，降低内存与推理开销。
- Oligodendrocyte-Driven Spiking Neural Model (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39306)] 
  > Couples each spiking neuron to an oligodendrocyte unit that modulates synaptic drive bidirectionally, diversifying spike patterns and sharpening firing precision so weak spikes are not lost.
  > zh: 为脉冲神经元配上少突胶质细胞单元进行双向调制，丰富脉冲表达的多样性并提升发放精度，使微弱脉冲不再被淹没。
- HLML-SNN：Fast Continual Learning in Spiking Neural Networks Achieved via Hebbian Learning-Driven Meta-Learning (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39942)] 
  > Splits continual learning into fast sample-level Hebbian adaptation and slower task-level meta-learning over consolidated weights, mirroring cortico-hippocampal memory transfer to limit forgetting.
  > zh: 将持续学习拆为样本级 Hebbian 快速适应与任务级元学习的权重固化两个阶段，模仿皮层-海马的记忆转移，抑制灾难性遗忘。
- DS-ATGO: Dual-Stage Synergistic Learning via Forward Adaptive Threshold and Backward Gradient Optimization for Spiking Neural Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37165)] 
  > Adapts firing thresholds from membrane-potential dynamics at each timestep while reshaping the surrogate gradient backward, balancing firing rates across layers so deep neurons still receive gradient.
  > zh: 前向按各时间步的膜电位动态自适应调节阈值，后向同步优化代理梯度，均衡各层发放率，让深层神经元也能拿到梯度。
- Pseudo-Spiking Neurons: A Noise-Based Training Framework for Heterogeneous-Latency Spiking Neural Networks (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40086)] 
  > Turns each neuron's timestep count into a learnable parameter by emulating spike discretization with tunable noise, training heterogeneous-latency networks in one BPTT-free pass.
  > zh: 用可学习噪声模拟脉冲的截断与量化，把每个神经元的时间步数变成可反传优化的参数，无需 BPTT 即可训练异构延迟网络。
- Spatial-Frequency Spiking Neural Network for Underwater Object Detection (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39109)] 
  > Fuses spatial and frequency-domain features inside spiking blocks to sharpen edges and texture in turbid water, converting a YOLOX detector from ANN to SNN for low-power deployment.
  > zh: 在脉冲模块中融合空域与频域特征，强化浑浊水下的边缘与纹理，并把 YOLOX 由 ANN 转换为 SNN，实现低功耗水下目标检测。
- SFedHIFI: Fire Rate-Based Heterogeneous Information Fusion for Spiking Federated Learning (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39787)] 
  > Decomposes SNN weights channel-wise so resource-poor clients train narrower models, then fuses firing-rate information across widths to aggregate heterogeneous clients into one federated model.
  > zh: 按通道分解权重让资源受限客户端只训练更窄的 SNN，再基于发放率跨宽度融合信息，使异构客户端能在联邦学习中统一聚合。
- Dynamic Weight Adaptation in Spiking Neural Networks Inspired by Biological Homeostasis (**AAAI 2026**).[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40146)] 
  > Ports the BCM homeostatic rule into spiking networks to retune weights online, stabilizing neuronal activity for obstacle avoidance and continuous control under degraded conditions without any fine-tuning.
  > zh: 把 BCM 稳态理论引入脉冲网络，在运行中实时调整权重以稳定神经元活动，无需微调即可改善退化条件下的避障与连续控制。
- GT-SNT: A Linear-Time Transformer for Large-Scale Graphs via Spiking Node Tokenization (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/38667)] 
  > Tokenizes graph nodes as spike counts from multi-step propagation, replacing predefined codebooks, and attends node-to-token so global context aggregation costs linear rather than quadratic time.
  > zh: 以多步特征传播后的脉冲计数作为节点 token，免去预定义码本，并通过 node-to-token 注意力把全局聚合降到线性复杂度。
- Exploring the Potentials of Spiking Neural Networks for Image Deraining (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37295)] 
  > Extends the LIF neuron with spatial context to counter frequency-domain saturation, then decomposes and enhances rain features across scales, deraining at 13% of prior SNN energy.
  > zh: 为 LIF 神经元补上空间上下文以缓解频域饱和，再做脉冲分解增强与多尺度表示，图像去雨能耗仅为已有 SNN 方法的 13%。
- Spiking-Aided Neural Architecture for Efficient and Robust WiFi Sensing (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39589)] 
  > Couples noise-resistant spiking neurons with conventional ANN feature extractors for WiFi indoor sensing, improving robustness to multipath fading and accelerating convergence.
  > zh: 将抗噪的脉冲神经元与常规 ANN 特征提取器结合用于 WiFi 室内感知，缓解多径衰落干扰并加快训练收敛。
- Stabilizing Spiking Neurons Through Biologically Inspired Polarization (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/39435)] 
  > Models depolarization, repolarization and hyperpolarization analytically to bound membrane potentials, stabilizing gradient flow in deep SNNs without learnable gates or surrogate-gradient tuning.
  > zh: 以解析式膜动力学刻画去极化、复极化与超极化，把膜电位约束在合理区间，稳定深层网络梯度，无需可学习门控与代理梯度调参。
- Spike Stream Memory Transfer for Dynamic Scene Reconstruction (**AAAI 2026**). 
  > Carries previously inferred light intensity and motion forward as memory across spike-stream clips, extending temporal context and suppressing inter- and intra-clip motion blur during reconstruction.
  > zh: 借鉴视觉记忆机制，将此前推断的光强与运动信息前传，扩展脉冲流的长时感知范围，并抑制片段间与片段内的运动模糊。
- LAS: Loss-less ANN-SNN Conversion for Fully Spike-Driven Large Language Models (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37151)] 
  > Converts pretrained LLMs into fully spike-driven models with two neuron types for activation outliers and nonlinear operations plus spike-equivalent Transformer blocks, reporting loss-less conversion.
  > zh: 用两类新神经元处理激活离群值与非线性算子，并配以脉冲等价的 Transformer 组件，把预训练 LLM 无损转换为全脉冲驱动模型。
- Spike Imaging Velocimetry: Dense Motion Estimation of Fluids Using Spike Streams (**AAAI 2026**).
  > Estimates dense fluid velocity fields from spike-camera streams via hierarchical detail-preserving transforms, a graph encoder and multi-scale refinement, released with a labelled particle-imaging benchmark.
  > zh: 以细节保持的分层变换、图编码器与多尺度细化，从脉冲相机流估计复杂流场的稠密速度场，并发布带标注的粒子成像数据集。
- BulletTime4D: Towards High Spatio-Temporal Resolution Dynamic Scene Rendering via Spike-Guided Stereo Vision (**AAAI 2026**).
  > Pairs a spike camera with binocular RGB cameras and fuses low-frequency spatio-temporal features with high-frequency inter-frame motion, rendering dynamic scenes at higher spatio-temporal resolution.
  > zh: 将脉冲相机与双目 RGB 相机联合，用多时间尺度形变表示融合低频时空特征与高频帧间运动，提升动态场景渲染的时空分辨率。
- Robust Noise Modeling for Spike Camera via Time-Interval Quantification and Spike-DSLR Multimodal Dataset in Low-Light Imaging (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37252)]
  > Measures spike-camera noise through an exposure-time-inspired interval quantification and releases the first aligned spike-DSLR capture set, sharpening low-light reconstruction by over 1.6 dB PSNR.
  > zh: 借鉴传统相机曝光时间提出时间间隔量化以精确刻画脉冲相机噪声，并发布首个脉冲-DSLR 对齐数据集，低光重建 PSNR 提升逾 1.6 dB。
- Generalized Threshold Optimization with Harmony Multi-Threshold Neurons for Accurate ANN-to-SNN Conversion (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37206)] 
  > Fires multiple spikes per step to drain residual membrane potential and optimizes thresholds generically across neuron variants, cutting the time steps ANN-to-SNN conversion requires.
  > zh: 让神经元单步发放多次脉冲以释放残余膜电位，并给出可迁移到多种神经元变体的通用阈值优化，减少 ANN 转 SNN 所需时间步。
- HypoxSpike: Ternary Spiking Neural Network for Opioid Overdose Detection (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/41237)] 
  > Fuses motion, respiration and oxygen-saturation signals in a ternary spiking network for shoulder-worn wearables, classifying hypoxemia stages while cutting false alarms and pulse-oximetry skin-tone bias.
  > zh: 用三值脉冲网络融合运动、呼吸与血氧信号，在肩戴式低功耗设备上分级识别低氧血症，降低误报率并修正脉搏血氧的肤色偏差。
- Bi-Spectrum Distillation: Addressing Spectral Mismatch in ANN-SNN Knowledge Transfer (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/40085)] 
  > Attributes ANN-to-SNN distillation loss to the SNN's low-pass behaviour, recovering high-frequency feature detail with a learnable filter and distilling high-frequency components of teacher logits.
  > zh: 针对脉冲网络的低通特性导致的频谱失配，用可学习滤波器在特征层补回高频细节，并在 logits 层蒸馏教师输出的高频分量。
- Towards Training-Free and Accurate ANN-to-SNN Conversion via Activation-Aware Redistribution (**AAAI 2026**). [[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37148)] 
  > Traces training-free conversion error to distribution mismatch and fits channel-wise parameters in adaptive integrate-and-fire neurons to realign spike rates, extending cleanly to Transformer backbones.
  > zh: 将免训练转换误差归因于分布失配，为自适应 IF 神经元引入逐通道参数以校准发放率，几乎零开销地适配 Transformer 主干。


### 2025

**Nature, Science, Cell**
- Spiking neural networks with fatigue spike-timing-dependent plasticity learning using hybrid memristor arrays (**Nature Electronics 2026**). [[paper](https://www.nature.com/articles/s41928-025-01554-4)]
  > Pairs a dynamic memristor's intrinsic fatigue with a non-volatile 1T1R cell so one synapse carries both short- and long-term traces, realizing fatigue-STDP for noise-tolerant online learning.
  > zh: 将动态忆阻器的固有疲劳特性与非易失 1T1R 单元配对，使单个突触同时承载短时与长时记忆，在硬件上实现 fatigue-STDP 的无监督在线学习。
- Neuromorphic computing paradigms enhance robustness through spiking neural networks (**Nature Communications 2025**). [[paper](https://www.nature.com/articles/s41467-025-65197-x)][[code](https://github.com/DingJianhao/SNNEnhancingRobustness)]
  > Front-loads task-critical information in the spike sequence and exits decoding early, letting SNNs discard later adversarial perturbations and outperform ANNs on robustness.
  > zh: 把任务关键信息前置到脉冲编码序列的早期，并采用提前退出解码忽略后段扰动，使脉冲神经网络的对抗鲁棒性超过传统 ANN。
- A spiking artificial neuron based on one diffusive memristor, one transistor and one resistor (**Nature Electronics 2025**). [[paper](https://www.nature.com/articles/s41928-025-01488-x)][[code](https://github.com/GnohzZ/Brain-Dynamics-Modeling-Acceleration)]
  > Builds a leaky integrate-and-fire neuron from one diffusive memristor, transistor and resistor stacked into a single-transistor footprint, delivering refractoriness, stochasticity and intrinsic plasticity at picojoule-per-spike cost.
  > zh: 用扩散型忆阻器、晶体管与电阻堆叠出单晶体管面积的神经元，具备阈值发放、不应期、随机性与内在可塑性，每脉冲能耗低至皮焦级。
- A biologically inspired artificial neuron with intrinsic plasticity based on monolayer molybdenum disulfide (**Nature Electronics 2025**). [[paper](https://www.nature.com/articles/s41928-025-01433-y)]
  > Couples a wafer-scale monolayer MoS2 DRAM cell with an inverter into an integrate-and-fire neuron whose tunable membrane potential emulates intrinsic plasticity and photopic-scotopic visual adaptation.
  > zh: 以晶圆级单层 MoS2 的 DRAM 单元加反相器构成积分发放神经元，通过调制膜电位模拟内在可塑性与人眼明暗视觉适应。
- Modeling macroscopic brain dynamics with brain-inspired computing architecture (**Nature Communications 2025**). [[paper](https://www.nature.com/articles/s41467-025-64470-3)]
  > Quantizes macroscopic brain-dynamics models in a dynamics-aware way and maps them hierarchically onto brain-inspired chips and GPUs, accelerating whole-brain simulation while preserving functional fidelity.
  > zh: 用面向动力学的量化与分层并行映射，将宏观脑动力学模型以低精度部署到类脑芯片和 GPU，在保持功能保真度的同时大幅加速仿真。
- A frugal Spiking Neural Network for unsupervised multivariate temporal pattern classification and multichannel spike sorting (**Nature Communications 2025**). [[paper](https://www.nature.com/articles/s41467-025-64231-2)][[code](https://codeocean.com/capsule/9829487/tree)]
  > Combines STDP, short-term and intrinsic plasticity in a single spiking layer to cluster recurring multivariate temporal motifs online, demonstrated on speech features and multichannel spike sorting.
  > zh: 在单层脉冲网络中联合 STDP、短时可塑性与内在可塑性，全无监督地在线聚类多变量时序模式，并用于语音特征与多通道 spike sorting。
- Efficient and robust temporal processing with neural oscillations modulated spiking neural networks (**Nature Communications 2025**). [[paper](https://www.nature.com/articles/s41467-025-63771-x)][[code](https://github.com/YinsongYan/Rhythm-SNN)]
  > Gates neurons with heterogeneous oscillatory signals so each stays active only within its own periodic window, cutting firing rates while improving long-range temporal processing and noise robustness.
  > zh: 用异质振荡信号调制脉冲神经元，使其只在各自的周期窗口内活跃，降低发放率并提升长时序处理能力与抗噪鲁棒性。
- Covariant spatio-temporal receptive fields for spiking neural networks (**Nature Communications 2025**). [[paper](https://www.nature.com/articles/s41467-025-63493-0)][[code](https://github.com/jegp/nrf)]
  > Derives spatio-temporal receptive fields from affine Gaussian kernels and leaky-integrator dynamics, provably covariant to affine and temporal scaling, and uses them as a prior improving event-based vision training.
  > zh: 用仿射高斯核与漏积分动力学构造时空感受野，对仿射与时间尺度变换保持协变，并作为先验改善事件相机上的脉冲网络训练。
- A multisynaptic spiking neuron for simultaneously encoding spatial and temporal dynamics in spiking neural networks (**Nature Communications 2025**). [[paper](https://doi.org/10.1038/s41467-025-62251-6)][[code](https://github.com/fanliangwei/Multisynaptic-spiking-neurons)]
  > Gives each axon multiple synapses with distinct thresholds on the postsynaptic neuron, so firing rate encodes input intensity while spike timing encodes temporal structure, generalizing LIF and ReLU.
  > zh: 让同一轴突在突触后神经元上建立多个不同阈值的突触，使发放率编码空间强度、脉冲时刻编码时间动态，并把 LIF 与 ReLU 纳为特例。
- Advancing spatio-temporal processing through adaptation in spiking neural networks (**Nature Communications 2025**). [[paper](https://www.nature.com/articles/s41467-025-60878-z)][[code](https://github.com/IGITUGraz/SE-adlif)]
  > Traces adaptive-LIF instability to Euler-forward discretization and switches to a symplectic Euler update, widening usable parameter ranges and lifting accuracy on event-based sequence benchmarks.
  > zh: 把自适应 LIF 的不稳定性归因于前向 Euler 离散化，改用辛 Euler 更新以拓宽可用参数范围，并在事件式时序基准上提升精度。
- Topology optimization of random memristors for input-aware dynamic SNN (**Science Advances 2025**). [[paper](https://www.science.org/doi/10.1126/sciadv.ads5340)][[code](https://github.com/bo-wang-up/PRIME)]
  > Prunes the topology of a randomly programmed memristive SNN to absorb device stochasticity and halts inference early per input, trimming latency on in-memory computing macros.
  > zh: 受结构可塑性启发剪枝随机忆阻 SNN 的拓扑以吸收器件编程随机性，并按输入难度提前停止推理，在存内计算宏上降低延迟与能耗。
- Fully memristive spiking neural network for energy-efficient graph learning (**Science Advances 2025**). [[paper](https://www.science.org/doi/10.1126/sciadv.adv2312)]
  > Finds shortest paths by letting spikes propagate in parallel through RRAM synapses and threshold-switching neurons, replacing arithmetic search and compensating neuron nonlinearity via nonlinear weight mapping.
  > zh: 用 RRAM 突触与 NbOx 阈值开关神经元让脉冲并行传播求最短路径，替代算术搜索，并以非线性权重映射补偿神经元非线性以支撑大规模图。
  
**AAAI, ICLR, CVPR, ICML, IJCAI, ICCV, ACM MM, Neurips**
- Adaptive Surrogate Gradients for Sequential Reinforcement Learning in Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=oGmROC4e4W)] [[code](https://github.com/korneelf1/SpikingCrazyflie)]
  > Schedules the surrogate-gradient slope to trade gradient magnitude against alignment, and bootstraps the spiking policy from a privileged guiding teacher, enabling real-world drone position control.
  > zh: 调度代理梯度斜率以平衡梯度幅值与方向一致性，并用特权引导策略热启动脉冲策略，使有状态强化学习可用于无人机位置控制。
- Toward Relative Positional Encoding in Spiking Transformers (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=MDWJlTWZHH)] [[code](https://github.com/microsoft/SeqSNN)]
  > Encodes relative distance with Gray code, whose binary patterns keep constant Hamming distance across power-of-two offsets, plus a log-distance variant folded directly into the spiking attention map.
  > zh: 用格雷码编码相对距离，使偏移为 2 的幂时汉明距离恒定；并给出将对数距离矩阵直接融入脉冲注意力图的 Log-PE，支持二维图块。
- High Dynamic Range Imaging with Time-Encoding Spike Camera (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=flIdch9eTf)] [[code](https://github.com/zkzhu123/TESC)]
  > Records when a fixed spike count overflows using cycles of a high-frequency timing signal instead of counting spikes, extending spike-camera dynamic range with few bits.
  > zh: 改用高频计时信号的周期数记录脉冲溢出时刻，替代逐次计数，以更少比特位宽扩展 spike camera 的动态范围。
- Bipolar Self-attention for Spiking Transformers (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=nG45z7lJ7D)] [[code](https://openreview.net/attachment?id=nG45z7lJ7D&name=supplementary_material)]
  > Models homopolar and heteropolar membrane-potential interactions with ternary matrix multiplication, adding a shift-based Softmax approximation that partly restores row-stochastic attention while staying fully spike-driven.
  > zh: 用三值矩阵乘法建模 Query 与 Key 的同极性与异极性膜电位交互，并以移位式 Softmax 近似 Shiftmax 部分恢复注意力行随机性，全程保持脉冲驱动。
- Spike-timing-dependent Hebbian learning as noisy gradient descent (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=YTbLri0siT)]
  > Recasts Hebbian spike-timing-dependent plasticity as noisy gradient descent on the probability simplex, proving the rule converges to the most active presynaptic neuron and linking it to mirror descent.
  > zh: 把 Hebbian 型 STDP 规则改写为概率单纯形上的含噪梯度下降，证明其最终选出活动最强的突触前神经元，并揭示与镜像下降的联系。
- Spike-RetinexFormer: Rethinking Low-light Image Enhancement with Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=8W8SRZIpJP)]
  > Rebuilds Retinex-based low-light enhancement entirely from spiking operators inside a Transformer backbone, matching strong ANN restoration quality at comparable parameters and lower theoretical energy and memory traffic.
  > zh: 用脉冲算子在 Transformer 架构中重建 Retinex 分解流程，在参数量相当、理论能耗与访存更低的情况下逼近 ANN 的低光增强画质。
- SPACE: SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=Di0RasgbQ6)] [[code](https://github.com/ethanxyluo/SPACE)]
  > Adapts a trained SNN at test time by maximizing spike-behavior consistency across augmentations of one test sample, absorbing distribution shift without any source data.
  > zh: 最大化单个测试样本各增强视图间的脉冲发放行为一致性，无需源数据即可让 SNN 在测试时适应分布偏移。
- MI-TRQR: Mutual Information-Based Temporal Redundancy Quantification and Reduction for Energy-Efficient Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=NRqGpUAjV9)] [[code](https://github.com/dfxue/MI-TRQR)]
  > Quantifies mutual information between spike features at different timesteps on local and global spatial scales, then probabilistically masks redundant spikes to raise sparsity without adding parameters.
  > zh: 度量不同时间步脉冲特征在像素级与全局尺度上的互信息冗余，再用概率掩码剔除冗余脉冲，无需额外参数即可提升稀疏度。
- Spik-NeRF: Spiking Neural Networks for Neural Radiance Fields (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=047VzZEpnu)] 
  > Swaps binary for ternary spike neurons in neural radiance fields, re-parameterizing at inference to stay multiplication-free while ANN-teacher distillation closes the rendering-quality gap.
  > zh: 改用三值脉冲神经元提升 NeRF 渲染中的信息容量，推理时重参数化以保持无乘法事件驱动，并借 ANN 教师蒸馏补齐画质。
- Dendritic Resonate-and-Fire Neuron for Effective and Efficient Long Sequence Modeling (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=ywzGKDStrm)] [[code](https://openreview.net/attachment?id=ywzGKDStrm&name=supplementary_material)]
  > Splits a resonate-and-fire neuron into dendritic branches tuned to separate frequency bands and adds a history-driven adaptive threshold, extending memory for long sequences while keeping spikes sparse.
  > zh: 把谐振-发放神经元拆成编码不同频段的多条树突分支，并在胞体引入随发放历史自适应的阈值，延长记忆跨度并保持脉冲稀疏。
- Spiking Neural Networks Need High-Frequency Information (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=owNPAl7LNK)] [[code](https://github.com/bic-L/MaxFormer)]
  > Shows spiking neurons act as low-pass filters, then restores high-frequency detail with extra max-pooling in patch embedding and depth-wise convolution replacing early self-attention.
  > zh: 指出脉冲神经元本质上是低通滤波器，并用 patch embedding 中的额外最大池化与浅层深度卷积替代自注意力，补回被抑制的高频信息。
- Activity Pruning for Efficient Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=zjOXZEXQKZ)] [[code](https://github.com/putshua/Activity-Pruning-SNN)]
  > Suppresses neuronal firing with an AT-LIF neuron and threshold adaptation that stabilizes sparse training, cutting synaptic operations and stacking with weight-based pruning.
  > zh: 改用 AT-LIF 神经元并自适应调整阈值，稳定稀疏训练的同时压低平均发放率与突触操作数，可与权重剪枝叠加。
- Multiplication-Free Parallelizable Spiking Neurons with Efficient Spatio-Temporal Dynamics (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=4q5ZYP0ynu)] [[code](https://github.com/PengXue0812/Multiplication-Free-Parallelizable-Spiking-Neurons-with-Efficient-Spatio-Temporal-Dynamics)]
  > Parallelizes neuron dynamics with channel-wise convolution and sawtooth dilations to lower the required order, replacing multiplications with bit shifts for cheaper training and hardware.
  > zh: 用逐通道卷积增强并行脉冲神经元的表达力，以锯齿状膨胀降低所需阶数，并以移位运算取代乘法，兼顾训练速度与硬件开销。
- SpikingVTG: A Spiking Detection Transformer for Video Temporal Grounding (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=SkhF3cuyev)] [[code](https://openreview.net/attachment?id=SkhF3cuyev&name=supplementary_material)]
  > Gates video clips by feedback saliency inside a multimodal spiking detection Transformer, training without BPTT via implicit differentiation at equilibrium and distilling from a non-spiking teacher.
  > zh: 用显著性反馈门控在多模态脉冲检测 Transformer 中放大相关视频片段，借平衡点隐式微分实现免 BPTT 训练，并从非脉冲教师蒸馏。
- S²M-Former: Spiking Symmetric Mixing Branchformer for Brain Auditory Attention Detection (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=WtMuGdHvh6)] [[code](https://github.com/JackieWang9811/S2M-Former)]
  > Mirrors parallel spatial and frequency branches with spike-driven token-channel mixers for EEG auditory attention decoding, swapping 3D operations for 1D token sequences to shrink parameters.
  > zh: 用镜像对称的空间与频率双分支及脉冲驱动 token-channel 混合器解码 EEG 听觉注意，并以一维 token 序列取代三维运算压缩参数与能耗。
- Local-Global Coupling Spiking Graph Transformer for Brain Disorders Diagnosis from Two Perspectives (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=kkhRTTmXFV)]
  > Couples locally constrained spiking population dynamics with globally optimized graph convolution, reading brain-disorder signatures from both inter-regional connectivity and abnormal regional firing rates.
  > zh: 耦合局部受限的脉冲群体动力学与全局优化的图卷积，从脑区间连接拓扑与脑区异常发放率两个视角刻画脑疾病特征。
- A Scalable, Causal, and Energy Efficient Framework for Neural Decoding with Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=oAbaGU9N1X)] [[code](https://spikachu-bci.github.io/)]
  > Projects binned neural spikes into a shared latent space processed by causal spiking modules, enabling real-time brain-computer-interface decoding that transfers few-shot across sessions and subjects.
  > zh: 将分箱脉冲投影到共享隐空间，由因果脉冲模块提取特征，实现低功耗实时脑机接口解码，并可少样本迁移到新会话与新个体。
- Spiking Meets Attention: Efficient Remote Sensing Image Super-Resolution with Attention Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=VaE33hkqmg)] [[code](https://github.com/XY-boy/SpikeSR)]
  > Modulates membrane potentials with inferred attention weights that jointly couple temporal and channel dimensions, exploiting global self-similarity for efficient remote-sensing image super-resolution.
  > zh: 用推断的注意力权重调制膜电位，联合建模时间与通道维度并利用遥感影像的全局自相似性，实现高效超分辨率重建。
- Adaptive Fission: Post-training Encoding for Low-latency Spike Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=2zZzdAMyYi)] [[code](https://github.com/JiangYizhou16/Adaptive-Fission)]
  > Splits sensitivity-critical neurons into groups with distinct scales and thresholds after training, cutting the timesteps rate-coded and converted SNNs need without any fine-tuning.
  > zh: 训练后将高敏感神经元裂分为不同尺度与阈值的神经元组，作为 population coding 的推广，无需微调即可降低率编码 SNN 的时间步与延迟。
- S²NN: Sub-bit Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=hFsCuVc1cB)] [[code](https://openreview.net/attachment?id=hFsCuVc1cB&name=supplementary_material)]
  > Compresses binary SNN weights below one bit by clustering kernel codewords, with outlier-aware quantization correcting the selection bias that skews training.
  > zh: 借助二值 SNN 卷积核的聚类规律把权重压缩到一比特以下，并用离群点感知量化 OS-Quant 校正码字选择偏差，降低存储与算力需求。
- Seemingly Redundant Modules Enhance Robust Odor Learning in Fruit Flies (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=d6WUTRJqP3)] [[code](https://github.com/L-0cean/Fly-SNN)]
  > Models fly olfactory circuits to separate the roles of lateral inhibition and spike-frequency adaptation, showing adaptation sustains odor discrimination as noise rises while inhibition fades.
  > zh: 用果蝇嗅觉环路模型拆解侧抑制与脉冲频率适应的分工：前者仅在中低噪声下有益，后者在各噪声水平都能提升气味辨别。
- Fully Spiking Neural Networks for Unified Frame-Event Object Tracking (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=FooiwsnEH9)] [[code](https://github.com/Noctis-A/SpikeFET)]
  > Fuses frame and event streams entirely in spikes by pairing spiking convolution with spiking Transformer blocks, restoring translation invariance via randomized patch reorganization.
  > zh: 在全脉冲框架内融合图像帧与事件流，卷积局部特征与 Transformer 全局建模并行，并用随机拼块模块消除卷积填充带来的位置偏置。
- Enhanced Self-Distillation Framework for Efficient Spiking Neural Network Training (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=dpmMg6aK1D)] [[code](openreview.net/pdf?id=dpmMg6aK1D)]
  > Distills intermediate firing rates through lightweight ANN branches trained with rate-based backpropagation, filtering unreliable teacher signals to cut BPTT's timestep-linear training cost.
  > zh: 把中间层发放率投影到轻量 ANN 分支做自蒸馏，并结合基于发放率的反传，剔除不可靠教师信号，避免 BPTT 随时间步线性增长的开销。
- Learning the Plasticity: Plasticity-Driven Learning Framework in Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=fllsm01JWS)] 
  > Learns synaptic plasticity rules rather than fixed weights, redefining functional and presynaptic-dependent plasticity so spiking networks adapt online and handle working-memory and multitask settings.
  > zh: 训练突触可塑性规则而非固定权重，重构功能性与突触前依赖可塑性，使脉冲网络在线适应动态环境，提升工作记忆与多任务能力。
- HetSyn: Versatile Timescale Integration in Spiking Neural Networks via Heterogeneous Synapses (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=YYz4fumVed)] [[code](https://github.com/dzcgood/HetSyn)]
  > Gives every synapse its own time constant, shifting temporal integration from membrane potential to synaptic current so one LIF variant spans diverse timescales.
  > zh: 为每个突触赋予独立时间常数，把时间积分从膜电位转移到突触电流，使单一 LIF 变体覆盖多种时间尺度，并增强噪声鲁棒性与工作记忆。
- Unveiling the Spatial-temporal Effective Receptive Fields of Spiking Neural Networks (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=tYnJC5ba6j)] [[code](https://github.com/EricZhang1412/Spatial-temporal-ERF)]
  > Measures spatio-temporal effective receptive fields to expose weak global context in spiking Transformers, then widens early-stage fields with MLPixer and splash-and-reconstruct channel mixers for detection and segmentation.
  > zh: 提出时空有效感受野指标，揭示脉冲 Transformer 缺乏全局时空感受野，并用 MLPixer 与 SRB 两种通道混合模块在浅层扩大感受野，改善检测与分割。
- Brain-like Variational Inference (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=573IcLusXq)] [[code](https://github.com/hadivafaii/IterativeVAE)]
  > Derives inference dynamics from natural gradients on free energy, yielding a recurrent spiking VAE that replaces amortized encoders with membrane-potential updates and integer spike counts.
  > zh: 从自由能的自然梯度推导推断动力学，得到循环脉冲 VAE：用膜电位迭代更新取代摊销编码器，并以整数脉冲计数表示，便于硬件实现。
- Proxy Target: Bridging the Gap Between Discrete Spiking Neural Networks and Continuous Control (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=RRBve5GwjS)] [[code](openreview.net/pdf?id=RRBve5GwjS)]
  > Trains a continuous differentiable proxy network to supply smooth target updates for spiking reinforcement learners, stabilizing continuous control while the deployed SNN stays overhead-free.
  > zh: 引入连续可微的代理网络提供平滑目标更新，化解目标网络软更新与脉冲离散动力学的冲突，代理仅用于训练，部署无额外开销。
- Synergy Between the Strong and the Weak: Spiking Neural Networks are Inherently Self-Distillers (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=BrmR69AhUg)]
  > Treats each timestep of an SNN as a submodel ranked by output confidence, then distills strong into weak and weak into strong without any external teacher.
  > zh: 把 SNN 每个时间步视作一个子模型并按置信度分强弱，双向自蒸馏（强教弱、弱教强），无需外部教师即可提升精度与对抗鲁棒性。
- Spike4DGS: Towards High-Speed Dynamic Scene Recontruction with 4D Gaussian Splatting via a Spike Camera Array (**NeurIPS 2025**). [[paper](https://openreview.net/pdf?id=V5efEA8nIr)] [[code](https://github.com/Qinghongye/Spike4DGS)]
  > Reconstructs fast-moving scenes from a multi-view spike-camera array, deriving dense point clouds and poses from continuous spike streams to initialize 4D Gaussian splatting.
  > zh: 用多视角脉冲相机阵列拍摄高速动态场景，从连续脉冲流中恢复稠密点云与相机位姿，为 4D Gaussian Splatting 提供初始化，并配套合成与真实数据集。
- Toward End-to-End Bearing Fault Diagnosis for Industrial Scenarios with Spiking Neural Networks (**KDD 2025**). [[paper](https://doi.org/10.48550/arXiv.2408.11067)][[code](https://github.com/yqding326/MRA-SNN)]
  > Encodes raw vibration signals directly into spatio-temporal spikes via multi-scale attention, then sharpens sparse spike features with residual and dendrite-inspired attention for end-to-end bearing fault diagnosis.
  > zh: 用多尺度注意力将原始振动信号直接编码为时空脉冲，免去预处理，再以脉冲残差注意力增强稀疏特征，实现端到端轴承故障诊断。
- DSF-Net: Dynamic Sparse Fusion of Event-RGB via Spike-Triggered Attention for High-Speed Detection (**ACM MM 2025**). 
  > Fuses RGB frames with event streams via spike-triggered dynamic sparse attention that selects discriminative features, and contributes a large-scale high-speed Event-RGB detection benchmark.
  > zh: 以脉冲触发的动态稀疏注意力筛选并融合 Event 与 RGB 的判别性特征，并发布面向高速目标检测的大规模双模态基准数据集。
- ESOD: Event-Based Small Object Detection (**ACM MM 2025**). 
  > Aggregates sparse event features inside the backbone and refines them with a coarse-to-fine deformable head, recovering discriminative detail small objects lose, and collects a real-world event benchmark.
  > zh: 在主干中聚合稀疏事件特征，再由粗到细的可变形检测头逐级细化，弥补小目标的判别信息缺失，并采集真实场景的事件基准。
- E-4DGS: High-Fidelity Dynamic Reconstruction from the Multi-view Event Cameras (**ACM MM 2025**). 
  > Drives 4D Gaussian Splatting purely from multi-view event streams, adding event-based initialization, time-aware adaptive slicing and intensity-importance pruning to suppress floaters in fast, low-light scenes.
  > zh: 仅用多视角事件流驱动 4D 高斯泼溅，通过事件初始化、时间自适应切片与强度重要性剪枝抑制漂浮伪影，重建高速与低光动态场景。
- Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics (**ACM MM 2025**). 
  > Raises a LIF neuron's threshold immediately after each spike to emulate the biological refractory period, curbing over-excitation and aberrant-input interference at negligible extra cost.
  > zh: 通过脉冲触发的阈值动态在发放后短暂抬高阈值，为 LIF 神经元引入不应期，抑制过度兴奋与异常输入干扰，几乎不增开销。
- Signal-SGN: A Spiking Graph Convolutional Network for Skeleton Action Recognition via Learning Temporal-Frequency Dynamics (**ACM MM 2025**). 
  > Treats skeleton frames as spike timesteps and combines 1D spiking graph convolution with frequency-domain convolution and multi-scale wavelet fusion, capturing skeleton dynamics at spiking-network energy cost.
  > zh: 把骨架序列的时间维当作脉冲时间步，联合一维脉冲图卷积、频域脉冲卷积与多尺度小波融合建模时频动态，以低能耗完成动作识别。
- SGM-Transformer: Rethinking Gradient Information Loss and Compensation in Spiking Neural Networks (**ACM MM 2025**). 
  > Compensates vanishing surrogate gradients with an MCLIF neuron that routes gradient information across time and space, and embeds a QK memory so attention reuses earlier timesteps.
  > zh: 用 MCLIF 神经元从时间与空间双维度补偿反向传播中损失的梯度，并以 QK Memory 嵌入时序特征，让脉冲注意力跨时间步复用信息。
- Advanced SpikingYOLOX: Extending Spiking Neural Network on Object Detection with Spike-based Partial Self-Attention and 2D-Spiking Transformer (**ACM MM 2025**). 
  > Inserts spike-based partial self-attention and a 2D spiking Transformer at the deepest backbone stage, and reassigns spiking layers across query, key and value for detection accuracy.
  > zh: 在主干最深层引入基于脉冲的部分自注意力与二维脉冲 Transformer，并重新分配 Q/K/V 上的脉冲层位置，提升 SNN 目标检测精度。
- Spiking Neural Networks with Temporal Attention-Guided Adaptive Fusion for imbalanced Multi-modal Learning (**ACM MM 2025**). 
  > Scores fused spiking features per timestep with cross-modal attention, then uses those scores to modulate each modality's learning rate so a dominant stream cannot monopolize training.
  > zh: 在每个时间步为融合后的脉冲特征打上跨模态注意力权重，并据此调节各模态学习率，缓解多模态 SNN 中的模态失衡与时间错位。
- Temporal-coded Spiking Transformer (**ACM MM 2025**). 
  > Adapts batch normalization and residual connections to time-to-first-spike coding, then builds temporal-coded spiking attention so a Transformer runs on single-spike timing instead of firing rates.
  > zh: 改造批归一化与残差连接以适配 TTFS 时间编码，并构建时间编码脉冲注意力，使 Transformer 以单次脉冲的发放时刻而非发放率承载信息。
- ClearSight: Human Vision-Inspired Solutions for Event-Based Motion Deblurring (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/1849)]  
  > Splits event-based deblurring across an SNN motion branch and an ANN color branch, with a configurator that retunes neuron parameters so spikes concentrate on blurred regions.
  > zh: 用 SNN 分支提取事件运动特征、ANN 分支处理色彩，并由神经元配置模块按跨模态特征动态调参，使脉冲集中于模糊区域完成去模糊。
- Robust Unfolding Network for HDR Imaging with Modulo Cameras (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/1986)]    
  > Recasts modulo-camera HDR recovery in the image-gradient domain and unrolls the optimization into a network whose sparsity prior is enforced by a spiking-neuron module, keeping the model light.
  > zh: 将取模相机的 HDR 重建改写到图像梯度域，把优化过程展开为网络，并用脉冲神经元模块施加可学习稀疏先验，模型轻量且更鲁棒。
- SpikeDiff: Zero-shot High-Quality Video Reconstruction from Chromatic Spike Camera and Sub-millisecond Spike Streams (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/1181)]    
  > Guides a pretrained diffusion sampler with the spike camera's imaging physics, reconstructing color video from chromatic spike streams with no domain-specific training data.
  > zh: 把脉冲相机的成像物理约束注入预训练扩散模型的采样过程，无需领域训练数据即可从彩色脉冲流零样本重建高时间分辨率视频。
- Noise-Modeled Diffusion Models for Low-Light Spike Image Restoration (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/1467)]    
  > Models low-light spike sensor noise as the forward diffusion process itself, then conditions reverse sampling on region masks, dark-current maps and spike density to restore degraded spike images.
  > zh: 把低光下脉冲成像的噪声退化直接建模为扩散前向过程，并以区域掩码、暗电流图与脉冲密度作为条件引导反向采样，复原脉冲图像。
- Efficient Spiking Point Mamba for Point Cloud Analysis (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/2271)]    
  > Ports Mamba state-space blocks into 3D spiking networks with hierarchical dynamic encoding, capturing long-range point-cloud dependencies that earlier 3D SNNs missed, and pre-trains through an asymmetric SNN-ANN architecture.
  > zh: 将 Mamba 状态空间模块引入 3D 脉冲网络，配合分层动态编码与非对称 SNN-ANN 预训练，弥补以往 3D SNN 难以建模长程依赖的缺陷。
- SpikePack: Enhanced Information Flow in Spiking Neural Networks with High Hardware Compatibility (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/345)]   
  > Redesigns the LIF neuron to cut information loss from temporal dependencies while keeping reset and leaky integration, giving O(1) cost, GPU parallelism and near-lossless ANN-to-SNN conversion.
  > zh: 重构 LIF 神经元以减少时间依赖带来的信息损失，同时保留复位与漏电积分，实现 O(1) 复杂度、GPU 并行与近乎无损的 ANN-SNN 转换。
- SpiLiFormer: Enhancing Spiking Transformers with Lateral Inhibition (**ICCV 2025**). [[paper](https://iccv.thecvf.com/virtual/2025/poster/1753)]   
  > Emulates cortical lateral inhibition inside spiking attention, sharpening focus on relevant tokens and suppressing the irrelevant context that attention modules borrowed from analog Transformers over-weight.
  > zh: 在脉冲注意力中引入侧抑制机制，增强对相关 token 的关注并压制无关上下文，纠正沿用模拟 Transformer 注意力造成的注意力错配。
- Adaptive Gradient Learning for Spiking Neural Networks by Exploiting Membrane Potential Dynamics (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7783.pdf)]  
  > Ties surrogate-gradient sharpness to the membrane-potential distribution that normalization layers shift at each timestep, keeping updates inside the gradient-available interval and mitigating vanishing gradients under low-latency inference.
  > zh: 将代理梯度的形状与各时间步的膜电位分布动态绑定，抵消归一化层引起的电位漂移，缓解梯度消失并支持低时延推理。
- ILIF: Temporal Inhibitory Leaky Integrate-and-Fire Neuron for Overactivation in Spiking Neural Networks (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/4566.pdf)]  
  > Couples two inhibitory units, one acting on membrane potential and one on current, to curb overactivation from wide surrogate-gradient supports without the vanishing gradients narrow supports cause.
  > zh: 引入分别作用于膜电位与电流的两个耦合抑制单元，在抑制过度发放、降低发放率的同时避免窄代理梯度带来的梯度消失。
- Neuromorphic Sequential Arena: A Benchmark for Neuromorphic Temporal Processing (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7408.pdf)]  
  > Assembles seven real-world temporal tasks spanning multiple timescales and benchmarks spiking neuron models and architectures on accuracy, training speed, memory use and energy.
  > zh: 汇集七项跨多时间尺度的真实时序任务，从任务性能、训练速度、内存占用与能耗四方面统一评测各类脉冲神经元模型与网络架构。
- MSVIT: Improving Spiking Vision Transformer Using Multi-scale Attention Fusion (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/7378.pdf)] 
  > Replaces the single-scale spiking attention block with multi-scale spiking attention fusion, letting spike-driven Transformers extract features across image scales rather than one resolution.
  > zh: 用多尺度脉冲注意力融合替换单一尺度的注意力块，使脉冲驱动 Transformer 能跨图像尺度提取特征，缓解 SNN 与 ANN Transformer 的性能差距。
- A Fast and Accurate ANN-SNN Conversion Algorithm with Negative Spikes (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/6149.pdf)] 
  > Extends conversion to Leaky-ReLU networks via a neuron that emits negative spikes, adding variance-based threshold optimization and joint layer calibration to stop errors accumulating across layers.
  > zh: 引入可发放负脉冲的神经元，使 Leaky ReLU 网络也能快速转换为 SNN，并用基于激活值方差的阈值优化与跨层联合校准抑制误差累积。
- ECC-SNN: Cost-Effective Edge-Cloud Collaboration for Spiking Neural Networks (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/3167.pdf)] 
  > Shifts inference from cloud ANNs to edge SNNs through joint ANN-SNN training plus on-device incremental learning, cutting cloud update requests, energy draw and processing latency.
  > zh: 通过 ANN-SNN 联合训练把推理负载从云端下放到边缘脉冲模型，并以端侧增量学习适应环境变化，降低通信开销、能耗与时延。
- Cost-Effective On-Device Sequential Recommendation with Spiking Neural Networks (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/3150.pdf)]
  > Encodes dense item embeddings as sparse spike-wise representations and adds spiking filter modules for temporal patterns, fitting sequential recommendation into edge-device memory and energy budgets.
  > zh: 把稠密的物品嵌入编码为稀疏脉冲表示，并用脉冲滤波模块提取时序模式，使序列推荐能在内存与能耗受限的端侧设备上运行。
- SCNNs: Spike-based Coupling Neural Networks for Understanding Structural-Functional Relationships in the Human Brain (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1337.pdf)]
  > Models structural-functional brain coupling with spiking neurons over fMRI time series and white-matter connectivity, using synaptic and neuronal filtering to quantify coupling for disease identification.
  > zh: 用脉冲神经元分别刻画 fMRI 时序的功能特征与结构网络的空间特征，借助突触与神经元滤波效应量化结构-功能耦合，用于脑疾病识别。
- Exploiting Label Skewness for Spiking Neural Networks in Federated Learning (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1298.pdf)]
  > Calibrates per-label weights inside each client and distills knowledge between clients, countering local model drift when federated SNN training meets label-skewed device data.
  > zh: 在客户端内校准各标签的学习权重，并在客户端之间做知识蒸馏补偿缺失类别，抑制标签倾斜导致的本地 SNN 模型漂移。
- Binary Event-Driven Spiking Transformer (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/1206.pdf)]
  > Binarizes both weights and attention maps to 1-bit in a spiking Transformer, recovering lost capacity via a reversible framework and mutual-information distillation from the full-precision counterpart.
  > zh: 将脉冲 Transformer 的权重与注意力图同时二值化为 1 bit，再用可逆框架与互信息增强蒸馏对齐全精度模型，弥补二值化的精度损失。
- Tackling Long-Tailed Data Challenges in Spiking Neural Networks via Heterogeneous Knowledge Distillation (**IJCAI 2025**). [[paper](https://ijcai-preprints.s3.us-west-1.amazonaws.com/2025/787.pdf)]
  > Distills from a trained CNN into a spiking Transformer at both cross-layer features and global predictions, correcting head-versus-tail bias when SNNs train on long-tailed data.
  > zh: 以训练充分的 CNN 作为异构教师，对脉冲 Transformer 同时做跨层特征与全局预测的多粒度蒸馏，缓解长尾数据下头部与尾部类别的分布偏差。
- SpikeVideoFormer: An Efficient Spike-Driven Video Transformer with Hamming Attention and O(T) Complexity (**ICML 2025**). [[paper](https://arxiv.org/abs/2505.10352)]
  > Adapts real-valued attention into a spike-driven Hamming attention and picks an optimal space-time scheme, keeping temporal cost linear in video length for tracking and segmentation.
  > zh: 把实值注意力改造为脉冲驱动的 Hamming 注意力，并筛选最优时空注意力方案，使视频任务的时间复杂度保持线性，可用于姿态跟踪与分割。
- Efficient ANN-SNN Conversion with Error Compensation Learning (**ICML 2025**). [[paper](https://www.arxiv.org/abs/2506.01968)]
  > Attacks clipping, quantization and non-uniformity conversion errors with learnable threshold clipping, dual-threshold neurons and tuned membrane-potential initialization, enabling accurate two-timestep inference.
  > zh: 以可学习阈值裁剪、双阈值神经元和膜电位初始化分别抑制截断、量化与不均匀三类转换误差，把推理压缩到两个时间步。
- Differential Coding for Training-Free ANN-to-SNN Conversion (**ICML 2025**). [[paper](https://arxiv.org/abs/2503.00301)] 
  > Transmits changes in firing rate rather than the rate itself during ANN-to-SNN conversion, and iteratively fits thresholds to activation distributions to cut spike counts.
  > zh: 在 ANN-to-SNN 转换中传递发放率的变化量而非发放率本身，并按激活分布迭代整定阈值，减少脉冲数与能耗。
- Efficient Logit-based Knowledge Distillation of Deep Spiking Neural Networks for Full-Range Timestep Deployment (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/44825)] 
  > Distills a teacher into an SNN whose implicit sub-models converge at every timestep, so one trained network deploys across the full timestep range without retraining.
  > zh: 通过时空解耦的 logit 蒸馏让 SNN 在所有时间步上的隐式子模型同时收敛，一次训练即可任意调整推理时间步而无需重训。
- ReverB-SNN: Reversing Bit of the Weight and Activation for Spiking Neural Networks (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/43640)] 
  > Binarizes weights instead of activations, keeping real-valued spike amplitudes plus a learnable weight scale, which restores information capacity while staying multiplication-free.
  > zh: 将二值化对象由激活换成权重，保留实值脉冲激活并给二值权重加可学习幅度因子，在无乘法前提下提升信息容量。
- TTFSFormer: A TTFS-based Lossless Conversion of Spiking Transformer (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/44159)] 
  > Redesigns TTFS neurons to widen their representable range and handle Transformer nonlinearities, giving a theoretically lossless one-spike-per-neuron conversion of pretrained Transformers.
  > zh: 重新设计 TTFS 神经元以扩展表示范围并处理 Transformer 中的非线性层，实现每神经元至多发放一次脉冲的理论无损转换。
- BSO: Binary Spiking Online Optimization (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/45087)] 
  > Updates binary spiking weights online with flip signals fired when gradient momentum times the weight exceeds a threshold, removing latent-weight storage; a temporal variant adapts that threshold across timesteps.
  > zh: 以梯度动量与权重乘积超过阈值触发的翻转信号在线更新二值脉冲网络，省去潜权重存储，并给出按时间步自适应调阈的变体。
- Delay-DSGN: A Dynamic Spiking Graph Neural Network with Delay Mechanisms for Evolving Graph (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/43816)] 
  > Gives a dynamic spiking graph network learnable propagation delays via a shiftable Gaussian kernel, letting past node states reach future timesteps at data-dependent speeds.
  > zh: 为动态脉冲图网络加入可学习传播延迟，用可调中心的高斯核生成节点级延迟表示，使历史信息影响未来时间步的节点表征。
- TS-SNN: Temporal Shift Module for Spiking Neural Networks (**ICML 2025**). [[paper](https://arxiv.org/abs/2505.04165)] 
  > Shifts spike features across adjacent timesteps and residually fuses them, exposing past, present and future context within one timestep at the cost of a single learnable parameter.
  > zh: 通过时间维度的移位操作在单个时间步内融合过去、当前与未来的脉冲特征，并用残差防止信息丢失，仅新增一个可学习参数。
- SpikF: Spiking Fourier Network for Efficient Long-term Prediction (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/46411)] 
  > Splits long sequences into patches and selects informative frequency components, giving an attention-free spiking forecaster that tracks long-range temporal dependencies.
  > zh: 将长序列切分为 patch 并在频域上做选择性筛选，构建无注意力的脉冲预测网络，以更低能耗捕捉长程时间依赖。
- Self-cross Feature based Spiking Neural Networks for Efficient Few-shot Learning (**ICML 2025**). [[paper](https://arxiv.org/pdf/2505.07921)] 
  > Pairs a self-feature extractor with a cross-feature contrastive module and trains with InfoNCE plus temporal-efficient loss, sharpening class comparisons for low-power few-shot recognition.
  > zh: 用自特征提取与交叉特征对比两个模块细化表征，并以 InfoNCE 与时间高效训练损失优化脉冲序列动态，提升低功耗小样本分类。
- Faster and Stronger: When ANN-SNN Conversion Meets Parallel Spiking Calculation (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/44986)] 
  > Maps each timestep of parallel spiking neurons onto cumulative firing rate and calibrates the residual error distribution, converting ANNs with general activations at very low latency.
  > zh: 把并行脉冲神经元各时间步与累积发放率建立数学映射，配合分布感知误差校准，在超低延迟下支持更一般激活函数的转换。
- Efficient Parallel Training Methods for Spiking Neural Networks with Constant Time Complexity (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/45776)] 
  > Rewrites LIF dynamics as a fixed-point iteration that converges in a few steps, cutting training time complexity from linear in timesteps to constant without architecture changes.
  > zh: 把 LIF 神经元改写为不动点迭代形式并行求解所有时间步，在不改网络结构的前提下将训练时间复杂度从 O(T) 降为常数。
- Training High Performance Spiking Neural Networks by Temporal Model Calibration (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/44216)] 
  > Rescales logit gradients across timesteps so each step contributes differently, raising temporal heterogeneity in directly trained SNNs rather than relying on neuron dynamics or architecture.
  > zh: 从梯度视角出发，按时间步对 logit 梯度做重缩放以提升时间异质性，使直接训练的 SNN 各时间步输出更具多样性并提升精度。
- Temporal Misalignment in ANN-SNN Conversion and Its Mitigation via Probabilistic Spiking Neurons (**ICML 2025**). [[paper](https://icml.cc/virtual/2025/poster/45627)] 
  > Identifies temporal misalignment, where random spike rearrangement across converted SNN layers improves accuracy, then exploits it with biologically plausible two-phase probabilistic spiking neurons.
  > zh: 指出 ANN-SNN 转换中的时间错位现象（层间脉冲随机重排反而提升精度），并据此引入两阶段概率脉冲神经元改进转换效果。
- Time to Spike? Understanding the Representational Power of Spiking Neural Networks in Discrete Time (**ICML 2025**). [[paper](https://arxiv.org/abs/2505.18023)] 
  > Proves discrete-time LIF networks compute piecewise-constant functions over polyhedral regions, quantifying how latency and depth shape input-space partitioning and the size needed for approximation.
  > zh: 证明离散时间 LIF 网络实现多面体区域上的分段常值函数，并量化时间步数与深度对输入空间划分复杂度及逼近规模的影响。
- Hybrid Spiking Vision Transformer for Object Detection with Event Cameras (**ICML 2025**). [[paper](https://arxiv.org/abs/2505.07715)] 
  > Splits event-based detection into parallel spatial and temporal extraction branches inside a hybrid spiking Transformer, and releases a privacy-preserving fall-detection event benchmark alongside GEN1 evaluation.
  > zh: 将事件相机目标检测拆分为空间与时间两条特征提取支路构成混合脉冲 Transformer，并公开一个保护隐私的跌倒检测事件数据集。
- Sorbet: A Neuromorphic Hardware-Compatible Transformer-Based Spiking Language Model (**ICML 2025**). [[paper](https://arxiv.org/abs/2409.15298)] 
  > Replaces softmax and layer normalization with shift-based equivalents, then distills and quantizes to binary weights so a transformer language model fits neuromorphic hardware.
  > zh: 用移位运算替代 softmax 与层归一化，再借助蒸馏与量化得到二值权重，使 Transformer 语言模型可在神经形态硬件上运行。
- EventGPT: Event Stream Understanding with Multimodal Large Language Models (**CVPR 2025**). [[paper](https://arxiv.org/pdf/2412.00832)] [[code](https://github.com/XduSyL/EventGPT)]
  > Bridges event streams to a pre-trained LLM through a spatio-temporal aggregator and event-language adapter, trained in three stages from RGB-text warm-up to real instruction data.
  > zh: 通过时空聚合器与事件-语言适配器把事件流接入预训练大语言模型，并以 RGB 图文预热、合成与真实指令数据三阶段训练。
- Spk2SRImgNet: Super-Resolve Dynamic Scene from Spike Stream via Motion Aligned Collaborative Filtering (**CVPR 2025**). [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33079)]
  > Suppresses spike-stream fluctuation by gathering motion-aligned features from neighboring moments in a collaborative filtering module, super-resolving high-speed scenes beyond the spike sensor's spatial resolution.
  > zh: 沿运动轨迹从相邻时刻聚合相似特征做协同滤波，抑制脉冲流波动，从低分辨率脉冲相机数据重建高分辨率高速场景图像。
- Decision SpikeFormer: Spike-Driven Transformer for Decision Making (**CVPR 2025**). [[paper](https://cvpr.thecvf.com/virtual/2025/poster/32864)]
  > Adapts spike-driven attention to offline reinforcement learning with temporal and positional spiking self-attention, modeling trajectory dependencies that vision-oriented spiking Transformers do not capture.
  > zh: 以时间型与位置型脉冲自注意力把脉冲驱动 Transformer 用于离线强化学习序列建模，捕捉视觉类脉冲注意力忽略的轨迹依赖。
- Self-Supervised Learning for Color Spike Camera Reconstruction (**CVPR 2025**). [[paper](https://cvpr.thecvf.com/virtual/2025/poster/34093)]
  > Estimates missing Bayer-pattern pixels along motion trajectories using cross-channel motion consistency, then denoises quantization artifacts with a self-supervised masked spike encoder.
  > zh: 利用颜色通道间的运动一致性联合估计运动，沿轨迹补全 Bayer 缺失像素，再以自监督掩码脉冲编码器抑制量化噪声。
- USP-Gaussian: Unifying Spike-based Image Reconstruction, Pose Correction and Gaussian Splatting (**CVPR 2025**). [[paper](https://arxiv.org/abs/2411.10504)]
  > Optimizes spike-to-image reconstruction, camera pose correction and Gaussian splatting jointly rather than in sequence, removing the error accumulation of cascaded spike-based 3D pipelines.
  > zh: 把脉冲流图像重建、相机位姿校正与 3D Gaussian Splatting 统一为端到端联合迭代优化，消除级联流程中的误差累积。
- VISTREAM: Improving Computation Efficiency of Visual Perception Streaming via Law-of-Charge-Conservation Inspired Spiking Neural Network (**CVPR 2025**). [[paper](https://cvpr.thecvf.com/virtual/2025/poster/34908)]
  > Encodes only frame-to-frame differences and drops membrane resets via a charge-conservation property of ST-BIF neurons, cutting streaming-perception compute while provably matching the ANN counterpart.
  > zh: 仅编码相邻帧的差分并借助 ST-BIF 神经元的电荷守恒性质免去膜电位重置，在等价于 ANN 精度的前提下降低流式感知的计算量。
- Efficient ANN-Guided Distillation: Aligning Rate-based Features of Spiking Neural Networks through Hybrid Block-wise Replacement (**CVPR 2025**). [[paper](https://arxiv.org/abs/2503.16572)]
  > Swaps ANN blocks for spiking ones one at a time, using the hybrid intermediates to align rate-based features and enable rate-based backpropagation during distillation.
  > zh: 逐块把 ANN 模块替换为脉冲模块，用中间混合模型渐进对齐发放率特征，并自然支持基于发放率的反向传播完成蒸馏。
- Spiking Transformer: Introducing Accurate Addition-Only Spiking Self-Attention for Transformer (**CVPR 2025**). [[paper](https://arxiv.org/abs/2503.00226)]
  > Mixes binary, ternary and ReLU spiking neurons inside self-attention to drop softmax and scaling, keeping the computation addition-only while recovering accuracy lost to pure binarization.
  > zh: 在自注意力中混用二值、三值与 ReLU 脉冲神经元，去掉 softmax 与缩放操作，使计算仅含加法并弥补纯二值化的精度损失。
- Brain-Inspired Spiking Neural Networks for Energy-Efficient Object Detection (**CVPR 2025**). [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33275)]
  > Builds a directly trained multi-scale detector around an optic-nerve-nucleus block whose spiking convolutional neuron deepens feature extraction, targeting interpretable low-power object detection.
  > zh: 以含脉冲卷积神经元的视神经核团模块增强深层特征提取，构建可直接训练的多尺度脉冲检测器，兼顾可解释性与低功耗。
- Temporal Separation with Entropy Regularization for Knowledge Distillation in Spiking Neural Networks (**CVPR 2025**). [[paper](https://arxiv.org/abs/2503.03144)]
  > Distills teacher logits separately at each time step instead of on time-averaged outputs, adding entropy regularization to stabilize optimization of the student spiking network.
  > zh: 在各时间步分别对 logits 做蒸馏而非只用时间平均输出，并引入熵正则稳定优化，提升脉冲学生网络的蒸馏效果。
- STAA-SNN: Spatial-Temporal Attention Aggregator for Spiking Neural Networks (**CVPR 2025**). [[paper](https://arxiv.org/abs/2503.02689)]
  > Combines spike-driven self-attention, temporal position encoding and step-wise attention, with time-step dropout escaping local optima, capturing spatial and temporal dependencies at fewer time steps.
  > zh: 融合脉冲驱动自注意力、时间位置编码与步间注意力，并用时间步随机丢弃跳出局部最优，以更少时间步捕获时空依赖。
- Towards Effective and Sparse Adversarial Attack on Spiking Neural Networks via Breaking Invisible Surrogate Gradients (**CVPR 2025**). [[paper](https://arxiv.org/abs/2503.03272)]
  > Derives surrogate gradients from membrane-potential distributions when the victim's own are hidden, and pairs them with a generate-then-reduce attack that sparsifies perturbations on event data.
  > zh: 针对代理梯度不可见的推理模型，由膜电位分布反推代理梯度，并用生成-削减范式稀疏化扰动，攻击事件相机的二值动态图像。
- Rethinking Spiking Self-Attention Mechanism: Implementing α-XNOR Similarity Calculation in Spiking Transformers (**CVPR 2025**). [[paper](https://cvpr.thecvf.com/virtual/2025/poster/33850)]
  > Replaces dot-product Q-K similarity with an XNOR score that assigns matched non-spike pairs a tunable weight α, restoring information lost to spike-train sparsity.
  > zh: 用 α-XNOR 相似度替代点积计算 Q-K 相关性，为成对非脉冲赋予权重 α，弥补脉冲序列稀疏带来的信息缺失。
- Spiking Transformer with Spatial-Temporal Attention (**CVPR 2025**). [[paper](https://arxiv.org/abs/2409.19764)]
  > Extends spiking self-attention over time by processing spatial-temporal chunks block-wise, keeping the cost of spatial-only attention and dropping into existing spike-based Transformers unchanged.
  > zh: 以分块方式在时空片段上计算脉冲自注意力，把时间依赖纳入注意力而保持纯空间注意力的复杂度，可直接嵌入已有脉冲 Transformer。
- Quantized Spike-driven Transformer (**ICLR 2025**). [[paper](https://openreview.net/forum?id=5J9B7Sb8rO)]
  > Traces quantized spike-driven attention degradation to a bimodal spike distribution, fixing it with an information-enhanced LIF neuron and fine-grained distillation from a full-precision teacher.
  > zh: 把量化脉冲驱动注意力的退化归因于脉冲分布双峰化，用信息增强 LIF 神经元与细粒度蒸馏对齐全精度教师，兼顾精度与低功耗。
- Rethinking Spiking Neural Networks from an Ensemble Learning Perspective (**ICLR 2025**). [[paper](https://openreview.net/forum?id=ZyknpOQwkT)]
  > Views timesteps as parameter-shared subnetworks whose inconsistent initial membrane potentials destabilize training, then smooths those potentials and lets adjacent timesteps guide each other to ease vanishing temporal gradients.
  > zh: 把各时间步视作共享参数的子网络集成，通过平滑初始膜电位并让相邻时间步互相引导，缓解训练不稳定与时间维梯度消失。
- DeepTAGE: Deep Temporal-Aligned Gradient Enhancement for Optimizing Spiking Neural Networks (**ICLR 2025**). [[paper](https://openreview.net/forum?id=drPDukdY3t)]
  > Shapes surrogate gradients per time step from the membrane-potential distribution and adds deep supervision across both stages and time steps, curbing gradient vanishing at no inference cost.
  > zh: 按各时间步的膜电位分布自适应调整代理梯度，并在网络阶段与时间步两个维度施加深监督，抑制梯度消失且不增加推理开销。
- QP-SNN: Quantized and Pruned Spiking Neural Networks (**ICLR 2025**). [[paper](https://openreview.net/forum?id=MiPyle6Jef)]
  > Rescales weights so uniform quantization uses the full bit width, and ranks kernels for structured pruning by the singular values of their spatiotemporal spike activity.
  > zh: 重缩放权重使均匀量化充分利用比特位宽，并按时空脉冲活动的奇异值识别冗余卷积核做结构化剪枝，面向边缘端部署。
- Temporal Flexibility in Spiking Neural Networks: Towards Generalization Across Time Steps and Deployment Friendliness (**ICLR 2025**). [[paper](https://openreview.net/forum?id=9HsfTgflT7)]
  > Assigns different network stages random time-step counts during training, so one trained SNN generalizes across inference time steps and deploys on both clock- and event-driven hardware.
  > zh: 训练时为网络各阶段随机分配时间步数，使同一模型在推理阶段可跨时间步泛化，并能部署到时钟驱动与事件驱动硬件。
- P-SpikeSSM: Harnessing Probabilistic Spiking State Space Models for Long-Range Dependency Tasks (**ICLR 2025**). [[paper](https://openreview.net/forum?id=Sf4ep9Udjf)]
  > Swaps sequential leaky-integrate-and-fire dynamics for stochastic spike sampling inside a state-space model, enabling parallel training while keeping activations sparse on long-range sequence benchmarks.
  > zh: 以随机脉冲采样取代串行 LIF 动力学并嵌入状态空间模型，使训练可并行化，在长程序列任务上保持稀疏发放。
- TS-LIF: A Temporal Segment Spiking Neuron Network for Time Series Forecasting (**ICLR 2025**). [[paper](https://openreview.net/forum?id=rDe9yQQYKt)]
  > Splits the spiking neuron into dendritic and somatic compartments tuned to different frequency bands, injecting current directly at the soma to preserve information for time-series forecasting.
  > zh: 把脉冲神经元拆为树突与胞体双腔室分别处理不同频段，并直接向胞体注入电流减少信息损失，提升时序预测精度与鲁棒性。
- Improving the Sparse Structure Learning of Spiking Neural Networks from the View of Compression Efficiency (**ICLR 2025**). [[paper](https://openreview.net/forum?id=gcouwCx7dG)]
  > Measures how compressible the current sparse subnetwork is with a PQ index, then sets the rewiring ratio for dynamic pruning and regrowth from that measurement instead of a fixed schedule.
  > zh: 先用 PQ 指数评估当前稀疏子网络的可压缩程度，据此自适应确定连接重连比例，再执行动态剪枝与再生长，提高稀疏 SNN 的压缩效率。
- SpikeLLM: Scaling up Spiking Neural Network to Large Language Models via Saliency-based Spiking (**ICLR 2025**). [[paper](https://openreview.net/forum?id=ZadnlOHsHv)]
  > Scales spiking to 7-70B-parameter LLMs by compressing spike trains with generalized integrate-and-fire neurons and spending extra spikes only on salient outlier channels, plugging into existing quantization pipelines.
  > zh: 用广义积分发放（GIF）神经元压缩脉冲长度，按显著性将额外脉冲预算分配给离群通道，把脉冲机制扩展到 7B-70B 参数的大语言模型。
- Spiking Vision Transformer with Saccadic Attention (**ICLR 2025**). [[paper](https://openreview.net/forum?id=qzZsz6MuEq)]
  > Scores Query-Key relevance from spike distributions instead of dot products and adds a temporal interaction module, giving saccade-inspired spiking attention linear complexity in token count.
  > zh: 借鉴眼跳机制，用脉冲分布而非点积衡量 Q-K 空间相关性，并加入时间交互模块，使脉冲注意力复杂度随 token 数线性增长。
- SpikeGS: Reconstruct 3D scene captured by a fast moving bio-inspired camera (**AAAI 2025**). [[paper](https://arxiv.org/pdf/2407.03771v2)]
  > Integrates spike streams into 3D Gaussian Splatting via accumulation rasterization and interval supervision, recovering sharp geometry and texture where fast camera motion blurs conventional frames.
  > zh: 将脉冲流接入 3D Gaussian Splatting，以累积光栅化与区间监督从高时间分辨率但缺纹理的脉冲流中重建几何与纹理，克服快速运动模糊。
- Rethinking High-speed Image Reconstruction Framework with Spike Camera (**AAAI 2025**). [[paper](https://arxiv.org/pdf/2501.04477)] [[code](https://github.com/chenkang455/SpikeCLIP)]
  > Supervises spike-to-image reconstruction with CLIP text-image alignment and unpaired high-quality images instead of synthetic pairs, restoring texture and brightness in real low-light spike streams.
  > zh: 借助 CLIP 的图文对齐，用场景文本描述与非配对高质量图像替代合成数据监督脉冲重建，改善真实低光场景下的纹理与亮度。
- Spiking Point Transformer for Point Cloud Classification (**AAAI 2025**).
  > Encodes point clouds through queue-driven sampling direct encoding that keeps the most useful support points per timestep, bringing transformer-based SNNs to 3D point cloud classification.
  > zh: 以队列驱动的采样直接编码在每个时间步保留最有效的支撑点，把脉冲 Transformer 从二维图像推广到三维点云分类。
- Efficient 3D Recognition with Event-driven Spike Sparse Convolution (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2412.07360)] [[code](https://github.com/bollossom/e-3dsnn)]
  > Voxelizes point clouds into sparse spike trains and applies spike sparse convolution, yielding one event-driven 3D backbone for classification, detection and segmentation on neuromorphic hardware.
  > zh: 用脉冲体素编码把点云转为稀疏脉冲序列，再以脉冲稀疏卷积提特征，得到可同时做分类、检测与分割的事件驱动三维骨干网络。
- GRSN: Gated Recurrent Spiking Neurons for POMDPs and MARL (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2404.15597)]
  > Accumulates historical state through single-step neuron updates instead of multi-step simulation and adds gated units for memory, solving POMDPs and multi-agent cooperation at about half the power of RNNs.
  > zh: 用脉冲神经元的单步更新累积历史状态以对齐 RL 时序，并引入门控增强记忆，在 POMDP 与多智能体协作上以约一半功耗接近 RNN。
- EventZoom: A Progressive Approach to Event-Based Data Augmentation for Enhanced Neuromorphic Vision (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2405.18880)]
  > Augments event streams by progressively scaling and shifting transformed samples into originals, preserving spatial integrity and temporal continuity that cropping-based augmentation destroys.
  > zh: 通过渐进缩放与平移把变换样本嵌入原始事件流，避免裁剪造成的空间信息丢失与时间中断，保持稀疏性与高动态范围。
- Leveraging Asynchronous Spiking Neural Networks for Ultra Efficient Event-Based Visual Processing (**AAAI 2025**).
  > Processes each event asynchronously into a dynamically evolving graph representation fed to spiking neurons, cutting energy by orders of magnitude versus frame-based pipelines at similar accuracy.
  > zh: 逐事件异步处理并动态演化图表示，配合脉冲神经元实现低延迟与高稀疏，能耗较帧式方法低若干数量级，精度相当。
- CREST: An Efficient Conjointly-trained Spike-driven Framework for Event-based Object Detection Exploiting Spatiotemporal Dynamics (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2412.12525)] [[code](https://github.com/shen-aoyu/CREST/)]
  > Trains spike-driven detectors with a conjoint learning rule that eases gradient vanishing, plus a multi-scale spatiotemporal event integrator and an ST-IoU loss for event-based detection.
  > zh: 以联合学习规则缓解深层 SNN 的梯度消失并支持双运行模式，配合多尺度时空事件整合器与 ST-IoU 损失完成全脉冲事件目标检测。
- UCF-Crime-DVS: A Novel Event-Based Dataset for Video Anomaly Detection with Spiking Neural Networks (**AAAI 2025**).
  > Converts the UCF-Crime surveillance benchmark into DVS event streams and pairs it with a multi-scale spiking fusion network, giving video anomaly detection its first event-based benchmark.
  > zh: 把 UCF-Crime 监控视频转为 DVS 事件流，构建首个事件相机视频异常检测基准，并配套多尺度脉冲融合网络 MSF 作为基线。
- SpikingSSMs: Learning Long Sequences with Sparse and Parallel Spiking State Space Models (**AAAI 2025**). [[paper](https://arxiv.org/pdf/2408.14909)][[code](https://github.com/shenshuaijie/SDN
  > Fuses dendrite-inspired neuronal dynamics into state space model blocks and predicts after-reset membrane potential with a surrogate network, restoring parallel training for long sequences.
  > zh: 将树突启发的神经元动力学分层融入状态空间模型，并用轻量代理网络预测复位后膜电位，化解事件驱动与并行计算的冲突。
)]
- Advancing Spiking Neural Networks towards Multiscale Spatiotemporal Interaction Learning (**AAAI 2025**). [[paper](https://arxiv.org/pdf/2405.13672)]
  > Captures multiscale spatiotemporal interactions with a spiking attention module and regularizes via attention-weighted ZoneOut pseudo-ensembles, closing the gap on deep non-transformer SNN backbones.
  > zh: 用脉冲多尺度注意力捕捉事件数据的时空交互，并以注意力权重驱动的 ZoneOut 伪集成正则化，缩小非 Transformer 架构 SNN 与 ANN 的差距。
- SpikingYOLOX: Improved YOLOX Object Detection with Fast Fourier Convolution and Spiking Neural Networks(**AAAI 2025**).
  > Extends YOLOX with ternary signed spiking neurons for richer deep-layer features and fast Fourier convolution for a global receptive field, adapting SNNs to object detection.
  > zh: 在 YOLOX 中引入可发放三值的带符号脉冲神经元以增强深层特征，并用快速傅里叶卷积提供全局感受野，把 SNN 推向目标检测任务。
- ALADE-SNN: Adaptive Logit Alignment in Dynamically Expandable Spiking Neural Networks for Class Incremental Learning (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2412.12696)]
  > Expands SNN structure per task while realigning logit distributions and suppressing old-to-new weight mappings during training, curbing bias and overfitting in class-incremental learning.
  > zh: 按任务动态扩展 SNN 结构，用自适应 logit 对齐平衡新旧任务特征，训练时抑制旧特征到新类的映射权重，缓解类增量学习中的偏置与过拟合。
- Efficient Spike-driven Transformer For High-performance Image Segmentation (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2412.14587)] [[code](https://github.com/BICLab/Spike2Former)]
  > Identifies and repairs the modules that collapse spike firing when converting segmentation architectures, adding normalized integer spiking neurons to stabilize training of deep SNN segmenters.
  > zh: 定位并改造导致脉冲发放骤降的分割架构模块，引入归一化整数脉冲神经元稳定复杂 SNN 的训练，提升语义分割 mIoU。
- Towards Accurate Binary Spiking Neural Networks: Learning with Adaptive Gradient Modulation Mechanism (**AAAI 2025**).
  > Diagnoses frequent weight sign flipping as the core obstacle in binary SNN training and adaptively modulates gradients to curb it, speeding convergence and raising accuracy.
  > zh: 将权重符号频繁翻转诊断为二值脉冲神经网络训练的主要障碍，通过自适应调制梯度加以抑制，加快收敛并提升精度。
- Adaptive Calibration: A Unified Conversion Framework of Spiking Neural Networks (**AAAI 2025**).
  > Cuts ANN-to-SNN conversion error with a layer-wise adaptive-firing neuron, then trims energy and latency via sensitivity-guided spike compression and input-dependent timestep selection.
  > zh: 以逐层自适应发放的神经元降低 ANN-to-SNN 转换误差，再通过敏感度引导的脉冲压缩与输入自适应时间步，削减能耗和延迟。
- Towards More Discriminative Feature Learning in SNNs with Temporal-Self-Erasing Supervision (**AAAI 2025**).
  > Erases the most strongly activated regions found across time steps during training, pushing the network toward weaker but informative cues and richer multi-step inference.
  > zh: 训练时自适应擦除各时间步预测中的高激活区域，迫使网络关注被忽略的弱激活线索，提升特征判别力与多时间步推理效果。
- FSTA-SNN: Frequency-based Spatial-Temporal Attention Module for Spiking Neural Networks (**AAAI 2025**).[[paper](https://arxiv.org/pdf/2501.14744)] [[code](https://github.com/yukairong/FSTA-SNN)]
  > Suppresses redundant spike features through frequency-domain spatial-temporal attention, exploiting that shallow layers encode vertical and deep layers horizontal variation, which lowers overall firing rates.
  > zh: 利用浅层偏重竖直、深层偏重水平变化且各时间步差异微小的观察，以频域时空注意力抑制冗余脉冲特征，降低发放率。

### 2024

**Review**
- Direct Training High-Performance Deep Spiking Neural Networks: A Review of Theories and Methods (**Frontiers in Neuroscience 2024**). [[paper]](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1383844/full) [[arxiv](https://arxiv.org/abs/2405.04289v2)] 
  > Surveys surrogate-gradient direct training end to end - neuron models, residual and Transformer-based architectures, software frameworks, neuromorphic chips and applications - as one roadmap for deep SNNs.
  > zh: 系统梳理基于代理梯度的直接训练路线：脉冲神经元模型、残差与 Transformer 架构、软件框架、神经形态硬件及应用与趋势。

**NeurIPS, ACM MM, ECCV, AAAI, ICLR, Frontiers in Neuroscience, CVPR, ICML, IJCAI**
- SpikedAttention: Training-Free and Fully Spike-Driven Transformer-to-SNN Conversion with Winner-Oriented Spike Shift for Softmax Operation (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=fs28jccJj5)]
  > Converts a trained Swin Transformer or BERT into a fully spike-driven SNN without retraining, implementing softmax through a winner-oriented spike shift that keeps attention intact.
  > zh: 免训练地把已训练好的 Swin Transformer 与 BERT 转换为全脉冲驱动 SNN，用 winner-oriented 脉冲移位实现 softmax，无需改动注意力结构。
- Spiking Graph Neural Network on Riemannian Manifolds (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=VKt0K3iOmO)]
  > Places spiking graph neurons on geodesically complete Riemannian manifolds, replacing backpropagation-through-time with a differentiation-via-manifold rule that sidesteps its latency cost while retaining graph geometry.
  > zh: 在测地完备的黎曼流形上定义脉冲神经元，以流形微分取代 BPTT，既保留图的结构几何又缓解高时延问题。
- Rethinking the Dynamics of Spiking Neural Networks (**NeurIPS 2024**). [[paper](https://neurips.cc/virtual/2024/poster/96543)]
  > Makes the initial membrane potential learnable to unlock firing patterns a zero start forbids, and pairs it with a last-time-step readout and label-smoothed TET loss.
  > zh: 将初始膜电位设为可学习参数，解锁零初值无法产生的放电模式，并配合末时间步读出与标签平滑 TET 损失重整优化目标。
- Long-Range Feedback Spiking Network Captures Dynamic and Static Representations of the Visual Cortex under Movie Stimuli (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=bxDok3uaK6)] [[code](https://github.com/Grasshlw/SNN-Neural-Similarity-Movie)]
  > Adds long-range top-down feedback between cortical-style stages of a spiking network, yielding higher representational similarity to mouse visual cortex under long movie stimuli.
  > zh: 在脉冲网络中引入跨脑区的长程自上而下反馈，对小鼠视觉皮层在长时程电影刺激下的动态与静态表征相似度更高。
- Take A Shortcut Back: Mitigating the Gradient Vanishing for Training Spiking Neural Networks (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=xjyU6zmZD7)]
  > Routes gradients directly from the loss to shallow layers to relieve surrogate-gradient vanishing, rebalancing shortcut and main-path contributions across training epochs via a scheduled coefficient.
  > zh: 让梯度从损失直达浅层，缓解代理梯度在深层脉冲网络中的消失问题，并按训练轮次动态调节捷径与主路径的权重比例。
- Advancing Training Efficiency of Deep Spiking Neural Networks through Rate-based Backpropagation (**NeurIPS 2024**). [[paper](https://arxiv.org/abs/2410.11488)] [[code](https://github.com/Tab-ct/rate-based-backpropagation)]
  > Backpropagates through averaged firing rates instead of per-timestep temporal derivatives, shrinking the BPTT computational graph to cut training memory while tracking BPTT accuracy.
  > zh: 以平均发放率而非逐时间步的时序导数做反向传播，精简 BPTT 计算图以降低训练显存与算力，同时保持与 BPTT 相当的精度。
- Latent Diffusion for Neural Spiking Data (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=ZX6CEo1Wtv)]
  > Compresses spike trains into continuous latents with an S4 autoencoder, then runs a conditional diffusion model there to synthesize behavior-conditioned population activity of variable length.
  > zh: 用带 S4 层的自编码器把离散脉冲记录压成连续隐空间，再在其上训练条件扩散模型，生成可变长度、行为条件化的群体放电数据。
- Autonomous Driving with Spiking Neural Networks (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=95VyH4VxN9)] [[code](https://github.com/ridgerchu/SAD)]
  > Chains spiking perception, dual-pathway prediction and planning into one end-to-end trained driving stack, producing bird's-eye-view occupancy and safe trajectories on nuScenes under event-driven compute.
  > zh: 把感知、双通路预测与规划串成端到端训练的全脉冲自动驾驶栈，从多视角相机构建鸟瞰时空表征并输出安全轨迹，在 nuScenes 上验证。
- Exact Gradients for Stochastic Spiking Neural Networks Driven by Rough Signals (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=mCWZj7pa0M)]
  > Models stochastic spiking networks as event-driven SDEs on cadlag rough paths, deriving exact pathwise gradients of both trajectories and spike times plus an autodifferentiable solver.
  > zh: 以粗糙路径理论将随机脉冲网络建模为带事件跳变的随机微分方程，导出轨迹与放电时刻的精确梯度，配套可自动微分求解器。
- Spatio-Temporal Interactive Learning for Efficient Image Reconstruction of Spiking Cameras (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=S4ZqnMywcM)]
  > Reconstructs frames from spike-camera streams by interleaving inter-frame motion alignment with intra-frame filtering coarse-to-fine, replacing step-by-step pipelines with one multi-scale interactive network.
  > zh: 从脉冲相机的二值脉冲流重建图像时，将帧间运动对齐与帧内特征滤波以由粗到细的方式交互进行，替代逐步串行的重建流水线。
- Slack-Free Spiking Neural Network Formulation for Hypergraph Minimum Vertex Cover (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=4A5IQEjG8c)]
  > Drops the QUBO reformulation for hypergraph minimum vertex cover, adding constraint-checking and correction neurons that steer the spiking solver toward feasible covers on neuromorphic hardware.
  > zh: 求解超图最小顶点覆盖时绕开 QUBO 重构与松弛变量，改用额外脉冲神经元做约束检查与修正，在神经形态硬件上稳定收敛到可行解。
- EnOF: Training Accurate Spiking Neural Networks via Enhancing the Output Feature Representation (**NeurIPS 2024**). [[paper](https://openreview.net/pdf/5a4dfaf8dc6861efa8e8356b3bd86743ab98838d.pdf)]
  > Swaps the final LIF layer for ReLU to give full-precision output features, and aligns them with an ANN teacher's features through a KL-divergence distillation loss.
  > zh: 把最后一层 LIF 换成 ReLU，以极小额外开销得到全精度输出特征，并用 KL 散度蒸馏损失将其与 ANN 教师特征对齐。
- Spiking Token Mixer: A event-driven friendly Former structure for spiking neural networks (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=iYcY7KAkSy)] [[code](https://github.com/brain-intelligence-lab/STMixer_demo)]
  > Builds a Transformer-like token mixer from only convolutions, fully connected layers and residual paths, eliminating spike-matrix multiplications so the network maps onto event-driven asynchronous chips.
  > zh: 仅用卷积、全连接与残差通路搭出类 Transformer 的 token 混合结构，去掉两个脉冲矩阵相乘，使网络可部署到事件驱动异步芯片。
- SpGesture: Source-Free Domain-adaptive sEMG-based Gesture Recognition with Jaccard Attentive Spiking Neural Network (**NeurIPS 2024**). [[paper](https://arxiv.org/abs/2405.14398)] [[code](https://github.com/guoweiyu/SpGesture/)]
  > Treats membrane potential as a memory list to bring source-free domain adaptation into SNNs, and adds a spiking Jaccard attention for drift-robust sEMG gesture recognition.
  > zh: 把膜电位当作记忆列表，将无源域自适应引入脉冲神经网络，并用脉冲 Jaccard 注意力提升 sEMG 手势识别对分布漂移的鲁棒性。
- Spiking Transformer with Experts Mixture (**NeurIPS 2024**). [[paper](https://openreview.net/pdf/35a5bc54de368426f66605d8e3f447638863888a.pdf)] 
  > Merges mixture-of-experts routing into spiking Transformers by making both experts and router emit spikes, whose element-wise product yields dynamic sparse conditional computation.
  > zh: 让专家与路由器都输出脉冲序列，二者逐元素相乘即得到动态稀疏的条件计算，从而把混合专家机制以脉冲驱动方式引入脉冲 Transformer。
- FEEL-SNN: Robust Spiking Neural Networks with Frequency Encoding and Evolutionary Leak Factor (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=TuCQdBo4NC)] [[code](https://github.com/zju-bmi-lab/FEEL_SNN)]
  > Encodes inputs at a different frequency per time step and evolves each neuron's leak factor, suppressing noise bands while preserving the original signal.
  > zh: 在不同时间步编码不同频段的输入，并让各神经元自行进化膜电位泄漏因子，在保留原始信息的同时抑制不同频段噪声。
- Spiking Neural Network as Adaptive Event Stream Slicer (**NeurIPS 2024**). [[paper](https://arxiv.org/abs/2410.02249)] 
  > Uses a low-power SNN to decide where to cut an event stream, shaping its firing times with a position-aware loss and feedback from the downstream ANN.
  > zh: 用低功耗脉冲网络自适应决定事件流的切分时刻，以位置感知损失调制神经元状态，并借下游 ANN 的反馈更新切分策略。
- Advancing Spiking Neural Networks for Sequential Modeling with Central Pattern Generators (**NeurIPS 2024**). [[paper](https://arxiv.org/abs/2405.14362)] [[code](https://github.com/microsoft/SeqSNN)]
  > Derives spike-form positional encoding from central pattern generator dynamics, showing sinusoidal encoding is one such solution and extending SNNs to forecasting and text classification.
  > zh: 从中枢模式发生器的膜电位动力学导出脉冲形式的位置编码，证明正弦编码只是其特解，使脉冲网络可胜任时序预测与文本分类。
- QKFormer: Hierarchical Spiking Transformer using Q-K Attention (**NeurIPS 2024**). [[paper](https://openreview.net/pdf?id=AVd7DpiooC)] [[code](https://github.com/zhouchenlin2096/QKFormer)]
  > Models token or channel importance with binary Q-K vectors at linear complexity, then stacks hierarchical stages and a deformed-shortcut patch embedding for multi-scale spiking features.
  > zh: 用二值 Q-K 向量以线性复杂度建模 token 或通道的重要性，并引入层次化结构与带形变捷径的 patch embedding，获得多尺度脉冲表征。
- Q-SNNs: Quantized Spiking Neural Networks (**ACM MM 2024**). [[paper](https://dl.acm.org/doi/10.1145/3664647.3681186)]
  > Quantizes both synaptic weights and membrane potentials, offsetting the resulting information loss with an entropy-motivated weight-spike dual regulation to shrink models for edge devices.
  > zh: 同时量化突触权重与膜电位，并用受信息熵启发的权重-脉冲双重调节弥补压缩损失，压缩模型体积以适配低功耗边缘设备。
- RSC-SNN: Exploring the Trade-off Between Adversarial Robustness and Accuracy in Spiking Neural Networks via Randomized Smoothing Coding (**ACM MM 2024**). [[paper](https://dl.acm.org/doi/10.1145/3664647.3680639)] [[code](https://github.com/KemingWu/RSC-SNN)]
  > Traces SNN adversarial robustness to Poisson coding, argues its equivalence to randomized smoothing, and tunes the coding noise to steer the robustness-accuracy trade-off.
  > zh: 把脉冲网络的对抗鲁棒性归因于 Poisson 编码，论证其与随机平滑等价，并通过调节编码噪声在鲁棒性与精度之间取舍。
- Reversing Structural Pattern Learning with Biologically Inspired Knowledge Distillation for Spiking Neural Networks (**ACM MM 2024**). [[paper](https://dl.acm.org/doi/pdf/10.1145/3664647.3680655)]
  > Grows SNN topology from scratch with an evolutionary rule that couples reverse knowledge distillation to connection pruning, trimming synaptic and neuronal redundancy as training proceeds.
  > zh: 用进化式规则从零构建脉冲网络拓扑，将反向知识蒸馏与连接剪枝结合，训练中动态调整突触连接以削减结构冗余。
- Towards High-performance Spiking Transformers from ANN to SNN Conversion (**ACM MM 2024**). [[paper](https://dl.acm.org/doi/10.1145/3664647.3680620)] [[code](https://github.com/h-z-h-cell/Transformer-to-SNN-ECMT)]
  > Converts Transformers to SNNs via an expectation compensation module that reconstructs each step's expected output from earlier steps, with multi-threshold neurons and parallel parameter normalization cutting latency.
  > zh: 用期望补偿模块借助此前时间步的输出还原非线性模块的期望值，再以多阈值神经元与并行参数归一化压缩转换所需时间步。
- Towards Low-latency Event-based Visual Recognition with Hybrid Step-wise Distillation Spiking Neural Networks (**ACM MM 2024**). [[paper](https://dl.acm.org/doi/10.1145/3664647.3680832)] [[code](https://github.com/hsw0929/HSD)]
  > Decouples event-frame count from SNN time steps, pre-training on many frames and fine-tuning on few, while step-wise distillation aligns the per-timestep output distributions.
  > zh: 解耦事件帧数量与脉冲网络时间步：训练阶段用更多事件帧、推理阶段用更少，并以逐时间步蒸馏对齐各步输出分布以降低延迟。
- Integer-Valued Training and Spike-Driven Inference Spiking Neural Network for High-performance and Energy-efficient Object Detection (**ECCV 2024**). [[paper](https://arxiv.org/pdf/2407.20708)] [[code](https://github.com/BICLab/SpikeYOLO)]
  > Simplifies YOLO into meta SNN blocks and activates integer values during training while expanding virtual timesteps at inference, keeping detection spike-driven despite membrane-potential quantization error.
  > zh: 将 YOLO 精简为元 SNN 模块，训练时激活整数值、推理时靠扩展虚拟时间步回到脉冲驱动，缓解膜电位量化误差对检测的影响。
- Spiking Wavelet Transformer (**ECCV 2024**). [[paper](https://arxiv.org/pdf/2403.11138)] [[code](https://github.com/bic-L/Spiking-Wavelet-Transformer)]
  > Drops self-attention for a sparse wavelet token mixer with convolutional and pointwise branches, capturing moving edges and brightness changes in a multiplication-free spike-driven manner.
  > zh: 以稀疏小波 token 混合器取代自注意力，配合卷积与逐点分支并引入负脉冲动力学，在无乘法的脉冲驱动下捕捉边缘等高频成分。
- Efficient Training of Spiking Neural Networks with Multi-Parallel Implicit Stream Architecture (**ECCV 2024**). [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05068.pdf)] [[code](https://github.com/kiritozc/MPIS-SNNs)]
  > Trains SNNs as equilibrium models by driving several fused parallel implicit streams to a fixed point, so the backward pass simulates one time step instead of storing activations.
  > zh: 借鉴平衡模型训练脉冲网络：前向让多条融合的并行隐式流同时收敛到平衡点，反向仅需单时间步模拟，免去存储大量激活值。
- Asynchronous Bioplausible Neuron for Spiking Neural Networks for Event-Based Vision (**ECCV 2024**). [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08133.pdf)] 
  > Auto-adjusts firing from membrane gradient, threshold history and spike efficiency, holding neurons near homeostasis under varying event-camera input while cutting power on classification and segmentation.
  > zh: 依据膜电位梯度、阈值回溯梯度与放电效率自适应调节发放行为，使神经元在事件相机输入波动下保持稳态，同时降低功耗。
- BKDSNN: Enhancing the Performance of Learning-based Spiking Neural Networks Training with Blurred Knowledge Distillation (**ECCV 2024**). [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/06649.pdf)] [[code](https://github.com/Intelligent-Computing-Research-Group/BKDSNN)]
  > Blurs the SNN feature map before the final layer so it must restore the ANN teacher's features, and mixes with logit distillation to close the surrogate-gradient accuracy gap.
  > zh: 对末层前的 SNN 特征图随机模糊以复原并模仿 ANN 教师特征，并与 logits 蒸馏结合，缩小代理梯度训练带来的精度差距。
- Exploring Vulnerabilities in Spiking Neural Networks: Direct Adversarial Attacks on Raw Event Data (**ECCV 2024**). [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09164.pdf)]
  > Relaxes ternary event values into probabilistic samples so adversarial optimization can hit raw DVS streams directly, with a sparsity norm keeping the perturbed events realistic.
  > zh: 将三值事件取值松弛为概率采样，在稀疏范数约束下直接对原始事件流做定向对抗攻击，暴露栅格化之前环节的安全隐患。
- EAS-SNN: End-to-End Adaptive Sampling and Representation for Event-based Detection with Recurrent Spiking Neural Networks (**ECCV 2024**). [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07766.pdf)] [[code](https://github.com/Windere/EAS-SNN)]
  > Learns event sampling itself with recurrent convolutional SNNs carrying temporal memory, adding residual potential dropout and spike-aware training so detection needs fewer parameters and timesteps.
  > zh: 用带时序记忆的循环卷积 SNN 端到端学习事件采样策略，并以残差膜电位 Dropout 与脉冲感知训练稳定膜电位分布，所需参数与时间步更少。
- Spike-Temporal Latent Representation for Energy-Efficient Event-to-Video Reconstruction (**ECCV 2024**). [[paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/05843.pdf)]
  > Encodes event voxels into layer-wise spiking latents whose depth approximates an iterative shrinkage-thresholding fixed point, then reconstructs grayscale video through a U-shaped spiking decoder.
  > zh: 把事件体素逐层编码为脉冲隐表示，以网络深度逼近迭代收缩阈值算法的不动点，再经 U 形脉冲解码器重建灰度视频，提升能效。
- EC-SNN: Splitting Deep Spiking Neural Networks on Edge Devices (**IJCAI 2024**). [[code](https://github.com/AmazingDD/EC-SNN)] 
  > Partitions a deep spiking network into channel-pruned sub-models running in parallel across several edge devices, cutting per-device inference latency and energy while preserving accuracy.
  > zh: 结合通道剪枝把深层 SNN 切分为若干子模型，分布到多台边缘设备并行执行，在保持精度的同时降低单设备时延与能耗。
- One-step Spiking Transformer with a Linear Complexity (**IJCAI 2024**).
  > Compresses the time dimension to a single step with a compensation module and replaces float attention with spiking linear transforms, bringing cost down to linear complexity.
  > zh: 通过时域压缩与补偿模块把时间步降到 1，并用脉冲线性变换替代浮点注意力运算，将复杂度与浮点乘加开销降到线性。
- TIM: An Efficient Temporal Interaction Module for Spiking Transformer (**IJCAI 2024**). [[paper](https://arxiv.org/pdf/2401.11687)] [[code](https://github.com/BrainCog-X/Brain-Cog/tree/main/examples/TIM)] 
  > Inserts a lightweight convolutional interaction path across timesteps inside spiking self-attention, letting spiking Transformers reuse past-step context on neuromorphic data at minimal parameter cost.
  > zh: 在脉冲自注意力内部加入轻量卷积式跨时间步交互路径，让脉冲 Transformer 复用历史时间步信息，额外参数开销极小。
- Learning a Spiking Neural Network for Efficient Image Deraining (**IJCAI 2024**). [[code](https://github.com/MingTian99/ESDNet)] 
  > Exploits the stronger spike response of rain pixels, reweighting membrane potentials by attention inside spiking residual blocks and training with surrogate gradients rather than ANN conversion.
  > zh: 利用雨纹像素触发更强脉冲响应的特性，在脉冲残差块中以注意力调制膜电位，缓解二值激活信息损失，并以代理梯度直接训练。
- LitE-SNN: Designing Lightweight and Efficient Spiking Neural Network through Spatial-Temporal Compressive Network Search and Joint Optimization (**IJCAI 2024**). [[paper](https://arxiv.org/pdf/2401.14652)] 
  > Folds pruning, mixed-precision quantization and timestep count into one automated architecture search, jointly learning topology and spatio-temporal compression under an explicit computation-cost budget.
  > zh: 把剪枝、混合精度量化与时间步数目一并纳入自动架构搜索空间，在计算开销约束下联合优化网络结构与时空压缩策略。
- Temporal Spiking Neural Networks with Synaptic Delay for Graph Reasoning (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/35073)] 
  > Turns spike timing into an extra coding dimension via synaptic delays, casting knowledge-graph reasoning as a neural-generalized path computation driven by sparse event-driven dynamics.
  > zh: 借助突触延迟把关系属性编码进脉冲发放时刻，以稀疏事件驱动的动力学把知识图谱推理表述为神经化的路径计算。
- Towards efficient deep spiking neural networks construction with spiking activity based pruning (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/33505)] 
  > Ranks convolutional kernels by their spiking activity and prunes then regenerates them during training, letting structure adapt to the task instead of fixing sparsity upfront.
  > zh: 以卷积核的脉冲发放活跃度作为结构化剪枝依据，在训练中动态剪除并再生通道，使稀疏结构随任务自适应调整而非一次定死。
- Efficient and Effective Time-Series Forecasting with Spiking Neural Networks (**ICML 2024**). [[paper](https://arxiv.org/pdf/2402.01533)] 
  > Settles temporal alignment and spike-encoding choices for sequence prediction, matching conventional time-series forecasters across diverse benchmarks while consuming far less energy.
  > zh: 针对时序对齐与脉冲编码难点构建统一的 SNN 预测框架并给出选型指引，在多个基准上以低得多的能耗匹敌常规时序预测方法。
- Autaptic Synaptic Circuit Enhances Spatio-temporal Predictive Learning of Spiking Neural Networks (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/33269)] 
  > Wires two learnable self-feedback pathways into the spiking neuron, borrowing autaptic circuits to extend temporal memory, coordinate spatial features and ease gradient vanishing.
  > zh: 借鉴自突触环路，在脉冲神经元中引入两条可学习的自反馈通路，增强时间记忆与空间协同，并缓解梯度消失问题。
- Robust Stable Spiking Neural Networks (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/33217)]
  > Analyzes membrane-potential perturbation dynamics as a nonlinear stability problem and trains modified LIF neurons to shrink that perturbation, hardening SNNs under noise and adversarial attack.
  > zh: 从非线性系统稳定性视角刻画膜电位扰动动力学，并改造 LIF 神经元以抑制扰动幅度，提升 SNN 在噪声与对抗攻击下的鲁棒性。
- CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks (**ICML 2024**). [[paper](https://arxiv.org/pdf/2402.04663)]
  > Traces the SNN accuracy gap to vanishing gradients along time and adds a complementary membrane path that carries temporal gradient while keeping outputs binary and hyperparameter-free.
  > zh: 将精度损失归因于时间维度的梯度消失，为 LIF 神经元增设互补路径以疏通时序梯度，同时保持二值脉冲输出且无需调参。
- NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/33481)]
  > Replaces BPTT unrolling with forward-in-time learning that splits the gradient into spatial and neuronal-dynamics-derived temporal parts, cutting the memory needed to store every time step.
  > zh: 以在线的前向时间学习替代 BPTT 展开，将梯度拆为空间项与源自神经元动力学的时间项，免去逐时间步保存中间状态。
- High-Performance Temporal Reversible Spiking Neural Networks with O(L) Training Memory and O(1) Inference Cost (**ICML 2024**). [[paper](https://arxiv.org/pdf/2405.16466)]
  > Switches off temporal dynamics in most neurons and makes the remaining ones temporally reversible, so activations need not be stored across time and inference cost stops growing with timesteps.
  > zh: 关闭多数脉冲神经元的时间动力学，仅在少数神经元间构建时间可逆交互，训练无需缓存各时间步激活，推理开销与时间步解耦。
- Towards Efficient Spiking Transformer: a Token Sparsification Framework for Training and Inference Acceleration (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/32674)]
  > Selects important tokens with a timestep-wise anchor and aligns attention maps within and across timesteps, accelerating spiking-Transformer training while lowering inference energy.
  > zh: 用逐时间步的锚点 token 统一筛选重要 token，并对注意力图做时间步内与跨时间步对齐，加速脉冲 Transformer 训练并降低能耗。
- SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/35024)]
  > Generalizes binary spikes to bidirectional pulses with elastic amplitude and controlled firing frequency, keeping addition-only computation while carrying enough semantics for discriminative and generative language tasks.
  > zh: 把 {0,1} 脉冲推广为带方向、幅值弹性与发放频率可控的双向脉冲，在保持纯加法运算的同时承载语义，覆盖判别与生成式语言任务。
- Sign Gradient Descent-based Neuronal Dynamics: ANN-to-SNN Conversion Beyond ReLU Network (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/33242)]
  > Casts integrate-and-fire dynamics as a subgradient optimizer and derives sign-gradient-descent neurons that approximate nonlinearities beyond ReLU, enabling low-latency conversion of ConvNeXt, MLP-Mixer and ResMLP.
  > zh: 将积分发放动力学解释为次梯度优化，据此设计 signGD 神经元以逼近 ReLU 之外的非线性，在低时间步下完成 ConvNeXt、MLP-Mixer、ResMLP 的转换。
- Enhancing Adversarial Robustness in SNNs with Sparse Gradients (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/34066)]
  > Bounds the gap between random- and adversarial-perturbation robustness by the sparsity of input gradients, then regularizes that sparsity during training on image and event-based data.
  > zh: 揭示随机扰动与对抗扰动的鲁棒性差距受输入梯度稀疏度约束，据此正则化梯度稀疏度来训练，图像与事件相机数据均适用。
- SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN (**ICML 2024**). [[paper](https://icml.cc/virtual/2024/poster/34194)]
  > Converts activation-quantized Transformers into exactly equivalent SNNs by giving softmax, LayerNorm and self-attention spike-domain counterparts, so no accuracy is lost across vision and language tasks.
  > zh: 为 softmax、LayerNorm 与自注意力设计脉冲等价算子，把激活量化的 Transformer 无损转换为 SNN，在视觉与语言任务上均不掉点。
- Are Conventional SNNs Really Efficient? A Perspective from Network Quantization (**CVPR 2024**). [[paper](https://arxiv.org/pdf/2311.10802)]
  > Equates SNN timesteps with activation bit-width and replaces SynOps counting with a Bit Budget that allocates resources across weights, activations and time, favoring quantization over longer simulation.
  > zh: 把时间步等同于激活量化位宽，用 Bit Budget 取代 SynOps 估算能耗，并指出把预算投向脉冲模式与权重量化比拉长时间步更划算。
- SFOD: Spiking Fusion Object Detector (**CVPR 2024**). [[paper](https://arxiv.org/pdf/2403.15192)] [[code](https://github.com/yimeng-fan/SFOD)]
  > Fuses multi-scale feature maps inside a spiking backbone for event-camera object detection, and pairs it with tuned spike-decoding and loss choices on the GEN1 detection benchmark.
  > zh: 在脉冲主干中首次融合多尺度特征图用于事件相机目标检测，并配套优化脉冲解码策略与损失函数，在 GEN1 数据集上验证。
- SpikingResformer: Bridging ResNet and Vision Transformer in Spiking Neural Networks (**CVPR 2024**). [[paper](https://arxiv.org/abs/2403.14302)] [[code](https://github.com/xyshi2000/SpikingResformer)]
  > Pairs a Dual Spike Self-Attention with a principled scaling rule and a ResNet-style multi-stage stem, restoring local feature extraction that flat spiking Transformers lack while trimming parameters.
  > zh: 以 ResNet 式多阶段结构承载带合理缩放的 Dual Spike Self-Attention，补足脉冲 Transformer 欠缺的局部特征提取并降低参数量。
- SGLFormer: Spiking Global-Local-Fusion Transformer with high performance (**Frontiers in Neuroscience 2024**).[[paper](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1371290/full)] [[code](https://github.com/ZhangHanN1/SGLFormer)]
  > Interleaves convolutional local blocks with global spiking transformer blocks, fixes gradient blocking in max-pooling, and aggregates spatial-temporal features in the classification head.
  > zh: 将卷积式局部提取与全局脉冲 Transformer 块交替堆叠，修复 maxpooling 处的梯度回传阻塞，并在分类头以时空块聚合空间与时间特征。
- Towards Energy Efficient Spiking Neural Networks: An Unstructured Pruning Framework (**ICLR 2024**). [[paper](https://openreview.net/forum?id=eoSeaK4QJo&referrer=%5Bthe%20profile%20of%20Zecheng%20Hao%5D(%2Fprofile%3Fid%3D~Zecheng_Hao1))]
  > Combines unstructured weight pruning with unstructured neuron pruning so that both synaptic and neuronal sparsity translate into fewer synaptic operations on neuromorphic hardware.
  > zh: 把非结构化权重剪枝与非结构化神经元剪枝结合，同时利用突触与神经元两级稀疏，直接减少神经形态硬件上的突触运算量。
- Online Stabilization of Spiking Neural Networks (**ICLR 2024**). [[paper](https://openreview.net/forum?id=CIj1CVbkpr)]
  > Restores batch-normalization-like benefits to memory-efficient online SNN training via a spiking renormalization that keeps train/test parameters consistent plus a threshold stabilizer for firing rates.
  > zh: 为省内存的在线训练补上批归一化式收益：用在线脉冲重归一化对齐训练与测试参数，并用阈值稳定器稳定发放率。
- SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition (**ICLR 2024**). [[paper](https://arxiv.org/pdf/2310.07189.pdf)]
  > Feeds raw event clouds straight into a point-based spiking network instead of rendering frames, preserving sparsity while a single-stage extractor captures global and local features.
  > zh: 直接以点云形式处理原始事件流而非转成帧，保留事件相机的稀疏性，并用单阶段结构同时提取全局与局部特征。
- Spatio-Temporal Approximation: A Training-Free SNN Conversion for Transformers (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=XrunSYwoLr)]
  > Converts pretrained Transformers to SNNs without retraining by approximating nonlinearities with universal group operators and handling self-attention's spike multiplications through a temporal estimate-then-correct layer.
  > zh: 免训练地把预训练 Transformer 转为 SNN：用通用群算子在空间维近似非线性，用时间校正自注意力层估计并修正脉冲乘法。
- Sparse Spiking Neural Network: Exploiting Heterogeneity in Timescales for Pruning Recurrent SNN (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=0jsfesDZDq)]
  > Prunes a randomly initialized recurrent SNN before any task training, using Lyapunov exponents and spectral graph sparsification to keep the sparse heterogeneous-timescale network stable.
  > zh: 在任务训练之前就对随机初始化的循环 SNN 剪枝，以 Lyapunov 指数与谱图稀疏化保证剪枝后稳定，得到异质时间尺度的稀疏网络。
- Learning Delays in Spiking Neural Networks using Dilated Convolutions with Learnable Spacings (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=4r2ybzJnmN)] [[code](https://github.com/Thvnvtos/SNN-delays)]
  > Encodes each synaptic delay as the position of a single nonzero weight in a temporal 1D kernel, learning positions and weights jointly by backpropagation on speech benchmarks.
  > zh: 把突触延迟表示为时间维一维卷积核中唯一非零权重的位置，借助 DCLS 与权重一同反向传播学习，在 SHD/SSC/GSC 等语音任务上无需循环连接。
- Threaten Spiking Neural Networks through Combining Rate and Temporal Information (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=xv8iGxENyI)] [[code](https://github.com/hzc1208/HART_Attack)]
  > Attacks spiking models by fusing rate and temporal information into a single perturbation whose rate-versus-timing balance is adjusted dynamically, after quantifying each channel separately.
  > zh: 先分别量化 SNN 中保留的发放率信息与时间信息，再把两者融合为可动态调节配比的混合对抗扰动，暴露更强的攻击面。
- TAB: Temporal Accumulated Batch Normalization in Spiking Neural Networks (**ICLR 2024**). [[paper](https://openreview.net/forum?id=k1wlmtPGLq&noteId=p5M9gOLAOf)] 
  > Normalizes each time-step using statistics accumulated over all preceding steps, matching batch normalization to membrane-potential accumulation and countering temporal covariate shift in direct SNN training.
  > zh: 用截至当前时间步的累积统计量做批归一化，使其与膜电位的累积动态对齐，缓解直接训练中沿时间维的协变量偏移。
- Certified Adversarial Robustness for Rate Encoded Spiking Neural Networks (**ICLR 2024**). [[paper](https://openreview.net/forum?id=5bNYf0CqxY)] 
  > Recasts rate encoding as a form of randomized smoothing, deriving provable l1-norm robustness certificates for spiking classifiers and adversarial training tailored to rate-encoded inputs.
  > zh: 把发放率编码等价视作随机平滑，从而给出脉冲分类器在 l1 范数扰动下的可证明鲁棒性界，并配套面向率编码的对抗训练算法。
- Bayesian Bi-clustering of Neural Spiking Activity with Latent Structures (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=ZYm1Ql6udy)] 
  > Clusters recorded neurons and time periods jointly with a nonparametric Bayesian model, tying neuron groups to shared latent trajectories and state segments to synchronous local linear dynamics.
  > zh: 用非参数贝叶斯模型对多脑区放电数据做神经元与时段的双向聚类，神经元簇由潜在轨迹界定，时段由同步局部线性动力学界定。
- Adaptive deep spiking neural network with global-local learning via balanced excitatory and inhibitory mechanism (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=wpnlc2ONu0)] 
  > Switches between local and global learning according to network connectivity, which an excitation-inhibition mechanism continually reshapes, aiming to keep global-learning accuracy at local-learning energy cost.
  > zh: 用兴奋-抑制机制动态调节网络连接度，并据此在局部学习与全局学习之间切换，兼顾全局学习的精度与局部学习的低能耗。
- Hebbian Learning based Orthogonal Projection for Continual Learning of Spiking Neural Networks (**ICLR 2024**). [[paper](https://arxiv.org/pdf/2402.11984.pdf)] [[code](https://github.com/pkuxmq/HLOP-SNN)]
  > Extracts the principal subspace of activity traces with Hebbian learning on lateral connections, then projects weight updates orthogonally to it so earlier continual-learning tasks resist forgetting.
  > zh: 在侧向连接上用 Hebbian/反 Hebbian 学习提取活动迹的主子空间，再把权重更新投影到其正交方向，以近乎无遗忘的方式持续学习新任务。
- A Progressive Training Framework for Spiking Neural Networks with Learnable Multi-hierarchical Model (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=g52tgL8jy6)] [[code](https://github.com/hzc1208/STBP_LMH)]
  > Generalizes the LIF neuron with learnable membrane factors that retune the mix of historical and current information, paired with a progressive schedule spanning hybrid and time-sliced online training.
  > zh: 以可学习的膜相关因子推广 LIF 神经元，动态调节历史与当前信息的提取比例，并给出涵盖混合训练与时间切片在线训练的渐进式方案。
- LMUFormer: Low Complexity Yet Powerful Spiking Model With Legendre Memory Units (**ICLR 2024**). [[paper](https://arxiv.org/pdf/2402.04882.pdf)] [[code](https://github.com/zeyuliu1037/LMUFormer)]
  > Augments a Legendre Memory Unit with convolutional patch embedding and channel mixing, plus a spiking variant, giving Transformer-level sequence accuracy while keeping streaming recurrent inference.
  > zh: 为 Legendre Memory Unit 加入卷积式 patch 嵌入与卷积通道混合器，并给出脉冲版本，在保持流式推理的同时逼近 Transformer 的序列建模精度。
- Spike-driven Transformer V2: Meta Spiking Neural Network Architecture Inspiring the Design of Next-generation Neuromorphic Chips (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=1SIBN5Xyw7)] [[code](https://github.com/BICLab/Spike-Driven-Transformer-V2)]
  > Extends the spike-driven Transformer into a meta architecture whose sparse-addition-only blocks serve classification, detection and segmentation from one directly trained backbone, guiding neuromorphic chip design.
  > zh: 把 Spike-driven Transformer 抽象为元架构，网络中只保留稀疏加法，用一个直接训练的骨干同时支撑分类、检测与分割，并为神经形态芯片设计提供参照。
- Can we get the best of both Binary Neural Networks and Spiking Neural Networks for Efficient Computer Vision? (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=lGUyAuuTYZ)] [[code](https://github.com/godatta/Ultra-Low-Latency-SNN)]
  > Merges SNN-style activation sparsity with binary networks via uni-polar binary activations, dropping the time dimension while keeping BNN-level accuracy and compute efficiency.
  > zh: 以单极性二值激活把 SNN 的稀疏性与 BNN 的精度结合起来，去掉时间维度，从而避免多时间步带来的延迟与能耗。
- A Graph is Worth 1-bit Spikes: When Graph Contrastive Learning Meets Spiking Neural Networks (**ICLR 2024**). [[paper](https://openreview.net/pdf?id=LnLySuf1vp)] [[code](https://github.com/EdisonLeeeee/SpikeGCL)]
  > Encodes graph nodes as sparse 1-bit spike representations for contrastive learning, and trains blockwise to avoid vanishing gradients while retaining full-precision-level expressiveness.
  > zh: 将图节点编码为稀疏的 1-bit 脉冲表示用于对比学习，并以分块训练缓解梯度消失，在压缩存储的同时保持与全精度相当的表达能力。
- Ternary Spike: Learning Ternary Spikes for Spiking Neural Networks (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2312.06372.pdf)] [[code](https://github.com/yfguo91/Ternary-Spike)]
  > Widens binary activations to ternary spikes to carry more information while staying multiplication-free, learning per-layer spike amplitudes that re-parameterize away at inference.
  > zh: 把二值脉冲扩展为三值脉冲以提升信息容量且仍然免乘法，逐层学习脉冲幅值，并在推理时通过重参数化还原为标准三值形式。
- Memory-Efficient Reversible Spiking Neural Networks (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2312.07922.pdf)] [[code](https://github.com/mi804/RevSNN)]
  > Extends reversible architectures along the temporal axis so activations and membrane potentials are recomputed rather than stored, keeping training memory flat as depth grows.
  > zh: 将可逆结构沿时间维度扩展，反向过程中重算中间激活与膜电位而非保存，使训练显存不随网络深度增长。
- Gated Attention Coding for Training High-performance and Efficient Spiking Neural Networks (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2308.06582.pdf)]
  > Replaces direct input coding with a multi-dimensional gated attention front-end, strengthening temporal dynamics while leaving the downstream network fully spike-driven and hardware-compatible.
  > zh: 用多维门控注意力前端取代直接编码，增强输入的时间动态，同时保持主干网络的脉冲驱动特性，便于神经形态硬件部署。
- SpikingBERT: Distilling BERT to Train Spiking Language Models Using Implicit Differentiation (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2308.10873.pdf)] [[code](https://github.com/NeuroCompLab-psu/SpikingBERT)]
  > Trains a spiking language model by implicit differentiation at the equilibrium spike rate instead of surrogate gradients, distilling from a BERT teacher and evaluating on GLUE.
  > zh: 以平衡态平均发放率的隐式微分替代代理梯度来训练脉冲语言模型，并从 BERT 教师蒸馏，在 GLUE 上验证脉冲注意力的可行性。
- TC-LIF: A Two-Compartment Spiking Neuron Model for Long-Term Sequential Modelling (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2308.13250.pdf)] [[code](https://github.com/ZhangShimin1/TC-LIF)]
  > Splits the LIF neuron into coupled somatic and dendritic compartments so error gradients survive long delays, improving long-range temporal credit assignment on sequential tasks.
  > zh: 将 LIF 神经元拆成相互耦合的胞体与树突两个隔室，使梯度能跨越长时间间隔传播，提升长序列任务的时序依赖建模能力。
- Shrinking Your TimeStep: Towards Low-Latency Neuromorphic Object Recognition with Spiking Neural Networks (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2401.01912.pdf)]
  > Cuts inference latency by staging the network with progressively shrinking timesteps, rescaling time through temporal transformers and adding early classifiers to stabilize surrogate-gradient training.
  > zh: 将网络分阶段并逐级缩减时间步以降低推理延迟，用时序变换模块平滑改变时间尺度，并加入多个早期分类器稳定代理梯度训练。
- Dynamic Spiking Graph Neural Networks (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2401.05373.pdf)]
  > Compensates spike-induced information loss on dynamic graphs by routing early-layer features to the last layer, and uses equilibrium implicit differentiation to avoid storing per-timestep activations.
  > zh: 在动态图上把浅层特征直传至最后一层以补偿脉冲化的信息损失，并用平衡态隐式微分免去跨时间步的反向存储，降低内存开销。
- An Efficient Knowledge Transfer Strategy for Spiking Neural Networks from Static to Event Domain (**AAAI 2024**). [[paper](https://arxiv.org/pdf/2303.13077.pdf)] [[code](https://github.com/Brain-Cog-Lab/Transfer-for-DVS)]
  > Bridges the static-to-event domain gap with a domain-alignment loss regularized by per-timestep event features, plus a sliding schedule that gradually swaps images for event streams during training.
  > zh: 用域对齐损失加逐时间步事件特征的时空正则缩小静态图像与事件数据的分布差异，并以滑动策略逐步把图像输入替换为事件流。



**Arxiv**
- Brain-Inspired Spiking Neural Networks for Industrial Fault Diagnosis: A Survey, Challenges, and Opportunities. [paper](https://doi.org/10.48550/arXiv.2401.02429)  
  > Surveys spiking models for industrial fault diagnosis, covering neuron and encoding fundamentals, existing SNN-based diagnosis pipelines, and the open challenges facing deployment on equipment monitoring.
  > zh: 系统梳理脉冲神经网络在工业故障诊断中的应用，涵盖神经元与编码基础、现有诊断模型，并归纳该方向落地面临的挑战与机会。
- Q-SNNs: Quantized Spiking Neural Networks. [[paper](https://arxiv.org/pdf/2406.13672)]
  > Quantizes both synaptic weights and membrane potentials, adding an entropy-motivated weight-spike dual regulation term to recover the accuracy that aggressive compression would otherwise cost.
  > zh: 同时量化突触权重与膜电位以压缩模型体积和计算量，并用基于信息熵的权重-脉冲双重调节缓解压缩带来的精度下降。
- Scalable MatMul-free Language Modeling. [[paper](https://arxiv.org/pdf/2406.02528)] [[code](https://github.com/ridgerchu/matmulfreellm)]
  > Removes matrix multiplication from the attention and feed-forward layers of language models up to 2.7B parameters, cutting inference memory and mapping onto multi-chip neuromorphic hardware.
  > zh: 从注意力与前馈层中彻底移除矩阵乘法，在最高 2.7B 参数规模上保持性能，大幅降低推理显存，并可映射到多芯片神经形态系统。
- QKFormer: Hierarchical Spiking Transformer using Q-K Attention. [[paper](https://arxiv.org/pdf/2403.16552.pdf)] [[code](https://github.com/zhouchenlin2096/QKFormer)]
  > Models token or channel importance with a binary spike-form Q-K attention of linear complexity, and adds hierarchical multi-scale stages plus a deformed-shortcut patch embedding.
  > zh: 用二值 Q-K 脉冲注意力以线性复杂度建模 token 或通道的重要性，并引入层次化多尺度结构与带形变捷径的 patch embedding 模块。
- Spikformer V2: Join the High Accuracy Club on ImageNet with an SNN Ticket. [[paper](https://arxiv.org/pdf/2401.02020.pdf)] [[code](https://github.com/ZK-Zhou/spikformer)]
  > Augments Spikformer with a spiking convolutional stem and mask-and-reconstruct self-supervised pretraining, letting larger, deeper spiking Transformers be trained for ImageNet classification.
  > zh: 为 Spikformer 补充脉冲卷积 stem，并引入掩码重建式自监督预训练，使更大更深的脉冲 Transformer 可训练并用于 ImageNet 分类。
- SpikeNAS: A Fast Memory-Aware Neural Architecture Search Framework for Spiking Neural Network Systems. [[paper](https://arxiv.org/pdf/2402.11322.pdf)]
  > Searches SNN architectures under an explicit memory budget by scoring how each operation affects accuracy, then quantizing, shortening search time for embedded deployment.
  > zh: 在给定内存预算下搜索 SNN 结构：先分析各类算子对精度的影响，再配合快速搜索与量化，缩短面向嵌入式部署的搜索时间。
- Astrocyte-Enabled Advancements in Spiking Neural Networks for Large Language Modeling. [[paper](https://arxiv.org/pdf/2312.07625v2.pdf)]
  > Couples each spiking unit with an astrocyte state modeled on tripartite synapses, extending long-term dependency handling for language generation while holding latency and memory low.
  > zh: 为脉冲单元耦合基于三方突触的星形胶质细胞调制状态，增强长时程依赖与记忆保持，在语言生成中兼顾低延迟与低内存占用。


### 2023

**Review**
- Direct Learning-Based Deep Spiking Neural Networks: A Review (**Frontiers in Neuroscience 2023**). [[paper](https://arxiv.org/pdf/2305.19725.pdf)]
  > Surveys surrogate-gradient direct training of deep spiking networks, sorting methods into accuracy, efficiency and temporal-dynamics tracks and mapping the open challenges for each.
  > zh: 综述基于代理梯度的深层脉冲神经网络直接训练工作，按精度提升、效率提升与时序动态利用三条脉络归类，并梳理各自的开放挑战。

**AAAI, ICLR, CVPR, ICML, IJCAI, ICCV, NeurIPS, TPAMI, Science Advances**
- Time series prediction and anomaly detection with recurrent spiking neural networks (**IJCNN 2023**). [[paper](https://ieeexplore.ieee.org/abstract/document/10191614)]
  > Pairs a sparse recurrent spiking network with tailored input encoding and readout decoding to forecast time series and flag anomalies without labels, plus an explicit compute-cost accounting.
  > zh: 为稀疏循环脉冲网络配套专门的编解码机制，实现时间序列预测与无监督异常检测，并给出可公平比较的计算开销核算方法。
- SpikingJelly: An open-source machine learning infrastructure platform for spike-based intelligence (**Science Advances 2023**). [[paper](https://www.science.org/doi/10.1126/sciadv.adi1480)] [[code](https://github.com/fangwei123456/spikingjelly)]
  > Bundles neuromorphic-dataset preprocessing, network construction, training and chip deployment into one full-stack framework, whose multilevel inheritance and code generation make deep-SNN training 11× faster.
  > zh: 将神经形态数据集预处理、建模、训练到芯片部署整合为全栈框架，借助多级继承与代码生成使深层 SNN 训练提速 11 倍。
- Spike-driven Transformer [[paper](https://arxiv.org/pdf/2307.01694.pdf)] [[code](https://github.com/BICLab/Spike-Driven-Transformer)]
  > Recasts Query-Key-Value multiplication as mask and addition under a linear-complexity spike-driven self-attention, cutting attention computation energy by up to 87.2× versus vanilla self-attention.
  > zh: 把 Query-Key-Value 之间的矩阵乘法改写为掩码与加法，构建线性复杂度的脉冲驱动自注意力，注意力计算能耗最高降低 87.2 倍。
- Parallel Spiking Neurons with High Efficiency and Long-term Dependencies Learning Ability (**NeurIPS 2023**). [[paper](https://arxiv.org/abs/2304.12760)] [[code](https://github.com/fangwei123456/Parallel-Spiking-Neuron)]
  > Drops the reset term so membrane dynamics rewrite into a non-iterative parallelizable form, adding masked and sliding variants for step-by-step inference and variable-length sequences.
  > zh: 去掉复位机制，将膜电位动态改写为非迭代形式以在时间步上并行仿真，并用 masked 与 sliding 变体适配逐步推理与变长序列。
- Temporal Conditioning Spiking Latent Variable Models of the Neural Response to Natural Visual Scenes (**NeurIPS 2023**). [[paper](https://arxiv.org/pdf/2306.12045.pdf)]
  > Generates spike trains directly from spiking latent variables to model responses to natural visual scenes, replacing fixed temporal filters with an adaptive temporal-conditioning operation.
  > zh: 以脉冲隐变量直接生成可与记录对齐的脉冲序列来建模自然视觉场景下的神经响应，用时间条件化操作取代固定时间滤波器。
- SEENN: Towards Temporal Spiking Early Exit Neural Networks (**NeurIPS 2023**). [[paper](https://openreview.net/pdf?id=mbaN0Y0QTw)]
  > Treats timestep count as input-dependent: one variant halts on a confidence threshold, the other learns the exit policy by reinforcement learning, cutting average inference steps.
  > zh: 把时间步数视为随输入而变的量：一种变体按置信度阈值提前退出，另一种用强化学习决定步数，降低平均推理时间步。
- EICIL: Joint Excitatory Inhibitory Cycle Iteration Learning for Deep Spiking Neural Networks (**NeurIPS 2023**). [[paper](https://openreview.net/pdf?id=OMDgOjdqoZ)]
  > Embeds excitatory and inhibitory neuronal behaviours into a single cycle-iterative training framework, expanding the representation space of spiking neurons and making deep SNN training more biologically faithful.
  > zh: 将兴奋与抑制两种神经元行为嵌入同一循环迭代训练框架，扩展脉冲神经元的表示空间，让深层 SNN 的训练更贴近生物信号传递。
- Addressing the speed-accuracy simulation trade-off for adaptive spiking neurons (**NeurIPS 2023**). [[paper](https://openreview.net/pdf?id=Ht79ZTVMsn)]
  > Reinterprets the adaptive leaky integrate-and-fire recursion to shorten sequential dependencies, giving over 50× faster training at small discretisation steps and sub-millisecond fits to cortical recordings.
  > zh: 重新推导 ALIF 神经元的递推结构以缩短串行依赖，使小离散步长下训练提速 50 倍以上，并能亚毫秒精度拟合真实皮层记录。
- Enhancing Adaptive History Reserving by Spiking Convolutional Block Attention Module in Recurrent Neural Networks (**NeurIPS 2023**). [[paper](https://openreview.net/pdf?id=aGZp61S9Lj)]
  > Inserts a spiking convolutional block attention module into a recurrent SNN so spatial and temporal history is recalled selectively, trimming stored memory on gesture and sequence data.
  > zh: 在循环脉冲网络中嵌入脉冲卷积块注意力模块 SCBAM，选择性调用空间与时间历史信息，在手势与时序数据上以更小内存取得更高精度。
- Trial matching: capturing variability with data-constrained spiking neural networks (**NeurIPS 2023**). [[paper](https://arxiv.org/abs/2306.03603)]
  > Fits a large recurrent spiking network to multi-area cortical recordings under an optimal-transport distance between trial distributions, reproducing trial-to-trial variability and predicting jaw movements.
  > zh: 用最优传输度量生成试次与真实试次的分布差异，将大型循环脉冲网络拟合到多脑区皮层记录，复现试次间变异并预测下颌运动。
- Evolving Connectivity for Recurrent Spiking Neural Networks (**NeurIPS 2023**). [[paper](https://arxiv.org/pdf/2305.17650.pdf)]
  > Reformulates weight tuning as a search over connection-probability distributions optimised by natural evolution strategies, yielding gradient-free sparse boolean recurrent spiking controllers for 17-DoF humanoid locomotion.
  > zh: 把权重训练改为对连接概率分布的搜索，用自然演化策略免梯度优化，得到稀疏布尔连接、硬件友好的 RSNN，可完成 17 自由度人形运动。
- SparseProp: Efficient Event-Based Simulation and Training of Sparse Recurrent Spiking Neural Networks (**NeurIPS 2023**). [[paper](https://openreview.net/pdf?id=yzZbwQPkmP)] 
  > Exploits connection sparsity with an event-based scheme that updates neuron states lazily, cutting exact forward and backward cost per spike from O(N) to O(log N).
  > zh: 利用网络稀疏性以事件驱动方式惰性更新神经元状态，把每个脉冲的前向与反向开销从 O(N) 降到 O(log N)，支持精确仿真与 BPTT 训练。
- Spiking PointNet: Spiking Neural Networks for Point Clouds (**NeurIPS 2023**). [[paper](https://arxiv.org/pdf/2310.06232v1.pdf)] [[code](https://github.com/dayongren/spiking-pointnet)]
  > Trains a spiking PointNet at a single timestep yet infers with several, sidestepping the memory and optimization cost of multi-step training on point clouds.
  > zh: 让脉冲版 PointNet 只用单个时间步训练、推理时再用多时间步，绕开多步训练的显存与优化瓶颈，把脉冲网络扩展到点云识别。
- Exploring Loss Functions for Time-based Training Strategy in Spiking Neural Networks (**NeurIPS 2023**). [[paper](https://openreview.net/pdf?id=8IvW2k5VeA)]
  > Maps rate-based loss functions onto time-based counterparts and shows analytically that losses supplying adequate positive overall gradients ease asynchronous temporal-coding training.
  > zh: 把基于发放率的损失函数映射为基于时间的形式，并从理论上说明提供足够正向整体梯度的损失更利于时间编码的异步训练。
- Membrane Potential Batch Normalization for Spiking Neural Networks (**ICCV 2023**). [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Guo_Membrane_Potential_Batch_Normalization_for_Spiking_Neural_Networks_ICCV_2023_paper.pdf)]
  > Inserts a second batch-normalization layer on the membrane potential just before firing, then folds it into the threshold so inference cost is unchanged.
  > zh: 在发放函数前对膜电位再做一次批归一化，并通过重参数化把它折叠进阈值，推理时不增加额外开销。
- Unleashing the Potential of Spiking Neural Networks with Dynamic Confidence (**ICCV 2023**). [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_Unleashing_the_Potential_of_Spiking_Neural_Networks_with_Dynamic_Confidence_ICCV_2023_paper.pdf)]
  > Decodes a confidence signal over time from SNN outputs and terminates each inference once it suffices, trimming latency per sample at runtime.
  > zh: 从脉冲网络的时序输出中解码置信度，为每个样本动态决定何时提前终止推理，在运行时按需削减时间步与延迟。
- RMP-Loss: Regularizing Membrane Potential Distribution for Spiking Neural Networks	(**ICCV 2023**). [[paper](https://arxiv.org/abs/2308.06787)]
  > Regularizes membrane potentials toward the spike levels with an added training loss, shrinking the quantization error caused by binarizing potentials into 0/1 spikes.
  > zh: 添加一项训练损失把膜电位分布拉向脉冲取值附近，减小二值化为 0/1 脉冲所引入的量化误差。
- Inherent Redundancy in Spiking Neural Networks	(**ICCV 2023**). [[paper](https://arxiv.org/abs/2308.08227)]
  > Traces redundant noise spikes to the spatio-temporal invariance of SNNs and adds paired spatial-attention sub-modules that reshape membrane-potential distributions, lowering firing rates.
  > zh: 把冗余噪声脉冲归因于脉冲网络的时空不变性，并用一对空间注意力子模块调整膜电位分布，有效降低发放率。
- Temporal-Coded Spiking Neural Networks with Dynamic Firing Threshold: Learning with Event-Driven Backpropagation (**ICCV 2023**). [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wei_Temporal-Coded_Spiking_Neural_Networks_with_Dynamic_Firing_Threshold_Learning_with_ICCV_2023_paper.pdf)]
  > Fixes over-sparse firing and costly causal-set search in TTFS coding via a dynamic firing threshold, enabling event-driven direct training of deep temporal-coded SNNs.
  > zh: 针对 TTFS 编码中脉冲过稀与因果集难求的问题引入动态发放阈值，使深层时间编码脉冲网络可用事件驱动方式直接训练。
- Efficient Converted Spiking Neural Network for 3D and 2D Classification	(**ICCV 2023**). [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Lan_Efficient_Converted_Spiking_Neural_Network_for_3D_and_2D_Classification_ICCV_2023_paper.pdf)]
  > Adapts thresholds to neuron activation state and widens the spiking output range, so ANN-to-SNN conversion reaches usable accuracy on point clouds and images in few time steps.
  > zh: 根据神经元激活状态自适应调整阈值并扩大脉冲输出范围，让 ANN 到 SNN 的转换在很少的时间步内同时适用于点云与图像分类。
- Deep Directly-Trained Spiking Neural Networks for Object Detection (**ICCV 2023**). [[paper](https://arxiv.org/abs/2307.11411)]
  > Trains an object detector directly with surrogate gradients instead of conversion, using a full-spike residual block proved to avoid vanishing or exploding gradients at depth.
  > zh: 用代理梯度直接训练目标检测脉冲网络而非依赖转换，并以全脉冲残差块 EMS-ResNet 在加深网络时避免梯度消失或爆炸。
- Towards Memory- and Time-Efficient Backpropagation for Training Spiking Neural Networks (**ICCV 2023**). [[paper](https://arxiv.org/abs/2302.14311)]
  > Drops the temporal routes of the backpropagation graph, which contribute little to gradients, making memory cost independent of the number of time steps.
  > zh: 舍弃 BPTT 计算图中对梯度贡献很小的时间维路径，使训练显存占用与总时间步数无关，同时减少标量乘法次数。
- SSF: Accelerating Training of Spiking Neural Networks with Stabilized Spiking Flow (**ICCV 2023**). [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_SSF_Accelerating_Training_of_Spiking_Neural_Networks_with_Stabilized_Spiking_ICCV_2023_paper.pdf)]
  > Averages each neuron's input and output activations over time and routes gradients through a mapping between them, cutting the training cost that temporal entanglement causes.
  > zh: 把每个神经元的输入输出在时间维上求平均得到稳定量，再经二者的映射关系直接回传梯度，摆脱时间纠缠带来的训练耗时。
- Masked Spiking Transformer (**ICCV 2023**). [[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_Masked_Spiking_Transformer_ICCV_2023_paper.pdf)]
  > Converts a trained Transformer into a spiking one, then randomly masks spikes in the manner of quantal synaptic failure to prune redundant firing and save power.
  > zh: 先经 ANN-to-SNN 转换得到脉冲 Transformer，再借鉴量子化突触失效随机掩蔽脉冲，剪除冗余发放以降低功耗。
- Spatial-Temporal Self-Attention for Asynchronous Spiking Neural Networks (**IJCAI 2023**). [[paper](https://www.ijcai.org/proceedings/2023/0344.pdf)]
  > Computes feature dependence jointly across time and space plus a spatio-temporal position bias, keeping attention compatible with asynchronous event-driven spike transmission.
  > zh: 在时间与空间维度上联合计算特征依赖并加入时空相对位置偏置，使注意力不破坏脉冲网络的异步事件驱动传输特性。
- Learnable Surrogate Gradient for Direct Training Spiking Neural Networks (**IJCAI 2023**). [[paper](https://www.ijcai.org/proceedings/2023/0335.pdf)]
  > Ties surrogate-gradient width to the membrane-potential distribution through trainable decay factors, so the width adapts during training and gradient vanishing or mismatch eases.
  > zh: 通过可训练的衰减因子把代理梯度的宽度与膜电位分布挂钩，训练中自动调节宽度，缓解梯度消失与梯度失配。
- Enhancing Efficient Continual Learning with Dynamic Structure Development of Spiking Neural Networks (**IJCAI 2023**). [[paper](https://www.ijcai.org/proceedings/2023/0334.pdf)]
  > Grows neurons for each new task and prunes redundant ones while reusing overlapping structure, giving continual learning without per-task subnetwork masks.
  > zh: 为每个新任务动态生长神经元并剪除冗余单元，通过共享重叠结构复用旧知识，无需为每个任务维护子网络掩码。
- Adaptive Smoothing Gradient Learning for Spiking Neural Networks (**ICML 2023**). [[paper](https://openreview.net/pdf?id=GdkwSGTpbC)]
  > Makes the surrogate's relaxation degree learnable and injects random spike noise, evolving a smoothed prototype network into a true SNN so smoothing error vanishes during training.
  > zh: 将代理梯度的松弛程度设为可学习参数并注入随机脉冲噪声，让平滑的原型网络逐步演化为真正的 SNN，从而消除平滑误差。
- Surrogate Module Learning: Reduce the Gradient Error Accumulation in Training Spiking Neural Networks (**ICML 2023**). [[paper](https://openreview.net/pdf?id=zRkz4duLKp)] [[code](https://github.com/brain-intelligence-lab/surrogate_module_learning)]
  > Attaches surrogate modules as a shortcut backward path and trains them jointly with a dedicated loss, curbing layerwise amplification of surrogate-gradient error in deep SNNs.
  > zh: 为深层 SNN 挂载代理模块以构建反传捷径，并用专门损失联合训练，抑制代理梯度误差在层间的逐层放大。
- Rate Gradient Approximation Attack Threats Deep Spiking Neural Networks (**CVPR 2023**). [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Bu_Rate_Gradient_Approximation_Attack_Threats_Deep_Spiking_Neural_Networks_CVPR_2023_paper.pdf)]
  > Exploits the rate-coding behavior of SNN layers to approximate gradients for adversarial attack, generalizing across leaky parameters and input encodings with a time-extended variant.
  > zh: 利用 SNN 层间以发放率编码通信的特性来近似梯度并构造对抗攻击，可推广到不同 LIF 泄漏参数与输入编码，并有时间维扩展增强。
- Constructing Deep Spiking Neural Networks from Artificial Neural Networks with Knowledge Distillation (**CVPR 2023**). [[paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Xu_Constructing_Deep_Spiking_Neural_Networks_From_Artificial_Neural_Networks_With_CVPR_2023_paper.pdf)]
  > Trains a spiking student jointly with an ANN teacher through knowledge distillation, transferring rich feature information instead of optimizing deep SNNs from scratch through non-differentiable spikes.
  > zh: 以 ANN 为教师、SNN 为学生做联合训练与蒸馏，迁移丰富的特征信息，避开在不可导脉冲上从零训练深层网络。
- Attention Spiking Neural Networks (**TPAMI 2023**) .[[paper](https://ieeexplore.ieee.org/abstract/document/10032591)] [[code](https://github.com/fangwei123456/spikingjelly/pull/329)]
  > Infers attention weights along temporal, channel and spatial dimensions and uses them to optimize membrane potentials, so spiking responses grow sparser while accuracy and energy efficiency improve.
  > zh: 推断时间、通道与空间维度上的注意力权重并用其优化膜电位，使脉冲发放更稀疏，同时提升精度与能效。
- Heterogeneous neuronal and synaptic dynamics for spike-efficient unsupervised learning: Theory and design principles (**ICLR 2023**).[[paper](https://arxiv.org/pdf/2302.11618.pdf)]
  > Diversifies neuronal integration/relaxation and STDP dynamics via Bayesian optimization, proving heterogeneity raises a recurrent SNN's memory capacity while cutting spiking activity in unsupervised learning.
  > zh: 借助贝叶斯优化使神经元积分/弛豫与 STDP 动力学异质化，理论证明异质性可提升循环 SNN 的记忆容量并降低发放量。
- Spiking Convolutional Neural Networks for Text Classification (**ICLR 2023**) .[[paper](https://openreview.net/pdf?id=pgU3k7QXuz0)]
  > Encodes pretrained word embeddings as spike trains and builds text classifiers by converting a standard CNN then fine-tuning it, extending SNNs to variable-length language input.
  > zh: 把预训练词向量编码为脉冲序列，并以「转换＋微调」两步流程训练文本分类器，将 SNN 推广到变长文本任务。
- Bridging the Gap between ANNs and SNNs by Calibrating Offset Spikes (**ICLR 2023**).[[paper](https://arxiv.org/pdf/2302.10685.pdf)] [[code](https://github.com/hzc1208/ANN2SNN_COS)]
  > Defines an offset spike to quantify firing-rate deviation and shifts the initial membrane potential by a provably optimal amount, iteratively shrinking ANN-SNN conversion error at low latency.
  > zh: 定义 offset spike 来度量实际与目标发放率的偏差，并按理论最优量平移初始膜电位，可迭代地压低 ANN-SNN 转换误差。
- Spikformer: When Spiking Neural Network Meets Transformer (**ICLR 2023**) .[[paper](https://openreview.net/forum?id=frE4fUwz_h)] [[code](https://github.com/ZK-Zhou/spikformer)]
  > Replaces dot-product attention with spike-form Query, Key and Value and drops softmax entirely, letting a Transformer backbone run on sparse, multiplication-free operations inside an SNN.
  > zh: 以脉冲形式的 Query/Key/Value 构建脉冲自注意力并彻底去掉 softmax，使 Transformer 主干在 SNN 中以稀疏、免乘法的方式运算。
- A Unified Framework of Soft Threshold Pruning (**ICLR 2023**). [[paper](https://openreview.net/forum?id=cCFqcrq0d8)] [[code](https://github.com/Yanqi-Chen/LATS)]
  > Recasts soft-threshold pruning as an ISTA solution to an implicit L1 problem, deriving a threshold scheduler that tracks the learning rate for better sparsity-performance tradeoffs.
  > zh: 将软阈值剪枝重构为求解隐式 L1 问题的 ISTA 过程，据此推出与学习率同步变化的阈值调度器，改善稀疏度与精度的权衡。
- Bridging the Gap between ANNs and SNNs by Calibrating Offset Spikes (**ICLR 2023**). [[paper](https://openreview.net/forum?id=PFbzoWZyZRX)] [[code](https://github.com/hzc1208/ANN2SNN_COS)]
  > Defines an offset spike to quantify firing-rate deviation and shifts the initial membrane potential by a provably optimal amount, iteratively shrinking ANN-SNN conversion error at low latency.
  > zh: 定义 offset spike 来度量实际与目标发放率的偏差，并按理论最优量平移初始膜电位，可迭代地压低 ANN-SNN 转换误差。
- Reducing ANN-SNN Conversion Error through Residual Membrane Potential (**AAAI 2023**). [[paper](https://arxiv.org/abs/2302.02091)] [[code](https://github.com/hzc1208/ANN2SNN_SRP)]
  > Categorizes the unevenness error caused by differing spike-arrival timings and corrects it with residual membrane potential, keeping ANN-SNN conversion accurate under very short time-step budgets.
  > zh: 将脉冲到达时序不同所致的不均匀误差分为四类，并用残差膜电位加以校正，使 ANN-SNN 转换在极少时间步下仍保持精度。
- Deep Spiking Neural Networks with High Representation Similarity Model Visual Pathways of Macaque and Mouse (**AAAI 2023**). [[paper](https://arxiv.org/abs/2303.06060)]
  > Benchmarks deep SNNs against CNNs and ViTs on macaque and mouse neural recordings under three similarity metrics, finding spiking models match biological visual hierarchies more closely.
  > zh: 在三种相似性度量下将深层 SNN 与 CNN、ViT 同猕猴和小鼠的神经记录对比，发现脉冲模型与生物视觉层级的表征更接近。
- ESL-SNNs: An Evolutionary Structure Learning Strategy for Spiking Neural Networks (**AAAI 2023**). [[paper](https://arxiv.org/pdf/2306.03693.pdf)]
  > Prunes and regrows synapses dynamically during training while holding connection density fixed, letting sparse SNNs be learned from scratch rather than compressed after convergence.
  > zh: 在训练过程中动态剪除并重新生长突触连接、始终保持结构稀疏度，实现从零训练稀疏 SNN，而非训练完成后再压缩。
- Exploring Temporal Information Dynamics in Spiking Neural Networks (**AAAI 2023**). [[paper](https://arxiv.org/pdf/2211.14406.pdf)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Exploring-Temporal-Information-Dynamics-in-Spiking-Neural-Networks)]
  > Tracks Fisher information of weights across timesteps to expose how trained spiking networks concentrate information in the earliest steps, then turns that signal into an iterative pruning criterion.
  > zh: 用权重的 Fisher 信息量化各时间步的信息分布，揭示训练后信息向早期时间步集中的现象，并据此设计迭代剪枝准则。
- Scaling Up Dynamic Graph Representation Learning via Spiking Neural Networks(**AAAI 2023**). [[paper](https://arxiv.org/pdf/2208.10364.pdf)] [[code](https://github.com/EdisonLeeeee/SpikeNet)]
  > Models temporal-graph evolution with populations of spiking neurons instead of RNNs, propagating structure as spike trains to cut computation and memory on million-node dynamic graphs.
  > zh: 以脉冲神经元群体替代 RNN 建模动态图的演化，用脉冲序列传递结构信息，在百万节点级时序图上降低计算与内存开销。
- Complex Dynamic Neurons Improved Spiking Transformer Network for Efficient Automatic Speech Recognition(**AAAI 2023**). [[paper](https://arxiv.org/pdf/2302.01194.pdf)] 
  > Post-processes spiking-Transformer sequence outputs through four neuronal dynamics richer than LIF, cutting phoneme error rate and computational cost on automatic speech recognition while improving robustness.
  > zh: 在脉冲 Transformer 的序列输出后接入四类比 LIF 更复杂的神经元动力学，降低语音识别的音素错误率与计算开销，并提升鲁棒性。

**Arxiv**
- Spikingformer: Spike-driven Residual Learning for Transformer-based Spiking Neural Network [[paper](https://arxiv.org/abs/2304.11954)] [[code](https://github.com/zhouchenlin2096/Spikingformer)]
  > Merges membrane-shortcut residuals with spiking self-attention so every layer stays spike-driven, eliminating the integer-float multiplications that Spikformer's residual structure leaves behind for neuromorphic deployment.
  > zh: 将膜电位残差与脉冲自注意力融合，使骨干各层保持脉冲驱动，消除 Spikformer 残差结构残留的整数-浮点乘法，便于神经形态部署。
- Enhancing the Performance of Transformer-based Spiking Neural Networks by Improved Downsampling with Precise Gradient Backpropagation [[paper](https://arxiv.org/abs/2305.05954)] [[code](https://github.com/zhouchenlin2096/Spikingformer-CML)]
  > Reorders the downsampling module into ConvBN-MaxPooling-LIF so gradients backpropagate without distortion, raising spiking-Transformer accuracy on both static-image and neuromorphic benchmarks over Spikingformer.
  > zh: 把下采样模块重排为 ConvBN-MaxPooling-LIF，消除梯度反传的失真，在静态图像与神经形态数据集上均超过 Spikingformer 的精度。
- Training Full Spike Neural Networks via Auxiliary Accumulation Pathway [[paper](https://arxiv.org/pdf/2301.11929.pdf)]
  > Attaches a detachable accumulation pathway alongside full-spike residual networks to compensate information lost in binary propagation, then removes it at test time for spike-only inference.
  > zh: 为全脉冲残差网络并联一条可拆卸的累积支路，补偿二值脉冲前传与反传中的信息损失，推理时移除以保持纯脉冲运算。
- MSS-DepthNet: Depth Prediction with Multi-Step Spiking Neural Network [[paper](https://arxiv.org/abs/2211.12156)]
  > Pairs a redesigned spiking residual block with multi-dimension attention and a dedicated event-stream encoding, surpassing same-size ANNs on MVSEC depth prediction while staying computationally cheap.
  > zh: 为事件相机深度估计重新设计脉冲残差块，并加入多维注意力与专用事件流编码，在 MVSEC 上超过同规模 ANN 且计算更省。
- SpikeGPT: Generative Pre-trained Language Model with Spiking Neural Networks [[paper](https://arxiv.org/abs/2302.13939)] [[code](https://github.com/ridgerchu/SpikeGPT)]
  > Adapts RWKV's linear-complexity attention into binary event-driven spiking units to build a 216M-parameter generative language model trainable by backpropagation, staying competitive with non-spiking baselines.
  > zh: 把 RWKV 的线性复杂度注意力改造为二值事件驱动脉冲单元，训练出 216M 参数的生成式语言模型，性能与非脉冲模型相当。
- Auto-Spikformer: Spikformer Architecture Search [[paper](https://arxiv.org/pdf/2306.00807.pdf)]
  > Searches Spikformer's channel and block configuration with a one-shot supernet plus evolved spiking-neuron parameters, scored by a joint accuracy-energy fitness that trims redundancy and inference energy.
  > zh: 用一次性超网搜索 Spikformer 的通道与模块配置，并进化优化脉冲神经元参数，以精度-能耗联合适应度剔除冗余、降低推理能耗。
- Advancing Spiking Neural Networks Towards Deep Residual Learning [[paper](https://arxiv.org/pdf/2112.08954.pdf)]
  > Routes shortcuts through membrane potentials instead of spikes and proves gradient-norm equality via block dynamical isometry, scaling directly trained SNNs to 482 layers without degradation.
  > zh: 让残差捷径走膜电位而非脉冲，并用块动力学等距理论证明梯度范数相等，把直接训练的 SNN 深度扩展到 482 层而不退化。


### 2022

**NeurIPS, CVPR, ICLR, AAAI, ICML, Nature Communications**

- Event-based Video Reconstruction via Potential-assisted Spiking Neural Network [[paper](https://arxiv.org/abs/2201.10943)] [[code](https://github.com/LinZhu111/EVSNN)]
  > Reconstructs video from event streams with a fully spiking encoder-decoder, reading out membrane potential instead of spikes so intensity detail survives, at a fraction of ANN energy.
  > zh: 用全脉冲编码器-解码器从事件流重建视频，以膜电位而非脉冲读出以保留灰度细节，能耗远低于同结构 ANN。
- Optimal ANN-SNN Conversion for High-accuracy and Ultra-low-latency Spiking Neural Networks [[paper](https://openreview.net/forum?id=7B3IJMM1k_M)] [[code](https://github.com/putshua/SNN-conversion-QCFS)]
  > Replaces ReLU in the source ANN with a quantization-clip-floor-shift activation that matches spiking firing-rate curves, driving expected conversion error to zero at very few time steps.
  > zh: 将源 ANN 的 ReLU 换成 quantization clip-floor-shift 激活以拟合脉冲发放率曲线，使期望转换误差归零，支持极少时间步推理。
- Optimized Potential Initialization for Low-latency Spiking Neural Networks (**AAAI 2022**). [[paper](https://arxiv.org/abs/2202.01440)]
  > Shows threshold scaling to act like weight normalization, then tunes each layer's initial membrane potential to cancel conversion loss and reach ANN accuracy in far fewer time steps.
  > zh: 先说明阈值缩放等价于权重归一化，再逐层优化初始膜电位以抵消转换误差，用远更少的时间步逼近原 ANN 精度。
- AutoSNN: Towards Energy-Efficient Spiking Neural Networks [[paper](https://arxiv.org/abs/2201.12738)]
  > Searches SNN architectures with a fitness that rewards low spike counts as well as accuracy, after excluding design choices found to inflate firing in hand-crafted backbones.
  > zh: 以同时权衡精度与脉冲发放数的适应度函数搜索网络结构，并剔除会推高发放率的常见设计，得到更省能的架构。
- Neural Architecture Search for Spiking Neural Networks [[paper](https://arxiv.org/abs/2201.10355)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Neural-Architecture-Search-for-Spiking-Neural-Networks)]
  > Ranks candidate networks at initialization by how diversely their spike patterns separate samples, and searches backward temporal-feedback connections alongside feedforward ones, avoiding any training during search.
  > zh: 在初始化阶段按脉冲激活模式的多样性对候选结构打分，实现免训练搜索，并同时搜索层间反向（时间反馈）连接。
- Neuromorphic Data Augmentation for Training Spiking Neural Networks [[paper](https://arxiv.org/abs/2203.06145)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/NDA_SNN)]
  > Adapts geometric image augmentations to event streams so sparse neuromorphic datasets stop overfitting, stabilizing training and enabling unsupervised contrastive learning for spiking networks.
  > zh: 把几何图像增广适配到事件数据上，缓解小规模神经形态数据集的过拟合，稳定训练，并首次支持 SNN 的无监督对比学习。
- State Transition of Dendritic Spines Improves Learning of Sparse Spiking Neural Networks [[paper](https://proceedings.mlr.press/v162/chen22ac.html)] [[code](https://github.com/Yanqi-Chen/STDS)]
  > Reparameterizes weights as dendritic-spine sizes whose state transitions gate pruning, letting a growing threshold schedule control pruning speed and avoid late-training collapse at high sparsity.
  > zh: 将权重重参数化为树突棘尺寸，用状态转换实现动态剪枝，并以生长阈值调节剪枝速度，避免训练后期在高稀疏度下崩溃。
- Training High-Performance Low-Latency Spiking Neural Networks by Differentiation on Spike Representation [[paper](https://arxiv.org/abs/2205.00459)] [[code](https://github.com/qymeng94/DSR)]
  > Treats spiking dynamics as a sub-differentiable map from weighted firing-rate representations, so gradients flow without surrogate functions, and trains per-layer thresholds to shrink representation error.
  > zh: 把脉冲动力学视为加权发放率表示上的次可微映射，绕开代理梯度直接求导，并训练逐层阈值以减小表示误差。
- Exploring Lottery Ticket Hypothesis in Spiking Neural Networks [[paper](https://arxiv.org/abs/2207.01382)] [[code](https://github.com/Intelligent-Computing-Lab-Yale/Exploring-Lottery-Ticket-Hypothesis-in-SNNs)]
  > Confirms winning tickets exist in deep spiking networks at high sparsity, then finds connectivity from only the earliest time steps to cut iterative-magnitude-pruning search cost.
  > zh: 验证深层 SNN 中存在高稀疏度的中奖彩票，并用仅由前几个时间步确定连接的 Early-Time 票，降低迭代幅值剪枝的搜索开销。
- Spiking Graph Convolutional Networks [[paper](https://arxiv.org/abs/2205.02767)] [[code](https://github.com/ZulunZhu/SpikingGCN)]
  > Encodes graph-convolved node features as spike trains fed to a single spiking classifier layer, keeping citation, image-graph and recommendation accuracy while running on neuromorphic chips.
  > zh: 用图卷积把节点特征编码成脉冲序列，再由单层脉冲分类器判别，在引文网络与推荐等任务上保持精度且可部署于神经形态芯片。
- A calibratable sensory neuron based on epitaxial VO2 for spike-based neuromorphic multisensory system [[paper](https://www.nature.com/articles/s41467-022-31747-w)] [[code](https://github.com/billyuanpku96/SNN-for-sensory-neuron)]
  > Builds artificial sensory neurons from epitaxial VO2 and adds calibration and scaling resistors, so one spike encoder handles illuminance, temperature, pressure and curvature with consistent device behavior.
  > zh: 用外延 VO2 制作人工感觉神经元，并加入校准电阻与缩放电阻，把光照、温度、压力和曲率统一编码为脉冲，改善器件间与循环间一致性。
- Online Training Through Time for Spiking Neural Networks (**NeurIPS 2022**). [[paper](https://arxiv.org/abs/2210.04195)] [[code](https://github.com/pkuxmq/OTTT-SNN)]
  > Derives a forward-in-time learning rule from BPTT by tracking presynaptic traces, holding training memory constant in the number of time steps and taking a three-factor Hebbian form.
  > zh: 由 BPTT 推导出沿时间前向的在线学习规则，仅跟踪突触前迹，使训练显存与时间步数无关，且形式上属于三因子 Hebbian 更新。
- Training Spiking Neural Networks with Event-driven Backpropagation [[paper](https://openreview.net/forum?id=d4JmP1T45WE)] [[code](https://github.com/zhuyaoyu/SNN-event-driven-learning)]
  > Backpropagates only at spike times rather than every step, proving gradient sums are preserved across convolutional layers and adding a backward kernel that fixes mistimed gradients.
  > zh: 仅在脉冲发放时刻反传梯度而非逐时间步展开，证明全连接与卷积层的梯度和守恒，并用反向卷积核修正梯度的时序错配。
- GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks [[paper](https://openreview.net/forum?id=UmFSx2c4ubT)] [[code](https://github.com/Ikarosy/Gated-LIF)]
  > Fuses several leaky-integrate-and-fire variants inside one neuron and learns gating factors that weight each bio-feature during training, widening the dynamics a single spiking layer can express.
  > zh: 在单个神经元内融合多种 LIF 变体的生物特性，用可训练的门控因子决定各特性占比，扩大脉冲神经元的动力学表达空间。
- Temporal Effective Batch Normalization in Spiking Neural Networks [[paper](https://openreview.net/forum?id=fLIgyyQiJqz)]
  > Rescales presynaptic inputs with a separate learned weight at every time-step, smoothing temporal distributions so batch normalization finally pays off inside spiking networks.
  > zh: 在每个时间步以独立权重重标定突触前输入，平滑时间维度分布，让批归一化在脉冲网络中真正生效，并降低超参数敏感度。
- Training Spiking Neural Networks with Local Tandem Learning (**NeurIPS 2022**). [[paper](https://arxiv.org/pdf/2210.04532.pdf)]
  > Trains each spiking layer locally to mimic a pretrained ANN's intermediate features, decoupling layers for fast convergence and on-chip calibration against analog device non-idealities.
  > zh: 让每层脉冲网络就地模仿预训练 ANN 的中间特征，逐层解耦训练以快速收敛，并支持在混合信号神经形态芯片上做片上校准。
- IM-Loss: Information Maximization Loss for Spiking Neural Networks (**NeurIPS 2022**). [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/010c5ba0cafc743fece8be02e7adb8dd-Paper-Conference.pdf)]
  > Maximizes information flow under 0/1 spike quantization with an auxiliary loss that doubles as normalization without extra inference operations, paired with evolutionary surrogate gradients.
  > zh: 用信息最大化损失缓解 0/1 脉冲量化带来的信息损失，同时充当归一化而不增加推理算子，并配合可演化的代理梯度。
- Temporal Effective Batch Normalization in Spiking Neural Networks (**NeurIPS 2022**). [[paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf)]
  > Applies per-time-step scaling on top of shared batch statistics so normalization accounts for the temporal dimension, reaching higher accuracy with fewer time-steps and steadier hyper-parameters.
  > zh: 在共享批统计之上为每个时间步加独立缩放，使归一化兼顾时间维度，以更少时间步取得更高精度且对超参数更稳健。
- Biologically Inspired Dynamic Thresholds for Spiking Neural Networks (**NeurIPS 2022**). [[paper](https://arxiv.org/pdf/2206.04426.pdf)]
  > Couples the firing threshold to average membrane potential and preceding depolarization rate, mirroring neuronal homeostasis and improving stability on noisy robotic obstacle-avoidance and control tasks.
  > zh: 依据神经元稳态，让阈值随平均膜电位上升、随去极化速率下降而动态调节，在含噪声的机器人避障与控制任务中更稳定。
- Optimal Conversion of Conventional Artificial Neural Networks to Spiking Neural Networks (**ICLR 2022**). [[paper](https://arxiv.org/pdf/2103.00476.pdf)] [[code](https://github.com/Jackn0/snn_optimal_conversion_pipeline)]
  > Decomposes ANN-to-SNN conversion error recursively into layer-wise terms, then combines threshold balancing with soft reset to match ANN accuracy at roughly a tenth of the usual simulation time.
  > zh: 把 ANN-SNN 转换误差递归分解为逐层求和，结合阈值平衡与软复位，用约十分之一的仿真时长逼近原 ANN 精度。
- Multi-Level Firing with Spiking DS-ResNet: Enabling Better and Deeper Directly-Trained Spiking Neural Networks (**IJCAI 2022**). [[paper](https://arxiv.org/pdf/2210.06386.pdf)]
  > Splits each neuron into multiple firing levels for more efficient gradient propagation and adds dormant-suppressed residual blocks that map discrete spikes identically, countering degradation in deep directly-trained SNNs.
  > zh: 将神经元拆成多级发放以改善梯度传播，并用抑制静默的残差块实现离散脉冲恒等映射，缓解深层直训 SNN 的梯度消失与退化。

### 2021

**NeurIPS, ICCV, IJCAI, ICML, AAAI**

- Deep Residual Learning in Spiking Neural Networks (**NeurIPS 2021**). [[paper](https://proceedings.neurips.cc/paper/2021/file/afe434653a898da20044041262b3ac74-Paper.pdf)] [[code](https://github.com/fangwei123456/Spike-Element-Wise-ResNet)]
  > Reworks the residual block so shortcuts add spikes element-wise, guaranteeing identity mapping and stable gradients, and enabling directly trained spiking networks beyond 100 layers.
  > zh: 将残差块改为脉冲逐元素相加，保证恒等映射并避免梯度消失与爆炸，首次让百层以上的脉冲网络可以直接训练。
- Spiking Deep Residual Network[[paper](https://arxiv.org/pdf/1805.01352.pdf)]
  > Converts a trained ResNet to spikes with a shortcut conversion model that scales activations to firing rates and a compensation step for discretization error, reaching depths beyond 40 layers.
  > zh: 用专门的捷径转换模型把激活值缩放到对应发放率，并以补偿机制减小离散化误差，将转换所得脉冲 ResNet 推进到 40 层以上。
- Incorporating Learnable Membrane Time Constant to Enhance Learning of Spiking Neural Networks (**ICCV 2021**). [[paper](https://arxiv.org/abs/2007.05785)] [[code](https://github.com/fangwei123456/Parametric-Leaky-Integrate-and-Fire-Spiking-Neuron)]
  > Makes the membrane time constant a trainable parameter learned jointly with weights, letting each layer set its own decay and reaching higher accuracy with fewer timesteps.
  > zh: 把膜时间常数变为可学习参数并与权重联合训练，让各层自行决定衰减速度，在更少时间步下取得更高精度与更强鲁棒性。
- Pruning of Deep Spiking Neural Networks through Gradient Rewiring [[paper](https://arxiv.org/abs/2105.04916)] [[code](https://github.com/Yanqi-Chen/Gradient-Rewiring)]
  > Reparameterizes each synapse so pruning and regrowth compete under one gradient, learning connectivity and weights jointly and exposing heavy redundancy in deep spiking networks without retraining.
  > zh: 为突触引入统一参数，让剪枝与连接再生在同一梯度下竞争，联合学习连接结构与权重，无需重训练即可揭示深层 SNN 的冗余。
- A Free Lunch From ANN: Towards Efficient, Accurate Spiking Neural Networks Calibration (**ICML 2021**). [[paper](https://arxiv.org/pdf/2106.06984)] [[code](https://github.com/yhhhli/SNN_Calibration)]
  > Corrects conversion error layer by layer with a handful of training samples, adjusting the converted network's weights and biases instead of retraining a spiking model from scratch.
  > zh: 用少量训练样本逐层校准转换后 SNN 的权重与偏置，修正沿深度累积的转换误差，无需从头训练即可提升转换精度。
- Optimal ANN-SNN Conversion for Fast and Accurate Inference in Deep Spiking Neural Networks [[paper](https://arxiv.org/pdf/2105.11654)] [[code](https://github.com/DingJianhao/OptSNNConvertion-RNL-RIL)]
  > Swaps ReLU for a rate norm layer with a learnable clipping bound and fits the activation-to-firing-rate curve, cutting the timesteps a converted network needs at inference.
  > zh: 用带可学习上界的 Rate Norm Layer 取代源 ANN 中的 ReLU，并拟合激活值与发放率的对应关系，在近乎无损转换的同时缩短推理时间步。
- Sparse Spiking Gradient Descent (**NeurIPS 2021**). [[paper](https://proceedings.neurips.cc/paper/2021/file/61f2585b0ebcf1f532c4d1ec9a7d51aa-Paper.pdf)]
  > Restricts backpropagation to neurons whose membrane potential sits near threshold, exploiting spatiotemporal spike sparsity to cut backward-pass time and memory against dense tensor implementations.
  > zh: 只对膜电位接近阈值的神经元做反向传播，利用脉冲的时空稀疏性，相比稠密张量实现大幅降低反向过程的耗时与显存。
- Training Spiking Neural Networks with Accumulated Spiking Flow (**AAAI 2021**). [[paper](https://arxiv.org/pdf/2011.05280.pdf)]
  > Derives gradients from spike counts accumulated over the whole time window rather than unrolling every timestep, using a linear estimate of neuron dynamics to keep training cost low.
  > zh: 用时间窗内累积的输入输出脉冲量替代逐时间步展开来计算梯度，并以自适应线性估计刻画神经元动态，降低训练复杂度。
- Temporal-wise Attention Spiking Neural Networks for Event Streams Classification (**ICCV 2021**). [[paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Yao_Temporal-Wise_Attention_Spiking_Neural_Networks_for_Event_Streams_Classification_ICCV_2021_paper.pdf)]
  > Scores each event frame's significance with temporal-wise attention during training and discards irrelevant frames at inference, trimming redundant timesteps for gesture, image and spoken-digit classification.
  > zh: 训练时用时间维注意力评估各事件帧的重要性，推理时丢弃无关帧，在手势、图像与语音数字等事件流分类中削减冗余时间步。


