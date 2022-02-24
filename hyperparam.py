"""
Hyperparameter settings of the problem
"""

dim_prg = 10  # int(sys.argv[1])
max_dim_prg = 2 * dim_prg
pop_size = 100  # int(sys.argv[2])
num_iteration = 250  # int(sys.argv[3])
function = "ackley_2d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP NOP'

function_set = ["alpine", "ackley", "griewank", "rastring", "xinshe", "vincent"]
fitn = "strong_fitness_2d"  # "strong_fitness_contour_2d"  # "strong_fitness_mul_4"
number_interpolation_point = 5
