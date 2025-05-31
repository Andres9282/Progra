'''
Clase:        5
Tema:         Fase de fortalecimiento lógico
Ejercicio:    Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. 
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

number = str(input("Ingresa un numero: "))
print(f"\nProceso de reduccion para: {number}")

while len(number) > 1:
    sum = 0
    for i in number:
        i = int(i)
        sum += i

    print(f"{number} = {sum}")
    number = str(sum)

print(f"\nEl resultado final es: {number}")
    