import numpy as np
from GraphMatrices import (
    degree_matrix,
    laplacian_pseudoinverse,
)

# ==========================================================
# 1. VERSION VECTRISEE (rapide)
# ==========================================================

def common_neighbors_matrix(A: np.ndarray) -> np.ndarray:


def preferential_attachment_matrix(A: np.ndarray) -> np.ndarray:


def cosine_similarity_matrix(A: np.ndarray) -> np.ndarray:


def dice_similarity_matrix(A: np.ndarray) -> np.ndarray:


def jaccard_similarity_matrix(A: np.ndarray) -> np.ndarray:

# ==========================================================
# 2. KATZ MATRIX
# ==========================================================

def katz_matrix(A: np.ndarray, alpha: float = 0.1) -> np.ndarray:
    """
    Katz = (I - alpha A)^(-1) - I
    """



# ==========================================================
# 3. FIRST PASSAGE TIME AND COMMUTE TIME (via L⁺)
# ==========================================================


def first_passage_time_matrix(A: np.ndarray) -> np.ndarray:
    """
    First Passage Time (FPT) matrix based on the generalized formula:

        m(i,j) = Σ_k (L⁺_{ik} - L⁺_{ij} - L⁺_{jk} + L⁺_{jj}) * d_k

    where:
        - L⁺ is the Moore–Penrose pseudoinverse of the Laplacian matrix,
        - d_k is the degree of node k,
        - vol(G) = Σ_k d_k is the total volume of the graph.
    """


def commute_time_matrix(A: np.ndarray) -> np.ndarray:
    """
    C_{ij} = vol(G) * (L⁺_{ii} + L⁺_{jj} - 2 L⁺_{ij})
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

    print("Common neighbors :\n", common_neighbors_matrix(A))
    print("Preferential attachment index:\n", preferential_attachment_matrix(A))
    print("Cosine coefficient:\n", np.round(cosine_similarity_matrix(A), 3))
    print("Dice coefficient:\n", np.round(dice_similarity_matrix(A), 3))
    print("Jaccard coefficient:\n", np.round(jaccard_similarity_matrix(A), 3))

    # Katz
    K = katz_matrix(A, alpha=0.2)
    print("\nKatz:\n", np.round(K, 4))

    # FTP / CT 
    M = first_passage_time_matrix(A)
    N = commute_time_matrix(A)
    print("\nFTP matrix (H):\n", np.round(M, 4))
    print("\nCT matrix (C):\n", np.round(N, 4))
