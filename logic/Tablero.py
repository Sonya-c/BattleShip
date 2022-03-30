from numpy import append, true_divide
from pygame import init
from logic.Barco import Barco


class Tablero:
    tableroJugador = []
    tableroEnemigo = []

    def __init__(self):
        self.tableroJugador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.tableroEnemigo = self.tableroJugador

    def ubicar(self, barco: Barco, x: int, y: int, tipo: int):
        if tipo == 1:
            if (barco.getSize == 1):
                if (self.verificarCasillaDisponibleHorizontal(x, y, self.tableroJugador, barco.getSize)):
                    self.tableroJugador[x-1][y-1] = 1
                else:
                    print("Posición ocuupada")
            elif barco.getSize == 2:
                if self.verificarCasillaDisponibleHorizontal(x, y, self.tableroJugador, barco.getSize):
                    self.tableroJugador[x-1][y-1] = 2
                    self.tableroJugador[x][y-1] = 2
                else:
                    print("Posición ocupada")
            elif barco.getSize == 3:
                if self.verificarCasillaDisponibleHorizontal(x, y, self.tableroJugador, barco.getSize):
                    self.tableroJugador[x-1][y-1] = 3
                    self.tableroJugador[x][y-1] = 3
                    self.tableroJugador[x+1][y-1] = 3
                else:
                    print("Posición ocupada")
            elif barco.getSize == 4:
                if self.verificarCasillaDisponibleHorizontal(x, y, self.tableroJugador, barco.getSize):
                    self.tableroJugador[x-1][y-1] = 4
                    self.tableroJugador[x][y-1] = 4
                    self.tableroJugador[x+1][y-1] = 4
                    self.tableroJugador[x+2][y-1] = 4
                else:
                    print("Posición ocupada")
        else:
            if barco.getSize == 2:
                if self.verificarCasillaDisponibleVertical(x, y, self.tableroJugador, barco.getSize):
                    self.tableroJugador[x-1][y-1] = 2
                    self.tableroJugador[x-1][y] = 2
                else:
                    print("Posición ocupada")
            elif barco.getSize == 3:
                if self.verificarCasillaDisponibleVertical(x, y, self.tableroJugador, barco.getSize):
                    self.tableroJugador[x-1][y-1] = 3
                    self.tableroJugador[x-1][y] = 3
                    self.tableroJugador[x-1][y+1] = 3
                else:
                    print("Posición ocupada")
            elif barco.getSize == 4:
                if self.verificarCasillaDisponibleVertical(x, y, self.tableroJugador, barco.getSize):
                    self.tableroJugador[x-1][y-1] = 4
                    self.tableroJugador[x-1][y] = 4
                    self.tableroJugador[x-1][y+1] = 4
                    self.tableroJugador[x-1][y+2] = 4
                else:
                    print("Posición ocupada")

    def verificarCasillaDisponibleHorizontal(x: int, y: int, tablero: list, tam: int):
        if (tam == 1):
            if (tablero[x-1][y-1] == 0):
                return True
            return False
        elif tam == 2:
            if tablero[x-1][y-1] == 0 and x-1 <= 8:
                if tablero[x][y-1] == 0:
                    return True
                return False
            return False
        elif tam == 3:
            if tablero[x-1][y-1] == 0 and x-1 <= 7:
                if tablero[x][y-1] == 0 and tablero[x+1][y-1] == 0:
                    return True
                return False
            return False
        elif tam == 4:
            if tablero[x-1][y-1] == 0 and x-1 <= 6:
                if tablero[x][y-1] == 0 and tablero[x+1][y-1] == 0 and tablero[x+1][y-1]:
                    return True
                return False
            return False

    def verificarCasillaDisponibleVertical(x: int, y: int, tablero: list, tam: int):
        if tam == 2:
            if tablero[x-1][y-1] == 0 and y-1 <= 8:
                if tablero[x-1][y] == 0:
                    return True
                return False
            return False
        elif tam == 3:
            if tablero[x-1][y-1] == 0 and y-1 <= 7:
                if tablero[x-1][y] == 0 and tablero[x-1][y+1] == 0:
                    return True
                return False
            return False
        elif tam == 4:
            if tablero[x-1][y-1] == 0 and y-1 <= 6:
                if tablero[x-1][y] == 0 and tablero[x-1][y+1] == 0 and tablero[x-1][y+2]:
                    return True
                return False
            return False

