#calculo de los posibles sucesores.

#esposible
#sucesores
#listaAcciones
        
class nodo:
    def __init__(self, tablero, cartas, jugador):
        self.tablero = tablero
        self.cartas = cartas
        self.jugador = jugador

def imprimirTablero(nodo):
    for i in range(len(nodo_inicial.tablero)):
        for j in range(len(nodo_inicial.tablero)):
            print(nodo_inicial.tablero[i][j], end = " ")
        print("\n")

def listaAcciones(nodo, jugador):

    lista_acciones = []

    if jugador == 1:
        for i in range(2,4):
            for j in range(2, 6):
                lista_acciones.append(nodo.cartas[i][j])
    else:
        for i in range(0,2):
            for j in range(2, 6):
                lista_acciones.append(nodo.cartas[i][j])

    return lista_acciones



def succ(nodo): #esto esta mal
    #Tomo decision, jugador = 1, bot = 0    

    acciones = listaAcciones(nodo, nodo.jugador)
    nodos_sucesores = []
    for accion in acciones:
        if esposible(accion, nodo):
            nodoinicial = aplica(nodo,accion)
            nodos_sucesores.append(nodoinicial)
    return nodos_sucesores 


def esposible(accion, nodo):
    #accion va a ser un vector como [[2,3],[1,2]], [3,2]
    posicionX = accion[1][1]
    posicionY = accion[1][2]

    if nodo.tablero[posicionX][posicionY] == ' ':
        return True
    return False

def aplica(nodo, accion):
    posicion_inicioX = accion[0][1]
    posicion_inicioY = accion[0][2]

    posicion_destinoX = accion[0][1]
    posicion_destinoY = accion[0][2]


    #copiamos la ficha de las posiciones inicio
    ficha = nodo.tablero[posicion_inicioX][posicion_inicioY]
    nodo.tablero[posicion_inicioX][posicion_inicioY] = ' '
    
    #ponempos la ficha en la posicion destino
    nodo.tablero[posicion_destinoX][posicion_destinoY] = ficha

    return nodo
        
    
    
    

tablero_inicial = [['b','b','B','b','b'],['','','','',''],['','','','',''],['','','','',''],['w','w','W','w','w']]
cartas_iniciales = [ [0,3,[-1,0],[0,1],[0,-1],[0,0]],[0,10,[-2,1],[-1,-1],[1,-1],[2,1]],   [1,6,[2,0],[0,-1],[-2,0],[0,0]],[1,1,[1,1],[0,-1],[-1,1],[0,0]],[-1,12,[-1,1],[-1,0],[1,0],[1,-1]] ]
jugador = 0


nodo_inicial = nodo(tablero_inicial, cartas_iniciales, jugador)

lista_acciones_jugador1 = listaAcciones(nodo_inicial, jugador)
print(lista_acciones_jugador1)


#Tienes que cambiar la forma de tratar la accion


