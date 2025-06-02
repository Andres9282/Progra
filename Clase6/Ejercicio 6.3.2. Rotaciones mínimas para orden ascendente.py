'''
Clase:        6
Tema:         Manejo de listas
Ejercicio:    Rotaciones mínimas para orden ascendente
Descripción:  Dada una lista circular, determina cuántas rotaciones mínimas a la izquierda se necesitan para que esté en orden estrictamente ascendente. Si no es posible,imprime -1.

Autor:        Andres Arturo Marroquin Soto
Fecha:        2025-06-02
Estado:       [ Terminado ]
'''

entrada = (str(input())).split()
entrada = list(map(int, entrada))

orden = sorted(entrada)
orden = list(map(str, orden))

soy_necio = ""
for numero in orden:
    soy_necio += f"{numero}, "
soy_necio = soy_necio.strip(" ")
soy_necio = soy_necio.strip(",")

contador = None
for i in range (len(entrada)):
    vuelta = ""
    vuelta += str(entrada[i:])
    vuelta += str(entrada[:i])

    texto1 = ""
    for j in vuelta:
        if j == "[":
            texto1 += ", "
        else:
            texto1 += j
    texto1 = texto1.strip(",")
    texto1 = texto1.strip(" ")
            
    texto2 = ""
    for k in texto1:
        if not k == "]":
            texto2 += k

    if texto2 == soy_necio:
        contador = i
        break

if contador == None:
    print(-1)
else:
    print(contador)
