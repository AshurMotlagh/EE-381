import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def experimentalBernoulliTrails(p):
    trials = 10000  # number of trials
    dieFace = [1,2,3,4,5,6]  # the faces of a six sided die
    X = 0  # number of "successes" in n rolls
    x = []  # will hold 0 and 1, 0 if fail and 1 if success

    for i in range(0,trials):
        X = 0  # need to change back to 0 to indicate it is a fail naturaly
        die = np.random.choice(dieFace, 1000, p)  # need 3 die rolling 1000 times each
        die2 = np.random.choice(dieFace, 1000, p)
        die3 = np.random.choice(dieFace, 1000, p)
        for j in range(0,1000):  # embedded for loop we are checking the chance that the die roll 1 ,2, 3
            if die[j] == 1 and die2[j] == 2 and die3[j] == 3:
                X += 1  # so if this statement is true it counts as a success!!!
        x.append(X)

    b = range(0, 20)
    sb = np.size(b)
    h1, bin_edges = np.histogram(x, bins=b)
    b1 = bin_edges[0:sb - 1]
    plt.close('all')

    prob = h1 / 10000  # this is to get the probability
    plt.stem(b1, prob)

    # labels referenced from the lab
    plt.title('Bernoulli Trials: PMF - Experimental Results')
    plt.xlabel('Number of successes in n = 1000 trials')
    plt.ylabel('Probability')
    plt.xticks(b1)
    plt.show()


experimentalBernoulliTrails([0.2, 0.1, 0.15, 0.3, 0.2, 0.05])
