"""
Hyperparameter settings of the problem
"""
import numpy as np

dim_prg = 10  # int(sys.argv[1])
max_dim_prg = 5 * dim_prg
pop_size = 100  # int(sys.argv[2])
num_iteration = 100  # int(sys.argv[3])

num_runs = 30

function_name = "schwefel"
dim = 3

function = function_name + "_" + str(dim) + "d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'
# 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP SIN COS EXP NOP'  # 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP NOP'

interval_dict = {"alpine": [[-10, 10]],
                 "ackley": [[-30, 30]],
                 "griewank": [[-600, 600]],
                 "michalewicz": [[0, np.pi]],
                 "rastring":  [[-5.12, 5.12]],
                 "rosenbrock": [[-5, 10]],  # [-2, 2]
                 "schwefel": [[-500, 500]],
                 "vincent": [[0.25, 10]],
                 "xinshe": [[-2 * np.pi, 2 * np.pi]]}

interval = interval_dict[function_name]

function_set = ["alpine", "ackley", "griewank", "michalewicz", "rastring", "rosenbrock", "schwefel", "vincent", "xinshe"]
if dim == 2:
    fitn = "strong_fitness_2d"  # "strong_fitness_2d_weighted"
if dim == 3:
    fitn = "strong_fitness_3d"  # "strong_fitness_2d_weighted"

number_interpolation_point = 15  # 51

