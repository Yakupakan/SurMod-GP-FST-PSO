"""
Hyperparameter settings of the problem
"""
import numpy as np


function_name = "griewank"
dim = 5

dim_prg = 10  # int(sys.argv[1])
max_dim_prg = 5 * dim_prg
if dim == 5:
    pop_size = 100  # int(sys.argv[2])
if dim == 2 or dim == 3:
    pop_size = 50
num_iteration = 100  # int(sys.argv[3])

flag_plot = 0
flag_countour = 0
num_runs = 30

function = function_name + "_" + str(dim) + "d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'
# 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP SIN COS EXP NOP'  # 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP NOP'

interval_dict = {"alpine": [[-10, 10]],  # 2
                 "ackley": [[-30, 30]],  # 2
                 "deceptive": [[0, 1]],
                 "griewank": [[-600, 600]],  # 2
                 "michalewicz": [[0, np.pi]],  # 2
                 "rastring":  [[-5.12, 5.12]],  # 2
                 "rosenbrock": [[-5, 10]],  # [-2, 2]
                 "schwefel": [[-100, 500]],
                 "shubert": [[-5.12, 5.12]],  # 2
                 "sum_power": [[-1, 1]],
                 "vincent": [[0.25, 10]],
                 "xinshe": [[-2 * np.pi, 2 * np.pi]]  # 2
                 }

interval = interval_dict[function_name]

function_set = ["alpine", "ackley", "griewank", "michalewicz", "rastring", "rosenbrock", "schwefel", "vincent", "xinshe"]
if dim == 2 and flag_plot == 1:
    fitn = "strong_fitness_2d"  # "strong_fitness_2d_weighted"
if dim == 2 and flag_plot == 1 and flag_countour == 1:
    fitn = "strong_fitness_contour_2d"
if dim == 2 and flag_plot == 0:
    fitn = "fitness_2d"  # "strong_fitness_2d_weighted"
if dim == 3:
    fitn = "strong_fitness_3d"  # "strong_fitness_2d_weighted"
if dim == 5:
    fitn = "strong_fitness_5d"

number_interpolation_point = 51  # 51

