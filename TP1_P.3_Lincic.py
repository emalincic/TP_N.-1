# =============
# Tercera Parte
# =============

# Importaciones
import termcolor as tm
from termcolor import colored
import random
import time

# Aisignación de los elemntos
hg = tm.colored("▓▓", 'red') # Hormigas
free = tm.colored("▓▓", 'green') # Espacios libres/celda verde
food = tm.colored("▓▓", 'white', 'on_green') # Comida
already = tm.colored("▓▓", 'yellow') # Celdas ya pisadas por una hormiga
obs = tm.colored("▓▓", 'grey') # Obstáculos

# Inputs de asignación
dimensión = int(input('Ingrese la dimensión de la grilla, la misma será cuadrada, por lo tanto solo ingrese para un eje: '))
cant_hg = int(input('Ingrese la cantidad de hormigas que quieras que haya: '))
cant_fd = int(input('Ingrese la cantidad de comida que quieras que haya: '))
cant_obs = int(input('Ingrese la cantidad de obstáculos que quieras que haya: '))

grilla = []
def proceso_de_creacion_de_grilla(grilla, dimensión):
    """
    Esta función crea la grilla, primero se crea una lista vacia que va a representar una fila de la matriz, la misma se rellena con las celdas verdes 
    dependiendo de la dimensión asigana.
    Luego de crearla copia y pega la lista en la grilla, que al igual que la anterior, depende de la dimensión, debido a que es una matriz cuadrada.
    Entradas: Lista e Ints
    Salida: Ningún tipo de dato. Actualiza una lista definida anteriormente
    """
    filas = []
    # Se agrega a una fila las celdas verdes
    for ejex in range(dimensión):
        filas.append(free)
    # Se copia y se pega la fila en la lista matriz
    for ejey in range(dimensión):
        grilla.append(filas.copy())



def objetos(cantidad, tipo):
    """
    Luego de crear la grilla, se introducen los elemtes de la misma, para ello se elige dos números aleatorios entre 0 y la dimensión establecida,
    el primero representa la posición que tendra dentro de una fila y el segundo elige en que fila estará ese objeto, siempre y cuando la celda a remplazar
    esté ocupada por una celda verde.
    Entradas: Ints, Strings
    Salidas: Ningún tipo de dato. Actualiza una lista definida anteriormente
    """
    global dimensión
    cantidad2 = 0
    while True:
        # Elección números aleatorios
        x = random.randint(0, (dimensión - 1))
        y = random.randint(0,(dimensión - 1))
        # Si el usuario ingresa 0, el programa cierra la función
        if cantidad != 0:
            # Si la posición aleatoria es una celda verda, esta es reemplazada
            if grilla[x][y] == free:
                grilla[x][y] = tipo
                cantidad2 += 1
        else:
            break
        if cantidad == cantidad2:
            break


posiciones_hg = []
def posición_hormigas(grilla): 
    """
    Cuando se introducen todos los objetos, se guarda la posición de cada hormiga en una lista, y en base a ella se modifican y se realizan los movimientos.
    se utiliza enumerate para darle a cada valor una "identidad" o "identificación" que facilita la forma en que uno puede hacer para que la hormiga se mueva 
    entre las direcciones posibles.
    Entradas: Listas
    Salida: Ningún tipo de dato. Actualiza una lista definida anteriormente
    """
    # Asignación de una identifiación a cada fila de la matriz
    for idy,b in enumerate(grilla):
        # Aignación de una identificación a cada elemento de una fila
        for idx,d in enumerate(b):
            # Si se encuentra una hormiga, se guarda su posición
            if d == hg:
                posiciones_hg.append([idy,idx])





def arriba_abajo(i, y, grilla):
    """
    Esta función hace que la hormiga pueda moverse hacia arriba (anterior fila) o hacia abajo (siguiente fila), si y solo si, cuando esté permitido hacerlo.
    Se retorna verdadero o falso en caso de la condición se cumpla o no. Se utiliza y se actualiza la posición de cada hormiga.
    Entradas: Listas, Ints
    Salida: Bool
    """
    # Se crea la nueva posición.
    nueva_posy = i[0] + y
    # está serie de condicionales restringe el movimiento de la hormiga para que no se salga de los límites, ni tampoco pueda ponerse encima de otra hormiga ni obstáculo.
    if ((nueva_posy) < len(grilla)) and ((nueva_posy) > -1) and grilla[nueva_posy][i[1]] != hg and grilla[nueva_posy][i[1]] != obs:
        # Se reemplaza la nueva posicón por la hormiga
        grilla[nueva_posy][i[1]] = hg
        # donde estaba antes la hormiga, se cambia por una celda amarrilla, o sea, que ya estuvo ahí.
        grilla[i[0]][i[1]] = already
        # Se actualiza la nueva posición de la hormiga en la lista.
        i[0] = nueva_posy
        return True
    return False


def izquierda_derecha(i, x, grilla):
    """
    A diferencia de la anterior, esta hace que la hormiga se mueva hacia la defercha o izquierda., con las mismas condiciones.
    Entradas: Listas, Ints
    Salida: Bool
    """
    # Se crea la nueva posición.
    nueva_posx = i[1] + x
    # La misma serie de condicionales que el anterior.
    if nueva_posx < len(grilla) and nueva_posx > -1 and grilla[i[0]][nueva_posx] != hg and grilla[i[0]][nueva_posx] != obs:
        # Reemplazamiento
        grilla[i[0]][nueva_posx] = hg 
        # Se marca la celda original con una amarilla
        grilla[i[0]][i[1]] = already
        # Y se actualiza la lista
        i[1] = nueva_posx
        
        return True
    return False


def movimiento_hormigas(grilla): 
    """
    Esta función da la aleatoriedad del moviemnto de las hotmigas. 
    Se elige un valor -1 o 1, ese valor será la dirección que tomará la hormiga. Luego, se elige aleatoriamente si la hormiga se moverá hacia arriba/abajo
    o hacia la izquierda/derecha, en caso de que una no se pueda, hace la otra. (Para esto sirve los returns booleanos anteriores)
    Entradas: Lista
    Salida: Ningún tipo de dato. Llama a otas funciones.
    """
    moov = [-1,1]
    for i in posiciones_hg:    
        # Selección aleatoria de un número para moverse
        x = random.choice(moov)
        y = random.choice(moov)
        posibilidad = random.randint(0,1)
        if posibilidad == 1:
            if not arriba_abajo(i, y, grilla):
                izquierda_derecha(i, x, grilla)
        else:
            if not izquierda_derecha(i, x, grilla):
                arriba_abajo(i, y, grilla)


def simulaciones(simulaciones):
    """
    Se utiliza un formato parecido al de la parte anterior, para este caso las hormigas se mueven hasta que se alcance la cantidad de iteraciones
    aignadas por el usuario. 
    Al finalizar cada simulación se hace un conteo en toda la grilla de la cantidad de celdas amarillas, en cada simulación se registra esa cantidad en una lista,
    en la cual se la promedia con la cantidad de simulaciones hechas para dar una área recorrido promedio.
    Entrada: Int
    Salida: Ningún tipo de dato
    """
    simulación = 0
    area = []
    print(f'Simulaciones en Proceso')
    while simulación != simulaciones:
        # Reseteo de la grilla y las posiciónes de las hormigas, además del contador de cada itetación de cada simulación
        iteración = 0
        grilla.clear()
        posiciones_hg.clear()
        proceso_de_creacion_de_grilla(grilla, dimensión)
        objetos(cant_hg, hg)
        objetos(cant_fd, food)
        objetos(cant_obs, obs)
        posición_hormigas(grilla)
        while True:
            movimiento_hormigas(grilla)
            iteración += 1
            if iteración == 200:
                for i in grilla:
                    # Contador de la cantidad de celdas amarillas
                    recorrido = (i.count(already))
                    area.append(recorrido)
                break
        simulación += 1
    # Promedio entre el area de todas las simulaciones + la cantidad de hormigas por la cantidad de simulaciones
    total = ((sum(area)+(cant_hg*simulaciones))/simulaciones)
    print(f'{simulaciones} simulaciones terminadas\nArea recorrida promedio: {total:.2f}')
simulaciones(int(input('Ingrese la cantidad de simulaciones que desea hacer: ')))


