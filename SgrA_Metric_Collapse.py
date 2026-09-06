import numpy as np
import matplotlib.pyplot as plt

# 1. Physics Setup for Sagittarius A* (Supermassive Black Hole)
G = 6.67430e-11       # Gravitational Constant (m^3 kg^-1 s^-2)
c = 299792458         # Speed of light (m/s)
M_sun = 1.98847e30    # 1 Solar Mass (kg)
M = 4.30e6 * M_sun    # Sagittarius A* Mass (~8.55e36 kg)

# Calculate the precise Event Horizon (Schwarzschild Radius)
R_s = (2 * G * M) / (c**2)  # In meters (~12.74 million km)

# 2. Set up the plotting environment
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(11, 7), facecolor='black')

# Target observational distances matching your research table checkpoints
probe_distances = [2.5, 2.0, 1.5, 1.1, 1.0, 0.7]

print("--- SAGITTARIUS A* LIGHT CONE COLLAPSE MONITOR ---")
print(f"Computed R_s: {R_s/1e9:.3f} million kilometers\n")

# 3. Simulate and plot local light cones at each position
for r in probe_distances:
    escape_ratio = np.sqrt(1.0 / r)
    t_local = np.linspace(-0.4, 0.4, 100)
    
    if r > 1.0:
        tilt_factor = 0.25 * (1.0 / (r - 0.9))
        x_left = r - np.abs(t_local) * 0.4
        x_right = r + np.abs(t_local) * 0.4 - (t_local * tilt_factor)
        
        ax.plot(x_left[t_local>=0], t_local[t_local>=0], color='cyan', alpha=0.6, linewidth=1.5)
        ax.plot(x_right[t_local>=0], t_local[t_local>=0], color='cyan', alpha=0.6, linewidth=1.5)
        ax.fill_betweenx(t_local[t_local>=0], x_left[t_local>=0], x_right[t_local>=0], color='cyan', alpha=0.15)
        status_text = f"$v_e$ = {escape_ratio*100:.1f}% of $c$"
        
    elif np.isclose(r, 1.0):
        x_left = r - np.abs(t_local) * 0.5 - (t_local * 0.5)
        x_right = np.full_like(t_local, r)
        
        ax.plot(x_left[t_local>=0], t_local[t_local>=0], color='yellow', alpha=0.9, linewidth=2)
        ax.plot(x_right[t_local>=0], t_local[t_local>=0], color='yellow', alpha=0.9, linewidth=2)
        ax.fill_betweenx(t_local[t_local>=0], x_left[t_local>=0], x_right[t_local>=0], color='yellow', alpha=0.25)
        status_text = "$v_e$ = 100% of $c$\n(Horizon Locked)"
        
    else:
        x_left = r - np.abs(t_local) * 0.3 - (t_local * 0.6)
        x_right = r + np.abs(t_local) * 0.3 - (t_local * 0.8)
        
        ax.plot(x_left[t_local>=0], t_local[t_local>=0], color='red', alpha=0.9, linewidth=2, linestyle='--')
        ax.plot(x_right[t_local>=0], t_local[t_local>=0], color='red', alpha=0.9, linewidth=2, linestyle='--')
        ax.fill_betweenx(t_local[t_local>=0], x_left[t_local>=0], x_right[t_local>=0], color='red', alpha=0.3)
        status_text = f"$v_e$ = {escape_ratio*100:.1f}% of $c$\n(Causal Inversion)"

    # Stagger vertical positions and directions to clear up text clutter completely
    if np.isclose(r, 1.0):
        y_offset = 0.54
        ha_val = 'center'
    elif np.isclose(r, 0.7):
        y_offset = 0.34
        ha_val = 'right'
    elif np.isclose(r, 1.1):
        y_offset = 0.44  
        ha_val = 'right'  # Changed to right-aligned to pull text away from 1.5
    elif np.isclose(r, 1.5):
        y_offset = 0.49  # Raised slightly to clear horizontal lines
        ha_val = 'left'
    else:
        y_offset = 0.45
        ha_val = 'center'

    ax.text(r, y_offset, status_text, color='white', fontsize=8, ha=ha_val, va='bottom')


# 4. Global Simulation Formatting
ax.axvline(1.0, color='#FF3366', linestyle='-', linewidth=2.5, label='Event Horizon ($R_s$)')
ax.axvline(0.0, color='purple', linestyle=':', linewidth=3, label='Singularity ($r=0$)')
ax.fill_between([0, 1.0], -0.6, 0.6, color='red', alpha=0.05)

ax.set_title('SAGITTARIUS A*: METRIC DEFORMATION & CAUSAL CONE COLLAPSE', 
             color='white', fontsize=12, pad=25, fontweight='bold')
ax.set_xlabel('Proximity to Singularity (Normalized Units $r / R_s$)', color='white', labelpad=10)
ax.set_ylabel('Localized Temporal Flow ($t$)', color='white', labelpad=10)
ax.set_xlim(-0.2, 3.0)
ax.set_ylim(-0.5, 0.7)
ax.legend(loc='upper right', framealpha=0.3)
ax.grid(True, color='dimgray', linestyle=':', alpha=0.4)

plt.show()
