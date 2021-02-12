import random
import string
letters = string.ascii_lowercase

m = 80000
k = 7


def passHacking1():
    elist = []
    succ = 0
    for i in range(0,m):
        hackerPass = ''.join(random.choice(letters) for i in range(4))
        elist.append(hackerPass)

    for j in range(0,1000):
        realPass = ''.join(random.choice(letters) for i in range(4))
        if realPass in elist:
            succ += 1

    print(succ/1000)


def passHacking2():
    elist = []
    succ = 0
    for i in range(0,m*k):
        hackerPass = ''.join(random.choice(letters) for i in range(4))
        elist.append(hackerPass)

    for j in range(0,1000):
        realPass = ''.join(random.choice(letters) for i in range(4))
        if realPass in elist:
            succ += 1

    print(succ/1000)


print("Hacker creates m words:\nProb. that at least one of the words matches the password \np = ", passHacking1())
print("--------------------------------------------------------------------------------------------------------")
print("Hacker creates m*k words:\nProb. that at least one of the words matches the password \np = ", passHacking2())
print("--------------------------------------------------------------------------------------------------------")

