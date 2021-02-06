import numpy as np
from numpy import random
import matplotlib
import matplotlib.pyplot as plt
#
def sum2dice(N):
    d1=random.randint(1,7,N)
    d2=random.randint(1,7,N)
    s=d1+d2
    b=range(1,15) ; sb=plt.size(b)
    h1, bin_edges = np.histogram(s,bins=b)
    b1=bin_edges[0:sb-1]
    plt.close('all')
    #
    fig1=plt.figure(1)
    plt.stem(b1,h1)
    plt.title('Stem plot - Sum of two dice')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Number of occurrences')
    fig1.savefig('1 EE381 Proj Stoch Exper-1.jpg') #
    fig2=plt.figure(2)
    p1=h1/N
    plt.stem(b1,p1)
    plt.title('Stem plot - Sum of two dice: Probability mass function')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')