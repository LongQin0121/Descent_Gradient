import numpy as np

# Constants
RHO_0 = 1.225  # Sea level density (kg/m³)
G = 9.81       # Gravitational acceleration (m/s²)
KNOTS_TO_MS = 0.514444  # knots to m/s
FT_PER_NM = 6076.12     # feet per nautical mile

def get_descent_gradient(IAS_knots, weight_kg, S_m2, CD0, k, T_idle_N):
    """
    Calculate descent gradient for constant IAS descent
    
    Parameters:
    - IAS_knots: Indicated airspeed in knots
    - weight_kg: Aircraft weight in kg
    - S_m2: Wing area in m²
    - CD0: Zero-lift drag coefficient (dimensionless)
    - k: Induced drag factor (dimensionless)
    - T_idle_N: Idle thrust in Newtons
    
    Returns:
    - sin_gamma: Descent gradient (dimensionless)
    - gamma_degrees: Flight path angle in degrees
    - gradient_ft_per_nm: Descent gradient in feet per nautical mile
    """
    
    # Convert units
    IAS_ms = IAS_knots * KNOTS_TO_MS  # knots to m/s
    W_N = weight_kg * G  # kg to Newtons
    
    # Dynamic pressure (constant for constant IAS)
    q = 0.5 * RHO_0 * IAS_ms**2
    
    # Total drag calculation
    D_zero_lift = q * S_m2 * CD0  # Zero-lift drag
    D_induced = (k * W_N**2) / (q * S_m2)  # Induced drag
    D_total = D_zero_lift + D_induced
    
    # Numerator: (D - T_idle) / W
    numerator = (D_total - T_idle_N) / W_N
    
    # Denominator: 1 +(1.225 × 10⁻⁴ × IAS²) / g
    # Note: IAS in m/s for this calculation
    denominator = 1 +(1.225e-4 * IAS_ms**2) / G
    
    # Final sin(γ) calculation
    sin_gamma = numerator / denominator
    
    # Convert to degrees
    gamma_rad = np.arcsin(np.clip(sin_gamma, -1, 1))  # Clip to valid range
    gamma_degrees = np.degrees(gamma_rad)
    
    # Calculate descent gradient in feet per nautical mile
    # sin(γ) = vertical distance / horizontal distance
    # For small angles: gradient ≈ sin(γ) × 6076.12 ft/nm
    gradient_ft_per_nm = sin_gamma * FT_PER_NM
    
    return sin_gamma, gamma_degrees, gradient_ft_per_nm

if __name__ == "__main__":
    # Direct function call - 您可以在这里随时修改输入参数
    print("=== Direct Function Call ===")
    sin_gamma, gamma_deg, gradient_ft_nm = get_descent_gradient(
        IAS_knots=250,     # knot
        weight_kg=58000,     # BADA MLW 64500
        S_m2=122.6,       # m
        CD0=0.023,     # dimensionless   openap  0.018   https://aircraftinvestigation.info/airplanes/A320-200.html     CD0=0.023    0.0235 ()
        k=0.0094,    # dimensionless     openap  0.039   https://aircraftinvestigation.info/airplanes/A320-200.html     k=0.0094     0.0089  A320-100
        T_idle_N=7000,        
    )
    print(f"sin(γ) = {sin_gamma:.6f}")
    print(f"γ = {gamma_deg:.3f}°")
    print(f"Descent gradient = {gradient_ft_nm:.0f} ft/nm")