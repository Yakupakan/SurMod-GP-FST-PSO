import fstpso
from fstpso import FuzzyPSO

import numpy as np
from benchmark_function import ackley


def example_fitness(particle):
    return sum(map(lambda x: x ** 2, particle))


dims = 10

FP = FuzzyPSO()

FP.set_search_space([[-10, 10]] * dims)

FP.set_fitness(example_fitness)

result = FP.solve_with_fstpso()

print((result[0]))
print((result[0].X))


def fun(x):
    return x ** 2


a = np.fromfunction(ackley, [5])
min_i = a.argmin(axis=0)
print(min_i)
