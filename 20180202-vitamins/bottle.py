import numpy as np

class Bottle:
    def __init__(self):
        self.contents = np.array(['red']*30 + ['blue']*30)
        self.my_vitamins = 0

    def drawVitamins(self):
        np.random.shuffle(self.contents)
        vitamin_sample = self.contents[:4]
        np.delete(self.contents, np.arange(4))
        self.my_vitamins += sum(vitamin_sample == 'blue')

    def runSimulation(self):
        for i in range(15):
            self.drawVitamins()
        return self.my_vitamins
