# 等表速下降中下降梯度恒定性的完整推理过程

## **步骤1：建立力平衡方程**

### 基本力平衡（非稳定状态）
在下降过程中，考虑惯性力的完整力平衡方程：

**沿航迹方向：** $T_{idle} - D + W \cdot \sin(\gamma) = \frac{W}{g} \cdot \frac{dTAS}{dt}$

**垂直航迹方向：** $L - W \cdot \cos(\gamma) = 0$

### 重新整理得到下降梯度基本公式
$$\sin(\gamma) = \frac{D - T_{idle}}{W} - \frac{1}{g} \cdot \frac{dTAS}{dt}$$

---

## **步骤2：阻力表达式**

**总阻力：** $D = q \cdot S \cdot C_{D0} + \frac{k \cdot W^2}{q \cdot S}$
- 第一项：零升阻力
- 第二项：诱导阻力
- $q = \frac{1}{2}\rho V^2$ = 动压
  
NOTE:在亚音速飞行中，空气可视为不可压缩流体，阻力可以分解为两个独立的组成部分,不考虑激波阻力和压缩性修正

---

## **步骤3：等表速条件下的TAS变化率推导**

### 3.1 基本关系
**IAS与TAS关系：** $IAS = TAS \times \sqrt{\frac{\rho}{\rho_0}} = 常数$

**因此：** $TAS = IAS \times \sqrt{\frac{\rho_0}{\rho}}$

### 3.2 TAS对时间的导数
$$\frac{dTAS}{dt} = \frac{d}{dt}\left[IAS \times \sqrt{\frac{\rho_0}{\rho}}\right]$$

$$= IAS \times \sqrt{\rho_0} \times \frac{d}{dt}\left[\rho^{-1/2}\right]$$

$$= IAS \times \sqrt{\rho_0} \times \left(-\frac{1}{2}\right) \times \rho^{-3/2} \times \frac{d\rho}{dt}$$

**简化：** $\frac{dTAS}{dt} = -\frac{1}{2} \times IAS \times \sqrt{\frac{\rho_0}{\rho^3}} \times \frac{d\rho}{dt}$

### 3.3 密度变化率
**链式法则：** $\frac{d\rho}{dt} = \frac{d\rho}{dh} \times \frac{dh}{dt}$

**其中：**
- $\frac{d\rho}{dh} = -1.225 \times 10^{-4} \times \rho$ （标准大气密度梯度）
- $\frac{dh}{dt} = -TAS \times \sin(\gamma) = -IAS \times \sqrt{\frac{\rho_0}{\rho}} \times \sin(\gamma)$

**代入：**
$$\frac{d\rho}{dt} = \left(-1.225 \times 10^{-4} \times \rho\right) \times \left(-IAS \times \sqrt{\frac{\rho_0}{\rho}} \times \sin(\gamma)\right)$$

$$= 1.225 \times 10^{-4} \times IAS \times \sin(\gamma) \times \sqrt{\rho_0 \times \rho}$$

### 3.4 最终TAS变化率公式
**代入密度变化率：**
$$\frac{dTAS}{dt} = -\frac{1}{2} \times IAS \times \sqrt{\frac{\rho_0}{\rho^3}} \times 1.225 \times 10^{-4} \times IAS \times \sin(\gamma) \times \sqrt{\rho_0 \times \rho}$$

**简化：**
$$\frac{dTAS}{dt} = -6.125 \times 10^{-5} \times IAS^2 \times \sin(\gamma) \times \frac{\rho_0}{\rho}$$

**实用形式：**
$$\boxed{\frac{dTAS}{dt} = -1.225 \times 10^{-4} \times IAS^2 \times \sin(\gamma) \text{ (m/s²)}}$$

---

## **步骤4：验证下降梯度恒定性**

### 4.1 代入完整力平衡方程
$$\sin(\gamma) = \frac{D - T_{idle}}{W} - \frac{1}{g} \cdot \frac{dTAS}{dt}$$

**代入TAS变化率：**
$$\sin(\gamma) = \frac{D - T_{idle}}{W} - \frac{1}{g} \times \left(-1.225 \times 10^{-4} \times IAS^2 \times \sin(\gamma)\right)$$

### 4.2 重新整理
$$\sin(\gamma) = \frac{D - T_{idle}}{W} + \frac{1.225 \times 10^{-4} \times IAS^2}{g} \times \sin(\gamma)$$

**移项：**
$$\sin(\gamma) - \frac{1.225 \times 10^{-4} \times IAS^2}{g} \times \sin(\gamma) = \frac{D - T_{idle}}{W}$$

**提取sin(γ)：**
$$\sin(\gamma) \times \left[1 - \frac{1.225 \times 10^{-4} \times IAS^2}{g}\right] = \frac{D - T_{idle}}{W}$$

### 4.3 最终下降梯度公式
$$\sin(\gamma) = \frac{\left[\frac{D - T_{idle}}{W}\right]}{1 - \frac{1.225 \times 10^{-4} \times IAS^2}{g}}$$

**其中阻力：**
$$\boxed{\sin(\gamma) = \frac{\left[\frac{q \cdot S \cdot C_{D0} + \frac{k \cdot W^2}{q \cdot S} - T_{idle}}{W}\right]}{1 - \frac{1.225 \times 10^{-4} \times IAS^2}{g}}}$$

---

## **步骤5：恒定性验证**

### 等表速下降条件下各项分析：
- $q = \frac{1}{2}\rho_0 \cdot IAS^2$ = 常数（等表速）
- $S, C_{D0}, k, W, T_{idle}$ = 常数
- **分子：$\frac{D - T_{idle}}{W}$** = 常数
- **分母：$\left[1 - \frac{1.225 \times 10^{-4} \times IAS^2}{g}\right]$** = 常数

---

## **最终结论**

**在等表速下降中，下降梯度sin(γ)保持恒定！**

这个结论成立的关键在于：
1. 虽然TAS在下降过程中发生变化
2. 但TAS的变化率与下降梯度成正比
3. 在力平衡方程中，这种正比关系导致了一个恒定的修正因子
4. 最终结果是下降梯度仍然保持恒定

这解释了为什么等表速下降是航空中如此可靠和常用的飞行技术。

---

## **符号说明**
- $\gamma$：下降角（负值表示下降）
- $W$：飞机重量
- $D$：总阻力
- $T_{idle}$：怠速推力
- $TAS$：真空速
- $IAS$：表速
- $q$：动压
- $\rho$：空气密度
- $\rho_0$：海平面标准密度
- $S$：机翼面积
- $C_{D0}$：零升阻力系数
- $k$：诱导阻力因子
- $g$：重力加速度



---
## **步骤2 NOTE：阻力表达式**

### 亚音速飞行条件下的阻力模型
在**亚音速飞行**中（M < 0.8），空气可视为不可压缩流体，阻力可以分解为两个独立的组成部分：

**总阻力：** $D = q \cdot S \cdot C_{D0} + \frac{k \cdot W^2}{q \cdot S}$

### 阻力组成分析：

#### **第一项：零升阻力（寄生阻力）**
- **$D_0 = q \cdot S \cdot C_{D0}$**
- **物理意义：** 机体在零升力条件下产生的阻力
- **包括：** 摩擦阻力、压差阻力、干扰阻力
- **特点：** 与动压成正比，与升力系数无关

#### **第二项：诱导阻力（升力相关阻力）**
- **$D_i = \frac{k \cdot W^2}{q \cdot S}$**
- **物理意义：** 产生升力时不可避免的阻力代价
- **来源：** 机翼翼尖涡流和下洗气流
- **特点：** 与升力系数的平方成正比，与动压成反比

### 关键参数：
- **$q = \frac{1}{2}\rho V^2$** = 动压
- **$S$** = 参考机翼面积
- **$C_{D0}$** = 零升阻力系数（取决于机体设计）
- **$k = \frac{1}{\pi \cdot AR \cdot e}$** = 诱导阻力因子
 - $AR$ = 展弦比（机翼展长²/机翼面积）
 - $e$ = 翼效系数（通常0.7-0.9）
- **$W$** = 飞机重量（等于所需升力）

### 亚音速假设的重要性：
1. **线性叠加原理成立：** 零升阻力和诱导阻力可以独立计算后相加
2. **压缩性效应忽略：** 不考虑激波阻力和压缩性修正
3. **升力线理论适用：** 诱导阻力与升力系数平方的关系保持线性
4. **阻力系数相对稳定：** $C_{D0}$和$k$在飞行包线内基本恒定

**注：** 当飞行速度接近音速（M > 0.8）时，需要考虑压缩性效应和激波阻力，此时阻力模型将变得更加复杂。