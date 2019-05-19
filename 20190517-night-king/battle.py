from random import random
from itertools import product
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def battle(H, Z):
    while H and Z:
        r = random()

        # Human wins
        if r > 0.5:
            Z -= 1
        # Zombie wins
        else:
            H -= 1
            Z += 1

    return True if H > 0 else False

def bootstrap_battle(H, Z, n_sim=1000):
    return np.mean([battle(H, Z) for _ in range(n_sim)])

if __name__ == '__main__':
    n_max = 50
    soldier_combos = product(range(1, n_max + 1), range(1, n_max + 1))
    battle_matrix = np.zeros((n_max, n_max))
    for H, Z in soldier_combos:
        battle_matrix[H - 1, Z - 1] = bootstrap_battle(H, Z)

    print(battle_matrix)
    ax = sns.heatmap(
        battle_matrix,
        vmin=0,
        vmax=1,
        xticklabels=np.arange(n_max) + 1,
        yticklabels=np.arange(n_max) + 1,
        cmap='coolwarm',
        annot=True,
        annot_kws={'size': 2},
        cbar=False
    )
    ax.invert_yaxis()
    ax.set_title('Probability of Human Survival')
    ax.set_xlabel('Size of Zombie Army')
    ax.set_ylabel('Size of Human Army')
    ax.tick_params(axis='both', labelsize=2)
    plt.savefig('armyplot.png', dpi=192*3)
