'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    Sub arreglo con suma divisible
Descripción:  Dado un arreglo de enteros, encuentra el número de subarreglos contiguos cuya suma total es divisible por k.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''

entrada = str(input()).split()
entrada = list(map(int, entrada))
k = int(input())
conteo = 0
for i in range(len(entrada)):
    try:
        suma = entrada[i]+entrada[i+1]
        if suma%k == 0:
            conteo += 1
    except IndexError:
        if entrada[i]%k == 0:
            conteo += 1

print()
print(conteo)

    
