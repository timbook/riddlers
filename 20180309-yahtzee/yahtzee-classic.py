import numpy as np

def rollDie():
    return np.random.randint(1, 7)

class Dice:
    def __init__(self):
        self.other_dice = np.array([2, 4, 5])
        self.d1 = 1
        self.dx = 7 # Dummy to be rerolled

    def rollStrategy(self, strategy):
        if strategy == 1:
            # Reroll only X
            self.dx = rollDie() if self.dx != 3 else self.dx
        elif strategy == 2:
            # Reroll both 1 and X
            if np.all(np.sort(np.array([self.d1, self.dx])) == np.array([3, 6])):
                pass
            elif self.d1 == 3 or self.d1 == 6:
                self.dx = rollDie()
            elif self.dx == 3 or self.dx == 6:
                self.d1 = rollDie()
            else:
                self.d1 = rollDie()
                self.dx = rollDie()

    def isLargeStraight(self):
        dice = np.append(self.other_dice, [self.d1, self.dx])
        dice = np.sort(dice)

        if np.all(dice == np.arange(1, 6)) or np.all(dice == np.arange(2, 7)):
            return 1
        else:
            return 0

    def playGame(self, strategy):
        self.rollStrategy(strategy)
        self.rollStrategy(strategy)
        return self.isLargeStraight()

ITER = int(1e5)
strat_one_wins = np.zeros(ITER)
strat_two_wins = np.zeros(ITER)

for i in range(ITER):
    d1 = Dice()
    strat_one_wins[i] = d1.playGame(1)

    d2 = Dice()
    strat_two_wins[i] = d2.playGame(2)

print("")
print("% wins rerolling only X:")
print(str(100 * np.mean(strat_one_wins)) + "%")

print("")
print("% wins rerolling both 1 and  X:")
print(str(100 * np.mean(strat_two_wins)) + "%")
