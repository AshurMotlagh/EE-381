# I used this as a resource for this lab - it gives us the binomial formula
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import binom


def calcsUsingBionomialDistrubutiuon(p):
    calc = p[0] * p[1] *p[2]
    b = range(0, 15+1)  # same range as num1

    bionomialFormula = binom.pmf(b, 1000, calc)  # range, number of times to roll

    plt.stem(b, bionomialFormula)   # plots range and prob
    plt.title('Bernoulli Trials: PMF – Binomial Formula')
    plt.xlabel('Number of successes')
    plt.ylabel('Probability')
    plt.xticks(b)  # same ticks as num1
    plt.show()


calcsUsingBionomialDistrubutiuon([0.2, 0.1, 0.15, 0.3, 0.2, 0.05])
