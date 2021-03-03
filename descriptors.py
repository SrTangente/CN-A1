import networkx
from networkx import *

toy_nets = []
star = networkx.read_pajek('./toy/star.net')
print(star.number_of_nodes())
print(star.number_of_edges())
node_list = list(star.nodes())
degree