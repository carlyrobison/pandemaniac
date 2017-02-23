import sys
import networkx as nx
import numpy as np
import heapq
import community
from collections import defaultdict
import matplotlib.pyplot as plt
import random as r
import viewer
import largest_clique

EXTRA = 5

#import random_top_nodes as strat
import highest_degree as strat

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

def setup(g, num_players, num_seeds):
    #first compute the best partition
    partition = community.best_partition(g)
    induced_graph = community.induced_graph(partition, g)

    # Play around with picking the "best" community
    # node boundary?
    #print nx.current_flow_closeness_centrality(induced_graph) # not better
    # print nx.katz_centrality(induced_graph) # doesn't converge
    #print nx.eigenvector_centrality(induced_graph) # not as good
    #print nx.communicability_centrality(induced_graph) # not as good
    #{0: 8.451771641899612, 1: 9.041654401534407, 2: 9.321830560246685, 3: 8.79634625159723, 4: 7.512000387517644, 5: 9.319261339431147, 6: 8.635502364748598, 7: 9.182167514276696, 8: 8.812816793986622, 9: 5.955242238035001, 10: 7.224124906314186, 11: 8.598864555204745, 12: 1.3780813983087927, 13: 8.574141188778002, 14: 1.4894068385674029}
    #{0: 0.03170498456257798, 1: 0.03351885293616147, 2: 0.982004394865475, 3: 0.009750044520081363, 4: 0.012642119637055598, 5: 0.08211419419246402, 6: 0.013202397926046897, 7: 0.15814666928657686, 8: 0.026268239793024895, 9: 0.0005523351650465954, 10: 0.0009839216844465231, 11: 0.019821817113884598, 12: 4.399697547690089e-05, 13: 0.016495461620553098, 14: 0.00022120782918811697}
    #{0: 1670.2226290285078, 1: 3648.298186716118, 2: 4153.05229512053, 3: 3214.282455755265, 4: 561.0349179323383, 5: 4068.320908838754, 6: 2977.2760610270666, 7: 3474.488922208751, 8: 3493.8811964338947, 9: 1521.5720949300896, 10: 2520.2823105797784, 11: 1385.0884502097147, 12: 281.6674672972596, 13: 2306.8136315883607, 14: 358.98207498678886}


    # viewer.draw_graph(induced_graph)
    # try:
    #     plt.show()
    # except:
    #     plt.hide()

    # Choose the community with the most number of outgoing edges
    #weights = nx.communicability_centrality(induced_graph) #weight='weight'
    weights = nx.degree(induced_graph, weight='weight')
    #print weights

    best_com = max(weights, key=weights.__getitem__)

    com = defaultdict(list)
    for node, c in partition.iteritems():
        com[c].append(node)

    selected_comm = g.subgraph(com[best_com])

    # get one node from every clique
    #print selected_comm.number_of_nodes()
    # max_size_clique = nx.graph_clique_number(selected_comm)
    # print max_size_clique
    # lst = []
    # for cl in nx.find_cliques(selected_comm):
    #     if len(cl) >= max_size_clique/2:
    #         lst.append(r.choice(cl))
    #         #return cl
    #         #print len(cl), cl
    # return lst
    #print nx.find_cliques(selected_comm)

    #setup = largest_clique.setup(selected_comm, num_players, num_seeds)
    #return setup

    return strat.setup(selected_comm, num_players, num_seeds)


# Picks the highest closeness-centrality nodes in the graph.
def choose_nodes_from_graph(g, num_players, num_seeds, setup):
    top_nodes = r.sample(strat.choose_nodes_from_graph(g, 2, num_seeds + EXTRA, setup), num_seeds)
    return top_nodes
    return largest_clique.choose_nodes_from_graph(g, num_players, num_seeds, setup)
