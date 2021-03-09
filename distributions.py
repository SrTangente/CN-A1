import matplotlib.pyplot as plt
from networkx.algorithms import *
import collections
import numpy as np

graphs = ['model/ER5000k8.net','model/SF_1000_g2.7.net','model/ws1000.net','real/airports_UW.net']

for i in graphs:
    G = nx.Graph(nx.read_pajek(i))

    degree_sequence = sorted([d for n, d in G.degree()])  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    total_count = np.sum(cnt)

    kmin = np.min(deg)
    kmax = np.max(deg)

    log_k = np.log(deg)

    log_kmin = np.log(kmin)
    log_kmax = np.log(kmax)

    print('log_kmin ', log_kmin)
    print('log_kmax ', log_kmax)

    x_bins = np.arange(log_kmin, np.log(kmax+1), 0.1*(np.log(kmax+1)-log_kmin))

    bins = np.zeros([10])

    for v in range(len(x_bins)-1):
        for l in range(len(log_k)):
            if log_k[l] >= x_bins[v] and log_k[l] < x_bins[v+1]:
                bins[v] += cnt[l]

    fig, ax = plt.subplots()

    print(bins)
    print(x_bins)

    plt.bar(bins/total_count, x_bins, color="b")

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")


    '''plt.bar(deg, cnt, width=0.80, color="b")

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)'''

    plt.show()