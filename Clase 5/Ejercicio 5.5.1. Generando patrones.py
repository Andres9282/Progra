'''
Clase:        5
Tema:         Fase de fortalecimiento lógico
Ejercicio:    Generando patrones
Descripción:  Imprime el siguiente patrón usando bloques for/while 
Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-05-31
Estado:       [ En proceso ]
'''

for i in range (1,11):
    if i%2 != 0:
        guiones = "_-_-_"
    elif i%2 == 0:
        guiones = "-_-_-"

    if i <= 5:
        for j in range(1,6):
            if j%2 == 0:
                continue
            else:
                print(i, "*"*j)