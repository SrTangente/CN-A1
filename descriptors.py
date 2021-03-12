from os import listdir

import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from networkx.algorithms import *
import csv

for dir in ['/toy/', '/model/', '/real/']:
    for f in listdir(dir):
        net = nx.Graph(nx.read_pajek(dir+f))
        n_nodes = net.number_of_nodes()
        n_edges = (net.number_of_edges())
        node_list = list(net.nodes())

        degree_list = net.degree(node_list)
        degrees = [x[1] for x in net.degree(node_list)]

        average_dg = np.average(degrees)
        max_dg = np.max(degrees)
        min_dg = np.min(degrees)

        #print('Maximum degree: ', max_dg, ' Minimum degree: ', min_dg, ' Average degree: ', average_dg)

        avg_clustering = (approximation.average_clustering(net))
        clustering = clustering(net)

        assortativity = degree_assortativity_coefficient(net)
        svg_shortest_path_len = average_shortest_path_length(net)
        diameter= diameter(net)

        # TODO, write into CSV
