import numpy as np
import matplotlib.pyplot as plt

from sockdrawer import run_sim

def run_sims_n(n):
    N_SIMS = 10_000
    return np.array([run_sim(n) for _ in range(N_SIMS)])

SOCK_PAIRS = list(range(1, 200))

pull_dict = {k: run_sims_n(k) for k in SOCK_PAIRS}

pull_means = [np.mean(v) for k, v in pull_dict.items()]
pull_upper = [np.quantile(v, 0.8) for k, v in pull_dict.items()]
pull_lower = [np.quantile(v, 0.2) for k, v in pull_dict.items()]

plt.fill_between(SOCK_PAIRS, pull_lower, pull_upper, alpha=0.3)
plt.plot(SOCK_PAIRS, pull_means)
plt.xlabel("Number of Sock Pairs in Drawer")
plt.ylabel("Number of Pulls Required")

plt.savefig("graph.png", dpi=192)
