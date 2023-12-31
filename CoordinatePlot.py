import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['text.usetex'] = True
ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
t = np.linspace (-10, 10, 10000) 
v = 1
b = 4
theta = np.pi / 9   
phi = np.pi / 3       
z = v * t * np.cos(theta)
x = b * np.cos(phi) + v * t * np.sin(theta) * np.sin(phi)
y = b * np.sin(phi) - v * t * np.sin(theta) * np.cos(phi)

# Plot axes
ax.plot(np.linspace(0, 8, 100), np.zeros(100), np.zeros(100), color="grey", linestyle = '--', alpha = 0.4)
ax.plot(np.zeros(100), np.linspace(0, 6, 100), np.zeros(100), color="grey", linestyle = '--', alpha=0.4)
ax.plot(np.zeros(t.shape), np.zeros(t.shape), t, color = "silver")
ax.plot(b * np.cos(phi) * np.ones(100), b * np.sin(phi) * np.ones(100), np.linspace(-10, 10,100), linestyle='-.', color="gray", alpha=0.5)
# Plot b
ax.plot(np.linspace(0, b * np.cos(phi), 100), np.linspace(0, b * np.sin(phi), 100), np.zeros(100))
# Plot phi and theta
angle = np.linspace(0, 1, 100)
ax.plot(b/3 * np.cos(angle * phi), b/3 * np.sin(angle * phi), 0)
ax.plot(b * np.cos(phi) + 4 * np.sin(angle * theta) * np.sin(phi), b * np.sin(phi) - 4 * np.sin(angle * theta) * np.cos(phi), 4 * np.cos(angle * theta))
# Plot particle track
ax.plot(x, y, z, label='Particle Track')

# Labels
ax.text(8, 0, -1.5, "x axes")
ax.text(0, 6, -1.5, "y axes")
ax.text(0, .1, 10, "wire (z axes)")
ax.text(x[0], y[0] + .2, z[0] - .2, 'Particle Track')
ax.text(b * np.cos(phi) / 2, b * np.sin(phi) / 2, -2, "b")
ax.text(b/2.5 * np.cos(1/4 * phi), b/2.5 * np.sin(1/4 * phi), -1.5, r'$\phi$')
ax.text(b * np.cos(phi) + 4.5 * np.sin(1/2 * theta) * np.sin(phi), b * np.sin(phi) - 4.5 * np.sin(1/2 * theta) * np.cos(phi), 4.5 * np.cos(1/2 * theta), r'$\theta$')

ax.axis("off")

plt.show()