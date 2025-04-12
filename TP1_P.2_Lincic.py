# =============
# Segunda Parte 2
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
    Salida: Ningún tipo de dato. Actualiza una lista definida anteriormente
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




comida = 0
def arriba_abajo(i, y, grilla):
    """
    Esta función hace que la hormiga pueda moverse hacia arriba (anterior fila) o hacia abajo (siguiente fila), si y solo si, cuando esté permitido hacerlo.
    Se retorna verdadero o falso en caso de la condición se cumpla o no, ¿Pero, por qué? estos retorno se utilizarán para más adelante.
    Por otra parte, se utiliza un contador para saber cuando una hormiga comió y además a otro contador se le suma cuando la hormiga se mueve.
    Entradas: Listas, Ints
    Salida: Ningún tipo de dato. Actualiza listas definidas anteriormente
    """
    global comida, pasos_it
    # Se crea la nueva posición
    nueva_posy = i[0] + y
    # Cadena de condiciones para que la hormiga se mueva
    if ((nueva_posy) < len(grilla)) and ((nueva_posy) > -1) and grilla[nueva_posy][i[1]] != hg and grilla[nueva_posy][i[1]] != obs:
        # Si la nueva posición estaba ocipada por comida, se suma un 1 a un contador
        if grilla[nueva_posy][i[1]] == food:
            comida += 1
        # Se reemplaza la nueva posición por la hormiga
        grilla[nueva_posy][i[1]] = hg
        # Se cambia donde etsaba la hormiga por una celda amarilla
        grilla[i[0]][i[1]] = already
        # Se actualiza la posición
        i[0] = nueva_posy
        # Contador de que la hormiga hizo un paso
        pasos_it += 1
        return True
    return False


def izquierda_derecha(i, x, grilla):
    """
    A diferencia de la anterior, esta hace que la hormiga se mueva hacia la defercha o izquierda., con las mismas condiciones.
    Entradas: Listas, Ints
    Salida: Ningún tipo de dato. Actualiza listas definidas anteriormente
    """
    global comida, pasos_it
    # Se crea la nueva posición
    nueva_posx = i[1] + x
    # Cadena de condiciones para que la hormiga se mueva
    if nueva_posx < len(grilla) and nueva_posx > -1 and grilla[i[0]][nueva_posx] != hg and grilla[i[0]][nueva_posx] != obs:
        # Si la nueva posición estaba ocipada por comida, se suma un 1 a un contador
        if grilla[i[0]][nueva_posx] == food:
            comida += 1
        # Se reemplaza la nueva posición por la hormiga
        grilla[i[0]][nueva_posx] = hg 
        # Se cambia donde etsaba la hormiga por una celda amarilla
        grilla[i[0]][i[1]] = already
        # Se actualiza la posición
        i[1] = nueva_posx
        # Contador de que la hormiga hizo un paso
        pasos_it += 1
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
        # Posibilidad de movimientos
        if posibilidad == 1:
            if not arriba_abajo(i, y, grilla):
                izquierda_derecha(i, x, grilla)
        else:
            if not izquierda_derecha(i, x, grilla):
                arriba_abajo(i, y, grilla)


def simulaciones(simulaciones):
    """
    Por último, tenemos la función simulaciones que lo que hace es repetir todo el código las veces que el usuario lo indique.
    Cada simulación termina cuando el contador anterior de comida es igual a la mitad de la cantidad de comida ingresada por el usuario.
    Por otra parte, en cada simulación se suman la cantidad de veces que las hormigas se movieron en cada iteración, a una lista la cual se hace el promedio.
    Entrada: Ints
    Salida: Ningún tipo de dato
    """
    global comida, pasos_it
    simulación = 0
    cant_pasos = []
    print(colored('En caso de que el programa se quede precesando en una simulación durante demasiado tiempo (10 segundos) reiniciar el programa', 'red'))
    while simulación != simulaciones:
        print(f'Simulación número {simulación + 1} en proceso')
        # Se resetea la grilla y la posición de las hormigas
        grilla.clear()
        posiciones_hg.clear()
        # Se llama de vuelta a las demás funciones
        proceso_de_creacion_de_grilla(grilla, dimensión)
        objetos(cant_hg, hg)
        objetos(cant_fd, food)
        objetos(cant_obs, obs)
        posición_hormigas(grilla)
        # Contadores generales de los pasos y comidas por simulación
        pasos_gen = 0
        comida = 0
        while True:
            # Contador por iteración de pasos
            pasos_it = 0
            movimiento_hormigas(grilla)
            # por iteración se suma los pasos a la cantidad de pasos por simulación
            pasos_gen += pasos_it
            # Condición de cuando termina una simulación
            if comida >= int(cant_fd/2):
                print(f'Simulación número {simulación + 1} terminada')
                simulación += 1
                break
        # se hace el promedio entre los pasos por simulación y la cantidad de hormigas
        cant_pasos.append(((pasos_gen/cant_hg)))
    # Se hace el promedio de la cantidad de pasos por simulación y la cantidad de simulaciones
    prom = (sum(cant_pasos)/len(cant_pasos))
    print(f'Pasos promedio: {prom:.2f}\nPasos mínimos: {min(cant_pasos):.2f}\nPasos máximos: {max(cant_pasos):.2f}')
simulaciones(int(input('Ingrese la cantidad de simulaciones que desea hacer: ')))


