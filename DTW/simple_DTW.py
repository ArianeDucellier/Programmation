""" Naive method to do Dynamic Time Warping """

import numpy as np

def DWT_vector(X, Y):
    """
    """
    assert np.shape(X)[0] < np.shape(Y)[Y], \
        'The first vector must be smaller than the second vector'
    n = np.shape(X)[0]
    p = np.shape(Y)[0]
    ix0 = 
    
def DWT_step_vector(X, Y):
    """
    """
    n = np.shape(X)[0]
    p = np.shape(Y)[0]
    L = n - p
    distance = np.zeros(L)
    for l in range(0, L + 1):
        Xl = np.concatenate(np.repeat(X[0], l + 1), \
            X[1:-1], np.repeat(X[-1], L - l + 1))