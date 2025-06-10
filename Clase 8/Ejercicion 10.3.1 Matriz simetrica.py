'''
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el usuario, comprueba si la matriz cuadrada es simétrica respecto a su diagonal principal.
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-09
Estado:       [ Terminado ]
'''

matriz = []
n = int(input("Numero de filas para la matriz: "))
for i in range(n):
    fila = list(map(int, input("Ingresa los caracteres de la fila separados por espacios: ").split(",")))
    matriz.append(fila)

validador = None
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == matriz [j][i]:
            validador = "La matriz es simetrica"
        else:
            validador = "La matriz no es simetrica"
            break

print(validador)