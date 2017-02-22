import sys
import networkx as nx
import heapq
import random as r

FACTOR = 5

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

def setup(g, num_players, num_seeds):
    return nx.closeness_centrality(g)

# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds, setup):
    top_nodes = getTopNodes(setup, num_seeds * FACTOR)
    play = r.sample(top_nodes, num_seeds)
    return play
