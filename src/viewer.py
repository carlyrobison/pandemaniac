import networkx as nx
import sys
import parse
import matplotlib.pyplot as plt

def draw_graph(G):
	nx.draw_networkx(G, node_size=50, node_color='r', alpha=.2, with_labels=True, font_size=6)

if __name__ == '__main__':
	filename = sys.argv[1]

	# load graph
	G = parse.parse_graph(filename)
	# draw graph
	print "graph successfully loaded"

	draw_graph(G)

	print "graph successfully drawn"

	try:
		plt.show()
	except:
		pass
