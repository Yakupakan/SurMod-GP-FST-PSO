import os
import scipy
import gplearn

import matplotlib.pyplot as plt

from gp import linear_GP
from fitness import fit_3_points as fit
from eval import make_function
from benchmark_function import *
from plot_function import plot_ackley, plot_prg


pop_size = 100
num_iteration = 100
dim_prg = 25


dir_results = "results/ackley/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + "fit_3/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + "pop" + str(pop_size) + "_it" + str(num_iteration) + "_dimprg" + str(dim_prg) + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)


best = linear_GP(fit,
                 pop_size=pop_size,
                 n_iter=num_iteration,
                 dim_prg=dim_prg,
                 dire=dir_results)

function_approximated = make_function(best)

D = 1  # dimensione del problema
interval = [-30, 30]

# x = np.linspace(interval[0], interval[1], 100)
