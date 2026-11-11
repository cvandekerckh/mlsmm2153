import numpy as np
from GraphMatrices import transition_matrix


def pagerank_eigen(A: np.ndarray, alpha: float = 0.85) -> np.ndarray:
    """
    Compute PageRank scores using the eigenvector method.

    Google matrix:
        G = α * Pᵀ + (1 - α) * E
    where:
        P is the transition probability matrix (row-stochastic),
        E is the uniform teleportation matrix (1/n for all entries).
    The dominant eigenvector of G gives the PageRank scores.
    """



def pagerank_power_iteration(A: np.ndarray, alpha: float = 0.85, max_iter: int = 100) -> np.ndarray:
    """
    Compute PageRank scores using the iterative (power) method.

    Iteration formula:
        PR_{k+1} = α * Pᵀ * PR_k + (1 - α) * u
    where:
        u is the uniform teleportation vector (1/n for all entries).
    Convergence is achieved after several iterations.
    """


# ----------------------------------------------------------
# Example usage
# ----------------------------------------------------------
if __name__ == "__main__":
    A = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ], dtype=int)

    print("PageRank (eigenvector method):")
    pr_eig = pagerank_eigen(A, alpha=0.827)
    print(np.round(pr_eig, 4))

    print("\nPageRank (power iteration):")
    pr_iter = pagerank_power_iteration(A, alpha=0.827, max_iter=100)
    print(np.round(pr_iter, 4))
