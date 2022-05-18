import numpy as np
from busqamplitud import BusquedaAmplitud

A = np.loadtxt('matriz.txt',dtype=int)

busqAmp = BusquedaAmplitud(A, "as", 0)
m = busqAmp.getMatriz()
movD = busqAmp.moverDerecha(2, 2)
print(movD)
print(busqAmp.getOperador())
#A[6][4] = 5
#print(A)
for columnas in range(len(A[0])):
    for filas in range(len(A)):
        if A[columnas][filas] == 2:
            print("")
            print(columnas)
            print(filas)
