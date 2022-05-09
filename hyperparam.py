"""
Hyperparameter settings of the problem
"""
import numpy as np

dim_prg = 10  # int(sys.argv[1])
max_dim_prg = 5 * dim_prg
pop_size = 50  # int(sys.argv[2])
num_iteration = 500  # int(sys.argv[3])

flag_plot = 1
flag_countour = 0
num_runs = 30

function_name = "alpine"
dim = 5

function = function_name + "_" + str(dim) + "d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'
# 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP SIN COS EXP NOP'  # 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP NOP'

interval_dict = {"alpine": [[-10, 10]],
                 "ackley": [[-30, 30]],
                 "deceptive": [[0, 1]],
                 "griewank": [[-600, 600]],
                 "michalewicz": [[0, np.pi]],
                 "rastring":  [[-5.12, 5.12]],
                 "rosenbrock": [[-5, 10]],  # [-2, 2]
                 "schwefel": [[-100, 500]],
                 "shubert": [[-5.12, 5.12]],
                 "sum_power": [[-1, 1]],
                 "vincent": [[0.25, 10]],
                 "xinshe": [[-2 * np.pi, 2 * np.pi]]}

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

