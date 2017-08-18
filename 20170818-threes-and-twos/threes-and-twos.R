sq <- c(3, 3, 3, 2)

ITER <- 1e5
for (i in 2:ITER) {
  sq <- c(sq, rep(3, sq[i]), 2)
}

table(sq)
prop.table(table(sq))

cum_mean <- cummean(sq - 2)

plot(cum_mean[1:300], type = 'l')
summary(cum_mean)
