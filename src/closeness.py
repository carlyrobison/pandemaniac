import sys
import networkx as nx
import heapq

def setup(g, num_players, num_seeds):
	return nx.closeness_centrality(g)

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds, setup):
    weights = setup
    top_nodes = getTopNodes(weights, num_seeds)
    return top_nodes
