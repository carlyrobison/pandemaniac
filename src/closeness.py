import sys
import networkx as nx
import heapq

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds):
    weights = nx.closeness_centrality(g)
    top_nodes = getTopNodes(weights, num_seeds)
    return top_nodes
