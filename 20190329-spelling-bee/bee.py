import random

N_BEES = 100000
ME_FIRST = False

class Speller:
    def __init__(self, p):
        self.p = p
        self.me = False
        self.inplay = True

    def spell(self):
        rnd = random.random()
        if rnd < self.p:
            self.inplay = False

def make_spellers(me_first):
    spellers = [Speller(0.01*i) for i in range(1, 11)]
    spellers[0].me = True
    if not me_first:
        spellers.reverse()
    return spellers

def n_remaining(spellers):
    return len([sp for sp in spellers if sp.inplay])

def cull_spellers(spellers):
    return [sp for sp in spellers if sp.inplay]

def did_i_win(spellers):
    return len(spellers) == 1 and spellers[0].me

def run_bee(me_first=True):
    spellers = make_spellers(me_first)
    
    while len(spellers) != 1:
        for i, sp in enumerate(spellers):
            if spellers[i].inplay:
                spellers[i].spell()
                if n_remaining(spellers) == 1:
                    break
        spellers = cull_spellers(spellers)
    return True if did_i_win(spellers) else False

if __name__ == '__main__':
    bees = [run_bee(ME_FIRST) for _ in range(N_BEES)]
    win_rate = sum(bees) / len(bees)
    print(f"WIN RATE: {win_rate}")
