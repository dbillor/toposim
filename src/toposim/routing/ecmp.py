import networkx as nx, pandas as pd
from collections import defaultdict
from ..schema import Demand

def _next_hops(G: nx.Graph, src: str, dst: str, metric: str = "cost"):
    paths = nx.all_shortest_paths(G, src, dst, weight=metric)
    hops = [p[1] for p in paths]           # first hop after src
    w = 1 / len(hops)
    return {h: w for h in hops}

def utilisation(G: nx.MultiDiGraph,
                demands: list[Demand],
                metric: str = "cost") -> pd.DataFrame:
    load = defaultdict(float)   # keyed by (u,v)
    for d in demands:
        nhops = _next_hops(G, d.src, d.dst, metric)
        for nh, w in nhops.items():
            load[(d.src, nh)] += d.rate_gbps * w

    rows = []
    for u, v, data in G.edges(data=True):
        gbps = load.get((u, v), 0.0)
        rows.append({
            "link": f"{u}->{v}",
            "gbps": gbps,
            "capacity": data["capacity"],
            "util": gbps / data["capacity"] if data["capacity"] else 0
        })
    return pd.DataFrame(rows)
