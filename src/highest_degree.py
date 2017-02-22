import networkx as nx
import heapq

def setup(graph, num_players, num_seeds):
	return nx.degree(graph)

def choose_nodes_from_graph(graph, num_players, num_seeds, setup):
    degrees = setup
    # Just choose the num_seeds highest-degree nodes
    return heapq.nlargest(num_seeds, degrees, key=degrees.__getitem__)
