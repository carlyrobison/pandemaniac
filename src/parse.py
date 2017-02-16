import networkx as nx
import json
import os

# Gets the game info (num_players, num_seeds, unique_id) from a graph's filename
def get_game_info_from_filename(filename):
    # Filename should be formatted 'num_players.num_seeds.unique_id'
    parts = os.path.basename(filename).split('.')
    assert(len(parts) == 3)
    num_players = int(parts[0])
    num_seeds = int(parts[1])
    unique_id = int(parts[2])
    return num_players, num_seeds, unique_id

# Parses a JSON-formatted graph with the given filename.
def parse_graph(filename):
    with open(filename) as infile:
        js_graph = json.load(infile)
    return nx.from_dict_of_lists(js_graph)
