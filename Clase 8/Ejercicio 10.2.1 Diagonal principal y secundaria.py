'''
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el usuario, crea dos listas, una con los elementos de la diagonal principal y la otra con los elementos de la diagonal secundaria.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-09
Estado:       [ Terminado ]
'''

matriz = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]

mayor = "Los valores en la diagonal mayor son: "
menor = "Los valores en la diagonal menor son: "
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            mayor += f"{matriz[i][j]} "
        elif i + j == len(matriz[i])-1:
            menor += f"{matriz[i][j]} "


print(mayor)
print(menor)

