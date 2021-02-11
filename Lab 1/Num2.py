import numpy as np
import matplotlib
import matplotlib.pyplot as plt

goal = 7  # goal of this code is to get to the number 7!
cnt = 0  # this is my counter
eList = []

cnt2 = 0  # this is for tracking the rolls it takes to get to seven
while cnt < 100000:
    d1 = np.random.randint(1, 7)  # referenced this code from SUM OF THE ROLLS OF TWO FAIR DICE
    d2 = np.random.randint(1, 7)  # referenced this code from SUM OF THE ROLLS OF TWO FAIR DICE
    sum = d1 + d2  # referenced this code from SUM OF THE ROLLS OF TWO FAIR DICE
    cnt2 += 1
    if sum == goal:
        eList.append(cnt2)
        cnt2 = 0  # reset the counter
    cnt += 1  # this is to break out of the while loop

print(eList)
b = range(1, 22)
sb = np.size(b)
h1, bin_edges = np.histogram(eList, bins=b)
b1 = bin_edges[0:sb - 1]
plt.close('all')

plt.figure(1)
plt.stem(b1, h1)
plt.title('Number of rolls needed to get a "7" with two dice')
plt.xlabel('Number of rolls')
plt.ylabel('Number of rolls it takes until you get a sum of "7"')
plt.xticks(b1)
plt.show()
