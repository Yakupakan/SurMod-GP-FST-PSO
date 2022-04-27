"""
Hyperparameter settings of the problem
"""

dim_prg = 10  # int(sys.argv[1])
max_dim_prg = 5 * dim_prg
pop_size = 50  # int(sys.argv[2])
num_iteration = 200  # int(sys.argv[3])
function = "xinshe_2d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'
# 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP SIN COS EXP NOP'  # 'PLUS MINUS TIMES DIVIDE MOD DUP SWAP NOP'

function_set = ["alpine", "ackley", "griewank", "michalewicz", "rastring", "rosenbrock", "schwefel", "vincent", "xinshe"]
fitn = "strong_fitness_2d"  # "strong_fitness_2d_weighted"
number_interpolation_point = 15  # 51
