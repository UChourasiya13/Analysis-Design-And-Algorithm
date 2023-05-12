import numpy as np

def page_rank(adj_matrix, beta=0.85, epsilon=1e-6):
    """
    Computes the PageRank scores for the nodes in a network represented by an adjacency matrix.
    
    Parameters:
    adj_matrix (numpy.ndarray): The adjacency matrix of the network, where adj_matrix[i,j] = 1 if there is a link from node j to node i, and 0 otherwise.
    beta (float): The damping factor, which determines the probability that a user will follow a link compared to jumping to a random page. Default value is 0.85.
    epsilon (float): The convergence threshold. The algorithm will stop when the change in PageRank scores between iterations is less than epsilon. Default value is 1e-6.
    
    Returns:
    numpy.ndarray: A 1D array of PageRank scores, where the i-th element corresponds to the i-th node in the network.
    """
    
    n = adj_matrix.shape[0]
    
    # Create a transition matrix by normalizing the adjacency matrix
    row_sum = np.sum(adj_matrix, axis=1)
    transition_matrix = adj_matrix / row_sum[:, np.newaxis]
    
    # Set up the initial PageRank scores
    page_rank = np.ones(n) / n
    
    # Iterate until convergence
    while True:
        prev_page_rank = page_rank.copy()
        page_rank = (1 - beta) / n + beta * np.dot(transition_matrix, page_rank)
        if np.linalg.norm(page_rank - prev_page_rank) < epsilon:
            break
    
    return page_rank
