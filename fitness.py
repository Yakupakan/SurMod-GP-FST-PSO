import numpy as np
import math

import fstpso
from fstpso import FuzzyPSO

from print import *
from eval import eval, make_function
from benchmark_function import ackley

from sklearn.metrics import mean_squared_error
from math import sqrt

dims = 1
interval = [[-30, 30]]


def fit(prg):
    try:
        fst_pso_loss(prg)
    except Exception:
        print("exception")
        return math.inf
    x_coord_best = fst_pso_loss(prg)
    y_benchmark_function = ackley(x_coord_best)
    return y_benchmark_function


def fit_3_points(prg):
    try:
        fst_pso_loss(prg)
    except Exception:
        return math.inf
    x_coord_best = fst_pso_loss(prg)
    first_point = [interval[0][0]]
    second_point = [interval[0][-1]]
    approx_fun = make_function(prg)
    y_true = [ackley(first_point), ackley(second_point), ackley(x_coord_best)]
    y_pred = [approx_fun(first_point), approx_fun(second_point), approx_fun(x_coord_best)]
    rmse = mean_squared_error(y_true, y_pred, sample_weight=[0.25, 0.25, 0.5])
    return rmse


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
