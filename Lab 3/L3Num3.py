# I used this as a resource for this lab - it gives us the binomial formula
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html#scipy.stats.poisson

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson  # imports poisson from package


def approximationBiomialPoissonDist(p,):
    n = 1000
    lp = p[0] * p[1] *p[2]  # lambda of p
    lambda_ = n * lp  # lambda = n * p
    b = range(1, 15+1)  # same as num 1 and 2

    poisson_ = poisson.pmf(b, lambda_)  # this does poisson calculation for us

    plt.stem(b, poisson_)  # plots range and prob
    plt.title('Bernoulli Trials: PMF – Poisson Approximation')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.xticks(b)  # same ticks as num1 & num2
    plt.show()


approximationBiomialPoissonDist([0.2, 0.1, 0.15, 0.3, 0.2, 0.05])