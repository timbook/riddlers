# If N points are generated at random places on the perimeter of a circle, what
# is the probability that you can pick a diameter such that all of those points
# are on only one side of the newly halved circle?

from random import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

N_SIMS = 10000
N_MAX = 20

def gen_points(n):
    return sorted([random() for _ in range(n)])

def dist(a, b):
    return abs(b - a)

def sim_game(n):
    pts = gen_points(n)
    dists = [dist(a, b) for a, b in zip(pts, pts[1:] + [1 + pts[0]])]
    return any(d > 0.5 for d in dists)

def sim_many_games(n_sims, n):
    games = np.array([sim_game(n) for _ in range(n_sims)])
    return np.mean(games)

results = [(n_pts, sim_many_games(N_SIMS, n_pts)) for n_pts in range(2, N_MAX + 1)]

probs = pd.DataFrame(results)
probs.columns = ["N", "prob"]

plt.plot(probs.N, probs.prob, color='#2C4F8E')
plt.grid(color='#D3D3D3')
plt.xlabel("Number of Points")
plt.ylabel("Probability of Success")
plt.xticks(probs.N, fontsize=8)
plt.yticks(np.linspace(0, 1, 11), fontsize=8)

plt.savefig('simplot.png', dpi=200)
