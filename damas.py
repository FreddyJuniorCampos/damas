import os

# Funcion para imprimir el tablero, antes de imprimir limpia la terminal.
def imprimir_tablero(): 
        os.system('clear')
        for fila in tablero:
            print(fila)

# Validación de que el numero de jugadas sea un numero entero
def validar_numero_jugadas(numero_jugadas):
    try:
        numero_jugadas = int(numero_jugadas)
    except ValueError:
        print('El numero de jugadas debe ser un numero entero.')
        return False

    return True
    
# Se valida la entrada por teclado para realizar los movimientos de las fichas
def validar_entrada(movimiento):
    # La entrada no puede contener masd de dos caracteres.
    if len(movimiento) != 2:
        print("Jugada invalida, solo puede tener dos caracteres")
        return False

    # Representación numérica de los caracteres
    caracter_1 = ord(movimiento[0].upper()) - 64
    if caracter_1 < 0 or caracter_1 > 8:
        print(f'El caracter {movimiento[0]} debe ser una letra entre A y H')
        return False

    try:
        caracter_2 = int(movimiento[1])
    except ValueError:
        print(f'El caracter {movimiento[1]} debe ser un número')   
        return False

    if caracter_2 < 0 or caracter_2 > 8:
        print(f'El caracter {movimiento[1]} debe estar entre 1 y 8')
        return False
    
    return True

def validar_jugada(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4):
    valor_1 = tablero[caracter_1][caracter_2]
    valor_2 = tablero[caracter_3][caracter_4]

    # Se valida que la casilla destino no esté ocupada
    if valor_2 != '0':
        print('La casilla destino está ocupada, debe elegir otra casilla libre.')
        return False

    # Se llama una funcion para validar las jugadas correctas para el jugador "X"
    if turno == 'X':
        if not validar_jugada_X(valor_1, caracter_1, caracter_2, caracter_3, caracter_4):
            return False

        return True

    else:
        if not validar_jugada_Y(valor_1, caracter_1, caracter_2, caracter_3, caracter_4):
            return False

        return True

def validar_jugada_X(valor_1, caracter_1, caracter_2, caracter_3, caracter_4):
    
    # Se valida que la ficha seleccionada pertenezca al jugador
    if valor_1 != 'X':
        print('La ficha seleccionada no es de tu pertenencia, elige una "X".')
        return False

    # Se verifica si el movimiento es solo en diagonal 
    if abs(caracter_1 - caracter_3) != abs(caracter_2 - caracter_4): 
        print('Solo se puede jugar en diagonal.')
        return False

    # Se valida que el jugador solo pueda jugar hacia adelante
    coordenada_x, coordenada_y = direccion_movimiento(caracter_1, caracter_2, caracter_3, caracter_4)
    if coordenada_y < 0: 
        print('Usted no puede jugar en esta dirección.')
        return False
    
    return True

def validar_jugada_Y(valor_1, caracter_1, caracter_2, caracter_3, caracter_4):
    
    # Se valida que la ficha seleccionada pertenezca al jugador
    if valor_1 != 'Y':
        print('La ficha seleccionada no es de tu pertenencia, elige una "Y".')
        return False

    # Se verifica si el movimiento es solo en diagonal 
    if abs(caracter_1 - caracter_3) != abs(caracter_2 - caracter_4): 
        print('Solo se puede jugar en diagonal.')
        return False

    # Se valida que el jugador solo pueda jugar hacia adelante
    coordenada_x, coordenada_y = direccion_movimiento(caracter_1, caracter_2, caracter_3, caracter_4)
    if coordenada_y > 0: 
        print('Usted no puede jugar en esta dirección.')
        return False
    
    return True

# Funcion que obtiene las coordenadas de la ficha a se comida
def coordenadas_ficha_comida(caracter_1, caracter_2, caracter_3, caracter_4):
    coordenada_x, coordenada_y = direccion_movimiento(caracter_1, caracter_2, caracter_3, caracter_4) 
    if coordenada_x > 0 and coordenada_y > 0:
        caracter_6 = caracter_4 - 1 # Si la jugada es Arriba y a la Derecha,
        caracter_5 = caracter_3 - 1 # resta un valor al caracter 4 y caracter 3

    elif coordenada_x < 0 and coordenada_y > 0: 
        caracter_6 = caracter_4 + 1 # Si la jugada es Arriba y a la Izquierda,
        caracter_5 = caracter_3 - 1 # se suma un valor al caracter 4 y se resta un valor al caracter 3

    elif coordenada_x < 0 and coordenada_y < 0: 
        caracter_6 = caracter_4 + 1 # Si la jugada es Abajo y a la Izquierda,
        caracter_5 = caracter_3 + 1 # se suma un valor al caracter 3 y al caracter 4

    elif coordenada_x > 0 and coordenada_y < 0: 
        caracter_6 = caracter_4 - 1 # Si la jugada es Abajo y a la Derecha,
        caracter_5 = caracter_3 + 1 # se resta un valor al caracter 4 y caracter 3

    return caracter_5, caracter_6 

# Funcion que determina la distancia del movimiento
def distancia(caracter_1, caracter_3):
    valor_distancia = abs(caracter_3 - caracter_1)
    
    return valor_distancia


# Funcion que determina la dirección del movimiento
def direccion_movimiento(caracter_1, caracter_2, caracter_3, caracter_4):
    coordenada_x = (caracter_4 - caracter_2)/distancia(caracter_2, caracter_4)
    coordenada_y = (caracter_3 - caracter_1)/distancia(caracter_2, caracter_4)

    return coordenada_x, coordenada_y

def jugada(movimiento):
    # Se invierten los caracteres para que coincidan con el formato de la matriz tablero
    caracter_1 = int(movimiento[1])
    caracter_2 = ord(movimiento[0].upper()) - 64

    return caracter_1, caracter_2

# Funcion que realiza una jugada simple
def realizar_jugada_simple(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4):
    tablero[caracter_1][caracter_2] = '0'
    if turno == 'X':
        tablero[caracter_3][caracter_4] = 'X'
    else:
        tablero[caracter_3][caracter_4] = 'Y'
    
    return True

# Funcion que realiza una jugada especial
def realizar_jugada_especial(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4, caracter_5, caracter_6):
    tablero[caracter_1][caracter_2] = '0'
    tablero[caracter_5][caracter_6] = '0'
    if turno == 'X':
        tablero[caracter_3][caracter_4] = 'X'
    else:
        tablero[caracter_3][caracter_4] = 'Y'
    
    return True
       
def main():
    # Se declara el numero de jugadas maximas
    numero_jugadas = input('Ingrese el numero de jugadas: ')
    while validar_numero_jugadas(numero_jugadas) == False: 
        numero_jugadas = input('Ingrese el numero de jugadas: ')

    numero_jugadas = int(numero_jugadas)
    imprimir_tablero()
    
    while(numero_jugadas != 0):
        jugada_realizada = False
        while(jugada_realizada == False):
            print(f'Numero de jugadas restantes: {numero_jugadas}')
            print('Turno de X')
            turno = 'X'
            movimiento = input('Ingrese la ficha a jugar: ')
            # Se valida que la entrada de teclado sea valida
            while validar_entrada(movimiento) == False:
                movimiento = input('Ingrese la ficha a jugar: ')

            # Se toman las coordenadas de la entrada por teclado para la ficha a jugar
            caracter_1, caracter_2 = jugada(movimiento)

            movimiento = input('Ingrese la casilla destino de su jugada: ')            
            while validar_entrada(movimiento) == False:
                movimiento = input('Ingrese la casilla destino de su jugada: ') 

            # Se toman las coordenadas de la entrada por teclado para la casilla destino de la jugada
            caracter_3, caracter_4 = jugada(movimiento)
            
            # Se realizan las validaciones de la rubrica del juego
            if not validar_jugada(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4):
                jugada_realizada = False
                continue

            valor_distancia = distancia(caracter_1, caracter_3)
            # Si el valor de la distancia es mayor a dos entonces es una jugada invalida, 
            # igual a 2 es una jugada especial (comiendo una ficha)
            # igual a 1 es una jugada simple
            if valor_distancia > 2:
                print('Jugada invalida, no puede moverse mas de 2 recuadros para comer o 1 recuadro para jugada simple.')
                continue
            
            elif valor_distancia == 2:
                caracter_5, caracter_6 = coordenadas_ficha_comida(caracter_1, caracter_2, caracter_3, caracter_4)
                valor_3 = tablero[caracter_5][caracter_6]
                # Se valida si en esas coordenadas hay una ficha que se pueda comer
                if valor_3 != 'Y':
                    print(f'En el recuadro {chr(caracter_6 + 64)}{str(caracter_5)} no hay una ficha contraria para comer')
                    continue

                # Se realiza la jugada luego de pasar todas las validaciones
                jugada_realizada = realizar_jugada_especial(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4, caracter_5, caracter_6)
            else:
                # Se realiza la jugada luego de pasar todas las validaciones
                jugada_realizada = realizar_jugada_simple(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4)

        imprimir_tablero()
        jugada_realizada = False
        while(jugada_realizada == False):
            print(f'Numero de jugadas restantes: {numero_jugadas}')
            print('Turno de Y')
            turno = 'Y'
            movimiento = input('Ingrese la ficha a jugar: ')
            # Se valida que la entrada de teclado sea valida
            while validar_entrada(movimiento) == False:
                movimiento = input('Ingrese la ficha a jugar: ')

            # Se toman las coordenadas de la entrada por teclado para la ficha a jugar
            caracter_1, caracter_2 = jugada(movimiento)

            movimiento = input('Ingrese la casilla destino de su jugada: ')            
            while validar_entrada(movimiento) == False:
                movimiento = input('Ingrese la casilla destino de su jugada: ') 

            # Se toman las coordenadas de la entrada por teclado para la casilla destino de la jugada
            caracter_3, caracter_4 = jugada(movimiento)

            # Se realizan las validaciones de la rubrica del juego
            if not validar_jugada(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4):
                jugada_realizada = False
                continue                

            valor_distancia = distancia(caracter_1, caracter_3)
            # Si el valor de la distancia es mayor a dos entonces es una jugada invalida, 
            # igual a 2 es una jugada especial (comiendo una ficha)
            # igual a 1 es una jugada simple
            if valor_distancia > 2:
                print('Jugada invalida, no puede moverse mas de 2 recuadros para comer o 1 recuadro para jugada simple.')
                continue
            
            elif valor_distancia == 2:
                caracter_5, caracter_6 = coordenadas_ficha_comida(caracter_1, caracter_2, caracter_3, caracter_4)
                valor_3 = tablero[caracter_5][caracter_6]
                # Se valida si en esas coordenadas hay una ficha que se pueda comer
                if valor_3 != 'X':
                    print(f'En el recuadro {chr(caracter_6 + 64)}{str(caracter_5)} no hay una ficha contraria para comer.')
                    continue
                
                # Se realiza la jugada luego de pasar todas las validaciones
                jugada_realizada = realizar_jugada_especial(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4, caracter_5, caracter_6)

            else:
                # Se realiza la jugada luego de pasar todas las validaciones
                jugada_realizada = realizar_jugada_simple(tablero, turno, caracter_1, caracter_2, caracter_3, caracter_4)
                
            imprimir_tablero()

        numero_jugadas -= 1

    piezas_X = 0
    piezas_Y = 0
    # Se cuenta el numero de fichas restantes para determinar el ganador
    for filas in tablero:
        piezas_X += filas.count('X')
        piezas_Y += filas.count('Y')

    if piezas_X == piezas_Y:
        print('Ambos jugadores terminaron con la misma cantidad de fichas, por tanto es un empate!')
        
    elif piezas_X > piezas_Y:
        print('El jugador de fichas X es el ganador!')

    else:
        print('El jugador de fichas Y es el ganador!')

    print(f'Fichas X: {piezas_X}')
    print(f'Fichas Y: {piezas_Y}')
    print('Gracias por participar.')

if __name__ == '__main__':
    # Cargamos valores iniciales del tablero
    tablero = [[' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['1', 'X', '0', 'X', '0', 'X', '0', 'X', '0'],]
    tablero += [['2', '0', 'X', '0', 'X', '0', 'X', '0', 'X'],['3', 'X', '0', 'X', '0', 'X', '0', 'X', '0']]
    tablero += [['4', '0', '0', '0', '0', '0', '0', '0', '0'], ['5', '0', '0', '0', '0', '0', '0', '0', '0']]
    tablero += [['6', '0', 'Y', '0', 'Y', '0', 'Y', '0', 'Y'], ['7', 'Y', '0', 'Y', '0', 'Y', '0', 'Y', '0']]
    tablero += [['8', '0', 'Y', '0', 'Y', '0', 'Y', '0', 'Y']]
    main()