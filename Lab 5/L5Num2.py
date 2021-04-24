import numpy as np
import math
import random

def problem2(b, N, mu, trials, t95, t99, size):
    successZ95 = 0  # Initialize variables.
    successZ99 = 0
    successT95 = 0
    successT99 = 0
    sample = size

    for z in range(0, trials):
        y = b[random.sample(range(N), sample)]
        yMean = np.sum(y) / sample
        total = 0
        for a in range(0, len(y)):
            total = total + (y[a] - yMean) ** 2
        yS = total / (sample - 1)
        yS = math.sqrt(yS)
        yStd = yS / math.sqrt(sample)

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


B = np.random.normal(55, 5, 1500000)
problem2(B, 1500000, 55, 10000, 2.78, 4.6, 5)
problem2(B, 1500000, 55, 10000, 2.02, 2.7, 40)
problem2(B, 1500000, 55, 10000, 1.98, 2.62, 120)
