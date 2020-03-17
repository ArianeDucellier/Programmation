"""
Scripts to visualize Internet traffic data
"""

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error

def aggregate(X, m):
    """
    Function to return aggregated time series

    Input:
        type X = numpy array
        X = Time series
        type m = integer
        m = Number of values for the aggregation
    Output:
        type Xm = numpy array
        Xm = Aggregated time series
    """
    N = len(X)
    N2 = int(N / m)
    X2 = X[0 : N2 * m]
    X2 = np.reshape(X2, (N2, int(m)))
    Xm = np.sum(X2, axis=1)
    return Xm

data = np.loadtxt('data/bpc10ms_1mn.dat')

params = {'legend.fontsize': 24, \
          'xtick.labelsize':24, \
          'ytick.labelsize':24}
pylab.rcParams.update(params)

# Plot data with different aggregation sizes
#plt.figure(1, figsize=(10, 12))
# 10 ms data counts
#X = np.copy(data)
#plt.subplot2grid((3, 1), (0, 0))
#plt.stem(0.01 * np.arange(0, len(X)), X, 'k-', markerfmt=' ', basefmt=' ')
#plt.xlim([-0.5, 0.01 * len(X) + 0.5])
#plt.ylabel('Nb packets', fontsize=24)
#plt.title('10 ms data counts', fontsize=24)
# 100 ms data counts
#X = aggregate(X, 10)
#plt.subplot2grid((3, 1), (1, 0))
#plt.stem(0.1 * np.arange(0, len(X)), X, 'k-', markerfmt=' ', basefmt=' ')
#plt.xlim([-0.5, 0.1 * len(X) + 0.5])
#plt.ylabel('Nb packets', fontsize=24)
#plt.title('100 ms data counts', fontsize=24)
# 1 s data counts
#X = aggregate(X, 10)
#plt.subplot2grid((3, 1), (2, 0))
#plt.stem(np.arange(0, len(X)), X, 'k-', markerfmt=' ', basefmt=' ')
#plt.xlim([-0.5, len(X) + 0.5])
#plt.xlabel('Time (s)', fontsize=24)
#plt.ylabel('Nb packets', fontsize=24)
#plt.title('1 s data counts', fontsize=24)
# Finalize
#plt.tight_layout()
#plt.savefig('figures/Figure1.eps', format='eps')
#plt.close(1)

# Plot variance with different aggregation sizes
#X = np.copy(data)
#N = len(X)
#m = np.array([1, 2, 3, 6, 10, 15, 25, 39, 63, 100])
#Vm = np.zeros(len(m))
#for i in range(0, len(m)):
#    N2 = int(N / m[i])
#    X2 = X[0 : N2 * m[i]]
#    X2 = np.reshape(X2, (N2, int(m[i])))
#    Xm = np.sum(X2, axis=1)
#    Vm[i] = np.var(Xm)
# Linear regression
#x = np.reshape(np.log10(m), (len(m), 1))
#y = np.reshape(np.log10(Vm / m), (len(m), 1))
#regr = linear_model.LinearRegression(fit_intercept=True)
#regr.fit(x, y)
#y_pred = regr.predict(x)
#R2 = r2_score(y, y_pred)
#H = 0.5 * (regr.coef_[0][0] + 1.0)
# Plot
#plt.figure(2, figsize=(12, 10))
#plt.plot(np.log10(m), np.log10(Vm / m), 'ko')
#plt.plot(x, y_pred, 'r-')
#plt.xlabel('Frame size', fontsize=24)
#plt.ylabel('Interframes variance normalized by frame size', fontsize=24)
#xticks = np.array([2, 5, 10, 20, 50, 100])
#xticks_labels = []
#for x in xticks:
#    xticks_labels.append('{:d}'.format(x))
#yticks = np.array([2, 5, 10, 20])
#yticks_labels = []
#for y in yticks:
#    yticks_labels.append('{:.2e}'.format(y))
#plt.xticks(np.log10(xticks), xticks_labels)
#plt.yticks(np.log10(yticks), yticks_labels)
#plt.title('H = {:4.2f} - R2 = {:4.2f}'.format(H, R2), fontsize=24)
#plt.tight_layout()
#plt.savefig('figures/Figure2.eps', format='eps')
#plt.close(2)

# Plot complementary distribution function
threshold = np.arange(1, 20)
proba = np.zeros(19)
for i in range(0, 19):
    proba[i] = np.sum(data >= threshold[i]) / np.sum(data)
plt.figure(2, figsize=(12, 10))
plt.plot(np.log10(threshold), np.log10(proba), 'k-')
plt.xlabel('Nb of packets per 10 ms', fontsize=24)
plt.ylabel('Probability', fontsize=24)
xticks = np.array([1, 5, 10, 19])
xticks_labels = []
for x in xticks:
    xticks_labels.append('{:d}'.format(x))
yticks = np.array([0.001, 0.002, 0.01, 0.02, 0.1, 0.2, 0.5,])
yticks_labels = []
for y in yticks:
    yticks_labels.append('{:.2e}'.format(y))
plt.xticks(np.log10(xticks), xticks_labels)
plt.yticks(np.log10(yticks), yticks_labels)
plt.title('Complementary distribution function', fontsize=24)
plt.tight_layout()
plt.savefig('figures/Figure3.eps', format='eps')
plt.close(3)
