import numpy as np
import matplotlib.pyplot as plt

# 1. Set up the spacetime grid
t = np.linspace(-5, 5, 400)
x = np.linspace(-5, 5, 400)
T, X = np.meshgrid(t, x)

# 2. Define our flat metric components (Time is negative, Space is positive)
# ds^2 = -t^2 + x^2
spacetime_interval = -(T**2) + X**2

# 3. Create the plot
plt.figure(figsize=(8, 8))

# Plot the Light Cone bounds where the interval equals exactly 0 (ds^2 = 0)
plt.plot(x, x, color='red', linestyle='--', linewidth=2, label='Path of Light (Interval = 0)')
plt.plot(x, -x, color='red', linestyle='--', linewidth=2)

# Shading regions dictated by the metric scale
plt.fill_between(x, np.abs(x), 5, color='blue', alpha=0.1, label='Future / Past (Time-like)')
plt.fill_between(x, -np.abs(x), -5, color='blue', alpha=0.1)
plt.fill_between(x, -np.abs(x), np.abs(x), color='gray', alpha=0.1, label='Elsewhere (Space-like)')

# Grid lines and formatting
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(color='gainsboro', linestyle=':', linewidth=1)

plt.title('Visualizing the Flat Spacetime Metric Scale', fontsize=14, pad=15)
plt.xlabel('Space Position (x)', fontsize=12)
plt.ylabel('Time Position (t)', fontsize=12)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(loc='upper right')

plt.show()
