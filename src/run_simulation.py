import sim
import parse
import sys
import json
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from copy import deepcopy

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


## run from the src directory as
# python run_simulation.py ../data/wednesday/4.5.1-RogueEngineers.json ../data/wednesday/4.5.1.json

if __name__ == '__main__':
    fl = sys.argv[1]
    graph = load_graph(fl)
    strategies = parse.get_strategies(fl)
    players = strategies.keys()

    for i in range(NUM_MATCHES):
        # make the output to simulate
        d = {}
        for n in players:
            d[n] = strategies[n][i]
        # simulate it?
        res = simulate_game(graph, d)
        print i, res

# ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init)

# ani.save('double_pendulum.mp4', fps=15)
try:
    plt.show()
except:
    pass

