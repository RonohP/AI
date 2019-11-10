import networkx as nx
import matplotlib.pyplot as plt
from bfs import BfsTransverse

G = nx.Graph()
nodes = ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8", "J9", "J10", "J11", "J12", "J13", "Karen", "Gitaru", "Loresho",
         "Langata", "Lavington", "Parklands", "Kilimani", "Kahawa", "Kasarani", "HillView", "Donholm", "CBD",
         "ImaraDaima"]
G.add_nodes_from(nodes)

# Add Edges and their weights
G.add_edge("Karen", "J6", weight="4")
G.add_edge("Karen", "J1", weight="2.8")
G.add_edge("J6", "Gitaru", weight="10")
G.add_edge("J6", "J7", weight="6")
G.add_edge("J6", "J4", weight="6")
G.add_edge("J1", "J4", weight="2.6")
G.add_edge("J1", "J2", weight="6")
G.add_edge("Gitaru", "J7", weight="6")
G.add_edge("J7", "J8", weight="7")
G.add_edge("J4", "J5", weight="9.7")
G.add_edge("J4", "J3", weight="9")
G.add_edge("J2", "Langata", weight="2.6")
G.add_edge("J2", "J3", weight="5.4")
G.add_edge("J8", "J9", weight="3")
G.add_edge("J8", "Loresho", weight="2")
G.add_edge("J5", "Kilimani", weight="0.5")
G.add_edge("J3", "J12", weight="6.7")
G.add_edge("J3", "J13", weight="6.2")
G.add_edge("J9", "Lavington", weight="7")
G.add_edge("J9", "J10", weight="4")
G.add_edge("Kilimani", "J11", weight="0.5")
G.add_edge("Kilimani", "J12", weight="2.3")
G.add_edge("J12", "CBD", weight="1.5")
G.add_edge("J13", "CBD", weight="5.5")
G.add_edge("J13", "ImaraDaima", weight="3.9")
G.add_edge("Lavington", "J11", weight="0.5")
G.add_edge("J10", "Parklands", weight="3")
G.add_edge("J10", "J11", weight="7")
G.add_edge("ImaraDaima", "Donholm", weight="10.4")
G.add_edge("Donholm", "HillView", weight="20")
G.add_edge("HillView", "Kasarani", weight="1.7")
G.add_edge("Kasarani", "Kahawa", weight="11.5")

# position the nodes to resemble Nairobi's map
G.node["Karen"]['pos'] = (0, 0)
G.node["J6"]['pos'] = (0, 6)
G.node["J1"]['pos'] = (2, -4)
G.node["J4"]['pos'] = (5, -4)
G.node["J7"]['pos'] = (0, 14)
G.node["Gitaru"]['pos'] = (-4, 12)
G.node["J8"]['pos'] = (3, 14)
G.node["Loresho"]['pos'] = (3, 20)
G.node["J9"]['pos'] = (6, 14)
G.node["Lavington"]['pos'] = (6, 8)
G.node["J10"]['pos'] = (9, 14)
G.node["Parklands"]['pos'] = (10, 19)
G.node["J11"]['pos'] = (10, 10)
G.node["Kilimani"]['pos'] = (10, 4)
G.node["J5"]['pos'] = (8, -4)
G.node["J2"]['pos'] = (4, -8)
G.node["Langata"]['pos'] = (4, -14)
G.node["J3"]['pos'] = (7, -8)
G.node["J12"]['pos'] = (13, 0)
G.node["CBD"]['pos'] = (16, 0)
G.node["J13"]['pos'] = (16, -6)
G.node["ImaraDaima"]['pos'] = (18, -10)
G.node["Donholm"]['pos'] = (18, 4)
G.node["HillView"]['pos'] = (18, 10)
G.node["Kasarani"]['pos'] = (18, 16)
G.node["Kahawa"]['pos'] = (20, 20)
# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')
# call BFS to return set of all possible routes to the goal
# route_bfs = BfsTransverse()
route_bfs = BfsTransverse()
routes = route_bfs.bfs(G, "Karen", "ImaraDaima")
print(route_bfs.visited)
route_list = route_bfs.visited
# color the nodes in the route_bfs
node_col = ['thistle' if not node in route_list else 'gold' for node in G.nodes()]
gold_colored_edges = list(zip(route_list, route_list[1:]))
# color the edges as well
# print(gold_colored_edges)
edge_col = ['thistle' if not edge in gold_colored_edges else 'gold' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
nx.draw_networkx_edge_labels(G, node_pos, edge_color=edge_col, edge_labels=arc_weight)
plt.axis('off')
plt.show()
