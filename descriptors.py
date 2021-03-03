import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from networkx.algorithms import *

net = nx.Graph(nx.read_pajek('./toy/star.net'))
print(net.number_of_nodes())
print(net.number_of_edges())
node_list = list(net.nodes())
print(net.degree(node_list))
degrees = [x[1] for x in net.degree(node_list)]
average_dg = np.average(degrees)
max_dg = np.max(degrees)
min_dg = np.min(degrees)

print('Maximum degree: ', max_dg, ' Minimum degree: ', min_dg, ' Average degree: ', average_dg)

print(approximation.average_clustering(net))
print(clustering(net))

print(degree_assortativity_coefficient(net))
print(average_shortest_path_length(net))
print(diameter(net))
