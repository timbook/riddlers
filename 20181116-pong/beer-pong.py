import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from cup import Cup, CupSet

def simulate_game(N):
    cset = CupSet(N)
    nrounds = 0
    while True:
        
        while True:
            cset.add_random_ball()
            if cset.check_all_full(): break

        cset.prune_cups()
        nrounds += 1

        if cset.check_all_full(): break

    return nrounds

means = np.array([])
stds = np.array([])
xrng = np.arange(1, 100)

for i in xrng:
    rounds = [simulate_game(i) for _ in range(100)]
    round_mean = np.mean(rounds)
    round_std = np.std(rounds)

    if i % 10 == 0:
        print(f"ROUND {i}:")
        print(f"MEAN = {round_mean} (PRED: {2*i - 1}), STD = {round_std}")
        print('='*81)

    means = np.append(means, round_mean)
    stds = np.append(stds, round_std)

err_high = means + stds
err_low = means - stds

ball_df = pd.DataFrame({
    'N': xrng,
    'means': means,
    'stds': stds
})
ball_df.to_csv('pong-counts.csv', index=False)

plt.fill_between(xrng, err_low, err_high, alpha=0.3)
plt.plot(xrng, means)
plt.plot(xrng, 2*xrng - 1, color='red')
plt.xlabel('N')
plt.ylabel('Expected Number of Rounds Played')
plt.savefig('ball-plot.png', dpi=300)
plt.show()
