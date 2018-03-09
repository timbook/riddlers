import numpy as np

# Strategy: Reroll 5s.
def scoreRoll(dice):
    if np.all(dice == 4):
        return 50
    else:
        return 12 + sum(dice)

def playGame():
    dice = np.random.randint(1, 7, 2)
    return scoreRoll(dice)

ITER = int(1e5)
scores = np.zeros(ITER)
for i in range(ITER):
    score = playGame()
    scores[i] = score

print("")
print("Mean Score:")
print(np.mean(scores))

prop_yahtzees = np.mean(scores == 50)

print("")
print("Score Tabulation:")
print("% Yahtzees: ".ljust(15), "{0:.4}%".format(100 * prop_yahtzees).rjust(6))
print("% 3oak/4oaks: ".ljust(15), "{0:.4}%".format(100 - 100 * prop_yahtzees).rjust(6))
