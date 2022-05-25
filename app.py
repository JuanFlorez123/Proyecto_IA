import numpy as np
from busqamplitud import BusquedaAmplitud

A = np.loadtxt('matriz.txt',dtype=int)

print(A)
print("")

class amplitud():
    pass   

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
verificacionInicial = busqAmp.verificar(encontrarJugador()[0], encontrarJugador()[1])

def busqueda_por_amplitud(mov, cont):
    if cont < 19:
        #print(busqAmp.mover(mov,encontrarJugador()[0], encontrarJugador()[1]))
        #print(busqAmp.getMatriz())
        mo = busqAmp.verificar(encontrarJugador()[0], encontrarJugador()[1])
        cont = cont + 1
        #print(mo)
        #print(busqAmp.getNodo())
        #print(busqAmp.getOperador())
        busqueda_por_amplitud(mo, cont)
    
    else:
        return 

def mainLopp():
    busqueda_por_amplitud(verificacionInicial, 0)
    mo = busqAmp.verificar(9,1)
    busqAmp.mover(mo,encontrarJugador()[0], encontrarJugador()[1])
    print(mo)


