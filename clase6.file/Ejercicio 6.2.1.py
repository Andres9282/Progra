'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    Eliminando valores duplicados
Descripción:  Dada una lista por el usuario, elimina los valores duplicados y mantene el orden de aparición.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

lista = input("Ingrese una lista de números separados por espacios: ")


lista = lista.split()
lista2 = []

for i in lista:
    if i not in lista2:
        lista2.append(i)

print(lista2)

output = " ".join(lista2)
print(output)