""" Blanchet and Charbit """

import numpy as np

def ex_5_2(X, Y):
    """
    """
    I = np.shape(X)[0]
    J = np.shape(Y)[0]
    d = np.zeros((I, J))
    for i in range(0, I):
        for j in range(0, J):
            d[i, j] = np.abs(X[i] - Y[j])
    D = np.zeros((I, J))
    D[0, 0] = d[0, 0]
    for k in range(1, min(I, J)):
        for i in range(0, k):
            if (i == 0):
                D[i, k] = D[i, k - 1] + d[i, k]
            else:
                path1 = D[i - 1, k] + d[i, k]
                path2 = D[i - 1, k - 1] + 2.0 * d[i, k]
                path3 = D[i, k - 1] + d[i, k]
                D[i, k] = min(path1, path2, path3)
        for j in range(0, k):
            if (j == 0):
                D[k, j] = D[k - 1, j] + d[k, j]
            else:
                path1 = D[k, j - 1] + d[k, j]
                path2 = [k - 1, j - 1] + 2.0 * d[k, j]
                path3 = D[k - 1, j] + d[k, j]
                D[k, j] = min(path1, path2, path3)
        path1 = D[k - 1, k] + d[k, k]
        path2 = D[k - 1, k - 1] + 2.0 * d[k, k]
        path3 = D[k, k - 1] + d[k, k]
        D[k, k] = min(path1, path2, path3)
    return D
