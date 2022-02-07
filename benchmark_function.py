import numpy as np


def ackley(x):
    D = len(x)
    y = 20 + np.e - 20 * np.exp((-0.2 * np.sqrt(1 / D * np.sum([x[i] ** 2 for i in range(D)])))) \
        - np.exp(1 / D * np.sum([np.cos(2 * np.pi * x[i]) for i in range(D)]))
    return y


def alpine(x):
    D = len(x)
    y = np.sum([(np.abs(x[i] * np.sin(x[i]) + 0.1 * x[i])) for i in range(D)])
    return y
