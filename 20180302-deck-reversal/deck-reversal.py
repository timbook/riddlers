from random import shuffle
import sys
import numpy as np

# First argument should be deck size: 13 or 53.
deck_size = int(sys.argv[1])

class Deck:
    def __init__(self, size = 13):
        self.cards = list(range(1, size + 1))
        shuffle(self.cards)
        self.n_shuffles = 0

    def peekAndReverse(self):
        k = self.cards[0]
        self.cards[:k] = self.cards[(k - 1)::-1]

    def incShuffles(self):
        self.n_shuffles += 1

    def playGame(self):
        while self.cards[0] != 1:
            self.peekAndReverse()
            self.incShuffles()
        return(self.n_shuffles)


ITER = int(1e4)
results = np.zeros(ITER)

for i in range(ITER):
    results[i] = Deck(deck_size).playGame()

print('')
print('Iters: '.ljust(10), len(results))
print('Size: '.ljust(10), deck_size)
print('')
print('Minimum: '.ljust(10), np.min(results))
print('Median: '.ljust(10), np.median(results))
print('Maximum: '.ljust(10), np.max(results))
print('')
print('Mean: '.ljust(10), np.mean(results))
print('SD: '.ljust(10), np.std(results))
