import enum
import math
import random

import numpy as np

from eval import eval, opcodes, make_function
from fitness import fit
from plot_function import plot_prg


def random_program(n):
    prg = []
    func = list(opcodes)
    for i in range(0, n):
        if random.random() < 0.25:  # 0.5
            op = random.choice(func)
        else:
            op = random.randint(-2, 2)
        prg.append(op)
    return prg


def tournament_selection(fit, pop, t_size=4):
    tournament = random.choices(pop, k=t_size)
    return min(tournament, key=fit)


def two_points_crossover(x, y):
    k1 = random.randint(0, len(x) - 1)
    k2 = random.randint(k1, len(x) - 1)
    h1 = random.randint(0, len(y) - 1)
    h2 = random.randint(h1, len(y) - 1)
    of1 = x[0:k1] + y[h1:h2] + x[k2:]
    of2 = y[0:h1] + x[k1:k2] + y[h2:]
    return of1, of2


def mutation(x, p_m):
    def change(b):
        if random.random() < p_m:
            if random.random() < 0.5:
                op = random.choice(list(opcodes))
            else:
                op = random.randint(-2, 2)
            return op
        else:
            return b

    return [change(b) for b in x]


def linear_GP(fit, pop_size, n_iter=100, dire=None):
    f = open(dire + "res.txt", "w")
    p_m = 0.1
    pop = [random_program(10) for _ in range(0, pop_size)]
    best = []
    for i in range(0, n_iter):
        selected = [tournament_selection(fit, pop) for _ in range(0, pop_size)]
        pairs = zip(selected, selected[1:] + [selected[0]])
        offsprings = []
        for x, y in pairs:
            of1, of2 = two_points_crossover(x, y)
            offsprings.append(of1)
            offsprings.append(of2)
        pop = [mutation(x, p_m) for x in offsprings]
        candidate_best = min(pop, key=fit)
        if fit(candidate_best) < fit(best):
            best = candidate_best
        if fit(best) == 0:
            return best

        print(f"Best individual at generation {i}: {best}")
        f.write(f"GEN: {i} \t Best individual: {best}\n")

        print(f"Best fitness at generation {i}: {fit(best)}")
        f.write(f"GEN: {i} \t Best fitness: {fit(best)}\n")

        # np_prg = np.fromfunction(make_function(best), [1])
        # min_i = np_prg.argmin(axis=0)
        # print(f"Mimimum of the prg at generation {i}: {min_i}\n")
        # f.write(f"GEN: {i} \t Mimimum of the prg: {min_i}\n\n")

        interval = [-30, 30]
        x = np.linspace(interval[0], interval[1], 100)
        if dire:
            plot_prg(best, x, dire, i)
    f.close()
    return best


'''
 def fit(prg):
  data = [(i, i**2 + 3*i + 2) for i in range(0, 100)]
  sq_errors = 0
  for x, y in data:
    try:
      stack = eval([x], prg)
    except Exception:
      return math.inf
    if stack == []:
      return math.inf
    else:
      sq_errors += (y - stack.pop())**2
  return sq_errors/len(data)
'''