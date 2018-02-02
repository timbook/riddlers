from bottle import Bottle
import numpy as np

def simulate(ITER):
    results = [0]*ITER
    for i in range(ITER):
        b = Bottle()
        results[i] = b.runSimulation()
    return np.mean(results)

ITER = 1000
print(simulate(ITER))
