'''
Clase:        Variables, tipos, entradas y salidas
Tema:         Variables
Ejercicio:    Uso de variables, entradas y salidas
Descripción:  Un ejercicio para calcular propinas, otro para generar un correo segun un nombre dado y otro para dividir 2 numeros y establecer la cantidad de decimales que mostrara

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-16
Estado:       [ Terminado ]
'''

#Ejercicio 1
print("Ejercicio 1")
cuenta = int(input("Cuenta total: $"))
porcentaje = int(input("Porcentaje de propina: "))

print(f"La propina es ${cuenta * (porcentaje/100)} y su total es ${cuenta + (cuenta * (porcentaje/100))}")

#Ejercicio 2
print("Ejercicio 2")
full_name = input("Ingrese su nombre completo: ").split()

if len(full_name) == 2:
    print(f"Su correo es {full_name[0].lower()}.{full_name[1].lower()}@keyinstitute.edu.sv")
elif len(full_name) == 4:
    print(f"Su correo es {full_name[0].lower()}.{full_name[2].lower()}@keyinstitute.edu.sv")
else:
    print("No cumple con el formato")

#Ejercicio 3
print("Ejercicio 3")

try:
    a = int(input("Ingrese un número entero: "))
    b = int(input("Ingrese otro número entero: "))
    k = int(input("Ingrese el numero de decimales: "))

    if k > 0: 
        if a%b == 0:
            division = a//b
            resultado = f"{division}." + "0" * k
            #resultado = str(a/b)+"0"*(k-1)
            
        elif a%b != 0:
            division = str(a/b) 
            enteros = len(str(a//b))
            resultado = ""
            for i in range(enteros):
                resultado += division[i]

            for i in range(k+1):
                try:    
                    resultado += division[i+enteros]
                except IndexError:
                    resultado += "0"*(k-i)
                    break

    
    elif k == 0:
        resultado = a//b

    elif k < 0:
        print("No puedes poner un negativo")
    
    print(resultado)
        
except ZeroDivisionError:
    print("No se puede dividir entre cero")

except ValueError:
    print("Escribe un numero")

except TypeError:
    print("No puedes poner un decimal en k")


#Ejercicio 1.4.2 Suma de cadenas de texto

a = "12345678901234567899"
b = "98765432109876543215"

a = a[::-1]
b = b[::-1]
c = 0
resultado = ""


for i,j in zip(a,b):
    i = int(i)
    j = int(j)
    suma = i + j + c
    if suma > 9:
        c = 1
        digito = str(suma-10)
    else:
        c = 0
        digito = str(suma)
    resultado = digito + resultado

print(resultado)
