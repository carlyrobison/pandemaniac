import sys
import networkx as nx
import random as r
import parse
import heapq

FACTOR = 5

# Get top n ranked nodes from the given dictionary of values
def getTopNodes(vals, n): # Taken from rankmaniac code
    return heapq.nlargest(n, vals, key=vals.__getitem__)

def choose_nodes_from_graph(g, num_players, num_seeds):
    degrees = nx.degree(g)
    top_nodes = getTopNodes(degrees, num_seeds * FACTOR * num_players)
    play = r.sample(top_nodes, num_seeds)
    return play

if __name__ == '__main__':
    fl = sys.argv[1]

    num_players, num_seeds, unique_id = parse.get_game_info_from_filename(fl)
    g = parse.parse_graph(fl)

    for i in range(50):
        for k in choose_nodes_from_graph(g, num_players, num_seeds):
            print "%d" % int(k)