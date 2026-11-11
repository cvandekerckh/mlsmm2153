import numpy as np


def hits(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Compute HITS scores (Authorities and Hubs) using the eigenvector method.

    Authority scores are the principal eigenvector of AᵀA.
    Hub scores are the principal eigenvector of AAᵀ.

    Both vectors are normalized to sum to 1.
    """


if __name__ == "__main__":
    A = np.array([
        [0, 1, 1, 1],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ], dtype=int)

    print("HITS (eigenvector method):")
    authority_eig, hub_eig = hits(A)
    print("Authorities:", np.round(authority_eig, 4))
    print("Hubs:", np.round(hub_eig, 4))