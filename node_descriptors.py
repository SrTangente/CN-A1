import networkx as nx
import numpy as np
from networkx.algorithms import approximation
from networkx.algorithms import *

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

net = nx.Graph(nx.read_pajek('./real/airports_UW.net'))


def eigenvector_centrality(G, nodes):
    dict = nx.eigenvector_centrality(G)
    return [dict[node] for node in nodes]

def pagerank(G, nodes):
    dict = nx.pagerank(G)
    return [dict[node] for node in nodes]

nodes = ['PAR', 'LON', 'FRA', 'AMS', 'MOW', 'CHI', 'NYC', 'ATL', 'BCN', 'WAW', 'CHC', 'DJE', 'ADA', 'AGU', 'TBO', 'ZVA']


nodes_strength = get_strenght(nodes, net)


print(eigenvector_centrality(net, nodes))
print(pagerank(net, nodes))


