import sys
import networkx as nx
import random as r
import parse

if __name__ == '__main__':
    fl = sys.argv[1]

    num_players, num_seeds, unique_id = parse.get_game_info_from_filename(fl)
    g = parse.parse_graph(fl)

    nodes = nodes(g)
    for i in range(50):
        for x in range(num_seeds):
            print "%" % nodes[random.randint(0, len(nodes))]
