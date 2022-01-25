import gplearn

from fitness import fstpso_loss
from plot_function import *
from benchmark_function import *

est_gp = gplearn.genetic.SymbolicRegressor(population_size=1000, generations=20, tournament_size=20,
                                           stopping_criteria=0.0,
                                           const_range=(-1.0, 1.0), init_depth=(2, 6), init_method='half and half',
                                           function_set=('add', 'sub', 'mul', 'div'),
                                           metric=fstpso_loss,
                                           parsimony_coefficient=0.001, p_crossover=0.9, p_subtree_mutation=0.01,
                                           p_hoist_mutation=0.01, p_point_mutation=0.01, p_point_replace=0.05,
                                           max_samples=1.0, feature_names=None, warm_start=False, low_memory=False,
                                           n_jobs=1, verbose=0, random_state=None)

est_gp.fit(X, y)



'''
y = ackley([2])
print(y)

plot_(range(1, 100))
'''
