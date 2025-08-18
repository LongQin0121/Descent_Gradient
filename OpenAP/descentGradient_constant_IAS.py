import numpy as np
import matplotlib.pyplot as plt

class DescentGradientCalculator:
    """
    Calculate descent gradient sin(γ) for constant IAS descent
    Based on the complete derivation formula
    """
    
    def __init__(self):
        # Standard atmosphere constants
        self.rho_0 = 1.225  # Sea level density (kg/m³)
        self.g = 9.81       # Gravitational acceleration (m/s²)
        
    def calculate_sin_gamma(self, IAS, W, S, CD0, k, T_idle, altitude=0):
        """
        Calculate sin(γ) for constant IAS descent
        
        Parameters:
        - IAS: Indicated airspeed (m/s)
        - W: Aircraft weight (N)
        - S: Wing area (m²)
        - CD0: Zero-lift drag coefficient
        - k: Induced drag factor
        - T_idle: Idle thrust (N)
        - altitude: Current altitude (m) - for density calculation
        
        Returns:
        - sin_gamma: Descent gradient
        - gamma_deg: Flight path angle in degrees
        """
        
        # Calculate air density at altitude (standard atmosphere)
        rho = self.rho_0 * np.exp(-altitude / 8435)  # Simplified exponential model
        
        # Dynamic pressure (constant for constant IAS)
        q = 0.5 * self.rho_0 * IAS**2
        
        # Total drag calculation
        D_zero_lift = q * S * CD0  # Zero-lift drag
        D_induced = (k * W**2) / (q * S)  # Induced drag
        D_total = D_zero_lift + D_induced
        
        # Numerator: (D - T_idle) / W
        numerator = (D_total - T_idle) / W
        
        # Denominator: 1 - (1.225 × 10⁻⁴ × IAS²) / g
        denominator = 1 - (1.225e-4 * IAS**2) / self.g
        
        # Final sin(γ) calculation
        sin_gamma = numerator / denominator
        
        # Convert to degrees
        gamma_rad = np.arcsin(sin_gamma)
        gamma_deg = np.degrees(gamma_rad)
        
        return sin_gamma, gamma_deg
    
    def analyze_drag_components(self, IAS, W, S, CD0, k):
        """
        Analyze drag components for given parameters
        """
        q = 0.5 * self.rho_0 * IAS**2
        D_zero_lift = q * S * CD0
        D_induced = (k * W**2) / (q * S)
        D_total = D_zero_lift + D_induced
        
        print(f"Drag Analysis:")
        print(f"Dynamic pressure q: {q:.2f} N/m²")
        print(f"Zero-lift drag: {D_zero_lift:.2f} N")
        print(f"Induced drag: {D_induced:.2f} N")
        print(f"Total drag: {D_total:.2f} N")
        
        return D_total, D_zero_lift, D_induced
    
    def plot_descent_gradient_vs_ias(self, W, S, CD0, k, T_idle, ias_range=(50, 150)):
        """
        Plot descent gradient vs IAS
        """
        ias_values = np.linspace(ias_range[0], ias_range[1], 100)
        sin_gamma_values = []
        gamma_deg_values = []
        
        for ias in ias_values:
            sin_gamma, gamma_deg = self.calculate_sin_gamma(ias, W, S, CD0, k, T_idle)
            sin_gamma_values.append(sin_gamma)
            gamma_deg_values.append(gamma_deg)
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # Plot sin(γ) vs IAS
        ax1.plot(ias_values, sin_gamma_values, 'b-', linewidth=2)
        ax1.set_xlabel('IAS (m/s)')
        ax1.set_ylabel('sin(γ)')
        ax1.set_title('Descent Gradient sin(γ) vs IAS')
        ax1.grid(True, alpha=0.3)
        
        # Plot γ in degrees vs IAS
        ax2.plot(ias_values, gamma_deg_values, 'r-', linewidth=2)
        ax2.set_xlabel('IAS (m/s)')
        ax2.set_ylabel('γ (degrees)')
        ax2.set_title('Flight Path Angle γ vs IAS')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

# Example usage and demonstration
def main():
    calc = DescentGradientCalculator()
    
    # Example aircraft parameters (typical regional jet)
    IAS = 120  # m/s (约 233 knots)
    W = 450000  # N (约 45,000 kg aircraft)
    S = 75  # m² wing area
    CD0 = 0.025  # Zero-lift drag coefficient
    k = 0.045  # Induced drag factor
    T_idle = 5000  # N idle thrust
    
    print("=== Descent Gradient Calculator ===")
    print(f"Aircraft Parameters:")
    print(f"IAS: {IAS} m/s")
    print(f"Weight: {W/9810:.0f} kg")
    print(f"Wing area: {S} m²")
    print(f"CD0: {CD0}")
    print(f"k: {k}")
    print(f"Idle thrust: {T_idle} N")
    print()
    
    # Calculate drag components
    D_total, D_zero_lift, D_induced = calc.analyze_drag_components(IAS, W, S, CD0, k)
    print()
    
    # Calculate descent gradient
    sin_gamma, gamma_deg = calc.calculate_sin_gamma(IAS, W, S, CD0, k, T_idle)
    
    print("=== Results ===")
    print(f"sin(γ): {sin_gamma:.6f}")
    print(f"Flight path angle γ: {gamma_deg:.3f}°")
    print(f"Descent rate at {IAS} m/s TAS: {IAS * sin_gamma:.2f} m/s")
    print(f"Descent rate: {IAS * sin_gamma * 60:.0f} m/min")
    
    # Verify constancy at different altitudes
    print("\n=== Constancy Verification at Different Altitudes ===")
    altitudes = [0, 3000, 6000, 9000]  # meters
    for alt in altitudes:
        sin_gamma_alt, gamma_deg_alt = calc.calculate_sin_gamma(IAS, W, S, CD0, k, T_idle, alt)
        print(f"Altitude {alt:4d}m: sin(γ) = {sin_gamma_alt:.6f}, γ = {gamma_deg_alt:.3f}°")
    
    # Plot descent gradient vs IAS
    print("\nGenerating plots...")
    calc.plot_descent_gradient_vs_ias(W, S, CD0, k, T_idle)

def calculate_custom_parameters():
    """
    Function for users to input custom parameters
    """
    calc = DescentGradientCalculator()
    
    print("\n=== Custom Parameter Calculator ===")
    try:
        IAS = float(input("Enter IAS (m/s): "))
        W = float(input("Enter aircraft weight (N): "))
        S = float(input("Enter wing area (m²): "))
        CD0 = float(input("Enter zero-lift drag coefficient CD0: "))
        k = float(input("Enter induced drag factor k: "))
        T_idle = float(input("Enter idle thrust (N): "))
        
        sin_gamma, gamma_deg = calc.calculate_sin_gamma(IAS, W, S, CD0, k, T_idle)
        
        print(f"\nResults:")
        print(f"sin(γ): {sin_gamma:.6f}")
        print(f"Flight path angle γ: {gamma_deg:.3f}°")
        print(f"Descent rate: {IAS * sin_gamma * 60:.0f} m/min")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
    
    # Uncomment the line below to use custom parameters
    # calculate_custom_parameters()