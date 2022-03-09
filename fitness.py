import numpy as np
import math
from math import sqrt
from sklearn.metrics import mean_squared_error

import fstpso
from fstpso import FuzzyPSO

from print import *
from eval import make_function
from hyperparam import *

if function == "ackley":
    from benchmark_function import ackley as benchmark_fun

    interval = [[-30, 30]]
    dims = 1

if function == "ackley_2d":
    from benchmark_function import ackley_2d as benchmark_fun

    interval = [[-30, 30]]
    dims = 2

if function == "alpine":
    from benchmark_function import alpine as benchmark_fun

    interval = [[-10, 10]]
    dims = 1

if function == "alpine_2d":
    from benchmark_function import alpine_2d as benchmark_fun

    interval = [[-10, 10]]
    dims = 2

if function == "griewank":
    from benchmark_function import griewank as benchmark_fun

    interval = [[-600, 600]]
    dims = 1

if function == "griewank_2d":
    from benchmark_function import griewank_2d as benchmark_fun

    interval = [[-600, 600]]
    dims = 2

if function == "michalewicz_2d":
    from benchmark_function import michalewicz_2d as benchmark_fun

    interval = [[0, np.pi]]
    dims = 2

if function == "rastring":
    from benchmark_function import rastring as benchmark_fun

    interval = [[-5.12, 5.12]]
    dims = 1

if function == "rastring_2d":
    from benchmark_function import rastring_2d as benchmark_fun

    interval = [[-5.12, 5.12]]
    dims = 2

if function == "rosenbrock_2d":
    from benchmark_function import rosenbrock_2d as benchmark_fun

    interval = [[-2, 2]]
    dims = 2

if function == "schwefel":
    from benchmark_function import schwefel as benchmark_fun

    interval = [[-500, 500]]
    dims = 1

if function == "schwefel_2d":
    from benchmark_function import schwefel_2d as benchmark_fun

    interval = [[-500, 500]]
    dims = 2

if function == "shubert":
    from benchmark_function import shubert as benchmark_fun

    interval = [[-10, 10]]
    dims = 1

if function == "shubert_2d":
    from benchmark_function import shubert_2d as benchmark_fun

    interval = [[-10, 10]]
    dims = 2

if function == "vincent":
    from benchmark_function import vincent as benchmark_fun

    interval = [[0.25, 10]]
    dims = 1

if function == "vincent_2d":
    from benchmark_function import vincent_2d as benchmark_fun

    interval = [[0.25, 10]]
    dims = 2

if function == "xinshe":
    from benchmark_function import xinshe as benchmark_fun

    interval = [[-2 * np.pi, 2 * np.pi]]
    dims = 1

if function == "xinshe_2d":
    from benchmark_function import xinshe_2d as benchmark_fun

    interval = [[-2 * np.pi, 2 * np.pi]]
    dims = 2


def strong_fitness(prg, n=number_interpolation_point):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here n)
    :param prg: program that approximate the function
    :param n: number of point for the rmse computation
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best:
        return math.inf
    if not (interval[0][0] < x_coord_best[0] < interval[0][1] and interval[0][0] < x_coord_best[1] < interval[0][1]):
        return math.inf
    y_benchmark_function = benchmark_fun(x_coord_best)

    points = [[point] for point in np.linspace(interval[0][0], interval[0][-1], n)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(point) for point in points]
    y_true.append(y_benchmark_function)

    try:
        y_pred = [approx_fun(point) for point in points]
    except Exception:
        return math.inf
    try:
        y_pred.append(approx_fun(x_coord_best))
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf

    return y_benchmark_function + rmse


def strong_fitness_2d(prg, n=number_interpolation_point):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here n)
    :param prg: program that approximate the function
    :param n: number of point for the rmse computation
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best or len(x_coord_best) < 2:
        return math.inf
    if not (interval[0][0] < x_coord_best[0] < interval[0][1] and interval[0][0] < x_coord_best[1] < interval[0][1]):
        return math.inf
    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1])
    except Exception:
        return math.inf

    x1_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]
    x2_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(x1, x2) for x1 in x1_points for x2 in x2_points]
    y_true.append(y_benchmark_function)

    try:
        y_pred = [approx_fun([x1, x2]) for x1 in x1_points for x2 in x2_points]
    except Exception:
        return math.inf
    try:
        y_pred.append(approx_fun(x_coord_best))
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf

    return y_benchmark_function + rmse


def strong_fitness_2d_weighted(prg, n=number_interpolation_point):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here n)
    :param prg: program that approximate the function
    :param n: number of point for the rmse computation
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best or len(x_coord_best) < 2:
        return math.inf
    if not (interval[0][0] < x_coord_best[0] < interval[0][1] and interval[0][0] < x_coord_best[1] < interval[0][1]):
        return math.inf
    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1])
    except Exception:
        return math.inf

    x1_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]
    x2_points = [point for point in np.linspace(interval[0][0], interval[0][-1], n)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(x1, x2) for x1 in x1_points for x2 in x2_points]
    y_true.append(y_benchmark_function)

    try:
        y_pred = [approx_fun([x1, x2]) for x1 in x1_points for x2 in x2_points]
    except Exception:
        return math.inf
    try:
        y_pred.append(approx_fun(x_coord_best))
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf

    return 0.5 * y_benchmark_function + 0.5 * rmse


def fst_pso_loss(prg):
    """
    :param prg: individual of the population (program)
    :param dims: dimension of the space (also called D)
    :param interval: interval of the problem (insert a list like: [[-10, 10]])
    :return: coordinates relative to the minimum of prg
    """
    blockPrint()
    FP = FuzzyPSO()
    FP.set_search_space(interval * dims)
    FP.set_fitness(make_function(prg))
    result = FP.solve_with_fstpso()
    enablePrint()
    return result[0].X  # the .X transfrom the Particle structure into a list
