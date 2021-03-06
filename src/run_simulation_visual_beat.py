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

    return sim.get_result(node_mappings.keys(), node_color), get_end_nodes(node_mappings.keys(), node_color)

def get_end_nodes(colors, node_color):
  """
  get_end_config
  Get the resulting mapping of colors to the nodes of that color.
  """
  color_nodes = {}
  for color in colors:
    color_nodes[color] = []
  for node, color in node_color.items():
    if color is not None:
      color_nodes[color].append(node)
  return color_nodes

def load_graph(fl):
    filename = ''.join(fl.split('-RogueEngineers'))
    with open(filename) as infile:
        js_graph = json.load(infile)
    return js_graph

def draw_graph(G, node_mappings, position):
    # nx.draw_networkx(G, pos=position, node_size=10, node_color='r', alpha=.1, with_labels=False, font_size=6) #, with_labels=True)
    nodezz = [] # will contain neighbor nodes of picked ones
    for name in node_mappings:
        nodezz += node_mappings[name]
        for n in node_mappings[name]:
            nodezz += G.neighbors(n)
    nx.draw_networkx_nodes(G, pos=position, node_size=10, node_color='k', alpha=.1, with_labels=False, font_size=6, nodelist=nodezz) #, with_labels=True)

    edges = set()
    num_players = len(node_mappings)
    i = 0
    # draw selected nodes
    for name in node_mappings:
        if name == 'RogueEngineers':
            nx.draw_networkx_nodes(G, pos=position, node_size=100, alpha=.5, nodelist=node_mappings[name], with_labels=True, node_color='g', font_size=6)
        else:
            nx.draw_networkx_nodes(G, pos=position, node_size=100, alpha=.5, nodelist=node_mappings[name], with_labels=True, node_color=plt.get_cmap('gist_rainbow')(float(i)/num_players), font_size=6)
        edges |= set(G.edges(node_mappings[name]))
        i += 1
    # and selected node edges
    nx.draw_networkx_edges(G, pos, edgelist=list(edges), alpha=.1)
    #nx.draw_networkx_edges(G, pos, alpha=.1)


## run from the src directory as
# python run_simulation.py ../data/wednesday/4.5.1-RogueEngineers.json ../data/wednesday/4.5.1.json

if __name__ == '__main__':
    print "loading data and strategies"
    fl = sys.argv[1]
    graph = load_graph(fl)
    strategies = parse.get_strategies(fl)
    players = strategies.keys()
    nxgraph = nx.from_dict_of_lists(graph)
    print "making layout"
    pos = nx.spring_layout(nxgraph)

    print "commencing simulation"
    for i in range(1):
        print "simulation", i
        # make the output to simulate
        d = {}
        for n in players:
            d[n] = strategies[n][i]
        # show the start conditions
        print "starting choices:", d
        draw_graph(nxgraph, d, pos)

        # simulate it?
        res, end_nodes = simulate_game(graph, d)
        print i, res
        rogue_result = res['RogueEngineers']
        rogue_ones = True # pun on Rogue One movie, means rogue won
        for r in res:
            if r != 'RogueEngineers' and 10 > rogue_result:
                rogue_ones = False
        #if rogue_ones: # if we won, draw the graph
        if True:
            plt.figure()
            draw_graph(nxgraph, end_nodes, pos)
        try:
            plt.show()
        except:
            plt.hide()
            break



# ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)), interval=25, blit=True, init_func=init)

# ani.save('double_pendulum.mp4', fps=15)
try:
    plt.show()
except:
    pass

