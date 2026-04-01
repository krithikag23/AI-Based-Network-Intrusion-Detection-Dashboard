import networkx as nx
def create_graph():
    G = nx.Graph()

    # Add nodes (devices/IPs)
    G.add_node("A")
    G.add_node("B")
    G.add_node("C")

    # Add edges (connections)
    G.add_edge("A", "B", weight=100)
    G.add_edge("B", "C", weight=5000)  # suspicious
    G.add_edge("A", "C", weight=200)

    return G
