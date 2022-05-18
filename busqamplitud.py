
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

    def getNodo(self):
        return self.nodo

    def moverDerecha(self, posColum, posFil):
        movFila = posFil + 1
        self.matriz[posColum][posFil] = 10
        self.matriz[posColum][movFila] = 2
        self.operador = "Derecha"
        self.nodo = f"({posColum}, {movFila})"
        return self.matriz

    def moverIzquierda(self, posColum, posFil):
        movFila = posFil - 1
        self.matriz[posColum][posFil] = 10
        self.matriz[posColum][movFila] = 2
        self.operador = "Izquierda"
        self.nodo = f"({posColum}, {movFila})"
        return self.matriz

    def moverAbajo(self, posColum, posFil):
        movColum = posColum + 1
        self.matriz[posColum][posFil] = 10
        self.matriz[movColum][posFil] = 2
        self.operador = "Abajo"
        self.nodo = f"({movColum}, {posFil})"
        return self.matriz

    def moverArriba(self, posColum, posFil):
        movColum = posColum - 1
        self.matriz[posColum][posFil] = 10
        self.matriz[movColum][posFil] = 2
        self.operador = "Arriba"
        self.nodo = f"({movColum}, {posFil})"
        return self.matriz

    def verificar(self, posColum, posFil):
        movimientos = []

        movFilaIz = posFil - 1
        if movFilaIz >= 0:
            izquierda: int = self.matriz[posColum][movFilaIz]

            if(izquierda != 1 and izquierda != 10):
                movimientos.append(f"({posColum}, {movFilaIz})")
            elif izquierda == 5:
                movimientos.append(f"({posColum}, {movFilaIz})")
        


        movFilaDe = posFil + 1
        if movFilaDe >= 0:
            derecha: int = self.matriz[posColum][movFilaDe]

            if(derecha != 1 and derecha != 10):
                movimientos.append(f"({posColum}, {movFilaDe})")
            elif derecha == 5:
                movimientos.append(f"({posColum}, {movFilaDe})")

        movColumAbajo = posColum + 1
        if movColumAbajo >= 0:
            abajo: int = self.matriz[movColumAbajo][posFil]

            if(abajo != 1 and abajo != 10):
                movimientos.append(f"({movColumAbajo}, {posFil})")
            elif abajo == 5:
                movimientos.append(f"({movColumAbajo}, {posFil})")

        movColumArriba = posColum - 1
        if movColumArriba >=0:
            arriba: int = self.matriz[movColumArriba][posFil]

            if(arriba != 1 and arriba != 10):
                movimientos.append(f"({movColumArriba}, {posFil})")
            elif arriba == 5:
                movimientos.append(f"({movColumArriba}, {posFil})")

        return movimientos