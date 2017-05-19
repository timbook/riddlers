probs <- c(A = 0.10, B = 0.15, C = 0.20, D = 0.25)

runCarPool <- function(i) {
  drivers <- c('A', 'B', 'C', 'D')
  tickets <- c(A = 0, B = 0, C = 0, D = 0)
  days <- 0
  
  while (TRUE) {
    # Morning driver
    this_driver <- sample(drivers, 1)
    ticked <- rbinom(1, 1, probs[this_driver])
    tickets[this_driver] <- tickets[this_driver] + ticked
    
    if (tickets[this_driver] >= 3) {
      drivers <- setdiff(drivers, this_driver)
      if (length(drivers) == 0) return(days)
    }
    
    # Evening driver
    this_driver <- sample(drivers, 1)
    ticked <- rbinom(1, 1, probs[this_driver])
    tickets[this_driver] <- tickets[this_driver] + ticked
    
    if (tickets[this_driver] >= 3) {
      drivers <- setdiff(drivers, this_driver)
      if (length(drivers) == 0) return(days)
    }
    
    # Increase days
    days <- days + 1
  }
}

ITERS <- 1e4
days_distn <- sapply(1:ITERS, runCarPool)
summary(days_distn)
