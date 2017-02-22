import sys
import networkx as nx
import numpy as np
import heapq
import community
from collections import defaultdict
import matplotlib.pyplot as plt

import random_top_nodes as strat

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

def setup(g, num_players, num_seeds):
    #first compute the best partition
    partition = community.best_partition(g)

    induced_graph = community.induced_graph(partition, g)

    # Choose the community with the most number of outgoing edges
    weights = nx.degree(induced_graph, weight='weight')

    best_com = max(weights, key=weights.__getitem__)

    com = defaultdict(list)
    for node, c in partition.iteritems():
        com[c].append(node)

    return g.subgraph(com[best_com])

# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds, setup):
    top_nodes = strat.choose_nodes_from_graph(setup, 2, num_seeds, 1)
    return top_nodes
