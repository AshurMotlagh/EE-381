import numpy as np
import matplotlib.pyplot as plt
import math as m
import random as r

def problem2(b, N, mu, trials, t95, t99, size):
    successZ95 = 0
    successZ99 = 0
    successT95 = 0
    successT99 = 0
    sample = size
    for z in range(0, trials):
        y = b[r.sample(range(N), sample)]
        yMean = np.sum(y) / sample
        total = 0
        for a in range(0, len(y)):
            total = total + (y[a] - yMean) ** 2
        yS = total / (sample - 1)
        yS = m.sqrt(yS)
        yStd = yS / m.sqrt(sample)

        yTop95 = yMean + 1.96 * yStd
        yBottom95 = yMean - 1.96 * yStd
        yTop99 = yMean + 2.58 * yStd
        yBottom99 = yMean - 2.58 * yStd

        tTop95 = yMean + t95 * (yStd)
        tBottom95 = yMean - t95 * (yStd)
        tTop99 = yMean + t99 * (yStd)
        tBottom99 = yMean - t99 * (yStd)

        if yBottom95 <= mu and yTop95 >= mu:
            successZ95 += 1
        if yBottom99 <= mu and yTop99 >= mu:
            successZ99 += 1
        if tBottom95 <= mu and tTop95 >= mu:
            successT95 += 1
        if tBottom99 <= mu and tTop99 >= mu:
            successT99 += 1

    print('Success Rate using normal, sample = %d,' % sample, '95% confidence interval')
    print(successZ95 / trials * sample)
    print('Success Rate using normal, sample = %d,' % sample, '99% confidence interval')
    print(successZ99 / trials * sample)
    print('Success Rate using student t, sample = %d,' % sample, '95% confidence interval')
    print(successT95 / trials * sample)
    print('Success Rate using student t, sample = %d,' % sample, '99% confidence interval')
    print(successT99 / trials * sample)
    print('')

trials = 10000
N = 1500000
mu = 55
sig = 5
n = 200
B = np.random.normal(mu, sig, N)
problem2(B, N, mu, trials, 2.78, 4.6, 5)
problem2(B, N, mu, trials, 2.02, 2.7, 40)
problem2(B, N, mu, trials, 1.98, 2.62, 120)