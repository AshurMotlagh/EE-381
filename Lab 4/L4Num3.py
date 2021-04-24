# Ashur Motlagh
# 018319910
import numpy as np
import matplotlib.pyplot as plt

def exponentialRV(a,b,n,beta):
    batteries = 24  # the number of batteries needed to

    batteryList = np.zeros((n, 1))
    for i in range(0, n):
        t = np.random.exponential(beta, batteries)
        batteryList[i] = np.sum(t)

    mu = batteries * beta
    sig = beta * np.sqrt(batteries)

    nbins = 40;  # Number of bins
    edgecolor = 'w';  # Color separating bars in the bargraph

    bins = [float(x) for x in np.linspace(a, b, nbins + 1)]
    h1, bin_edges = np.histogram(batteryList, bins, density=True)
    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')

    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)

    plt.title('PDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('PDF')


    def gaussian(mu_x, sig_x, z):
        f = np.exp(-(z - mu_x) ** 2 / (2 * sig_x ** 2)) / (sig_x * np.sqrt(2 * np.pi))
        return f


    f = gaussian(mu, sig, b1)
    plt.plot(b1, f, 'r')

    fig2 = plt.figure(2)
    h2 = np.cumsum(h1) * barwidth
    plt.bar(b1, h2, width=barwidth, edgecolor=edgecolor)
    plt.title('CDF of lifetime of a 24 batteries carton')
    plt.xlabel('Lifetime of a 24 batteries carton')
    plt.ylabel('CDF')
    plt.show()


exponentialRV(300, 2000, 10000, 40)
