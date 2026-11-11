import numpy as np

def shortest_path_matrix(A: np.ndarray) -> np.ndarray:
    """
    Compute the all-pairs shortest path matrix from an adjacency matrix A
    using Floyd–Warshall, with the same logic as your preprocess() + floyd().

    - A is assumed to be an unweighted adjacency matrix (0 = no edge, 1 = edge)
    - unreachable pairs will get a large value (100000)
    """
    # work on a copy so we don't modify A
    SP = A.copy().astype(float)
    n = SP.shape[0]

    # --- preprocess step: replace 0 by "infinity"
    for i in range(n):
        for j in range(n):
            if SP[i, j] == 0:
                SP[i, j] = 100000.0

    # Floyd–Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                SP[i, j] = min(SP[i, j], SP[i, k] + SP[k, j])

    # distance from a node to itself is 0
    for i in range(n):
        SP[i, i] = 0.0

    return SP