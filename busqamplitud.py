
from importlib.util import set_loader


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
        meta: str = "0"

        movFilaIz = posFil - 1
        if movFilaIz >= 0:
            izquierda: int = self.matriz[posColum][movFilaIz]

            if(izquierda != 1 and izquierda != 10):
                movimientos.append("1")
            elif izquierda == 5:
                meta = "1"
            else:
                movimientos.append("0")
        else:
                movimientos.append("0")

        
        movColumArriba = posColum - 1
        if movColumArriba >=0:
            arriba: int = self.matriz[movColumArriba][posFil]

            if(arriba != 1 and arriba != 10):
                movimientos.append("1")
            elif arriba == 5:
                meta = "1"
            else:
                movimientos.append("0")
        
        else:
                movimientos.append("0")

        movFilaDe = posFil + 1
        if movFilaDe >= 0:
            derecha: int = self.matriz[posColum][movFilaDe]

            if(derecha != 1 and derecha != 10):
                movimientos.append("1")
            elif derecha == 5:
                meta = "1"
            else:
                movimientos.append("0")
        else:
                movimientos.append("0")



        movColumAbajo = posColum + 1
        if movColumAbajo >= 0:
            abajo: int = self.matriz[movColumAbajo][posFil]
            print(movColumAbajo, posFil)
            if(abajo != 1 and abajo != 10):
                movimientos.append("1")
            elif abajo == 5:
                meta = "1"
            else:
                movimientos.append("0")
        
        else:
                movimientos.append("0")

        movimientos.append(meta)
    
        return movimientos

    def mover(self, movimientos, posColum, posFil):
        matrizMovimientos:str = ""
        for mv in movimientos:
            matrizMovimientos += mv

        if matrizMovimientos == "10100":
            self.moverDerecha(posColum, posFil)
        
        if matrizMovimientos == "10010":
            self.moverIzquierda(posColum, posFil)
        
        if matrizMovimientos == "01000":
            self.moverArriba(posColum, posFil)

        if matrizMovimientos == "00100":
            self.moverDerecha(posColum, posFil)

        if matrizMovimientos == "01100":
            self.moverArriba(posColum, posFil)
        
        if matrizMovimientos == "10000":
            self.moverIzquierda(posColum, posFil)

        if matrizMovimientos == "00010":
            self.moverAbajo(posColum, posFil)

        return matrizMovimientos
