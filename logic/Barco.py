from logic.Tablero import Tablero 


class Barco:
    """
    La clase barco se utilizara para crear cada uno de ellos.
    Parametros:
    - nombre: Nombre asignado al Barco.
    - tamano: Cantidad de bloques que ocupa el barco en el tablero.
    Debe verificar que no sobrepase las dimensiones especificadas.
    """
    def __init__(self, nombre : str, tamano : int):
        self._name = nombre
        self._size = tamano

    def getNombre(self):
        return self._name

    def getSize(self):
        return self._size

    def ubicar(self, tablero: Tablero,  tipo: int, x:int, y:int):
        # tipo = 1. vertical, 2. horizontal
        # Metodo utilizado para ubicar el en el tablero
        tablero.ubicar(self,x,y,tipo)

barco = Barco("Catalizador", 3)
nuevoTabler = Tablero()
barco.ubicar(nuevoTabler,2,3,4)
print(nuevoTabler.tableroJugador)