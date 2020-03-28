import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def check_if_done(die):
    return np.all(die == die[0])

def run_game(sides=6):
    die = np.arange(1, sides + 1)
    count = 0
    while not check_if_done(die):
        die = np.random.choice(die, size=sides, replace=True)
        count += 1

    return count

def get_row(sides, ix):
    results = np.array([run_game(sides) for _ in range(1_000)])
    return pd.DataFrame({
        'N': sides,
        'lower': np.quantile(results, 0.10),
        'avg': np.mean(results),
        'upper': np.quantile(results, 0.90)
    }, index=[ix])

data_list = [get_row(sides, ix) for ix, sides in enumerate(range(2, 100))]
data = pd.concat(data_list, axis=0)

plt.plot(
    data.N,
    data.avg,
    color='darkblue'
)
plt.fill_between(
    data.N,
    y1=data.upper,
    y2=data.lower,
    color='lightblue',
    alpha=0.3
)
plt.savefig('./dice-plot.png', dpi=200)
