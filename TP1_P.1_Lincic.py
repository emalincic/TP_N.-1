# =============
# Primera Parte
# =============


import termcolor as tm
import random
import time

hg = tm.colored("▓▓", 'red')
free = tm.colored("▓▓", 'green')
food = tm.colored("▓▓", 'white', 'on_green')
already = tm.colored("▓▓", 'yellow')
obs = tm.colored("▓▓", 'grey')


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
    """
    filas = []
    for ejex in range(dimensión):
        filas.append(free)
    for ejey in range(dimensión):
        grilla.append(filas.copy())


def objetos(cantidad, tipo):
    """
    Luego de crear la grilla, se introducen los elemtes de la misma, para ello se elige dos números aleatorios entre 0 y la dimensión establecida,
    el primero representa la posición que tendra dentro de una fila y el segundo elige en que fila estará ese objeto, siempre y cuando la celda a remplazar
    esté ocupada por una celda verde.
    """
    global dimensión
    cantidad2 = 0
    while True:
        x = random.randint(0, (dimensión - 1))
        y = random.randint(0,(dimensión - 1))
        if cantidad != 0:
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
    """
    # 
    for idy,b in enumerate(grilla):
        # 
        for idx,d in enumerate(b):
            if d == hg:
                posiciones_hg.append([idy,idx])





def arriba_abajo(i, y, grilla):
    """
    Esta función hace que la hormiga pueda moverse hacia arriba (anterior fila) o hacia abajo (siguiente fila), si y solo si, cuando esté permitido hacerlo.
    Se retorna verdadero o falso en caso de la condición se cumpla o no, ¿Pero, por qué? estos retorno se utilizarán para más adelante.
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
    """
    moov = [-1,1]
    for i in posiciones_hg:    
        x = random.choice(moov)
        y = random.choice(moov)
        posibilidad = random.randint(0,1)

        if posibilidad == 1:
            if not arriba_abajo(i, y, grilla):
                izquierda_derecha(i, x, grilla)
        else:
            if not izquierda_derecha(i, x, grilla):
                arriba_abajo(i, y, grilla)

proceso_de_creacion_de_grilla(grilla, dimensión)
objetos(cant_fd, food)
objetos(cant_obs, obs)
objetos(cant_hg, hg)
posición_hormigas(grilla)

movimiento = 0
while movimiento < 200:  
    """
    Acá lo que tenemos es que repite la función del movimiento de las hormigas las veces que el usuario lo pida/la cantidad de veces
    que estén ingresadas.
    Para la visualización de la grilla se utiliza un primer join que une todos los elemntos de la lista en un solo string y así con todas las demás.
    Y luego un segundo join que lo que hace es que para cada fila (o sea cada lista) las une con un salto de línea para darle la forma de grilla.
    """
    if movimiento > 0:               
        movimiento_hormigas(grilla)
    movimiento += 1
    grilla_organizada = '\n'.join(''.join(fila)for fila in grilla)
    time.sleep(0.25)
    print(f'{grilla_organizada}\n')