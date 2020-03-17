"""
Script to run examples of DWT
"""

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np

from math import pi

from simple_DTW import ex_5_2

# Plot example of use of DTW for a numeric 1-D signal

x = np.cos(2.0 * pi * np.power(3.0 * np.arange(1, 1001) / 1000.0, 2.0))
y = np.cos(2.0 * pi * 9.0 * np.arange(1, 401) / 400.0)

(D, phi_x, phi_y) = ex_5_2(x, y)
T = len(phi_x)

params = {'legend.fontsize': 24, \
          'xtick.labelsize':24, \
          'ytick.labelsize':24}
pylab.rcParams.update(params)
plt.figure(1, figsize=(30, 10))
plt.plot(phi_x, x[phi_x], 'b-', label='x')
plt.plot(phi_y, 3.0 + y[phi_y], 'r-', label='y')
for i in range(0, T, 50):
    plt.plot([phi_x[i], phi_y[i]], [x[phi_x[i]], 3.0 + y[phi_y[i]]], 'k--')
plt.xlabel('Time', fontsize=24)
plt.legend(loc=1)
plt.title('Dynamic Time Warping', fontsize=30)
plt.savefig('figures/simple_DTW.eps', format='eps')
plt.close(1)
