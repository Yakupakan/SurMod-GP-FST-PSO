import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

from hyperparam import enum_set, interval_dict
from eval import opcodes, make_function
from plot_function import plot_3d

matplotlib.rc('font', **{'size': 8, 'weight': 'bold'})

bf_dict = {"alpine": [opcodes.TIMES, opcodes.DUP, opcodes.TIMES, 1, opcodes.SWAP, -9, opcodes.MINUS, opcodes.PLUS,
                      -10, opcodes.DIVIDE, -5, opcodes.TIMES, 7, opcodes.PLUS],
           "ackley": [opcodes.TIMES, opcodes.DUP, opcodes.TIMES, opcodes.DUP, 4, 0, 1, opcodes.PLUS, opcodes.PLUS,
                      10, opcodes.DIVIDE, opcodes.PLUS, 9, opcodes.DIVIDE, opcodes.DUP, 10, 10, opcodes.PLUS,
                      opcodes.MINUS],
           "deceptive": None,
           "griewank": [opcodes.TIMES, 132, -332, opcodes.TIMES, 42, opcodes.MINUS, -234, 328, opcodes.DIVIDE,
                        opcodes.DIVIDE, opcodes.TIMES, opcodes.DUP, opcodes.TIMES, 62, opcodes.PLUS],
           "michalewicz": None,
           "rastring": [2, -5, opcodes.DIVIDE, 8, opcodes.DUP, opcodes.PLUS, opcodes.DIVIDE, opcodes.TIMES,
                        opcodes.TIMES, -2, 4, 10, opcodes.DIVIDE, -9, opcodes.TIMES, -3, opcodes.MINUS,
                        opcodes.SWAP, -10, opcodes.DIVIDE, opcodes.SWAP, opcodes.PLUS, opcodes.SWAP,
                        opcodes.DIVIDE, opcodes.DUP, opcodes.TIMES, -3, -10, opcodes.TIMES, opcodes.PLUS],
           "rosenbrock": [30, opcodes.TIMES, opcodes.SWAP, opcodes.DUP, 164, opcodes.DUP, 26, opcodes.PLUS, -996,
                          opcodes.MINUS, -87, opcodes.MINUS, opcodes.DIVIDE, 30, opcodes.PLUS, opcodes.TIMES,
                          opcodes.TIMES, opcodes.MINUS],
           "schwefel": None,
           "shubert": None,
           "sum_power": None,
           "vincent": [opcodes.TIMES, opcodes.DUP, opcodes.DUP, opcodes.TIMES, 7, opcodes.TIMES, 8, opcodes.SWAP,
                       opcodes.DIVIDE, 8, opcodes.PLUS, 8, opcodes.SWAP, -8, opcodes.DUP, opcodes.PLUS, opcodes.DUP,
                       opcodes.DIVIDE, opcodes.MINUS, opcodes.TIMES, -6, opcodes.DUP, opcodes.TIMES, opcodes.DIVIDE],
           "xinshe": [-7, opcodes.DIVIDE, 10, opcodes.TIMES, opcodes.DIVIDE, 8, opcodes.DIVIDE, opcodes.DUP,
                      opcodes.TIMES, 6, opcodes.PLUS]}


def plot_prg_2d(fun_name):
    prg = bf_dict[fun_name]
    if prg is None:
        return
    function_from_prg = make_function(prg)
    ax = plt.axes(projection='3d')

    x = np.linspace(interval_dict[fun_name][0][0], interval_dict[fun_name][0][1], 100)
    y = np.linspace(interval_dict[fun_name][0][0], interval_dict[fun_name][0][1], 100)

    X, Y = np.meshgrid(x, y)

    Z = np.array([[function_from_prg([x_, y_]) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='magma', edgecolor='none')

    # plt.show()
    plt.savefig("plot/plot_2d/" + fun_name + "_approx.png")
    plt.close()


plot_3d("schwefel")

# for name_function in bf_dict.keys():
#    plot_3d(name_function)
#   plot_prg_2d(name_function)
