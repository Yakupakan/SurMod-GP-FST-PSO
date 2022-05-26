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


def plot_3d(name_function):
    ax = plt.axes(projection='3d')

    x = np.linspace(interval_dict[name_function][0][0], interval_dict[name_function][0][1], 100)
    y = np.linspace(interval_dict[name_function][0][0], interval_dict[name_function][0][1], 100)
    X, Y = np.meshgrid(x, y)
    if name_function == "ackley":
        Z = np.array([[ackley_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "alpine":
        Z = np.array([[alpine_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "deceptive":
        Z = np.array([[deceptive_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "griewank":
        Z = np.array([[griewank_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "michalewicz":
        Z = np.array([[michalewicz_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "rastring":
        Z = np.array([[rastring_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "rosenbrock":
        Z = np.array([[rosenbrock_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "schwefel":
        Z = np.array([[schwefel_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "shubert":
        Z = np.array([[shubert_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "sum_power":
        Z = np.array([[sum_power_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "xinshe":
        Z = np.array([[xinshe_2d(x_, y_) for x_ in x] for y_ in y])
    if name_function == "vincent":
        Z = np.array([[vincent_2d(x_, y_) for x_ in x] for y_ in y])

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='magma', edgecolor='none')
    # plt.show()
    plt.savefig("plot/plot_2d/" + name_function + ".png")


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
    plt.title("rastring")
    plt.show()
    plt.close()


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
    plt.savefig("plot/plot_2d/xinshe.png")


def plot_vincent(interv):
    y = [vincent([el]) for el in interv]
    plt.plot(interv, y)
    plt.title("vincent")
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