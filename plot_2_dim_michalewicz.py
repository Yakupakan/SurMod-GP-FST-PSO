import matplotlib.pyplot as plt
import numpy as np

def N_dim_michalewicz(x):
    y = -1 * np.sum([np.sin(item) * np.sin((1 * item ** 2) / np.pi) ** 20 for item in x], axis=0)
    return y

def plot_2_dim_michalewicz(x):
    x1, x2 = np.meshgrid(x[0], x[1])
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x1, x2, N_dim_michalewicz([x1, x2]))
    plt.show()

N=2
x = []
for i in range(N):
    i = np.linspace(0, 3.2, 50)
    x.append(i)

plot_2_dim_michalewicz(x)
