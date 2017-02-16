import sys
import networkx as nx
import random as r
import parse
import heapq

FACTOR = 5

# Beat the TA that can only pick fewer seed nodes than we can

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

# Picks the highest degree nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds):
    degrees = nx.degree(g)
    top_nodes = getTopNodes(degrees, num_seeds)
    #play = r.sample(top_nodes, num_seeds)
    return top_nodes