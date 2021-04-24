# Ashur Motlagh
# 018319910
import numpy as np
import math
import random


def problem2(sig, N, mu, trials, t95, t99, size):
    NGD = np.random.normal(mu, sig, N)  # Normal Gaussian Distribution

    success95 = 0  # Initialize variables.
    success99 = 0
    _success95 = 0  # for t
    _success99 = 0  # for t

    for i in range(0, trials):
        x = NGD[random.sample(range(N), size)]  # size will change according to instructions
        mean = np.sum(x) / size  # calculate mean
        total = 0
        for j in range(0, len(x)):
            total = total + (x[j] - mean) ** 2
        s = total / (size - 1)
        s = math.sqrt(s)
        std = s / math.sqrt(size)  # create / calculate standard deviation

        # Normal
        top95 = mean + 1.96 * std
        bottom95 = mean - 1.96 * std
        top99 = mean + 2.58 * std
        bottom99 = mean - 2.58 * std

        # Students t
        _top95 = mean + t95 * std
        _bottom95 = mean - t95 * std
        _top99 = mean + t99 * std
        _bottom99 = mean - t99 * std

        # Success Counters for normal
        if bottom95 <= mu <= top95:
            success95 += 1
        if bottom99 <= mu <= top99:
            success99 += 1

        # For Student's t
        if _bottom95 <= mu <= _top95:
            _success95 += 1
        if _bottom99 <= mu <= _top99:
            _success99 += 1

    print("Success Rate using normal, size = ", size, " with 95% confidence interval")
    print(success95 / trials * size)
    print("Success Rate using normal, size = ", size, " with 99% confidence interval")
    print(success99 / trials * size)
    print("Success Rate using student t, size = ", size, " with 95% confidence interval")
    print(_success95 / trials * size)
    print("Success Rate using student t, size = ", size, " with 99% confidence interval")
    print(_success99 / trials * size, "\n")


problem2(5, 1500000, 55, 10000, 2.78, 4.6, 5)
problem2(5, 1500000, 55, 10000, 2.02, 2.7, 40)
problem2(5, 1500000, 55, 10000, 1.98, 2.62, 120)
