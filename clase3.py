# Ejercicio 1
password = 'Poneme10'
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

# Ejercicio 2

number = 21

if number%7 == 0 and number%5 != 0:
    print("Es magico")
else: 
    print("No es magico")