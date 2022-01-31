import fstpso
from fstpso import FuzzyPSO

import numpy as np
from benchmark_function import ackley
from eval import eval, make_function
from gp import random_program

prg = random_program(10)
print(prg)


print(eval([0], prg))
func = make_function(prg)
print(func([0]))
