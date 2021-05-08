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

def markov(n):
    S = []
    initial = [1/4, 0, 3/4]
    stm1 = [1/2, 1/4, 1/4]
    stm2 = [1/4, 1/8, 5/8]
    stm3 = [1/3, 2/3, 0]
    for i in range(n):  # 15 steps
        r = nSidedDie(initial)
        S.append(r)
    print("Initial states", S)
    for k in range(1, n):
        if S[k - 1] == 0:
            S[k] = nSidedDie(stm1)
        elif S[k - 1] == 1:
            S[k] = nSidedDie(stm2)
        else:
            S[k] = nSidedDie(stm3)
    b = list(range(0, len(S)))
    print("Final states", S)
    plt.title("A sample simulation run of a three-state Markov Chain")
    plt.xlabel("Step Number")
    plt.ylabel("State")
    plt.plot(b, S, 'm:')
    plt.plot(b, S, 'bo', label="State")
    plt.legend()
    plt.show()


def markov_thousand(n ,N):
    initial = [1/4, 0, 3/4]
    stm1 = [1/2, 1/4, 1/4]
    stm2 = [1/4, 1/8, 5/8]
    stm3 = [1/3, 2/3, 0]
    # stm1 = [1/2, 1/4, 1/4]
    # stm2 = [1/2, 0, 1/2]
    # stm3 = [1/4, 1/4, 1/2]
    P = np.matrix([stm1, stm2, stm3])
    S = np.zeros((n, 3))
    S[0, :] = initial
    for k in range(1, n):
        S[k, :] = S[k - 1, :] * P
    b = list(range(0, n))
    plt.plot(b, S[:, 0], 'b--*', label='Rain')
    plt.plot(b, S[:, 1], 'g--o', label='Nice')
    plt.plot(b, S[:, 2], 'r--h', label='Snow')
    plt.title("Three-state Markov Chain With State Transition Matrix")
    plt.xlabel("Step")
    plt.ylabel("State")
    plt.legend()
    plt.show()

    M = np.zeros((n, 3))
    S = np.array(np.zeros((n, N)))
    for k in range(0, N):
        r = nSidedDie(initial)
        S[0, k] = r

    for k in range(0, N):
        for j in range(1, n):
            current = S[j - 1, k]
            if current  == 0:
                r = nSidedDie(stm1)
            elif current  == 1:
                r = nSidedDie(stm2)
            else:
                r = nSidedDie(stm3)
            S[j, k] = r
    for j in range(0, n):
        u = S[j, :]
        r = 0
        n = 0
        s = 0
        for k in range(0, N):
            if u[k] == 0:
                r += 1
            elif u[k] == 1:
                n += 1
            else:
                s += 1
        M[j, :] = [r / N, n / N, s / N]
    plt.plot(M[:, 0], 'b--*', label='Rain')
    plt.plot(M[:, 1], 'g--o', label='Nice')
    plt.plot(M[:, 2], 'r--+', label='Snow')
    plt.title('Three-state Markov Chain Without State Transition Matrix')
    plt.xlabel('Step')
    plt.ylabel('State')
    plt.legend()
    plt.show()


markov(15)
markov_thousand(15, 10000)
