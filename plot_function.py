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


def plot_prg(prg, x, dire=None, it=-1):
    function_from_prg = make_function(prg)
    y_pred = [function_from_prg([el]) for el in x]

    if function == "ackley":
        y = [ackley([el]) for el in x]
        plt.xlim([-30, 30])

    if function == "alpine":
        y = [alpine([el]) for el in x]
        plt.xlim([-10, 10])

    if function == "griewank":
        y = [griewank([el]) for el in x]
        plt.xlim([-600, 600])

    plt.ylim([0, 24])
    plt.plot(x, y, color='r', lw=1, alpha=0.4)
    plt.plot(x, y_pred, color='g', lw=2)
    plt.legend(['benchmark function', 'smoothed prg'])
    plt.suptitle(function)
    plt.title("best prg at gen: " + str(it))
    if dire:
        if it > 0 or it == 0:
            plt.savefig(dire + "/best_prg_" + str(it) + ".png")
    plt.close()


# interval = [-600, 600]
# x = np.linspace(interval[0], interval[1], 1001)
# plot_griewank(x)
