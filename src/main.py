import sys
import networkx as nx
import parse
import heapq

# RUNS THIS SHIT

if __name__ == '__main__':
    fl = sys.argv[1]
    strategy = sys.argv[2]

    num_players, num_seeds, unique_id = parse.get_game_info_from_filename(fl)
    g = parse.parse_graph(fl)

    if (strategy == 'smartrandom'):
        import random_top_nodes as s
    elif strategy == 'top':
        import pick_top_nodes as s
    elif strategy == 'surroundta':
        import surround_ta as s

    rounds = []
    for i in range(50):
        rounds.append(s.choose_nodes_from_graph(g, num_players, num_seeds))
    parse.write_choices_to_file('../' + fl.strip('.json') + '_choices.txt', rounds)
