library(dplyr)
library(ggplot2)

runSim <- function(i, p) {
  cells <- 1
  while (TRUE) {
    cells <- sum(2*rbinom(cells, 1, p))
    if (cells == 0) return(TRUE)
    if (cells > 1000) return(FALSE)
  }
}

p_index <- seq(0.001, 1, 0.001)

runAggSim <- function(p) mean(sapply(1:1e3, function(i) runSim(i, p)))

probs <- sapply(p_index, runAggSim)

truep <- sapply(p_index, function(p) min(1, (1 - p)/p))

df <- data.frame(p_index, probs, truep)

pl <- ggplot(df) +
  theme_minimal() +
  geom_line(aes(p_index, truep), color = 'red', size = 3, alpha = 1/2) +
  geom_line(aes(p_index, probs), size = 1/4) +
  xlab('p') + ylab('Probability of Extinction')
