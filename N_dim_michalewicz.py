import numpy as np

def N_dim_michalewicz(x):
    y = -1 * np.sum([np.sin(item) * np.sin((1 * item ** 2) / np.pi) ** 20 for item in x], axis=0)
    return y

N = 2 #dimension of vector x
x = []
for i in range(N):
    i = np.linspace(0, 3.2, 50)
    x.append(i)

print(N_dim_michalewicz(x))
