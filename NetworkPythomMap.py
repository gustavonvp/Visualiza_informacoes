from typing import List, Any

import pandas as pd
from pyvis.network import Network

#net = Network(notebook=True)
df = pd.read_excel("dados/owid-co2-data.xlsx", index_col=0)
nodes = df.columns.to_list()
nodes = [node.strip() for node in nodes]


#nodes
def get_edges(node, weights: list, all_nodes: list, minium_weight: str):
    nodes = all_nodes.copy()

    # Remove target node
    # nodes.remove(node)

    # Create a list of edges with weights
    edges = [(node, connection, weight) for connection, weight in zip(nodes, weights)]

    # Get only edges with weights greater than the minimum weight
    edges = [edge for edge in edges if str(edge[2]) >= str(minium_weight)]

    return edges


def draw_network(
        nodes: list,
        df: pd.DataFrame,
        minium_weight: int = 0,
        repulsion: int = 100,
        spring_length=200,
        buttons=False,
):
    net = Network("500px", "500px", notebook=True)
    net.add_nodes(nodes)

    # add edges
    for node, weights in df.iterrows():
        edges = get_edges(node, str(weights), nodes, str(minium_weight))
        net.add_edges(edges)

    # change node distance and spring length
    net.repulsion(repulsion, spring_length=spring_length)

    # Tweek configuration UI
    net.show_buttons(filter_=buttons)
    return net


net = draw_network(nodes, df, minium_weight=9, repulsion=100, spring_length=500)
net.show("match.html")

net = draw_network(
    nodes, df, minium_weight=0, repulsion=100, spring_length=500, buttons=["physics"]
)
net.show("match_with_buttons.html")
