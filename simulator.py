import random
import pandas as pd

def generate_traffic():
    data = {
        "duration": random.randint(1, 10),
        "src_bytes": random.randint(50, 10000),
        "dst_bytes": random.randint(50, 15000)
    }
    return pd.DataFrame([data])
