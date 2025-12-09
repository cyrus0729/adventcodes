import numpy as np
from scipy.spatial import KDTree
import networkx as nx

import matplotlib.pyplot as plt
import iplotx as ipx

txt = open(r"D:\Users\cyrus\Desktop\code stuff\cadvent2025\data.txt").readlines()

data = np.array([list(map(int, line.split(','))) for line in txt])

tree = KDTree(data)

G = nx.Graph()

pears = {}

for x in data:
    distance, index = tree.query(x, k=2)
    neighbor_index = index[1]
    neighbor_distance = distance[1]
    neighbor_tuple = tuple(data[neighbor_index])
    node_tuple = tuple(x)
    pears[node_tuple] = (neighbor_tuple, neighbor_distance)

sorted_pears = dict(sorted(pears.items(), key=lambda item: item[1][1]))

for k,x in sorted_pears.items():
    print(k,x)

for node, (neighbor_node, weight) in sorted_pears.items():
    if not G.has_edge(node, neighbor_node):
        print(f"connecting {tuple([int(x) for x in node])}, {tuple([int(x) for x in neighbor_node])} with distance {weight}")
        G.add_edge(node, neighbor_node, weight=weight)
        print(f"Total nodes: {G.number_of_nodes()}")

        H = nx.Graph()

        for node in G.nodes():
            # Convert each element of the tuple to a Python int
            new_node = tuple(int(i) for i in node)
            # Add node to new graph
            H.add_node(new_node)

        for u, v, data in G.edges(data=True):
            new_u = tuple(int(i) for i in u)
            new_v = tuple(int(i) for i in v)
            H.add_edge(new_u, new_v, **data)

        G = H
        H = None

        pos = nx.spring_layout(G, k=4)  # Adjust 'k' for spacing

        nx.draw(G, pos=pos, with_labels=True, node_size=30, node_color='yellow', edge_color='gray')

        plt.title("Graph with Islands Layout")
        plt.show()
    else:
        print(f"skipping {tuple([int(x) for x in node])}, {tuple([int(x) for x in neighbor_node])}")

