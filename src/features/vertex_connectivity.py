import networkx as nx


def vc(network):
    # Return number of connected components in graph.
    net = network.to_undirected()
    v = nx.number_connected_components(net)
    return v

def vc_strong(network):
    # Return number of strongly connected components in graph.
    v = nx.number_strongly_connected_components(network)
    return v


def vc_weak(network):
    # Return the number of connected components in G.
    v = nx.number_weakly_connected_components(network)
    return v
