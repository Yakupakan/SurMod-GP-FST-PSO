import matplotlib.pyplot as plt

from eval import make_function
from benchmark_function import *


def plot_ackley(x):
    y = [ackley([el]) for el in x]
    plt.plot(x, y)
    plt.title("ackley")
    plt.show()
    plt.close()


def plot_prg(prg, x, dire=None, it=-1):
    function_from_prg = make_function(prg)
    y = [function_from_prg([el]) for el in x]
    plt.xlim([-30, 30])
    plt.ylim([0, 20])
    plt.plot(x, y)
    plt.title("best prg")
    if dire:
        if it > 0:
            plt.savefig(dire + "/best_prg_" + str(it) + ".png")
    plt.close()
