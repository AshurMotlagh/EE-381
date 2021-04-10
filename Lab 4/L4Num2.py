# Ashur Motlagh
# 018319910
import numpy as np
import matplotlib.pyplot as plt

def centralLimitTheorem(a,b,n):
    X = [None] * 10000
    for i in range(0, 10000):
        w = np.random.uniform(a, b, n)
        X[i] = np.sum(w)

    mu_x = np.mean(X)
    sig_x = np.std(X)

    print('mean:', mu_x)
    print('std:', sig_x)

    # Create bins and histogram
    nbins = 30  # Number of bins
    edgecolor = 'w'  # Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(n * a, n * b, nbins + 1)]
    h1, bin_edges = np.histogram(X, bins, density=True)

    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')

    # PLOT THE BAR GRAPH
    fig1 = plt.figure(1)
    plt.bar(b1, h1, width=barwidth, edgecolor=edgecolor)
    label = 'Book stack height for n = %d' % n
    plt.title('PDF of %d book stack height and comparison with Gaussian' % n)
    plt.xlabel(label)
    plt.ylabel('PDF')

    def gaussian(mu, sig, z):
        f = np.exp(-(z - mu_x) ** 2 / (2 * sig_x ** 2)) / (sig_x * np.sqrt(2 * np.pi))
        return f

    f = gaussian(mu_x * n, sig_x * np.sqrt(n), b1)
    plt.plot(b1, f, 'r')
    plt.show()


centralLimitTheorem(1.0, 4.0, 1)
centralLimitTheorem(1.0, 4.0, 5)
centralLimitTheorem(1.0, 4.0, 15)
