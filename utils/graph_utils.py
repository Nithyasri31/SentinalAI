import networkx as nx
import matplotlib.pyplot as plt
from utils.graph_utils import *
# -------------------------------------
# Create Fraud Network Graph
# -------------------------------------

def create_graph(df):
    """
    Creates a graph connecting
    Phone Numbers <----> UPI IDs
    """

    G = nx.Graph()

    for _, row in df.iterrows():

        phone = row["Phone"]
        upi = row["UPI"]

        G.add_node(
            phone,
            node_type="Phone"
        )

        G.add_node(
            upi,
            node_type="UPI"
        )

        G.add_edge(
            phone,
            upi,
            amount=row["Amount"],
            fraud=row["Fraud"],
            transaction=row["Transaction_ID"]
        )

    return G


# -------------------------------------
# Node Colors
# -------------------------------------

def get_node_colors(G):

    colors = []

    for node in G.nodes():

        node_type = G.nodes[node]["node_type"]

        if node_type == "Phone":
            colors.append("#1f77b4")      # Blue

        else:
            colors.append("#2ca02c")      # Green

    return colors


# -------------------------------------
# Node Sizes
# -------------------------------------

def get_node_sizes(G):

    sizes = []

    for node in G.nodes():

        degree = G.degree(node)

        sizes.append(600 + degree * 350)

    return sizes


# -------------------------------------
# Network Statistics
# -------------------------------------

def network_statistics(G):

    return {

        "Nodes": G.number_of_nodes(),

        "Edges": G.number_of_edges(),

        "Connected Components":
            nx.number_connected_components(G),

        "Average Degree":
            round(
                sum(dict(G.degree()).values())
                / G.number_of_nodes(),
                2
            )
    }


# -------------------------------------
# Draw Network
# -------------------------------------

def draw_graph(G):

    fig, ax = plt.subplots(
        figsize=(12,8)
    )

    pos = nx.spring_layout(
        G,
        seed=42,
        k=1
    )

    nx.draw_networkx_nodes(

        G,

        pos,

        node_color=get_node_colors(G),

        node_size=get_node_sizes(G),

        alpha=0.9,

        edgecolors="black"

    )

    nx.draw_networkx_edges(

        G,

        pos,

        width=2,

        edge_color="gray",

        alpha=0.7

    )

    nx.draw_networkx_labels(

        G,

        pos,

        font_size=8,

        font_weight="bold"

    )

    ax.set_title(
        "Fraud Network Graph",
        fontsize=18,
        weight="bold"
    )

    ax.axis("off")

    return fig


# -------------------------------------
# Top Connected Accounts
# -------------------------------------

def top_connected_nodes(G, top_n=10):

    degree = dict(G.degree())

    degree = sorted(

        degree.items(),

        key=lambda x: x[1],

        reverse=True

    )

    return degree[:top_n]