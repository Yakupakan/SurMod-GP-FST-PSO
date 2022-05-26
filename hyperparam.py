"""
Hyperparameter settings of the problem
"""
import numpy as np


function_name = "michalewicz"
dim = 2

dim_prg = 10
max_dim_prg = 5 * dim_prg
if dim == 4 or dim == 5:
    pop_size = 100
if dim == 2 or dim == 3:
    pop_size = 50
num_iteration = 500

flag_plot = 1
flag_countour = 0
num_runs = 30

function = function_name + "_" + str(dim) + "d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'

interval_dict = {"alpine": [[-10, 10]],
                 "ackley": [[-30, 30]],
                 "deceptive": [[0, 1]],
                 "griewank": [[-600, 600]],
                 "michalewicz": [[0, np.pi]],
                 "rastring":  [[-5.12, 5.12]],
                 "rosenbrock": [[-5, 10]],
                 "schwefel": [[-500, 500]],
                 "shubert": [[-5.12, 5.12]],
                 "sum_power": [[-1, 1]],
                 "vincent": [[0.25, 10]],
                 "xinshe": [[-2 * np.pi, 2 * np.pi]]
                 }

interval = interval_dict[function_name]

function_set = ["alpine", "ackley", "griewank", "michalewicz", "rastring", "rosenbrock", "schwefel", "vincent", "xinshe"]
if dim == 2 and flag_plot == 1:
    fitn = "strong_fitness_2d"
if dim == 2 and flag_plot == 1 and flag_countour == 1:
    fitn = "strong_fitness_contour_2d"
if dim == 2 and flag_plot == 0:
    fitn = "fitness_2d"
if dim == 3:
    fitn = "strong_fitness_3d"
if dim == 4:
    fitn = "strong_fitness_4d"
if dim == 5:
    fitn = "strong_fitness_5d"

number_interpolation_point = 51

