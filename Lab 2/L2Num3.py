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

def conditionalProb2(p,e0,e1):
    succ = 0
    rec = 0

    for i in range(0,100000):  # loop from 0 - 100,000
        S = nSidedDie([p, 1-p])  # generating
        S = S - 1

        if S ==1:
            R = nSidedDie([e1, 1-e1])  # generating
            R = R - 1
        else:
            R = nSidedDie([1-e0, e0])  # generating
            R = R - 1

        if R == 1:
            rec = rec + 1
            if S == 1:
                succ = succ + 1

    conProb = (succ / rec)  # this is to get probability
    return conProb

print(conditionalProb2(.6, .05, .03))
