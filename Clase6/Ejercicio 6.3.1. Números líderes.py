'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    Numeros lideres
Descripción:  Un numero de la lista es lider si es mayor que todos los numeros a su derecha.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

lista = input("Ingrese una lista de números separados por espacios: ")

lista = lista.split()
lista_int = []
for i in lista :
    i = int(i)
    lista_int.append(i)

lista = lista_int
    
lideres = []
for i in range(len(lista)):
    lista2 = lista[i:]
    if lista[i-1] > max(lista2):
        lideres.append(lista[i-1])

lideres_str = []
for i in lideres:
    i = str(i)
    lideres_str.append(i)

lideres = ' '.join(lideres_str)
print(lideres)
    
