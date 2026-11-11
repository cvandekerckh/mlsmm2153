import numpy as np
from ShortestPathMatrix import shortest_path_matrix

def closeness_centrality(A: np.ndarray) -> np.ndarray:
    """
    Standard closeness centrality:
        C(i) = (n - 1) / Σ_j d(i, j)
    Computed using the shortest path matrix.
    """

def residual_closeness_centrality(A: np.ndarray) -> np.ndarray:
    """
    Residual closeness centrality:
        RCC(k) = Σ_{i ≠ j} (1 / 2^{d(i, j)})
    Computed by removing node k from the graph, recalculating
    the shortest paths on the remaining subgraph, and summing
    the inverse powers of the distances.
    """


def eccentricity_centrality(A: np.ndarray) -> np.ndarray:
    """
    Eccentricity centrality of each node:
        ecc(i) = 1 / max_j d(i, j)
    The inverse is used so that larger distances correspond
    to smaller eccentricity values. Unreachable distances
    (set to 100000) are ignored in the logic of shortest_path_matrix.
    """


def graph_radius(A: np.ndarray) -> float:
    """
    Graph radius:
        radius = min_i eccentricity(i)
    The radius is computed as the minimum of the inverted
    eccentricity values.
    """

if __name__ == "__main__":
    A = np.array([
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]
    ], int)
    
    A_RC = np.array([[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 0]],int)

    print("Closeness:\n", np.round(closeness_centrality(A), 4))
    print("Residual closeness:\n", np.round(residual_closeness_centrality(A_RC), 4))
    print("Eccentricity:\n", eccentricity_centrality(A))
    print("Radius:\n", graph_radius(A))
