from pyvis.network import Network
net = Network(notebook=True)
net.add_node(1, label="Alex")
net.add_node(2, label="Cathy")
net.show("nodes.html")

net.add_nodes(
    [1, 2, 3, 4, 5, 6],
    label=["Alex", "Cathy", "Michael", "Ben", "Oliver", "Olivia"],
    color=["#00bfff", "#ffc0cb", "#3da831", "#9a31a8", "#3155a8", "#eb4034"],
)
net.add_edge(1, 5, value=2)
net.add_edges([(2, 5, 5), (3, 4, 2), (1, 6), (2, 6), (3, 5)])

net.show("edges_with_weights.html")

def add_repulsion(node_distance: int, spring_length: int):
    net = Network(notebook=True)

    net.add_nodes(
        [1, 2, 3, 4, 5, 6],
        label=["Alex", "Cathy", "Michael", "Ben", "Oliver", "Olivia"],
        color=["#00bfff", "#ffc0cb", "#3da831", "#9a31a8", "#3155a8", "#eb4034"],
    )

    net.add_edge(1, 5, value=2)
    net.add_edges([(2, 5, 5), (3, 4, 2), (1, 6), (2, 6), (3, 5)])

    net.repulsion(node_distance=node_distance, spring_length=spring_length)

    net.show(f"distance_{node_distance}_spring_length_{spring_length}.html")

    return net
net = add_repulsion(node_distance=100, spring_length=200)
net.show("distance_100_spring_length_200.html")
net = add_repulsion(node_distance=100, spring_length=1000)
net.show(f"distance_100_spring_length_1000.html")
net = add_repulsion(node_distance=500, spring_length=200)
net.show(f"distance_500_spring_length_200.html")
