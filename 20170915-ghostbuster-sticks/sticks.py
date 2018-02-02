import numpy as np

# Question 1: If you break the stick in two places at random,
# forming 3 pieces, what is the probability of being able to
# form a triangle with the pieces?

def isTriangle():
    stick_cuts = sorted(np.random.rand(2))
    stick1 = stick_cuts[0]
    stick2 = stick_cuts[1] - stick_cuts[0]
    stick3 = 1 - stick_cuts[1]

    side_check = []
    side_check.append(stick1 > stick2 + stick3)
    side_check.append(stick2 > stick1 + stick3)
    side_check.append(stick3 > stick1 + stick2)

    return(np.all(side_check))

ITER = int(1e5)
num_triangles = np.zeros(ITER)
for i in range(ITER):
    num_triangles[i] = isTriangle()
#num_triangles = [isTriangle() for i in range(1e5)]
print(np.mean(num_triangles))
