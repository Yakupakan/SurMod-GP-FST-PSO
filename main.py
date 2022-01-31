import os
import scipy
import gplearn

import matplotlib.pyplot as plt

from gp import linear_GP
from fitness import fit
from eval import make_function
from benchmark_function import *
from plot_function import plot_ackley, plot_prg


pop_size = 99
num_iteration = 1000
dir_results = "results/ackley/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + "pop" + str(pop_size) + "_it" + str(num_iteration) + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)


best = linear_GP(fit, pop_size, num_iteration, dir_results)
function_approximated = make_function(best)

D = 1  # dimensione del problema
interval = [-30, 30]

# x = np.linspace(interval[0], interval[1], 100)
