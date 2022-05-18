import numpy as np
from busqamplitud import BusquedaAmplitud

A = np.loadtxt('matriz.txt',dtype=int)

print(A)
print("")

def encontrarJugador():
    cordenadasJugador = []
    colum: int
    fil: int 
    for columnas in range(len(A[0])):
        for filas in range(len(A)):
            if A[columnas][filas] == 2:
                colum = columnas
                fil = filas
    cordenadasJugador.append(colum)
    cordenadasJugador.append(fil)
    return cordenadasJugador

busqAmp = BusquedaAmplitud(A, "as", 0)

def busqueda_por_amplitud():
    print("")
    m = busqAmp.getMatriz()
    mo = busqAmp.verificar(encontrarJugador()[0], encontrarJugador()[1])
    print(mo)
    movD = busqAmp.moverIzquierda(encontrarJugador()[0], encontrarJugador()[1])
    print(movD)
    print(busqAmp.getOperador())
    print(busqAmp.getNodo())
    print("")
    mo = busqAmp.verificar(encontrarJugador()[0], encontrarJugador()[1])
    print(mo)
    print("")
    movIz = busqAmp.moverIzquierda(encontrarJugador()[0], encontrarJugador()[1])
    print(movIz)
    print(busqAmp.getOperador())
    print(busqAmp.getNodo())
    mo = busqAmp.verificar(encontrarJugador()[0], encontrarJugador()[1])
    print(mo)
    #movIzz = busqAmp.moverArriba(encontrarJugador()[0], encontrarJugador()[1])
    #print(movIzz)
    #print(busqAmp.getOperador())
    #print(busqAmp.getNodo())
    #mo = busqAmp.verificar(encontrarJugador()[0], encontrarJugador()[1])
    #print(mo)


