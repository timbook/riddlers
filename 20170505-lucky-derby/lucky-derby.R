probs <- seq(0.52, 0.90, by = 0.02)

runDerby <- function(probs) {
  pos <- rep(0, 20)
  
  while (all(pos < 200)) {
    movs <- 2 * rbinom(20, 1, probs) - 1
    pos <- pos + movs
    pos <- ifelse(pos >= 0, pos, 0)
  }
  
  return(which(pos >= 200))
}

nraces <- 1e5

winners <- unlist(sapply(1:nraces, function(i) runDerby(probs)))

prop.table(table(winners)) * 100
