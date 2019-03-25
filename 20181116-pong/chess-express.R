library(ggplot2)

pointLookup <- c('W'=1, 'L'=0, 'D'=0.5)

runMatch <- function(N) {
  turnout <- sample(c('W', 'L', 'D'), size=N, replace=TRUE, prob=c(0.20, 0.15, 0.65))
  points <- sum(pointLookup[turnout])
  return((points > 6.5) * 1)
}

runMatchSim <- function(N) {
  sims <- sapply(1:10000, function(i) runMatch(N))
  return(mean(sims))
}

win_rates <- sapply(7:25, runMatchSim)

win_df <- data.frame(n=7:25, rate=win_rates)

ggplot(win_df) +
  theme_bw() +
  geom_line(aes(n, rate)) +
  geom_hline(yintercept=c(0.75, 0.9, 0.99), color='red')



