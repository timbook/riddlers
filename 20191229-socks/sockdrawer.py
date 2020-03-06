from random import shuffle

class SockDrawer:
    def __init__(self, n):
        self.drawer = list(range(n)) * 2
        self.hand = []
        shuffle(self.drawer)

    def pull(self):
        new_sock = self.drawer.pop()
        self.hand.append(new_sock)

    def has_pair(self):
        return len(self.hand) != len(set(self.hand))

    @property
    def socks(self):
        return len(self.hand)

def run_sim(n):
    s = SockDrawer(n)
    while not s.has_pair():
        s.pull()
    return s.socks
