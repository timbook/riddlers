from random import choices
from collections import deque

class Team:
    def __init__(self):
        if isinstance(self, Moonwalkers):
            self.name = "Moonwalkers"
        elif isinstance(self, Doubloons):
            self.name = "Doubloons"
        elif isinstance(self, Taters):
            self.name = "Taters"

    def sim_game(self):
        self.score = 0
        return sum([self.sim_inning() for _ in range(9)])

    def overtime_inning(self):
        self.score += self.sim_inning()

class Moonwalkers(Team):
    def sim_at_bat(self):
        # 40% walk, 60% strikeout
        return choices(["walk", "strikeout"], weights=[0.4, 0.6])[0] 

    def sim_inning(self):
        inning_score = 0
        inning_outs = 0
        bases = deque([0, 0, 0, 0])

        while inning_outs < 3:
            at_bat = self.sim_at_bat()
            if at_bat == "strikeout":
                inning_outs += 1
            elif at_bat == "walk":
                inning_score += bases.pop()
                bases.appendleft(1)

        return inning_score

class Doubloons(Team):
    def sim_at_bat(self):
        # 20% double, 80% strikeout
        return choices(["double", "strikeout"], weights=[0.2, 0.8])[0] 

    def sim_inning(self):
        inning_score = 0
        inning_outs = 0
        bases = deque([0, 0, 0, 0])

        while inning_outs < 3:
            at_bat = self.sim_at_bat()
            if at_bat == "strikeout":
                inning_outs += 1
            elif at_bat == "double":
                inning_score += bases.pop()
                inning_score += bases.pop()
                bases.extendleft([0, 1])

        return inning_score

class Taters(Team):
    def sim_at_bat(self):
        # 10% home run, 90% strikeout
        return choices(["homer", "strikeout"], weights=[0.1, 0.9])[0] 

    def sim_inning(self):
        inning_score = 0
        inning_outs = 0

        while inning_outs < 3:
            at_bat = self.sim_at_bat()
            if at_bat == "strikeout":
                inning_outs += 1
            elif at_bat == "homer":
                inning_score += 1

        return inning_score
