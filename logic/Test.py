tableroJugador = [[0, 0, 4, 4, 4, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                                                0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
tableroEnemigo = tableroJugador

def matarBarco(x:int, y:int, tab: list):
    if (tab[x-1][y-1] != 0 and tab[x-1][y-1] != -1):
        print('mató')
    elif (tab[x-1][y-1] == -1):
        print('pos ocupada')
        return
    
    tab[x-1][y-1] = -1


i = 0
for i in range(len(tableroJugador)):
    j = 0
    for j in range (len(tableroJugador)):
        if (tableroJugador[i][j] != 0 and tableroJugador[i][j] != -1):
            print("=falso")
            pass



matarBarco(2,1,tableroJugador)







