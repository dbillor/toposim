from pydantic import BaseModel
from typing import Optional

class Node(BaseModel):
    id: str                 # switch / GPU / OCS label
    role: str = "UNKNOWN"   # T1 / GPU / OCS … (optional)
    plane: Optional[int] = None

class Link(BaseModel):
    id: str
    a: str                  # src_node
    z: str                  # dst_node
    capacity_gbps: float
    latency_ns: Optional[int] = None
    link_type: Optional[str] = None
    cost: int = 1           # default IGP metric
    srlg: Optional[str] = None
class Demand(BaseModel):
    src: str          # source node id
    dst: str          # destination node id
    rate_gbps: float  # traffic volume
