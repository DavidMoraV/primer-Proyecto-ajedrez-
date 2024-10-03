def crear_tablero():
    # Crear un tablero vacío de 8x8
    tablero = [[" . " for _ in range(8)] for _ in range(8)]
    return tablero

def imprimir_tablero(tablero):
    # Imprimir la parte superior con las etiquetas de columnas
    print("     a   b   c   d   e   f   g   h")  # Etiquetas de columnas
    for i in range(8):
        # Imprimir cada fila con la etiqueta del número de fila a la izquierda
        print(8 - i, "|", " ".join(tablero[i]), "|", 8 - i) # Etiqueta de fila y contenido del tablero
    # Imprimir la parte inferior con las etiquetas de columnas
    print("     a   b   c   d   e   f   g   h")  # Etiquetas de columnas

def colocar_piezas_iniciales(tablero):
    # Colocar piezas blancas en su posición inicial
    piezas_blancas = ["","T","  ""C","  " "A","  " "D","  " "R","  " "A","  " "C","  " "T"" "]
    tablero[0] = piezas_blancas

def mover_pieza(tablero):
    while True:
        movimineto = input("Introduce tu movimineto (ej. Te5) o Fin para terminar: ")

def colocar_piezas_usuario(tablero):

def mostrar_menu():
    print("Elige una opción para iniciar el juego:")
    print("1. Posición estandar de partida de ajedrez")
    print("2. Posición por el usuario")
    print("3. Salir")

def main():
