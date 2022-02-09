import enum
import math
import random

import numpy as np

from hyperparam import *
from print import *
from eval import eval, opcodes, make_function
from plot_function import plot_prg

if fitn == "strong_fitness_4":
    from fitness import strong_fitness_4 as fit
if fitn == "strong_fitness_mul_4":
    from fitness import strong_fitness_mul_4 as fit


snap = 5
min_con, max_con = -10, 10  # minimum and maximum value that constants can assume
if function == "griewank":
    max_fit = 5 * 10 ** 3
    min_con, max_con = -50, 50  # minimum and maximum value that constants can assume
else:
    max_fit = 10 ** 3


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
        if fit(prg) and fit(prg) < max_fit:
            enablePrint()
            print("program find with fitness :" + str(fit(prg)))
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
        if fit(of1) and fit(of2) and fit(of1) < 10 ** 4 and fit(of2) < 10 ** 4:
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
        if fit(mutated_prg) and fit(mutated_prg) < 10 ** 4:
            flag = 1
        if numb_combination == max_number_combination:
            return x  # non modifico i vettori se non riesco a combinarli in modo intelligente dopo 100 tentativi
    return mutated_prg


def linear_GP(fit, pop_size=100, n_iter=100, dim_prg=10, dire=None):
    f, f_loss = open(dire + "res.txt", "w"), open(dire + "loss.txt", "w")
    p_m = 0.2
    pop = [random_program_attention(dim_prg) for _ in range(0, pop_size)]  # 10
    best = []
    for i in range(0, n_iter):
        if i > 0:
            pop.append(best)  # the best solution is inserted again

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

        """
        number_real_solution = [sol for sol in pop if fit(sol) != math.inf]
        enablePrint()
        print("number of real solution : " + str(len(number_real_solution)))
        for j in range(len(number_real_solution)):
            print(str(j) + " real solution : " + str(number_real_solution[j]) + "\t fitness : " + str(
                fit(number_real_solution[j])))
        """
        enablePrint()
        candidate_best = min(pop, key=fit)
        print("\n fitness candidate best : " + str(fit(candidate_best)))
        if fit(candidate_best) < fit(best):
            best = candidate_best
        if fit(best) == 0:
            return best

        print(f"GEN: {i} \t Best individual: {best}")
        f.write(f"GEN: {i} \t Best individual: {best}\n")

        print(f"GEN: {i} \t Best fitness: {fit(best)}\n")
        f.write(f"GEN: {i} \t Best fitness: {fit(best)}\n")

        f_loss.write(f"{fit(best)}\n")

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

        x = np.linspace(interval[0], interval[1], 10001)
        if dire and i % snap == 0:
            plot_prg(best, x, dire, i)

    f.close()
    f_loss.close()

    return best
