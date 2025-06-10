'''
Clase:        10
Tema:         Manejo de matrices
Ejercicio:    Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el usuario, verifica para cada celda de una matriz binaria cuántos elementos con valor de 1 hay en las celdas vecinas 
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-10
Estado:       [ Terminado ]
'''

n = int(input("Filas de la matriz: "))
m = int(input("Columnas de la matriz: "))

matriz = []
for filas in range(n):
    matriz.append(list(map(int, input("Numeros separados por comas: ").split(","))))
'''
matriz = [
    [1,0,1,1,1],
    [0,1,0,0,0],
    [0,0,1,0,1],
    [1,1,0,0,0]
]
'''
contador = []
for i in range (len(matriz)):
    cuenta_fila = []
    for j in range (len(matriz[i])):    
        Li = [i-1, i, i+1]
        Lj = [j-1, j, j+1]
        conteo = 0
        for k in Li :
            if k == -1 or  k == (len(matriz)):
                continue
            else: 
                for l in Lj:
                    if l == -1 or l == (len(matriz[i])) or (k == i and l == j):
                        continue   
                    elif  matriz[k][l] == 1: 
                        conteo += 1
            
        cuenta_fila.append(conteo)
    contador.append(cuenta_fila)

print(contador)