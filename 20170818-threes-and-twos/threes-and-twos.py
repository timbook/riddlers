import numpy as np
import pandas as pd

sq = [3, 3, 3, 2]

ITER = int(1e4)
for i in range(1, ITER):
  sq = sq + [3] * sq[i] + [2]

print('\nTable of 3s and 2s:')
print(pd.Series(sq).value_counts())
print('\nProportion of 3s and 2s:')
print(pd.Series(sq).value_counts() / len(sq))
