library(ggplot2)

pong = read.csv('pong-counts.csv')

pong['err_high'] = pong['means'] + pong['stds']
pong['err_low'] = pong['means'] - pong['stds']

p <- ggplot(pong) +
  theme_bw() +
  geom_ribbon(aes(x=N, ymin=err_low, ymax=err_high), fill='blue', alpha=0.1) +
  geom_smooth(aes(x=N, y=means),
              method='lm', se=FALSE,
              color='indianred', size=0.3) +
  geom_line(aes(x=N, y=means), color='darkblue') +
  labs(x='N', y='Expected Number Rounds')
p
  
ggsave(plot=p, filename='ggpong.png', dpi=300, width=8, height=5, units='in')
