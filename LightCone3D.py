import numpy as np
import matplotlib.pyplot as plt

# 1. Generate the space grid (x, y floor)
r = np.linspace(0, 4, 100)
theta = np.linspace(0, 2 * np.pi, 100)
R, THETA = np.meshgrid(r, theta)

X = R * np.cos(THETA)
Y = R * np.sin(THETA)

# 2. Metric calculation: t = +/- sqrt(x^2 + y^2)
T_future = R
T_past = -R

# 3. Create the 3D plot with a dark theme
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Plot Future Light Cone (Top half) using an intense fiery map
ax.plot_surface(X, Y, T_future, cmap='hot', alpha=0.7, edgecolor='none', antialiased=True)

# Plot Past Light Cone (Bottom half) using a deep cool ice map
ax.plot_surface(X, Y, T_past, cmap='cool', alpha=0.5, edgecolor='none', antialiased=True)

# Make the grid lines and panes blend cleanly into the dark theme
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.set_edgecolor('white')
ax.grid(True, color='dimgray', linestyle='--', linewidth=0.5)

# Sophisticated labeling and text customization
ax.set_title('4D MINKOWSKI SPACETIME BOUNDARY\n(Flat Metric Interval: $ds^2 = 0$)', 
             fontsize=14, color='white', pad=20, fontweight='bold')
ax.set_xlabel('Spatial Position (x)', fontsize=11, color='white', labelpad=10)
ax.set_ylabel('Spatial Position (y)', fontsize=11, color='white', labelpad=10)
ax.set_zlabel('Time (t)', fontsize=11, color='white', labelpad=10)

# Change tick labels to clean white
ax.tick_params(colors='white')

# Set equal viewing limits
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-4, 4)

plt.show()
