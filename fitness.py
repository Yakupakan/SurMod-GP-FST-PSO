import numpy as np
import math

import fstpso
from fstpso import FuzzyPSO

from print import *
from eval import eval, make_function
from benchmark_function import ackley

dims = 1
interval = [[-30, 30]]


def fit(prg):
    #    function__ = make_function(prg)
    #    print(function__([3, 3, 3, 3]))
    #    print(eval([3,3,3,3], prg))
    try:
        fst_pso_loss(prg)
    except Exception:
        return math.inf
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
    blockPrint()
    FP = FuzzyPSO()
    FP.set_search_space(interval * dims)
    FP.set_fitness(make_function(prg))
    result = FP.solve_with_fstpso()
    enablePrint()
    return result[0].X  # the .X transfrom the Particle structure into a list
