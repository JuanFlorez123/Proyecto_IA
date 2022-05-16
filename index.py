import numpy as np

A = np.loadtxt('matriz.txt',dtype=int)
A[6][4] = 5
print(A)