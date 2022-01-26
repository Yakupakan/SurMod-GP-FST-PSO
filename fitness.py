import numpy as np
import math

import fstpso
from fstpso import FuzzyPSO

from benchmark_function import ackley


def fit(prg):
    print(prg)
    x_coord_best = fst_pso_loss(prg)
    y_benchmark_function = ackley(x_coord_best)
    return y_benchmark_function


def fst_pso_loss(prg):
    """
    :param prg: individual of the population (program)
    :param dims: dimension of the space (also called D)
    :param interval: interval of the problem (insert a list like: [[-10, 10]])
    :return: coordinates relative to the minimum of prg
    """
    dims = 1
    interval = [[-30, 30]]
    FP = FuzzyPSO()
    FP.set_search_space(interval * dims)
    FP.set_fitness(prg)
    result = FP.solve_with_fstpso()
    return result[0]

