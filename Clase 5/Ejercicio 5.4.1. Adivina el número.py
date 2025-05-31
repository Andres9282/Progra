'''
Clase:        5
Tema:         Fase de fortalecimiento lógico
Ejercicio:    ¡Adivina el número!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine. El programa debe seguir pidiendo números hasta que acierte. En cadaintento fallido el programa notificará al usuario si el número secreto esmayor o menor al último valor ingresado.
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

import random

random_number = random.randint(1, 100)

while True:
    number = int(input("Ingresa un numero entre 1 y 100: "))
    if number == random_number:
        break
    elif number < random_number:
        print("El número es mayor")
    elif number > random_number:
        print("El número es menor")
print(f"¡Felicidades! Has adivinado el número secreto: {random_number}")
print("Fin del juego")


