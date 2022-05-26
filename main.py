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
dir_results = dir_results + str(dim) + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
dir_results = dir_results + function + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)
if dim == 2:
    dir_results = dir_results + fitn + "/"
    if not os.path.exists(dir_results):
        os.mkdir(dir_results)
dir_results = dir_results + "prg_size" + str(dim_prg) + "_pop_size" + str(pop_size) + "_iter" + str(num_iteration) + "/"
if not os.path.exists(dir_results):
    os.mkdir(dir_results)

for run in range(5, 10):  # num_runs):
    best = linear_GP(fit,
                     pop_size=pop_size,
                     n_iter=num_iteration,
                     dim_prg=dim_prg,
                     dire=dir_results,
                     run=run)


