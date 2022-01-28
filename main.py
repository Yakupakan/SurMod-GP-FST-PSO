import scipy
import gplearn

import matplotlib.pyplot as plt

from gp import linear_GP
from fitness import fit
from eval import make_function
from benchmark_function import *
from plot_function import plot_ackley, plot_prg


def function(x):
    return ackley(x)


pop_size = 50
num_iteration = 10

best = linear_GP(fit, pop_size, num_iteration)
function_approximated = make_function(best)

D = 1  # dimensione del problema
interval = [-30, 30]

x = np.linspace(interval[0], interval[1], 100)

plot_ackley(x)
plot_prg(best, x)
print(best)