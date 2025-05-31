sudoku = []

for i in range (9):
    line = input()
    fila = [] 
    for i in line.split():
        i = int(i)
        fila.append(i)
    sudoku.append(fila)
    
for linea in sudoku:
    if sum(linea) != 45:
        validador = 'No valido'
        break
    else:
        validador = "Valido"
        
print("")
print(validador)
