# damas
Juego de Damas
El codigo es una versión básica del juego de Damas.

Las reglas del juego son:
Se juega en un tablero de 8x8 casilleros
Las fichas se deben mover de forma diagonal, una casilla a la vez (jugada simple), dos casillas cuando se come una ficha(jugada especial)
Los jugadores juegan un turno a la vez. 
Una ficha no se puede mover si está “bloqueada” es decir, que ya hay otra ficha en la 
ubicación donde se quiere mover. 
El tablero se numera desde el 1 al 8 en un eje, y de la letra A a la H en el otro eje. Una 
ficha determinada podría estar por ejemplo en la posición “E3”. 
Las fichas sólo pueden “avanzar”, las fichas "X" solo pueden bajar y las fichas "Y" solo pueden subir.
Los jugadores pueden “comer” la ficha de un adversario si es que está se encuentra 
“frente” a la ficha de él, en diagonal, y si es que hay un espacio vacío en la posición 
inmediata posterior. En este caso se “salta” la ficha. 
En esta versión gana el jugador que coma más fichas después de un número determinado 
de jugadas (que se ingresará como parámetro antes de iniciar el juego). 
El usuario debe ir ingresando en cada turno dos datos: La posición de la ficha original, y la 
posición deseada.  En el formato "D4" por ejemplo.
