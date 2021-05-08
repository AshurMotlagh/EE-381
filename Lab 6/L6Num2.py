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
    return d - 1


def GooglePageRank(n):
    stm0 = [0, 1, 0, 0, 0]          # A
    stm1 = [0.5, 0, 0.5, 0, 0]      # B
    stm2 = [1/3, 1/3, 0, 0, 1/3]    # C
    stm3 = [1, 0, 0, 0, 0]          # D
    stm4 = [0, 1/3, 1/3, 1/3, 0]    # E
    P = np.matrix([stm0, stm1, stm2, stm3, stm4])  # make into matrix

    V = [[1/5, 1/5, 1/5, 1/5, 1/5], [0, 0, 0, 0, 1]]  # Define initial

    for i in range(2):
        transposed = np.transpose(V[i])
        P2 = V[i]
        temp = [V[i]]

        for num in range(n):
            P2 = np.matmul(P2,P)
            metadata = P2.tolist()[0]
            temp.append(metadata)

        data = np.transpose(temp).tolist()
        plt.figure("2")
        plt.title("Calculated Five-state Markov State with initial vector: '{}'".format(V[i]))
        plt.xlabel("Step Number")
        plt.ylabel("Probability")
        x = range(n+1)
        plt.plot(x,data[0],'ko',LINESTYLE='--', label='A')
        plt.plot(x,data[1],'bo',LINESTYLE='--', label='B')
        plt.plot(x,data[2],'go',LINESTYLE='--', label='C')
        plt.plot(x,data[3],'yo',LINESTYLE='--', label='D')
        plt.plot(x,data[4],'ro',LINESTYLE='--', label='E')
        plt.legend(loc='upper right')
        plt.show()

        print("Probabilities for intial vector {}".format(V[i]))
        results = [(str(x[-1])[:6],data.index(x)) for x in data]
        print(sorted(results,reverse=True))
        getPrinted = [print("State: {} Probability: {}".format(x[1],x[0])) for x in sorted(results, reverse=True)]


GooglePageRank(20)
