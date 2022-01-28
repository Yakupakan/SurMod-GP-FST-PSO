import matplotlib.pyplot as plt

from eval import make_function
from benchmark_function import *


def plot_ackley(x):
    y = [ackley([el]) for el in x]
    plt.plot(x, y)
    plt.title("ackley")
    plt.show()
    plt.close()


def plot_prg(prg, x):
    function_from_prg = make_function(prg)
    y = [function_from_prg([el]) for el in x]
    plt.plot(x, y)
    plt.title("best prg")
    plt.show()
    plt.close()
