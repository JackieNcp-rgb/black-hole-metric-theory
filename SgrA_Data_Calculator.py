import numpy as np

# 1. Physical Constants
G = 6.67430e-11  # Universal Gravitational Constant
c = 299792458    # Speed of light (m/s)

# 2. Sagittarius A* Mass Properties
M_sun = 1.98847e30
M_sgrA = 4.30e6 * M_sun  # ~8.55e36 kg

# 3. CALCULATE THE EVENT HORIZON RADIUS (Rs)
R_s = (2 * G * M_sgrA) / (c**2)

# 4. DEFINE THE TWO DISTINCT INTERNAL RADII TO EVALUATE
# We will test exactly at the Horizon, and 30% inside the Horizon
test_radii = {
    "At the Event Horizon (1.0 Rs)": R_s,
    "Deep Inside the Horizon (0.7 Rs)": R_s * 0.7
}

print("=== SAGITTARIUS A* INTERNAL METRIC CALCULATOR ===")
print(f"Calculated Horizon Radius (Rs): {R_s:,.2f} meters (~{R_s/1e9:.2f} million km)\n")

for label, r_val in test_radii.items():
    # Classical Escape Velocity Equation: v_e = sqrt(2GM / r)
    v_e = np.sqrt((2 * G * M_sgrA) / r_val)
    pct_c = (v_e / c) * 100
    
    print(f"--- {label} ---")
    print(f"-> Radius Coordinate (r): {r_val:,.2f} meters")
    print(f"-> Escape Velocity (v_e): {v_e:,.1f} m/s")
    print(f"-> Percentage of Light Speed: {pct_c:.2f}%\n")
