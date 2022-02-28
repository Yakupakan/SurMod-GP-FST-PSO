import numpy as np


def ackley(x):
    D = len(x)
    y = 20 + np.e - 20 * np.exp((-0.2 * np.sqrt(1 / D * np.sum([x[i] ** 2 for i in range(D)])))) \
        - np.exp(1 / D * np.sum([np.cos(2 * np.pi * x[i]) for i in range(D)]))
    return y


def ackley_2d(x, y):
    return 20 + np.e - 20 * np.exp((-0.2 * np.sqrt(1 / 2 * (x ** 2 + y ** 2)))) - np.exp(
        1 / 2 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))


def alpine(x):
    D = len(x)
    y = np.sum([(np.abs(x[i] * np.sin(x[i]) + 0.1 * x[i])) for i in range(D)])
    return y


def alpine_2d(x, y):
    return np.abs(x * np.sin(x) + 0.1 * x) + np.abs(y * np.sin(y) + 0.1 * y)


def griewank(x):
    D = len(x)
    y = 1 / 4000 * np.sum([x[i] ** 2 for i in range(D)]) - np.prod(
        [(np.cos(x[i] / np.sqrt(i + 1))) for i in range(D)]) + 1
    return y


def griewank_2d(x, y):
    return 1 / 4000 * (x ** 2 + y ** 2) - np.cos(x / np.sqrt(2)) * np.cos(y / np.sqrt(2)) + 1


def rastring(x):
    D = len(x)
    y = 10 * D + np.sum([(x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i])) for i in range(D)])
    return y


def xinshe(x):
    D = len(x)
    y = np.sum([(np.abs(x[i]) * (np.exp(np.sum([np.sin(x[k] ** 2) for k in range(D)]))) ** (-1)) for i in range(D)])
    return y


def vincent(x):
    D = len(x)
    y = np.sum([np.sin(10 * np.log(x[i])) for i in range(D)])
    return y
