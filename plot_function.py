import matplotlib.pyplot as plt

from hyperparam import *
from eval import make_function
from benchmark_function import *


def plot_ackley(x):
    y = [ackley([el]) for el in x]
    plt.plot(x, y)
    plt.title("ackley")
    plt.show()
    plt.close()


def plot_alpine(interv):
    y = [alpine([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("alpine")
    plt.show()
    plt.close()


def plot_griewank(interv):
    y = [griewank([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("griewank")
    plt.show()
    plt.close()


def plot_rastring(interv):
    y = [rastring([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("griewank")
    plt.show()
    plt.close()


def plot_prg(prg, x, dire=None, it=-1):
    function_from_prg = make_function(prg)
    y_pred = [function_from_prg([el]) for el in x]

    if function == "ackley":
        y = [ackley([el]) for el in x]
        plt.xlim([-30, 30])
        plt.ylim([-2, 24])

    if function == "alpine":
        y = [alpine([el]) for el in x]
        plt.xlim([-10, 10])
        plt.ylim([-2, 10])

    if function == "griewank":
        y = [griewank([el]) for el in x]
        plt.xlim([-600, 600])
        plt.ylim([-2, 10])

    if function == "rastring":
        y = [rastring([el]) for el in x]
        plt.xlim([-5.12, 5.12])
        plt.ylim([-2, 40])

    plt.plot(x, y, color='k', lw=0.8, alpha=0.5)
    plt.plot(x, y_pred, color='g', lw=2.5)
    plt.legend(['benchmark function', 'smoothed prg'])
    plt.suptitle(function)
    plt.title("best prg at gen: " + str(it))
    if dire:
        if it > 0 or it == 0:
            plt.savefig(dire + "/best_prg_" + str(it) + ".png")
    plt.close()


# interval = [-5.12, 5.12]
# x = np.linspace(interval[0], interval[1], 10001)
# plot_rastring(x)
