source('functions.R')

runSim <- function(dummy) {
  p1 <- runif(2)
  p2 <- c(runif(1, -1, 0), runif(1))
  p3 <- runif(2, -1, 0)
  p4 <- c(runif(1), runif(1, -1, 0))
  is_convex(p1, p2, p3, p4)
}

ITER <- 1e5
num_convex <- sapply(1:ITER, runSim)
mean(num_convex)
