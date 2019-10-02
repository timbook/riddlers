from teams import Moonwalkers, Doubloons, Taters

def sim_game(t1, t2):
    t1.sim_game()
    t2.sim_game()

    while t1.score == t2.score:
        t1.overtime_inning()
        t2.overtime_inning()

    return t1.name if t1.score > t2.score else t2.name

N_GAMES = 20000
m_wins, d_wins, t_wins = 0 , 0 , 0

# Moonwalkers vs Doubloons
m_vs_d = [sim_game(Moonwalkers(), Doubloons()) for _ in range(N_GAMES)]

# Moonwalkers vs Taters
m_vs_t = [sim_game(Moonwalkers(), Taters()) for _ in range(N_GAMES)]

# Doubloons vs Taters
d_vs_t = [sim_game(Doubloons(), Taters()) for _ in range(N_GAMES)]

all_games = m_vs_d + m_vs_t + d_vs_t
m_wins = all_games.count("Moonwalkers")
d_wins = all_games.count("Doubloons")
t_wins = all_games.count("Taters")

print("="*20 + " RESULTS " + "="*20)
print("Moonwalkers: {} wins ({:.2f}% win rate)".format(m_wins, 100*m_wins/(2*N_GAMES)))
print("Doubloons: {} wins ({:.2f}% win rate)".format(d_wins, 100*d_wins/(2*N_GAMES)))
print("Taters: {} wins ({:.2f}% win rate)".format(t_wins, 100*t_wins/(2*N_GAMES)))
