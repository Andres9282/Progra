'''
Clase:        5
Tema:         Fase de fortalecimiento lógico
Ejercicio:    Suma de valores
Descripción:  Dada una lista de longitud variable de números enteros ingresada por el usuario, calcula e imprime la suma de todos los números usando un bucle for.
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

numbers = input("Ingrese una lista de números enteros separados por espacios: ")
sum = 0

for i in numbers.split():
        i = int(i)
        sum += i

print(sum)