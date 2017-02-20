import sys
import networkx as nx
import random as r
import parse
import heapq

# Beat the TA that picks the top degree nodes

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

# For the highest degree nodes, pick two neighbors
def getNeighbors(g, node, n, avoid):
	neighbors = g.neighbors(node)
	valid = []
	for candidate in neighbors:
		if len(set(g.neighbors(candidate)).intersection(avoid)) < 2:
			# only neighboring one bad node
			valid.append(candidate)
	return r.sample(valid, min(n, len(valid)))

# Picks the highest degree nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds):
    degrees = nx.degree(g)
    top_nodes = getTopNodes(degrees, num_seeds)
    num_left = num_seeds
    play = set([])
    for node in top_nodes:
    	play |= set(getNeighbors(g, node, min(2, num_left), set(top_nodes)))
    	num_left = num_seeds - len(play)
    assert(len(play) == num_seeds)
    return play