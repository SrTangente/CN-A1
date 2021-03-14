from os import listdir

import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from networkx.algorithms import *

import os
import pandas as pd

files = ['model','real','toy']
df = pd.DataFrame(columns=['Graph', 'n_nodes', 'n_edges', 'min_degree', 'max_degree', 'av_degree', 'clustering_cof', 'assortativity',
             'av_path_length', 'diameter'])

for f in files:
    graphs = os.listdir(f)
    for g in graphs:
        print(g)
        path = './'+f+'/'+g

        net = nx.Graph(nx.read_pajek(path))

        d = dict()
        d['Graph'] = g
        d['n_nodes'] = net.number_of_nodes()
        d['n_edges'] = net.number_of_edges()


        node_list = list(net.nodes())

        degrees = [x[1] for x in net.degree(node_list)]
        average_dg = np.average(degrees)
        max_dg = np.max(degrees)
        min_dg = np.min(degrees)

        d['min_degree'] = round(min_dg,4)
        d['max_degree'] = round(max_dg,4)
        d['av_degree'] =  round(average_dg,4)

        #print('Maximum degree: ', max_dg, ' Minimum degree: ', min_dg, ' Average degree: ', average_dg)

        d['clustering_cof'] = round(approximation.average_clustering(net),4)
        d['assortativity'] = round(degree_assortativity_coefficient(net),4)
        d['av_path_length'] = round(average_shortest_path_length(net),4)
        d['diameter'] = round(diameter(net),4)


        df = df.append(d, ignore_index=True)
        df.to_csv('descriptors.csv', index=False)

