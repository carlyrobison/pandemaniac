import networkx as nx
from collections import defaultdict

def attackNodes(graph, targets, allottment):

    adj = dict({})
    for node in targets:
        for neighbor in all_neighbors(graph, node):
            adj[neighbor] += 1

    return sorted(adj, key=adj.get, reverse=True)[:allottment]
