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


def michalewicz(x):
    return - np.sin(x) * np.sin(x ** 2 / np.pi) ** 20


def michalewicz_2d(x, y):
    return - (np.sin(x) * np.sin(x ** 2 / np.pi) ** 20) - (np.sin(y) * np.sin(2 * y ** 2 / np.pi) ** 20)


def rastring(x):
    D = len(x)
    y = 10 * D + np.sum([(x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i])) for i in range(D)])
    return y


def michalewicz(x):
    D = len(x)
    y = -1 * np.sum([np.sin(x[i]) * np.sin((1 * x[i] ** 2) / np.pi) ** 20 for i in range(D)])
    return y


def michalewicz_Nd(x):
    y = -1 * np.sum([np.sin(item) * np.sin((1 * item ** 2) / np.pi) ** 20 for item in x], axis=0)
    return y


def rastring_2d(x, y):
    return 20 + (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y))


def rosenbrock_2d(x, y):
    return 100 * (x ** 2 - y) ** 2 + (x - 1) ** 2


def schwefel_2d(x, y):
    return 2 * 418.9829 - x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y)))


def xinshe(x):
    D = len(x)
    y = np.sum([(np.abs(x[i]) * (np.exp(np.sum([np.sin(x[k] ** 2) for k in range(D)]))) ** (-1)) for i in range(D)])
    return y


def xinshe_2d(x, y):
    return np.abs(x) * np.abs(np.exp(np.sin(x ** 2) + np.sin(y ** 2))) ** (-1) + np.abs(y) * np.abs(
        np.exp(np.sin(x ** 2) + np.sin(y ** 2))) ** (-1)


def schwefel(x):
    D = len(x)
    y = (418.9829 * D) - np.sum([x[i] * np.sin(np.sqrt(np.abs(x[i]))) for i in range(D)])
    return y


def schwefel_2d(x, y):
    return (418.9829 * 2) - (x * np.sin(np.sqrt(np.abs(x)))) - (y * np.sin(np.sqrt(np.abs(y))))


def shubert(x):
    D = len(x)
    y = np.prod([np.sum([i * np.cos(((i + 1) * x[d]) + i for i in range(5))]) for d in range(D)])
    return y


def shubert_2d(x, y):
    return np.sum([i * np.cos(((i + 1) * x) + i for i in range(5))]) * np.sum(
        [i * np.cos(((i + 1) * y) + i for i in range(5))])


def vincent(x):
    D = len(x)
    y = np.sum([np.sin(10 * np.log(x[i])) for i in range(D)])
    return y


def vincent_2d(x, y):
    return np.sin(10 * np.log(x)) + np.sin(10 * np.log(y))
