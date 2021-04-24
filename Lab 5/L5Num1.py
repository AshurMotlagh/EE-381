# Ashur Motlagh
# 018319910
import numpy as np
import matplotlib.pyplot as plt
import math
import random

def SSonConIntervals(N, mu, sig, n):
    NGD = np.random.normal(mu, sig, N)  # Normal Gaussian

    mean = []   # initializing list
    topof95 = []
    bottomof95 = []
    topof99 = []
    bottomof99 = []

    for i in range(0, n):
        count = i + 1
        x = NGD[random.sample(range(N), count)]
        mean.append(np.sum(x) / count)
        std = sig / math.sqrt(count)
        topof95.append(mu + 1.96 * std)  # append the values
        bottomof95.append(mu - 1.96 * std)
        topof99.append(mu + 2.58 * std)
        bottomof99.append(mu - 2.58 * std)

    list = [x for x in range(1, count + 1)]  # making new list with range from 1 to count + 1

    fig1 = plt.figure(1)
    plt.scatter(list, mean, c='Blue', marker='x')
    plt.plot(list, topof95, 'r--')
    plt.plot(list, bottomof95, 'r--')
    plt.title('Sample Means and 95% confidence Intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x_bar')

    fig2 = plt.figure(2)
    plt.scatter(list, mean, c='Blue', marker='x')
    plt.plot(list, topof99, 'g--')
    plt.plot(list, bottomof99, 'g--')
    plt.title('Sample Means and 99% confidence Intervals')
    plt.xlabel('Sample Size')
    plt.ylabel('x_bar')

    plt.show()


N = 1500000
mu = 55
sig = 5
n = 200
SSonConIntervals(N, mu, sig, n)
