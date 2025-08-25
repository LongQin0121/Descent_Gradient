# 进近与下降要点整理

## 1. 落地许可
- **在距离跑道接地点 (Touchdown) 2 NM 之前，必须发布落地许可**。

---

## 2. 切入最后进近航向道
- 切入前：至少 **2 公里平飞**。  
- 切入后：保持 **1 NM 平飞**。

---

## 3. 五边与速度控制
- 五边越短 → **MP 控速越小**。  
- 五边短时，后续航迹调整和追赶的余地有限。

---

## 4. 单跑道参数（示例）
- **12/600**  
- **18/900**

（注：具体对应条件需结合净空/机场情况）

---

## 5. 下滑长度
- **取决于五边的净空条件**。

---

## 6. A320 巡航与下降速度剖面

### 巡航速度范围
- **Mach 0.70 – 0.78**

### 下降速度剖面
- **最早下降方案**  
  - M 0.78  
  - 转换为 IAS 310 kt  
  - FL100 前减为 IAS 250 kt  
  - MP 点前减为 IAS 170 kt  

- **最晚下降方案**  
  - M 0.70  
  - 转换为 IAS 250 kt  
  - FL150 减为 IAS 220 kt  
  - MP 点前减为 IAS 170 kt


---

# Approach and Descent Notes

## 1. Landing Clearance
- **Landing clearance must be issued before the aircraft is within 2 NM of touchdown**.

---

## 2. Final Approach Interception
- Before interception: at least **2 km level flight**.  
- After interception: maintain **1 NM level flight**.

---

## 3. Base Leg and Speed Control
- The shorter the base leg → the **less margin for MP (Missed Approach Point) speed control**.  
- A shorter base leg leaves limited room for adjustments or catching up.

---

## 4. Single Runway Parameters (Example)
- **12/600**  
- **18/900**

(Note: actual values depend on obstacle clearance and airport conditions)

---

## 5. Glide Path Length
- Determined by **obstacle clearance on the base leg**.

---

## 6. A320 Cruise and Descent Speed Profiles

### Cruise Speed Range
- **Mach 0.70 – 0.78**

### Descent Speed Profiles
- **Early Descent Profile**  
  - M 0.78  
  - Transition to IAS 310 kt  
  - Reduce to IAS 250 kt before FL100  
  - Reduce to IAS 170 kt before MP  

- **Late Descent Profile**  
  - M 0.70  
  - Transition to IAS 250 kt  
  - Reduce to IAS 220 k





---

# FL250以上 M=0.70 对应指示空速（ISA标准大气）

## 关键假设与说明
- 使用 **ISA** 温度/压强分布（对流层线性递减到 11 km，之后温度常数）。
- 先由 **马赫数 M** 计算 **真空速 TAS**：
  \[
  TAS = M \cdot a
  \]
  其中声速 \(a = \sqrt{\gamma R T}\)。
- 将 TAS 换成 **等效空速 EAS**：
  \[
  EAS = TAS \cdot \sqrt{\frac{\rho}{\rho_0}}
  \]
- 把 EAS 近似为 **IAS**（忽略仪表误差和可压缩性导致的 CAS/EAS 差异）。
- 常数：\(\gamma = 1.4\)，\(R = 287.058 \text{ J/(kg·K)}\)，\(\rho_0 = 1.225 \text{ kg/m³}\)。
- 速度单位最终换算为 **节 (kt)**。

R = 287.058 J/(kg·K)，ρ₀ = 1.225 kg/m³。速度单位最后换算为节（kt）。

## 高度 vs 指示空速表

| 高度 | 温度 (K) | 真空速 TAS (kt) | 近似 IAS (kt) |
|---:|---:|---:|---:|
| FL250 (25 000 ft) | 238.62 | 421 | 282 |
| FL300 (30 000 ft) | 228.71 | 413 | 252 |
| FL350 (35 000 ft) | 218.81 | 406 | 224 |
| FL400 (40 000 ft) | 216.65 | 402 | 199 |
| FL450 (45 000 ft) | 216.65 | 402 | 177 |

## 解释要点
- 随高度上升，**TAS 对同一马赫数变化不大**（主要取决温度），但空气密度 \(\rho\) 快速下降，导致 **EAS/IAS** 随高度显著下降。
- 上表给出的是 **近似 IAS**。
- 若需要更精确的 CAS（考虑可压缩性修正），可按 **ICAO/FAA CAS ↔ EAS ↔ TAS 公式**进行进一步计算。
- 可选扩展：
  - 更细高度步长（如每 1000 ft）；
  - 输出 m/s 或 km/h；
  - 针对具体飞机的仪表偏差修正。

