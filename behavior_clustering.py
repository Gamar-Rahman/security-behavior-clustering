import numpy as np

# --------------------------------------------------
# Distance function
# --------------------------------------------------
def D(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1])**2


# --------------------------------------------------
# 1. Centroid function
# --------------------------------------------------
def Centroid(L):
    """
    Computes the centroid of points in L.
    L is a 2xN NumPy array.
    Returns a 2x1 NumPy array.
    """
    return np.mean(L, axis=1).reshape(2, 1)


# --------------------------------------------------
# 2. CreateCentroids function (DO NOT MODIFY SEED)
# --------------------------------------------------
def CreateCentroids(K):
    """
    Creates K initial centroids in the range [0, 100].
    """
    np.random.seed(30)
    C = np.random.randint(0, 101, size=(2, K))
    return C


# --------------------------------------------------
# 3. CentroidAssignment function
# --------------------------------------------------
def CentroidAssignment(L, C):
    """
    Assigns each point in L to the closest centroid in C.
    Returns an array A of length N with values in [0, K-1].
    """
    N = L.shape[1]
    K = C.shape[1]
    A = np.zeros(N, dtype=int)

    for i in range(N):
        distances = []
        for j in range(K):
            distances.append(D(L[:, i], C[:, j]))
        A[i] = int(np.argmin(distances))

    return A


# --------------------------------------------------
# 4. NewCentroids function
# --------------------------------------------------
def NewCentroids(L, A, K):
    """
    Computes new centroids based on assignments A.
    Returns a 2xK NumPy array.
    """
    C_new = np.zeros((2, K))

    for k in range(K):
        indices = np.where(A == k)[0]

        if len(indices) == 0:
            # Leave centroid unchanged if no points assigned
            C_new[:, k] = np.nan
        else:
            C_new[:, k] = np.mean(L[:, indices], axis=1)

    return C_new
