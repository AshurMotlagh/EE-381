# Ashur Motlagh
# 018319910
import numpy as np
import matplotlib.pyplot as plt
import math
import random

def SSonConIntervals(N, mu, sig, n):
    B = np.random.normal(mu, sig, N)


N = 1500000
mu = 55
sig = 5
n = 200
SSonConIntervals(N, mu, sig, n)
