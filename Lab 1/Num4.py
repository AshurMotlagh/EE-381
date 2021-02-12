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


def passGuessing():
    elist = []
    succ = 0
    prob = 0.0
    nums = 90000

    # while prob < .49 or prob > .51:
    while True:

        for i in range(0, nums):
            hackerPass = ''.join(random.choice(letters) for i in range(4))
            elist.append(hackerPass)

        for j in range(0, 1000):
            realPass = ''.join(random.choice(letters) for i in range(4))
            if realPass in elist:
                succ += 1.0

        prob = succ/1000.0
        print(prob)

        if prob < .49:
            nums += 18000
            succ = 0.0
            print(1)
            elist = []
            continue
        elif prob > .510:
            nums = nums - 16000
            succ =0.0
            print(2)
            elist = []
            continue
        elif prob > .49 or prob < .51:
            break

    print(nums)





# print("Hacker creates m words:\nProb. that at least one of the words matches the password \np = ", passHacking1())
# print("--------------------------------------------------------------------------------------------------------")
# print("Hacker creates m*k words:\nProb. that at least one of the words matches the password \np = ", passHacking2())
# print("--------------------------------------------------------------------------------------------------------")
passGuessing()