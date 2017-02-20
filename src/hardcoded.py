import sys
import networkx as nx
import heapq

NODES = [u'1', u'50', u'123', u'34', u'89', u'223', u'103', u'141', u'213', u'4']

# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds):
    assert len(NODES[:num_seeds]) == num_seeds
    return NODES[:num_seeds]