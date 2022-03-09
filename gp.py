import enum
import math
import random

import numpy as np

from hyperparam import *
from print import *
from eval import opcodes, make_function
from fitness import fst_pso_loss
from plot_function import plot_prg, plot_prg_2d


if fitn == "strong_fitness_4":
    from fitness import strong_fitness_4 as fit
if fitn == "strong_fitness_2d":
    from fitness import strong_fitness_2d as fit
if fitn == "strong_fitness_contour_2d":
    from fitness import strong_fitness_contour_2d as fit


snap = 1
if function == "griewank" or function == "griewank_2d":
    max_fit = 5 * 10 ** 4
    min_con, max_con = -500, 500  # minimum and maximum value that constants can assume
if function == "rosenbrock_2d":
    max_fit = 10 ** 4
    min_con, max_con = -10 ** 3, 10 ** 3  # minimum and maximum value that constants can assume
elif function == "schwefel" or function == "schwefel_2d":
    max_fit = 5 * 10 ** 6
    min_con, max_con = -250, 250
elif function == "vincent":
    max_fit = 10 ** 3
    min_con, max_con = -2, 2  # minimum and maximum value that constants can assume
else:
    max_fit = 10 ** 3
    min_con, max_con = -10, 10  # minimum and maximum value that constants can assume


def random_program(n):
    prg = []
    func = list(opcodes)
    for i in range(0, n):
        if random.random() < 0.5:
            op = random.choice(func)
        else:
            op = random.randint(-2, 2)
        prg.append(op)
    return prg


def random_program_attention(n):
    flag = 0  # return if the program is valid
    while not flag:
        prg = []
        func = list(opcodes)
        for i in range(0, n):
            if random.random() < 0.5:  # 0.5
                op = random.choice(func)
            else:
                op = random.randint(min_con, max_con)  # (-2, 2)
            prg.append(op)
        fit_prg = fit(prg)
        if fit_prg and fit_prg < max_fit:
            enablePrint()
            print("program find with fitness :" + str(fit_prg))
            flag = 1
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


def two_points_crossover_attention(x, y):
    flag = 0  # return if the program is valid
    max_number_combination = 50
    numb_combination = 0
    while not flag:
        numb_combination += 1
        k1 = random.randint(0, len(x) - 1)
        k2 = random.randint(k1, len(x) - 1)
        h1 = random.randint(0, len(y) - 1)
        h2 = random.randint(h1, len(y) - 1)
        of1 = x[0:k1] + y[h1:h2] + x[k2:]
        of2 = y[0:h1] + x[k1:k2] + y[h2:]

        if len(of1) > max_dim_prg:
            of1 = of1[:max_dim_prg]
        if len(of2) > max_dim_prg:
            of2 = of2[:max_dim_prg]

        if fit(of1) and fit(of2) and fit(of1) < max_fit and fit(of2) < max_fit:
            flag = 1
        if numb_combination == max_number_combination:
            return x, y  # non modifico i vettori se non riesco a combinarli in modo intelligente dopo 100 tentativi
    return of1, of2


def mutation(x, p_m):
    def change(b):
        if random.random() < p_m:
            if random.random() < 0.5:  # 0.5
                op = random.choice(list(opcodes))
            else:
                op = random.randint(min_con, max_con)  # (-2, 2)
            return op
        else:
            return b

    return [change(b) for b in x]


def mutation_attention(x, p_m):
    flag = 0  # return if the program is valid
    max_number_combination = 50
    numb_combination = 0

    def change(b):
        if random.random() < p_m:
            if random.random() < 0.5:  # 0.5
                op = random.choice(list(opcodes))
            else:
                op = random.randint(min_con, max_con)  # (-2, 2)
            return op
        else:
            return b

    while not flag:
        mutated_prg = [change(b) for b in x]
        if fit(mutated_prg) and fit(mutated_prg) < max_fit:
            flag = 1
        if numb_combination == max_number_combination:
            return x  # non modifico i vettori se non riesco a combinarli in modo intelligente dopo 100 tentativi
    return mutated_prg


def linear_GP(fit, pop_size=100, n_iter=100, dim_prg=10, dire=None):
    f, f_loss, f_argmin = open(dire + "res.txt", "w"), open(dire + "loss.txt", "w"), open(dire + "argmin.txt", "w")
    p_m = 0.2
    pop = [random_program_attention(dim_prg) for _ in range(0, pop_size)]  # 10
    best = random_program_attention(dim_prg)  # []
    for i in range(0, n_iter):
        if i > 0:
            pop.append(best)  # the best solution is inserted (elitism)

        pop = list(dict.fromkeys([tuple(el) for el in pop]))
        pop = [list(el) for el in pop]

        selected = [tournament_selection(fit, pop) for _ in range(0, pop_size)]
        pairs = zip(selected, selected[1:] + [selected[0]])
        offsprings = []
        for x, y in pairs:
            of1, of2 = two_points_crossover_attention(x, y)
            offsprings.append(of1)
            offsprings.append(of2)

        pop = [mutation_attention(x, p_m) for x in offsprings]

        enablePrint()
        candidate_best = min(pop, key=fit)

        if fit(candidate_best) < fit(best):
            best = candidate_best
        if function != "michalewicz_2d":
            if fit(best) < 10**(-8):
                print("termination criteria satisfied")
                return best

        try:
            argmin_best = fst_pso_loss(best)
        except Exception:
            print("not able to compute argmin within fst-pso")
            argmin_best = [math.inf, math.inf]

        print(f"GEN: {i} \t best individual: \t {best}")
        f.write(f"GEN: {i} \t best individual: \t {best}\n")

        print(f"GEN: {i} \t best fitness: \t {fit(best)}")
        f.write(f"GEN: {i} \t best fitness: \t {fit(best)}\n")

        print(f"GEN: {i} \t argmin best prg: \t {argmin_best}\n")
        f.write(f"GEN: {i} \t argmin best prg: \t {argmin_best}\n")

        f_loss.write(f"{fit(best)}\n")
        f_argmin.write(f"{argmin_best}\n")

        if function[-2:] != "2d":
            if function == "ackley":
                interval = [-30, 30]
            if function == "alpine":
                interval = [-10, 10]
            if function == "griewank":
                interval = [-600, 600]
            if function == "rastring":
                interval = [-5.12, 5.12]
            if function == "xinshe":
                interval = [-2 * np.pi, 2 * np.pi]
            if function == "vincent":
                interval = [0.25, 10]

            x = np.linspace(interval[0], interval[1], 10001)
            if dire and i % snap == 0:
                plot_prg(best, x, dire, i)
        else:
            if dire and i % snap == 0:
                plot_prg_2d(best, dire, i)

    f.close()
    f_loss.close()
    f_argmin.close()

    return best
