import sim
import parse
import sys
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
from copy import deepcopy

import random_top_nodes as rhd
import random_closeness as rc
import highest_degree as hd
import closeness as c
import AttackTopDegree as a
import surround_ta as st
import random_nodes as rs
import grab_cluster as gc


# STRATEGIES = [rs, rhd, hd, a, st, rc, c]
STRATEGIES = [gc]

NUM_MATCHES = 50

def do_round(node_color, adj_list, prev):
    prev = deepcopy(node_color)
    nodes = adj_list.keys()
    for node in nodes:
        (changed, color) = sim.update(adj_list, prev, node)
        # Store the node's new color only if it changed.
        if changed:
            node_color[node] = color
    return node_color, prev

def simulate_game(adj_list, node_mappings):
    node_color = dict([(node, None) for node in adj_list.keys()])
    sim.init(node_mappings, node_color)
    generation = 1
    prev = None

    while not sim.is_stable(generation, random.randint(100, 200), prev, node_color):
        node_color, prev = do_round(node_color, adj_list, prev)
        # then display the round
        generation += 1

    return sim.get_result(node_mappings.keys(), node_color)

def load_graph(fl):
    filename = ''.join(fl.split('-RogueEngineers'))
    with open(filename) as infile:
        js_graph = json.load(infile)
    return js_graph


## run from the root directory as
# python src/test_strategies.py data/test_data/2.10.10.json

if __name__ == '__main__':
    print "loading data and strategies"
    fl = sys.argv[1]
    graph = load_graph(fl)
    strategies = parse.get_strategies(fl)
    players = strategies.keys()
    nxgraph = nx.from_dict_of_lists(graph)

    num_players, num_seeds, _ = parse.get_game_info_from_filename(fl.split("-")[0])

    print "commencing simulation"
    for i in range(10):
        print "simulation", i
        # make the output to simulate
        d = {}
        for n in players:
            d[n] = strategies[n][i]

        for s in STRATEGIES:
            # spoof our own strategy
            setup = s.setup(nxgraph, num_players, num_seeds)
            d['RogueEngineers'] = s.choose_nodes_from_graph(nxgraph, num_players, num_seeds, setup)
            # show the start conditions
            print "starting choices:", d['RogueEngineers']
        
            # simulate it?
            res = simulate_game(graph, d)
            print 'RogueEngineers', res['RogueEngineers']
            print res
            #print res['strategy1'] > res['strategy2'], res

