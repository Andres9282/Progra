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

    if k >= 0: 
        if a%b == 0:
            resultado = str(a//b) + "." + "0"*k 
            #resultado = str(a/b)+"0"*(k-1)
            
        elif a%b != 0:
            division = str(a/b) 
            resultado = f"{division[0]}."

            for i in range(k):
                try:    
                    resultado += division[i+2]
                except IndexError:
                    resultado += "0"*(k-i)
                    break
        print(resultado)
    
    elif k == 0:
        print(a//b)
    
    elif k < 0:
        print("Como va a tener decimales negativos pendejo")
        
except ZeroDivisionError:
    print("No se puede dividir entre cero")

except ValueError:
    print("Escribe un numero")

except TypeError:
    print("No puedes poner un decimal en k")

    