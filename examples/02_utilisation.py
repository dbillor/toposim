import pathlib
from toposim.loader_csv import load_links_csv, build_graph
from toposim.demand import load_demands_csv
from toposim.routing.ecmp import utilisation

base = pathlib.Path(__file__).parent.parent / "data"

nodes, links = load_links_csv(base / "full_network_links_dual_dc_3200km.csv")
G = build_graph(nodes, links)

demands = load_demands_csv(base / "example_demand.csv")
df = utilisation(G, demands, metric="latency_ns")

hot = df.sort_values("util", ascending=False).head(10)
print(hot[["link", "gbps", "capacity", "util"]])
