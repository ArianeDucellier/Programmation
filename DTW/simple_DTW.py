""" Blanchet and Charbit """

import numpy as np

def ex_5_2(X, Y):
    """
    Carry out simple DTW on 1D numerical signal

    Input:
        type X = 1D numpy array
        X = First time series
        type Y = 1D numpy array
        Y = Second time series
    Output:
        type D = 2D numpy array
        D = Defined in Blanchet and Charbit vol. 2 p. 118
        type phi_x = list of integers
        phi_x = Defined in Blanchet and Charbit vol. 2 p. 119
        type phi_y = list of integers
        phi_y = Defined in Blanchet and Charbit vol. 2 p. 119
    """
    I = np.shape(X)[0]
    J = np.shape(Y)[0]
    # Distance matrix
    d = np.zeros((I, J))
    for i in range(0, I):
        for j in range(0, J):
            d[i, j] = np.abs(X[i] - Y[j])
    # Minimal path matrix
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
                D[i, k] = min([path1, path2, path3])
        for j in range(0, k):
            if (j == 0):
                D[k, j] = D[k - 1, j] + d[k, j]
            else:
                path1 = D[k, j - 1] + d[k, j]
                path2 = D[k - 1, j - 1] + 2.0 * d[k, j]
                path3 = D[k - 1, j] + d[k, j]
                D[k, j] = min([path1, path2, path3])
        path1 = D[k - 1, k] + d[k, k]
        path2 = D[k - 1, k - 1] + 2.0 * d[k, k]
        path3 = D[k, k - 1] + d[k, k]
        D[k, k] = min([path1, path2, path3])
    if (I > J):
        for k in range(J, I):
            for j in range(0, J):
                if (j == 0):
                    D[k, j] = D[k - 1, j] + d[k, j]
                else:
                    path1 = D[k, j - 1] + d[k, j]
                    path2 = D[k - 1, j - 1] + 2.0 * d[k, j]
                    path3 = D[k - 1, j] + d[k, j]
                    D[k, j] = min([path1, path2, path3])
    else:
        for k in range(I, J):
            for i in range(0, I):
                if (i == 0):
                    D[i, k] = D[i, k - 1] + d[i, k]
                else:
                    path1 = D[i - 1, k] + d[i, k]
                    path2 = D[i - 1, k - 1] + 2.0 * d[i, k]
                    path3 = D[i, k - 1] + d[i, k]
                    D[i, k] = min([path1, path2, path3])
    # Path correspondance
    phi_x = [0]
    phi_y = [0]
    while ((phi_x[-1] != I - 1) or (phi_y[-1] != J - 1)):
        i = phi_x[-1]
        j = phi_y[-1]
        if (i == I - 1):
            for k in range(j + 1, J):
                phi_x.append(I - 1)
                phi_y.append(k)
        if (j == J - 1):
            for k in range(i + 1, I):
                phi_x.append(k)
                phi_y.append(J - 1)
        if ((j < J - 1) and (i < I - 1)):
            if (D[i + 1, j + 1] == min([D[i + 1, j], D[i, j + 1], D[i + 1, j + 1]])):
                phi_x.append(i + 1)
                phi_y.append(j + 1)
            elif (D[i + 1, j] == min([D[i + 1, j], D[i, j + 1], D[i + 1, j + 1]])):
                phi_x.append(i + 1)
                phi_y.append(j)
            else:
                phi_x.append(i)
                phi_y.append(j + 1)
    return (D, phi_x, phi_y)
