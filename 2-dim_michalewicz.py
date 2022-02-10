from matplotlib import cm  # color map
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 3.2, 50)
x2 = np.linspace(0, 3.2, 50)
x1, x2 = np.meshgrid(x1, x2)

# Michalewicz function
y = -1 * ((np.sin(x1) * np.sin((1 * x1 ** 2) / np.pi) ** 20) + \
          (np.sin(x2) * np.sin((2 * x2 ** 2) / np.pi) ** 20))

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x1, x2, y, \
                       rstride=1, cstride=1, cmap=cm.jet, \
                       edgecolor='darkred', linewidth=0.1)

ax.set_xlabel('x1', fontsize=10)
ax.set_ylabel('x2', fontsize=10)
ax.set_zlabel('f(x1,x2)', fontsize=10)
ax.tick_params(axis='both', which='major',
               labelsize=6)

plt.show()
