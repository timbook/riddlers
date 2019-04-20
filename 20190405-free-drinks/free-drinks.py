import random

N_SIMS = 10_000

class Card:
    def __init__(self):
        self.n_drinks = 50

    def consume(self):
        self.n_drinks -= 1

def run_sim():
    cards = [Card(), Card()]
    while True:
        r = random.randint(0, 1)
        if cards[r].n_drinks == 0:
            return cards[1 - r].n_drinks
        else:
            cards[r].consume()
    
sims = [run_sim() for _ in range(N_SIMS)]

n_zeros = len([s for s in sims if s == 0]) / len(sims)
n_drinks = sum(sims) / len(sims)

print(f"The probability the other card is empty: {n_zeros}")
print(f"The expected number of remaining drinks: {n_drinks}")
