
class Barco:
    """
    La clase barco se utilizara para crear cada uno de ellos.
    Parametros:
    - nombre: Nombre asignado al Barco.
    - tamano: Cantidad de bloques que ocupa el barco en el tablero.
    Debe verificar que no sobrepase las dimensiones especificadas.
    """

    def __init__(self, nombre: str, tamano: int):
        self._name = nombre
        self._size = tamano

    def get_nombre(self):
        return self._name

    def get_size(self):
        return self._size
