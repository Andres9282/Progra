'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    Numeros lideres
Descripción:  Un numero de la lista es lider si es mayor que todos los numeros a su derecha.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

lista = input("Ingrese una lista de números separados por espacios: ").split()
lista = list(map(int, lista))
       
lideres = []
for i in range(len(lista)):
    lista2 = lista[i:]
    if lista[i-1] > max(lista2):
        lideres.append(lista[i-1])

lideres = list(map(str, lideres))
print(*lideres)