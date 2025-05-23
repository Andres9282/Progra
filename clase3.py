'''
Clase:        Bloque condicional
Tema:         Operadores condicionales
Ejercicio:    Uso de if, elif, else, and, or, not
Descripción:  Ejercicios de verificar seguridad de contraseña y otro que identifica si un número es mágico.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''

# Ejercicio 1
password = 'Pongame10porfa'
upper = 0
digit = 0 

for i in password:
    if i.isdigit():
        digit += 1
    if i.isupper():
          upper += 1

if upper > 0 and digit > 0 and len(password) >= 8:
    print("Contraseña es segura")
else: 
    print("Contraseña no es segura")

#Ejercicio 2

consumo = 150
if consumo <= 100:
    print("Sin impuesto")
elif consumo > 100 and consumo <= 200:
    print(f"Su impuesto a pagar es ${consumo*0.5}")
elif consumo > 200:
    print(f"Su impuesto a pagar es ${consumo*0.7}")

# Ejercicio 3

number = 21
if number%7 == 0 and number%5 != 0:
    print("Es magico")
else: 
    print("No es magico")

# Ejercicio 4

year = 2024
if year%4 == 0 or (year%100 == 0 and year%400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

# Ejercicio 5

elevadorA, elevadorB, piso = 8, 10, 9

if elevadorA == elevadorB:
    print("Elevador A")
elif (elevadorA - piso)**2 < (elevadorB - piso)**2:
    print("Elevador A")
elif (elevadorA - piso)**2 > (elevadorB - piso)**2:
    print("Elevador B")
else:
    print("Elevador A")

# Ejercicio 6

x , y = 10, 2

if x > 0 and y > 0:
    estado = "Peligro"

if x**2 + y**2 <= 25:
    estado = "Peligro"
else:
    estado = "Seguro"
print(estado)