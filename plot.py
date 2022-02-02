import os

import matplotlib.pyplot as plt
import seaborn as sns


sns.set(context='notebook',
        style='whitegrid',
        palette='deep',
        font='sans-serif',
        font_scale=1)


def fitness_plot(dir):
    print(os.getcwd())
    with open(dir + "loss.txt") as f:
        lines = f.readlines()
    fitness = [float(line[:-2]) for line in lines]

    plt.plot(fitness)
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.show()
    plt.savefig(dir + "fitness.png")
    plt.close()
