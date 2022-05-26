import os
import numpy as np

import colorsys
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

from hyperparam import interval_dict

sns.set_theme(style="whitegrid")
matplotlib.rc('font', **{'size': 1, 'weight': 'bold'})

function_name = "alpine"
dim = 2

dim_prg = 10
max_dim_prg = 5 * dim_prg
if dim == 4 or dim == 5:
    pop_size = 100
if dim == 2 or dim == 3:
    pop_size = 50
num_iteration = 100

num_runs = 30
function = function_name + "_" + str(dim) + "d"  # sys.argv[4]
interval = interval_dict[function_name]

fitness_2d = "fitness_2d"
enum_set = 'PLUS MINUS TIMES DIVIDE DUP SWAP'

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
    if dim == 2:
        dir = enum_set.replace(" ", "_") + "/" + str(dim) + "/" + fun + "/" + fitness_2d + "/" + "prg_size" \
              + str(dim_prg) + "_pop_size" + str(pop_size) + "_iter" + str(num_iteration) + "/"
    return dir


def print_median(fun=function, dim=dim, dim_prg=dim_prg, pop_size=pop_size, num_iteration=num_iteration, enum_set=enum_set):
    dir = mk_dir(fun, dim, dim_prg, pop_size, num_iteration, enum_set)
    losses = []
    for run in range(num_runs):
        dir_runs = dir + str(run) + "/loss.txt"
        if os.path.exists(dir_runs):
            with open(dir_runs) as f:
                contents = f.readlines()
                if contents:
                    contents = [float(cont) for cont in contents]
                    losses.append(min(contents))
    if losses:
        print(function + " " + str(dim) + " :" + str(np.median(losses)))


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
                    contents = [float(cont) for cont in contents]
                    losses.append(min(contents))
    if losses:
        col = "black"
        col2 = "indigo"
        lw = 2
        lw_median = 2.5
        boxprops = dict(linestyle='-', linewidth=3, color="w", edgecolor="black", alpha=.75)
        medianprops = dict(linestyle='-', linewidth=lw_median, color='firebrick')
        meanpointprops = dict(marker='D', markeredgecolor='black',
                              markerfacecolor='green')

        ax2 = sns.boxplot(data=losses,
                          boxprops=boxprops,
                          medianprops=medianprops,
                          meanprops=meanpointprops,
                          showmeans=True,
                          linewidth=lw,
                          showfliers=False)

        for i, artist in enumerate(ax2.artists):
            artist.set_edgecolor(col)
            artist.set_facecolor('khaki')

            for j in range(i * 6, i * 6 + 6):
                line = ax2.lines[j]
                line.set_color(col)
                line.set_mfc(col2)

            for line in ax2.get_lines()[4::12]:
                line.set_color('crimson')

        current_values = plt.gca().get_yticks()
        if np.abs(np.mean(current_values)) < 0.01:
            plt.gca().set_yticklabels(['{:.1e}'.format(x) for x in current_values])
        else:
            plt.gca().set_yticklabels(['{:.2f}'.format(x) for x in current_values])

        plt.xticks([])
        plt.savefig(dir + "bp_fitness.png")
        plt.savefig("plot/bp_loss_no_outliers/bp_no_" + function + ".png")
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
                          linewidth=2,
                          color='#F08030')
        plt.title(function)
        plt.savefig(dir + "bp_fitness.png")
        plt.savefig("plot/loss/loss_" + function + ".png")
        plt.close()


for function_name in interval_dict.keys():
    for dim in range(2, 5):
        function = function_name + "_" + str(dim) + "d"  # sys.argv[4]
        print_median(fun=function, dim=dim)
        # bp(fun=function, dim=dim)
        # bp_no(fun=function, dim=dim)
        # loss(fun=function, dim=dim)
