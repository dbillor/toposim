import pandas as pd
from .schema import Demand

def load_demands_csv(path: str) -> list[Demand]:
    """
    CSV columns: src,dst,rate_gbps
    """
    df = pd.read_csv(path)
    return [Demand(**row) for _, row in df.iterrows()]
