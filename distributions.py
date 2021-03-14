import matplotlib.pyplot as plt
from networkx.algorithms import *
import collections
import numpy as np

graphs = ['model/ER5000k8.net', 'model/SF_1000_g2.7.net', 'model/ws1000.net', 'real/airports_UW.net']
apply_log = [False,True,False,True]

for i,a in zip(graphs,apply_log):
    G = nx.Graph(nx.read_pajek(i))

    degree_sequence = sorted([d for n, d in G.degree()])  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    total_count = np.sum(cnt)

    kmin = np.min(deg)
    kmax = np.max(deg)

    log_k = np.log10(deg)

    log_kmin = np.log10(kmin)
    log_kmax = np.log10(kmax)

    print('log_kmin ', log_kmin)
    print('log_kmax ', log_kmax)

    x_bins = np.arange(log_kmin, np.log10(kmax+1), 0.1*(np.log10(kmax+1)-log_kmin))

    bins = np.zeros([10])

    for v in range(len(x_bins)-1):
        for l in range(len(log_k)):
            if log_k[l] >= x_bins[v] and log_k[l] < x_bins[v+1]:
                bins[v] += cnt[l]

    fig, ax = plt.subplots(2)

    print(bins)
    print(x_bins)
    true_x = [np.power(10, x_bins[i]) for i in range(len(x_bins))]
    div_bins = bins / total_count

    # PDF
    if a:
        #ax[0].bar(true_x, div_bins, color="b")
        ax[0].hist(log_k, bins=10)
    else:
        #ax[0].bar(deg, cnt, color="b")
        ax[0].hist(cnt, bins=10)
    ax[0].set_title("PDF")
    ax[0].set_ylabel("P(k)")
    ax[0].set_xlabel("k")

    # CCDF
    accumulated_bins = [np.sum(div_bins[0:i]) for i in range(1, len(bins)+1)]

    ax[1].set_title("CCDF")
    ax[1].set_ylabel("P(K>=k)")
    ax[1].set_xlabel("k")
    ax[1].bar(true_x, accumulated_bins / total_count, color="b")

    plt.show()