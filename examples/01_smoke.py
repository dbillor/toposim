from toposim.loader_csv import load_links_csv, build_graph
import pathlib, networkx as nx

csv_path = pathlib.Path(__file__).parent.parent / "data/full_network_links_dual_dc_3200km.csv"
nodes, links = load_links_csv(csv_path)
G = build_graph(nodes, links)

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# peek at one edge’s attributes
u, v, data = next(iter(G.edges(data=True)))
print(f"{u} -> {v}  {data}")
