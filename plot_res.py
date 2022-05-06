import os
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from hyperparam import interval_dict

sns.set_theme(style="darkgrid")
matplotlib.rc('font', **{'size': 6, 'weight': 'bold'})

dim_prg = 10  # int(sys.argv[1])
max_dim_prg = 5 * dim_prg
pop_size = 50  # int(sys.argv[2])
num_iteration = 100  # int(sys.argv[3])

num_runs = 30

function_name = "alpine"
dim = 3

function = function_name + "_" + str(dim) + "d"  # sys.argv[4]

enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'
interval = interval_dict[function_name]

min_dict = {"alpine": 0,
            "ackley": 0,
            "deceptive": -1,
            "griewank": 0,
            "michalewicz": None,
            "rastring": 0,
            "rosenbrock": 0,  # [-2, 2]
            "schwefel": 0,
            "shubert": None,
            "sum_power": 0,
            "vincent": -dim,
            "xinshe": 0}


def mk_dir(fun=function, dim=dim, dim_prg=dim_prg, pop_size=pop_size, num_iteration=num_iteration, enum_set=enum_set):
    dir = enum_set.replace(" ", "_") + "/" + str(dim) + "/" + fun + "/" + "prg_size" + str(dim_prg) + "_pop_size" + str(
        pop_size) + "_iter" + str(num_iteration) + "/"
    return dir


def bp(fun=function, dim=dim, dim_prg=dim_prg, pop_size=pop_size, num_iteration=num_iteration, enum_set=enum_set):
    dir = mk_dir(fun, dim, dim_prg, pop_size, num_iteration, enum_set)
    losses = []
    for run in range(num_runs):
        dir_runs = dir + str(run) + "/loss.txt"
        if os.path.exists(dir_runs):
            with open(dir_runs) as f:
                contents = f.readlines()
                if contents:
                    losses.append(float(contents[-1]))
    if losses:
        sns.boxplot(data=losses,
                    linewidth=2)
        plt.xticks(plt.xticks()[0], [fun[:-3]])
        plt.savefig(dir + "bp_fitness.png")
        plt.savefig("plot/bp_loss/bp_" + function + ".png")
        # plt.show()
        plt.close()


def bp_no(fun=function, dim=dim, dim_prg=dim_prg, pop_size=pop_size, num_iteration=num_iteration, enum_set=enum_set):
    dir = mk_dir(fun, dim, dim_prg, pop_size, num_iteration, enum_set)
    losses = []
    for run in range(num_runs):
        dir_runs = dir + str(run) + "/loss.txt"
        if os.path.exists(dir_runs):
            with open(dir_runs) as f:
                contents = f.readlines()
                if contents:
                    losses.append(float(contents[-1]))
    if losses:
        sns.boxplot(data=losses,
                    linewidth=2,
                    showfliers=False)
        plt.xticks(plt.xticks()[0], [fun[:-3]])
        plt.savefig(dir + "bp_fitness.png")
        plt.savefig("plot/bp_loss_no_outliers/bp_no_" + function + ".png")
        plt.show()
        plt.close()


def loss(fun=function, dim=dim, dim_prg=dim_prg, pop_size=pop_size, num_iteration=num_iteration, enum_set=enum_set):
    dir = mk_dir(fun, dim, dim_prg, pop_size, num_iteration, enum_set)
    losses = []
    for run in range(num_runs):
        dir_runs = dir + str(run) + "/loss.txt"
        if os.path.exists(dir_runs):
            with open(dir_runs) as f:
                contents = f.readlines()
                if contents:
                    losses.append([float(el) for el in contents])
    col_average = [sum(los) / len(los) for los in zip(*losses)]
    if losses:
        ax = sns.lineplot(data=col_average,
                          linewidth=2)
        # plt.xticks(plt.xticks()[0], [fun[:-3]])
        plt.title(function)
        plt.savefig(dir + "bp_fitness.png")
        plt.savefig("plot/loss/loss_" + function + ".png")
        # plt.show()
        plt.close()


for function_name in interval_dict.keys():
    function = function_name + "_" + str(dim) + "d"  # sys.argv[4]
    bp(fun=function)
    bp_no(fun=function)
    loss(fun=function)
