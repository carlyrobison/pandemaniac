import networkx as nx
import heapq

def choose_nodes_from_graph(graph, num_players, num_seeds):
    degrees = nx.degree(g)
    # Just choose the num_seeds highest-degree nodes
    return heapq.nlargest(num_seeds, degrees.__get_item__)
