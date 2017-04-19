library(plyr)
library(dplyr)

scotus <- c()
df <- data.frame()

ITER <- 1e4
for (t in 0:ITER) {
  if (t %% 2 == 0) senate <- sample(c('R', 'D'), 1)
  if (t %% 4 == 0) president <- sample(c('R', 'D'), 1)
  
  scotus <- scotus - 1
  scotus <- scotus[scotus != 0]
  
  if (length(scotus) < 9 & (senate == president)) {
    num_replace <- 9 - length(scotus)
    for (i in 1:num_replace) {
      new_scotus <- sample(0:40, 1)
      scotus <- c(scotus, new_scotus)
    }
  }
  
  df_add <- data.frame(time = t,
                       president = president,
                       senate = senate,
                       n_scotus = length(scotus))
  
  df <- rbind.fill(df, df_add)
}

df %>% 
  filter(time >= 1000) %>% 
  summarise(e_vacancies = 9 - mean(n_scotus))

table(df[df$time >= 1000, 'n_scotus'])
