import fstpso
from fstpso import FuzzyPSO

def example_fitness( particle ):

    return sum(map(lambda x: x**2, particle))


dims = 10

FP = FuzzyPSO( )

FP.set_search_space( [[-10, 10]]*dims )

FP.set_fitness(example_fitness)

result = FP.solve_with_fstpso()

print((result[0]))
print((result[0].X))

