import networkx as nx
import networkx.algorithms.approximation as approx
import random as r
import viewer
import matplotlib.pyplot as plt

def setup(graph, num_players, num_seeds):
    print approx.max_clique(graph)
    return list(approx.max_clique(graph))

    # print selected_comm.number_of_nodes()
    # max_size_clique = nx.graph_clique_number(selected_comm)
    # print max_size_clique
    # for cl in nx.find_cliques(selected_comm):
    #     if len(cl) == max_size_clique:
    #         return cl
    #         #print len(cl), cl
    #print nx.find_cliques(selected_comm)


def choose_nodes_from_graph(graph, num_players, num_seeds, setup2):
    leftover = num_seeds - len(setup2)
    if leftover > 0:
        lst = setup2 + r.sample(graph.nodes(), leftover)
    else:
        lst = r.sample(setup2, num_seeds)
    return lst

if __name__ == '__main__':
    g = nx.icosahedral_graph()
    setup = setup(g, 2, 2)
    print setup
    print choose_nodes_from_graph(g, 2, 2, setup)
    viewer.draw_graph(g)
    try:
        plt.show()
    except:
        plt.hide()