'''
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    Identificando islas
Descripción:  Dada una matriz binaria ingresada por el usuario (0 = agua, 1 = tierra), cuenta la cantidad de islas disponibles. Una isla está formada por elementos con valor de 1 conectados horizontal o verticalmente.
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

n = int(input("Filas de la matriz: "))
m = int(input("Columnas de la matriz: "))
matriz = []

for filas in range(n):
    matriz.append(list(map(int, input("Numeros separados por comas: ").split(","))))

conteo_islas = 0
for i in range (len(matriz)):
    for j in range (len(matriz[i])):  
        if j  <= len(matriz[i])-1 and matriz[i][j] == 1:
            conteo_islas += 1
            if j > 0 and matriz[i][j-1] == 1:
                conteo_islas += -1

            elif i > 0 and matriz[i-1][j]:
                conteo_islas += -1

print(conteo_islas)