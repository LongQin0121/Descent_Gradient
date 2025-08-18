# Complete Derivation of Descent Gradient Constancy in Constant IAS Descent

## **Step 1: Establish Force Balance Equations**

### Basic Force Balance (Non-Steady State)
During descent, considering inertial forces, the complete force balance equations are:

**Along flight path:**
$$T_{idle} - D + W \cdot \sin(\gamma) = \frac{W}{g} \cdot \frac{dTAS}{dt}$$

**Normal to flight path:**
$$L - W \cdot \cos(\gamma) = 0$$

### Rearranged Basic Descent Gradient Formula
$$\sin(\gamma) = \frac{D - T_{idle}}{W} + \frac{1}{g} \cdot \frac{dTAS}{dt}$$

---

## **Step 2: Drag Expression**

**Total Drag:**
$$D = q \cdot S \cdot C_{D0} + \frac{k \cdot W^2}{q \cdot S}$$

- First term: Zero-lift drag
- Second term: Induced drag
- $q = \frac{1}{2}\rho V^2$ = dynamic pressure

**NOTE:** In subsonic flight, air can be considered incompressible fluid. Drag can be decomposed into two independent components, excluding wave drag and compressibility corrections.

---

## **Step 3: Derivation of TAS Rate of Change Under Constant IAS Conditions**

### 3.1 Basic Relationships

**IAS to TAS relationship:**
$$IAS = TAS \times \sqrt{\frac{\rho}{\rho_0}} = \text{constant}$$

**Therefore:**
$$TAS = IAS \times \sqrt{\frac{\rho_0}{\rho}}$$

### 3.2 Time Derivative of TAS

$$\frac{dTAS}{dt} = \frac{d}{dt}\left[IAS \times \sqrt{\frac{\rho_0}{\rho}}\right]$$

$$= IAS \times \sqrt{\rho_0} \times \frac{d}{dt}\left[\rho^{-1/2}\right]$$

$$= IAS \times \sqrt{\rho_0} \times \left(-\frac{1}{2}\right) \times \rho^{-3/2} \times \frac{d\rho}{dt}$$

**Simplified:**
$$\frac{dTAS}{dt} = -\frac{1}{2} \times IAS \times \sqrt{\frac{\rho_0}{\rho^3}} \times \frac{d\rho}{dt}$$

### 3.3 Density Rate of Change

**Chain rule:**
$$\frac{d\rho}{dt} = \frac{d\rho}{dh} \times \frac{dh}{dt}$$

**Where:**
- $\frac{d\rho}{dh} = -1.225 \times 10^{-4} \times \rho$ (Standard atmosphere density gradient)
- $\frac{dh}{dt} = -TAS \times \sin(\gamma) = -IAS \times \sqrt{\frac{\rho_0}{\rho}} \times \sin(\gamma)$

**Substituting:**
$$\frac{d\rho}{dt} = \left(-1.225 \times 10^{-4} \times \rho\right) \times \left(-IAS \times \sqrt{\frac{\rho_0}{\rho}} \times \sin(\gamma)\right)$$

$$= 1.225 \times 10^{-4} \times IAS \times \sin(\gamma) \times \sqrt{\rho_0 \times \rho}$$

### 3.4 Final TAS Rate of Change Formula

**Substituting density rate:**
$$\frac{dTAS}{dt} = -\frac{1}{2} \times IAS \times \sqrt{\frac{\rho_0}{\rho^3}} \times 1.225 \times 10^{-4} \times IAS \times \sin(\gamma) \times \sqrt{\rho_0 \times \rho}$$

**Simplified:**
$$\frac{dTAS}{dt} = -6.125 \times 10^{-5} \times IAS^2 \times \sin(\gamma) \times \frac{\rho_0}{\rho}$$

**Practical form:**
$$\boxed{\frac{dTAS}{dt} = -1.225 \times 10^{-4} \times IAS^2 \times \sin(\gamma) \text{ (m/s²)}}$$

---

## **Step 4: Verification of Descent Gradient Constancy**

### 4.1 Substitution into Complete Force Balance Equation

$$\sin(\gamma) = \frac{D - T_{idle}}{W} + \frac{1}{g} \cdot \frac{dTAS}{dt}$$

**Substituting TAS rate of change:**
$$\sin(\gamma) = \frac{D - T_{idle}}{W} + \frac{1}{g} \times \left(-1.225 \times 10^{-4} \times IAS^2 \times \sin(\gamma)\right)$$

### 4.2 Rearrangement

$$\sin(\gamma) = \frac{D - T_{idle}}{W} - \frac{1.225 \times 10^{-4} \times IAS^2}{g} \times \sin(\gamma)$$

**Moving terms:**
$$\sin(\gamma) + \frac{1.225 \times 10^{-4} \times IAS^2}{g} \times \sin(\gamma) = \frac{D - T_{idle}}{W}$$

**Factoring sin(γ):**
$$\sin(\gamma) \times \left[1 + \frac{1.225 \times 10^{-4} \times IAS^2}{g}\right] = \frac{D - T_{idle}}{W}$$

### 4.3 Final Descent Gradient Formula

$$\sin(\gamma) = \frac{\left[\frac{D - T_{idle}}{W}\right]}{1 + \frac{1.225 \times 10^{-4} \times IAS^2}{g}}$$

**Where drag is:**
$$\boxed{\sin(\gamma) = \frac{\left[\frac{q \cdot S \cdot C_{D0} + \frac{k \cdot W^2}{q \cdot S} - T_{idle}}{W}\right]}{1 + \frac{1.225 \times 10^{-4} \times IAS^2}{g}}}$$

---

## **Step 5: Constancy Verification**

### Analysis of Each Term Under Constant IAS Descent:

- $q = \frac{1}{2}\rho_0 \cdot IAS^2$ = constant (constant IAS)
- $S, C_{D0}, k, W, T_{idle}$ = constants
- **Numerator: $\frac{D - T_{idle}}{W}$** = constant
- **Denominator: $\left[1 + \frac{1.225 \times 10^{-4} \times IAS^2}{g}\right]$** = constant

---

## **Final Conclusion**

**In constant IAS descent, the descent gradient sin(γ) remains constant!**

This conclusion holds because:

1. Although TAS changes during descent
2. The rate of TAS change is proportional to the descent gradient
3. In the force balance equation, this proportional relationship results in a constant correction factor
4. The final result is that the descent gradient remains constant

This explains why constant IAS descent is such a reliable and commonly used flight technique in aviation.

Moreover, the magnitude of the descent gradient is mainly determined by IAS and aircraft weight, but it also depends on inherent aircraft characteristics such as CD0 (zero-lift drag coefficient), S (wing area), and k (induced drag factor).

---

## **Symbol Definitions**

- $\gamma$: Flight path angle (negative for descent)
- $W$: Aircraft weight
- $D$: Total drag
- $T_{idle}$: Idle thrust
- $TAS$: True airspeed
- $IAS$: Indicated airspeed
- $q$: Dynamic pressure
- $\rho$: Air density
- $\rho_0$: Sea level standard density
- $S$: Wing area
- $C_{D0}$: Zero-lift drag coefficient
- $k$: Induced drag factor
- $g$: Gravitational acceleration

---

