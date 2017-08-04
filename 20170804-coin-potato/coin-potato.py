import numpy as np
import pandas as pd

def runPotato():
    n_people = 31

    curr_pos = 0
    visited = np.zeros(n_people)
    visited[curr_pos] = 1

    while True:
        mv_right = np.random.binomial(1, 0.5, 1)[0]
        if mv_right:
            curr_pos += 1
        else:
            curr_pos -= 1

        curr_pos %= 31
        visited[curr_pos] = 1

        if np.sum(visited) == n_people - 1:
            break

    winner = np.where(visited == 0)[0][0]
    return winner

ITER = 1000
winners = np.zeros(ITER)
for i in range(ITER):
    winners[i] = runPotato()

print(pd.Series(winners).value_counts())
print(len(winners))
