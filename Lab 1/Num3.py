import numpy as np
headcnt = 0  # This is my heads counter
succtest = 0 # this is my counter for the successful tests

for i in range(0, 100000):
    coin = np.random.randint(0, 2, 100)
    headcnt = sum(coin)
    if headcnt == 50:
        succtest += 1

print("Probability of 50 heads in tossing 100 fair coins: ", succtest / 100000)
