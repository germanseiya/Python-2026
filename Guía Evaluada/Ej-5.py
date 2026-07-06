"""5. Escribir un programa que simule el movimiento de piezas en un tablero de ajedrez, mos-
trando gráficamente el estado del tablero (por consola) y registrando las piezas captu-
radas.
a) Inicialización del tablero
Crea un diccionario para el tablero cuyas claves sean las coordenadas en no-
tación algebraica (“a1”. . . “h8”) y cuyos valores sean el nombre de la pieza con
sufijo “B” (blancas) o “N” (negras), por ejemplo:
• Fila 1: “TorreB”, “CaballoB”, “AlfilB”, “ReinaB”, “ReyB”, “AlfilB”, “CaballoB”,
“TorreB”.
• Fila 8: “TorreN”, “CaballoN”, “AlfilN”, “ReinaN”, “ReyN”, “AlfilN”, “CaballoN”,
“TorreN”.
Consejo: Usar bucles anidados puede ser una solución.
b) Mapa de símbolos ASCII
Prepara un diccionario con el nombre simbolos que asocie cada pieza a un
carácter:
• Blancas: TorreB → R, CaballoB → N, AlfilB → B, ReinaB → Q, ReyB → K,
PeónB → P
• Negras: TorreN → r, CaballoN → n, AlfilN → b, ReinaN → q, ReyN → k,
PeónN → p
c) Mostrar el tablero dibujado
Cada turno, imprime en consola el tablero con filas numeradas (8 a 1) y colum-
nas encabezadas (a a h), usando:
• El símbolo correspondiente si la casilla está ocupada.
• Un punto . si la casilla está vacía. El tablero debe ser similar como se
muestra a continuación en la 2.1:
Figura 2.1: Ejemplo de salida por consola del tablero de ajedrez
d) Interacción con el usuario
Declara una lista vacía donde se almacenarán las piezas capturadas.
Debe existir una interacción con el usuario, es decir, solicitar por consola un
input para que el jugador ingrese la casilla de origen (pieza a seleccionar) y
una casilla de destino (donde se va a mover la pieza seleccionada).
e) Lógica de movimiento
Si en el tablero no existe la clave origen, muestra un mensaje de error y vuelve
a pedir movimiento.
Si existe:
• Extrae la pieza de origen.
• Si la pieza de origen se mueve a una casilla de destino donde existe una
pieza enemiga, añade la pieza rival a la lista capturadas y muestra un men-
saje similar a lo siguiente: “Capturó a PeonN en B5”.
f) Reporte tras cada turno
Redibuja el tablero con los cambios.
Imprime la lista capturadas (convertida a símbolos ASCII)."""

#Martín Aguirre y Germán Cortés

from colorama import init, Fore
init()

tablero = dict(
    letra = [" A ", " B ", " C ", " D ", " E ", " F ", " G ", " H "],
    uno = ["NT1", "NC1", "NA1", "NR ", "NK ", "NA2", "NC2", "NT2"],
    dos = ["NP1","NP2","NP3","NP4","NP5","NP6","NP7","NP8"],
    tres = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    cuatro = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    cinco = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    seis = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
    siete = ["BP1","BP2","BP3","BP4","BP5","BP6","BP7","BP8"],
    ocho = ["BT1", "BC1", "BA1", "BR ", "BK ", "BA2", "BC2", "BT2"]
)

tipos = ("letra","uno", "dos", "tres", "cuatro", "cinco", "seis","siete", "ocho")

for i in range(len(tablero)):
    total = tipos[i]
    print("-----------------------------------")
    print(f"{i} |{"|".join(tablero[total])}|")