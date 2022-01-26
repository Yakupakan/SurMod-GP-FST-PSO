import scipy

import gplearn

from fitness import fstpso_loss
from plot_function import *
from benchmark_function import *


def function(x):
    return ackley(x)


D = 1  # dimensione del problema
interval = [-30, 30]
