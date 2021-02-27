import random
import numpy as np


def nSidedDie(p):  # same code from lab 1
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
        testcase = 1  # Only need one roll for this lab
        eList = []  # empty list to append to

        cs = np.cumsum(p)  # Cumulative Sum
        sp = np.append(0, cs)

        for i in range(0, testcase):  # 0 - 10,000
            r = random.random()
            for j in range(0, length):  # 0 - size of p
                if r > sp[j] and r <= sp[j + 1]:
                    d = j + 1
            eList.append(d)
    return d

def erronrousTransmission(p, e0, e1):
    cnt = 0  # counter for the amount of errors need to calculate

    for i in range(0,100000):  # loop from 0 - 100,000
        S = nSidedDie([p, 1 - p])  # generating (got from lab manual)
        S = S - 1

        if S == 1:
            R = nSidedDie([1-e1, e1])  # generating
            R = R - 1

        elif S == 0:
            R = nSidedDie([1 - e0, e0])  # generating
            R = R - 1

        if R != S:
            cnt = cnt + 1  # updating the counter

    prob = cnt / 100000  # getting the probability of errers
    return prob

print(erronrousTransmission(.6,.05,.03))
