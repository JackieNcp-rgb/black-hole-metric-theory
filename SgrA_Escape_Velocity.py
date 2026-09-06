import numpy as np

# Fundamental Constants
G = 6.67430e-11  # m^3 kg^-1 s^-2
c = 299792458    # m/s
M_sun = 1.98847e30

# Sagittarius A* parameters
M_sgrA = 4.30e6 * M_sun
R_s = (2 * G * M_sgrA) / (c**2)

# Specific proximity factors requested in Table II
proximities = [5.0, 2.0, 1.0, 0.7]

print(f"Calculated Horizon Radius (Rs) for Sgr A*: {R_s:,.2f} meters\n")
print(f"{'Proximity':<12}{'Distance (km)':<20}{'ve (m/s)':<20}{'% of Light Speed'}")
print("-" * 65)

for r_factor in proximities:
    r_meters = R_s * r_factor
    r_km = r_meters / 1000
    
    # Escape velocity calculation: ve = sqrt(2GM/r)
    v_e = np.sqrt((2 * G * M_sgrA) / r_meters)
    pct_c = (v_e / c) * 100
    
    print(f"{r_factor:<12.1f}{r_km:<20,.2f}{v_e:<20,.2f}{pct_c:.4f}%")
