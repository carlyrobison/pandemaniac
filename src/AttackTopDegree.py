import networkx as nx
import pick_top_nodes
from collections import defaultdict

def attackNodes(graph, targets, allottment):

    adj = defaultdict(int)
    for node in targets:
        for neighbor in nx.all_neighbors(graph, node):
            adj[neighbor] += 1

    adj = sorted(adj, key=adj.get, reverse=True)

    choosen = adj[:allottment]
    extra = adj[allottment:]

    i = 0
    while len(extra) > 0 and i < allottment:
        if(not hasSupport(graph, choosen[i], choosen, targets)):
            i = 0
            del choosen[i]
            choosen.append(extra.pop(0))
        else:
            i += 1

    return choosen

def setup(g, n, s):
    return pick_top_nodes.choose_nodes_from_graph(g, n, s, pick_top_nodes.setup(g, n, s))

def hasSupport(graph, node, choosen, enemy):

    support = len(set(nx.all_neighbors(graph, node)).intersection(choosen))
    opposition = len(set(nx.all_neighbors(graph, node)).intersection(enemy))

    return support >= opposition

def choose_nodes_from_graph(graph, num_players, num_seeds, setup):
    return attackNodes(graph, setup, num_seeds)
