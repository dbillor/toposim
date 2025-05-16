import pandas as pd, networkx as nx
from .schema import Node, Link

def load_links_csv(path: str):
    """
    Read a link CSV with columns:
      src_node, src_port, dst_node, dst_port,
      link_type, bw_Gbps, latency_ns
    Return (nodes, links).
    """
    df = pd.read_csv(path)
    if "id" not in df.columns:
        df["id"] = [f"link-{i}" for i in range(len(df))]

    links = [
        Link(id=row.id,
             a=row.src_node,
             z=row.dst_node,
             capacity_gbps=row.bw_Gbps,
             latency_ns=row.latency_ns,
             link_type=row.link_type)
        for row in df.itertuples(index=False)
    ]

    nodes = {row.src_node for row in df.itertuples(index=False)}
    nodes |= {row.dst_node for row in df.itertuples(index=False)}
    nodes = [Node(id=n) for n in nodes]

    return nodes, links


def build_graph(nodes, links) -> nx.MultiDiGraph:
    G = nx.MultiDiGraph()
    for n in nodes:
        G.add_node(n.id, role=n.role, plane=n.plane)
    for l in links:
        G.add_edge(l.a, l.z,
                   id=l.id,
                   capacity=l.capacity_gbps,
                   latency_ns=l.latency_ns,
                   cost=l.cost,
                   link_type=l.link_type)
    return G
