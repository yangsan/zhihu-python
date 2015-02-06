# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = np.loadtxt("count.txt")
    wz = np.loadtxt("wz.txt")
    #print data
    plt.hist(data, bins=100, alpha=0.5)
    plt.hist(wz, bins=100, alpha=0.5)
    plt.show()
