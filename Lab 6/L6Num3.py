# Ashur Motlagh
# 018319910
import numpy as np
import matplotlib.pyplot as plt
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

def drunkardWalk(n):
    S = []  # empty list
    initial = [0, 1/3, 1/3, 1/3, 0]
    mat0 = [1, 0, 0, 0, 0]
    mat1 = [0.3, 0, 0.7, 0, 0]
    mat2 = [0, 0.5, 0, 0.5, 0]
    mat3 = [0, 0, 0.6, 0, 0.4]
    mat4 = [0, 0, 0, 0, 1]


    for i in range(n):
        r = nSidedDie(initial)
        S.append(r)
    print("Initial states:", S)

    for k in range(1, n):
        if S[k - 1] == 0:
            S[k] = nSidedDie(mat0)
        elif S[k - 1] == 1:
            S[k] = nSidedDie(mat1)
        elif S[k - 1] == 2:
            S[k] = nSidedDie(mat2)
        elif S[k - 1] == 3:
            S[k] = nSidedDie(mat3)
        else:
            S[k] = nSidedDie(mat4)

    print("Final states:", S)
    b = list(range(0, len(S)))
    plt.title("A sample simulation run of Drunkard's Walk")
    plt.xlabel("Step Number")
    plt.ylabel("State")
    plt.plot(b, S, 'c:')
    plt.plot(b, S, 'bo', label="State")
    plt.legend()
    plt.show()


drunkardWalk(15)

