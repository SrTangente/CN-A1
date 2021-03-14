import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from networkx.algorithms import *
import pandas as pd

def get_strenght(node_list, G):
    strength_dict = {}
    for node in node_list:
        edges_list = G.edges(node)
        strength = 0
        for edge in edges_list:
            strength += net[edge[0]][edge[1]]['weight']
        strength_dict[node] = strength
    return strength_dict

def average_path_length(node_list, G):
    average_list = list()
    for node in node_list:
        average_list.append(np.mean(list(nx.single_source_shortest_path_length(G, node).values())))
    return average_list

def maximum_path_length(node_list, G):
    average_list = list()
    for node in node_list:
        average_list.append(np.max(list(nx.single_source_shortest_path_length(G, node).values())))
    return average_list

def betweenness(node_list,G):
    bet = list()
    bet_dict = nx.betweenness_centrality(G)
    for node in node_list:
        bet.append(bet_dict[node])
    return bet

def eigenvector_centrality(G, nodes):
    dict = nx.eigenvector_centrality(G)
    return [dict[node] for node in nodes]

def pagerank(G, nodes):
    dict = nx.pagerank(G)
    return [dict[node] for node in nodes]


nodes = ['PAR', 'LON', 'FRA', 'AMS', 'MOW', 'CHI', 'NYC', 'ATL', 'BCN', 'WAW', 'CHC', 'DJE', 'ADA', 'AGU', 'TBO', 'ZVA']
net = nx.Graph(nx.read_pajek('./real/airports_UW.net'))
# Descriptors of the nodes
degree_list = net.degree(nodes)
nodes_strength = get_strenght(nodes, net)
clustering = clustering(net, nodes)
avg_path_len = average_path_length(nodes, net)
max_path_len = maximum_path_length(nodes, net)
betweeness = betweenness(nodes, net)
eigen_centrality = eigenvector_centrality(net, nodes)
pagerank = pagerank(net, nodes)

df = pd.DataFrame(columns=['Airport', 'Degree', 'Strength', 'Clustering coff', 'av_path_length', 'max_path_length', 'Betweenes', 'Eigenvector centrality',
             'Pagerank'])

for i,n in enumerate(nodes):
    d = dict()
    print(n)
    d['Airport'] = n
    d['Degree'] = round(degree_list[n],8)
    d['Strength'] = round(nodes_strength[n],8)
    d['Clustering coff'] = round(clustering[n],8)
    d['av_path_length'] = round(avg_path_len[i],8)
    d['max_path_length'] = round(max_path_len[i],8)
    d['Betweenes'] = round(betweeness[i],8)
    d['Eigenvector centrality'] = round(eigen_centrality[i],8)
    d['Pagerank'] = round(pagerank[i],8)
    df = df.append(d, ignore_index=True)

df.to_csv('node_descriptors.csv', index=False)