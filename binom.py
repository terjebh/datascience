import numpy as np 
from scipy import stats
from matplotlib import pyplot as pl

prob_flere = stats.binom_test(15,20,0.5)
prob_en = stats.binom.pmf(range(20),20,0.5)

print(prob_flere)

print(prob_en)



pl.scatter(range(20),prob_en)
pl.show()
