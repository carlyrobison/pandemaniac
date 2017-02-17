import sim
import parse
import sys
import networkx
import matplotlib

def do_round(node_color, adj_list, prev):
	prev = deepcopy(node_color)
	nodes = adj_list.keys()
    for node in nodes:
      (changed, color) = sim.update(adj_list, prev, node)
      # Store the node's new color only if it changed.
      if changed: node_color[node] = color
    return node_color, prev

def simulate_game(adj_list, node_mappings):
	node_color = dict([(node, None) for node in adj_list.keys()])
  	init(node_mappings, node_color)
  	generation = 1
  	prev = None

  	while not sim.is_stable(generation, randint(100, 200), prev, node_color):
  		node_color, prev = do_round(node_color, adj_list, prev)
  		# then display the round
  		generation += 1

  	return get_result(node_mappings.keys(), node_color)

if __name__ == '__main__':
	fl = sys.argv[1]
	parse.get_strategies(fl)


