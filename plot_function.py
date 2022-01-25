import matplotlib.pyplot as plt

from benchmark_function import *


def plot_(x):
    y = [ackley([el]) for el in x]
    plt.plot(x, y)
    plt.show()