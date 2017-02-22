import sys
import networkx as nx
import random as r

def setup(g, num_players, num_seeds):
    return ""

# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds, setup):
    return r.sample(g.nodes(), num_seeds)
