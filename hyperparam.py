"""
Hyperparameter settings of the problem
"""

dim_prg = 5  # int(sys.argv[1])
max_dim_prg = 2 * dim_prg
pop_size = 100  # int(sys.argv[2])
num_iteration = 100  # int(sys.argv[3])
function = "vincent"  # sys.argv[4]
function_set = ["alpine", "ackley", "griewank", "rastring", "xinshe", "vincent"]
fitn = "strong_fitness_4"  # "strong_fitness_contour_2d"  # "strong_fitness_mul_4"
number_interpolation_point = 7
