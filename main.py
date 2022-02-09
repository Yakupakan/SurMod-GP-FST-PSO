import os
import sys
import warnings

import scipy
import gplearn

import matplotlib.pyplot as plt

from hyperparam import *
from gp import linear_GP
from eval import make_function
from plot_function import plot_ackley, plot_prg
from plot import fitness_plot

if fitn == "strong_fitness_4":
    from fitness import strong_fitness_4 as fit

if function == "alpine":
    from benchmark_function import alpine as benchmark_fun
    interval = [[-10, 10]]

if function == "ackley":
    from benchmark_function import ackley as benchmark_fun
    interval = [[-30, 30]]

if function == "griewank":
    from benchmark_function import griewank as benchmark_fun
    interval = [[-600, 600]]


warnings.filterwarnings("ignore")


dir_results = "results/" + function + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + "/" + fitn + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + "prg_size" + str(dim_prg) + "_pop_size" + str(pop_size) + "_iter" + str(num_iteration) + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)

best = linear_GP(fit,
                 pop_size=pop_size,
                 n_iter=num_iteration,
                 dim_prg=dim_prg,
                 dire=dir_results)

# function_approximated = make_function(best)
fitness_plot(dir_results)
