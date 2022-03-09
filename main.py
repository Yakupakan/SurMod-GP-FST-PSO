import os
import sys
import warnings

import scipy
import gplearn

import matplotlib.pyplot as plt

from hyperparam import *
from gp import linear_GP, fit
from eval import make_function
from plot_function import plot_ackley, plot_prg
from plot import fitness_plot


warnings.filterwarnings("ignore")


dir_results = enum_set.replace(" ", "_") + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + function + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + "/" + fitn + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
if fitn == "strong_fitness_2d" or fitn == "strong_fitness_contour_2d":
    dir_results = dir_results + "/" + str(number_interpolation_point) + "/"
    if not os.path.exists(dir_results):
        os.mkdir(dir_results)
dir_results = dir_results + "prg_size" + str(dim_prg) + "_pop_size" + str(pop_size) + "_iter" + str(num_iteration) + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)

print(function)
print(fitn)
if fitn == "strong_fitness_2d":
    print(number_interpolation_point)
print("program size: \t" + str(dim_prg) + "\npop size: \t" + str(pop_size))
print(enum_set)

best = linear_GP(fit,
                 pop_size=pop_size,
                 n_iter=num_iteration,
                 dim_prg=dim_prg,
                 dire=dir_results)

# function_approximated = make_function(best)
fitness_plot(dir_results)
