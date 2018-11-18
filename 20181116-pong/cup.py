import numpy as np

class Cup:
    def __init__(self, num):
        self.num = num
        self.balls = []

    def add_ball(self, ball):
        self.balls.append(ball)

class CupSet:
    def __init__(self, N):
        self.N = N
        self.cups = [Cup(num=n) for n in range(N)]

    def add_random_ball(self):
        rnd_cup = np.random.choice(self.N)
        rnd_ball = np.random.choice(self.N)
        self.cups[rnd_cup].add_ball(rnd_ball)

    def check_all_full(self):
        for cup in self.cups:
            if len(cup.balls) == 0:
                return False
        return True

    def prune_cups(self):
        for i, cup in enumerate(self.cups):
            self.cups[i].balls = [ball for ball in cup.balls if ball == cup.num]
