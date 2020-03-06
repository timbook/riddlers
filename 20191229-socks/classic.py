from sockdrawer import run_sim

N_SIMS = 100_000
sims = [run_sim(10) for _ in range(N_SIMS)]
mean_sims = sum(sims) / len(sims)
print(f"Average pulls for n = 10: {mean_sims}")
