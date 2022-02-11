import numpy as np

def N_dim_michalewicz(x):
    y = -1 * np.sum([np.sin(item) * np.sin((1 * item ** 2) / np.pi) ** 20 for item in x], axis=0)
    return y

N = 2 #dimension of vector x
interval = [0, np.pi]
x = []
for i in range(N):
    i = np.linspace(interval[0], interval[1], 50)
    x.append(i)

print(N_dim_michalewicz(x))
