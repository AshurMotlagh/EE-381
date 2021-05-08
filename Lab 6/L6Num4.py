import numpy as np
import random

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
    return d -1

def ProbAbsorption(N, n):
    temp1 = 0
    temp2 = 0
    S = []
    initial = [0, 0, 1, 0, 0]
    stm0 = [1, 0, 0, 0, 0]
    stm1 = [0.3, 0, 0.7, 0, 0]
    stm2 = [0, 0.5, 0, 0.5, 0]
    stm3 = [0, 0, 0.6, 0, 0.4]
    stm4 = [0, 0, 0, 0, 1]
    for i in range(N):
        for j in range(n):
            r = nSidedDie(initial)
            S.append(r)
        for k in range(1, n): # using nSidedDie
            if S[k - 1] == 0:
                S[k] = nSidedDie(stm0)
            elif S[k - 1] == 1:
                S[k] = nSidedDie(stm1)
            elif S[k - 1] == 2:
                S[k] = nSidedDie(stm2)
            elif S[k - 1] == 3:
                S[k] = nSidedDie(stm3)
            else:
                S[k] = nSidedDie(stm4)

        if 4 in S:
            temp1 += 1
        elif 0 in S:
            temp2+= 1
        S = []
    print("P(ending at b_20) = ", temp1 / N)
    print("P(ending at b_24) = ", temp2 / N)


ProbAbsorption(10000,15)
