import numpy as np
import math
from math import sqrt
from sklearn.metrics import mean_squared_error

import fstpso
from fstpso import FuzzyPSO

from hyperparam import *
from print import *
from eval import make_function
from select_function import benchmark_fun


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


def fitness_2d(prg):
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

    return y_benchmark_function  # + rmse


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


def strong_fitness_3d(prg, n=number_interpolation_point):
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
    for coord_best in x_coord_best:
        if not interval[0][0] < coord_best < interval[0][1]:
            return math.inf

    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1], x_coord_best[2])
    except Exception:
        return math.inf

    return y_benchmark_function  # + rmse


def strong_fitness_4d(prg, n=number_interpolation_point):
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
    for coord_best in x_coord_best:
        if not interval[0][0] < coord_best < interval[0][1]:
            return math.inf

    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1], x_coord_best[2], x_coord_best[3])
    except Exception:
        return math.inf

    return y_benchmark_function  # + rmse


def strong_fitness_5d(prg, n=number_interpolation_point):
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
    for coord_best in x_coord_best:
        if not interval[0][0] < coord_best < interval[0][1]:
            return math.inf

    try:
        y_benchmark_function = benchmark_fun(x_coord_best[0], x_coord_best[1], x_coord_best[2], x_coord_best[3], x_coord_best[4])
    except Exception:
        return math.inf

    return y_benchmark_function  # + rmse


def fst_pso_loss(prg):
    """
    :param prg: individual of the population (program)
    :param dim: dimension of the space (also called D)
    :param interval: interval of the problem (insert a list like: [[-10, 10]])
    :return: coordinates relative to the minimum of prg
    """
    blockPrint()
    FP = FuzzyPSO()
    FP.set_search_space(interval * dim)
    FP.set_fitness(make_function(prg))
    result = FP.solve_with_fstpso()
    enablePrint()
    return result[0].X  # the .X transfrom the Particle structure into a list
