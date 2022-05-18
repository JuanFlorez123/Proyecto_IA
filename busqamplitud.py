
class BusquedaAmplitud():
    operador: str

    def __init__(self, matriz, nodo: str, profundidad: int):
        self.matriz = matriz
        self.nodo = nodo
        
        self.profundidad = profundidad

    def getMatriz(self):
        return self.matriz

    def getOperador(self):
        return self.operador

    def moverDerecha(self, posColum, posFil):
        self.matriz[posColum][posFil] = 0
        self.matriz[posColum][posFil+1] = 2
        self.operador = "->"
        return self.matriz

    def moverIzquierda(self, posColum, posFil):
        self.matriz[posColum][posFil] = 0
        self.matriz[posColum][posFil+1] = 2
        self.operador = "<-"
        return self.matriz