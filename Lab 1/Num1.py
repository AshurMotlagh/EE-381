

import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt


def nSidedDie(p):
    listsum = 0
    length = len(p)
    checker = float(1.0)
    flag = True
    # print(np.size(p))

    for i in range(length):  # this gives us length of the list
        listsum += p[i]
    # print(listsum)  # this is for debugging

    if listsum > checker:
        print("WRONG, the sum of the list cannot be greater than 1!!!!!")
        flag = False

    if flag:  # if the flag is true we will continue
        testcase = 10000
        eList = []  #empty list to append to

        cs = np.cumsum(p)  # Return the cumulative sum of the elements along a given axis.
        sp = np.append(0, cs)
        r = random.random()

        for i in range(0, testcase):  # 0 - 10,000
            for j in range(0, length):  # 0 - size of p
                if r > sp[i] and r <= sp[j + 1]:
                    d = j + 1
                    eList.append(d)

        b = range(1, length + 2); sb = np.size(b)
        h1, bin_edges = np.histogram(eList, bins=b)

nSidedDie([0.10,  0.15,  0.20,  0.05,  0.30, 0.10, 0.10])
