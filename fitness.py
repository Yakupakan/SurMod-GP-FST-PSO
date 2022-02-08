import numpy as np
import math
from math import sqrt
from sklearn.metrics import mean_squared_error

import fstpso
from fstpso import FuzzyPSO

from print import *
from eval import eval, make_function
from hyperparam import *

if function == "alpine":
    from benchmark_function import alpine as benchmark_fun
    interval = [[-10, 10]]

if function == "ackley":
    from benchmark_function import ackley as benchmark_fun
    interval = [[-30, 30]]

if function == "griewank":
    from benchmark_function import griewank as benchmark_fun
    interval = [[-600, 600]]


dims = 1


def fit(prg):
    try:
        fst_pso_loss(prg)
    except Exception:
        # enablePrint()
        print("exception")
        return math.inf
    x_coord_best = fst_pso_loss(prg)
    y_benchmark_function = benchmark_fun(x_coord_best)
    return y_benchmark_function


def fit_combined_2(prg):
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best:
        return math.inf
    y_benchmark_function = benchmark_fun(x_coord_best)

    first_point = [interval[0][0]]
    second_point = [interval[0][-1]]
    approx_fun = make_function(prg)

    y_true = [benchmark_fun(first_point), benchmark_fun(second_point)]
    try:
        y_pred = [approx_fun(first_point), approx_fun(second_point)]
    except Exception:
        return math.inf

    rmse = mean_squared_error(y_true, y_pred)

    return y_benchmark_function + rmse


def fit_combined_4(prg):
    """
    Fitness combined: we want both that the minimum of the approx program coincide with the minimum of the function and
    that the function and the approx program have some points in common (here 4)
    :param prg: program that approximate the function
    :return: fitness
    """
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best:
        return math.inf
    y_benchmark_function = benchmark_fun(x_coord_best)

    points = [[point] for point in np.linspace(interval[0][0], interval[0][-1], 4)]

    approx_fun = make_function(prg)

    y_true = [benchmark_fun(point) for point in points]
    try:
        y_pred = [approx_fun(point) for point in points]
    except Exception:
        return math.inf

    try:
        rmse = mean_squared_error(y_true, y_pred)
    except Exception:
        return math.inf

    return y_benchmark_function + rmse


def strong_fitness_4(prg):
    try:
        x_coord_best = fst_pso_loss(prg)
    except Exception:
        return math.inf
    if not x_coord_best:
        return math.inf

    y_benchmark_function = benchmark_fun(x_coord_best)

    points = [[point] for point in np.linspace(interval[0][0], interval[0][-1], 4)]

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


def strong_fitness(prg, n=8):
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
