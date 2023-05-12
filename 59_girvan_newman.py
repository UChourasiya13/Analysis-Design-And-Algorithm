import networkx as nx

def girvan_newman(G):
    # Create a copy of the original graph
    # so that we don't modify the original graph
    # during the algorithm
    G_copy = G.copy()

    # Keep track of the number of connected components
    num_components = nx.number_connected_components(G_copy)

    # Loop until the graph is completely disconnected
    while num_components == 1:
        # Compute the betweenness centrality of all edges in the graph
        # and sort them in descending order
        betweenness = nx.edge_betweenness_centrality(G_copy)
        sorted_edges = sorted(betweenness.items(), key=lambda x: (-x[1], x[0]))

        # Remove the edge with highest betweenness centrality
        edge_to_remove = sorted_edges[0][0]
        G_copy.remove_edge(*edge_to_remove)

        # Update the number of connected components
        num_components = nx.number_connected_components(G_copy)

    # Return the list of connected components
    return list(nx.connected_components(G_copy))
