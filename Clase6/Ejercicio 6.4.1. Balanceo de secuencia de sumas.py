'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    Balanceo de secuencia de sumas
Descripción:  Dado un arreglo de enteros, encuentra un índice i tal que la suma de los elementos desde el inicio hasta i sea igual a la suma desde i+1 hasta el final. Si no existe, imprime -1.
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''

lista = input().split()
lista = list(map(int, lista))

validador = -1
for i in range(len(lista)):
    suma1 = sum(lista[:i])
    suma2 = sum(lista[i:])

    if suma1 == suma2:
        validador = i-1

print(validador)
    