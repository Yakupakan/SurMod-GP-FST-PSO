import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from hyperparam import *
from eval import make_function, opcodes
from benchmark_function import *


def plot_ackley(x):
    y = [ackley([el]) for el in x]
    plt.plot(x, y)
    plt.title("ackley")
    plt.show()
    plt.close()


def plot_ackley_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-30, 30, 100)
    y = np.linspace(-30, 30, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[ackley_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_alpine(interv):
    y = [alpine([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("alpine")
    plt.show()
    plt.close()


def plot_alpine_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[alpine_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_deceptive_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(0, 1, 100)
    y = np.linspace(0, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[deceptive_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_griewank(interv):
    y = [griewank([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("griewank")
    plt.show()
    plt.close()


def plot_griewank_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-600, 600, 100)
    y = np.linspace(-600, 600, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[griewank_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_michalewicz_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(0, np.pi, 100)
    y = np.linspace(0, np.pi, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[michalewicz_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_rastring(interv):
    y = [rastring([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("rastring")
    plt.show()
    plt.close()


def plot_rastring_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-5.12, 5.12, 100)
    y = np.linspace(-5.12, 5.12, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[rastring_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_rosenbrock_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[rosenbrock_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_schwefel_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-500, 500, 100)
    y = np.linspace(-500, 500, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[schwefel_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_shubert_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-5.12, 5.12, 100)
    y = np.linspace(-5.12, 5.12, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[shubert_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_sum_power_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[sum_power_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_xinshe(interv):
    y = [xinshe([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("xinshe")
    plt.show()
    plt.close()


def plot_xinshe_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[xinshe_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


def plot_vincent(interv):
    y = [vincent([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("vincent")
    plt.show()
    plt.close()


def plot_vincent_3d():
    ax = plt.axes(projection='3d')

    x = np.linspace(0.25, 10, 100)
    y = np.linspace(0.25, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[vincent_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    plt.show()


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
    if function == "xinshe":
        y = [xinshe([el]) for el in x]
        plt.xlim([-2 * np.pi, 2 * np.pi])
        plt.ylim([-2, 18])
    if function == "vincent":
        y = [vincent([el]) for el in x]
        plt.xlim([0, 10])
        plt.ylim([-1.25, 1.25])

    plt.plot(x, y, color='k', lw=0.8, alpha=0.5)
    plt.plot(x, y_pred, color='g', lw=2.5)
    plt.legend(['benchmark function', 'smoothed prg'])
    plt.suptitle(function)
    plt.title("best prg at gen: " + str(it))
    if dire:
        if it > 0 or it == 0:
            plt.savefig(dire + "/best_prg_" + str(it) + ".png")
    plt.close()


def plot_prg_2d(prg, dire=None, it=-1):
    function_from_prg = make_function(prg)
    ax = plt.axes(projection='3d')

    x = np.linspace(interval[0][0], interval[0][1], 100)
    y = np.linspace(interval[0][0], interval[0][1], 100)

    X, Y = np.meshgrid(x, y)

    Z = np.array([[function_from_prg([x_, y_]) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='magma', edgecolor='none')
    plt.suptitle(function)
    plt.title("best prg at gen: " + str(it))
    if it == -1:
       plt.show()
    if dire:
        if it > 0 or it == 0:
            plt.savefig(dire + "/best_prg_" + str(it) + ".png")
    plt.close()


def plot_interpolation_points(points, dire=None):
    x_points = [point[0] for point in points]
    y_points = [point[1] for point in points]
    plt.scatter(x_points, y_points, marker='o')
    if dire:
        plt.savefig(dire + "/interpolation_point.png")
    else:
        plt.show()
    plt.close()


'''
from fitness import fst_pso_loss
import scipy
from eval import *

prg = [-1, opcodes.PLUS, -1, opcodes.TIMES, opcodes.DUP, opcodes.TIMES, opcodes.MINUS, opcodes.DUP, 0, -10, opcodes.DIVIDE, 10, opcodes.PLUS, opcodes.DUP, opcodes.PLUS]

plot_prg_2d(prg)
fun = make_function(prg)
print(fun([0, 0]))
print(fun([10, 10]))
print(fst_pso_loss(prg))
# print(scipy.optimize.fminbound(fun, np.array(-30, 30), np.array(-30, 30)))
# interval = [[0.25, 10], [0.25, 10]]
# x = np.linspace(interval[0], interval[1], 10000)
# plot_ackley(x)
'''