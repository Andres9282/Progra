import numpy as np

#Caso de Estudio: Consumo Energetico
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])
'''
print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miércoles (día 3):", consumo[:, 2])
'''

#Introduccion al Analisis Estadistico
promedio_por_hogar = np.mean(consumo, axis = 1)

promedio_por_dia = np.mean(consumo, axis = 0)

total_consumo = np.sum(consumo)

maximos = np.max(consumo, axis = 1)

minimos = np.min(consumo, axis = 0)

desviacion = np.std(consumo)

consumo_total_hogar = np.sum(consumo, axis=1)

hogar_mayor_consumo = np.argmax(consumo_total_hogar)

hogar_mas_eficiente = np.argmin(consumo_total_hogar)

#Transformaciones y filtros
consumo_total_hogar = np.sum(consumo, axis = 1)

altos = consumo_total_hogar > 100

consumo_mayor_100 = np.where(altos)[0]

consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())



'''
Cuestionario
Instrucciones:
Responde cada pregunta escribiendo el código necesario para obtener la respuesta.
Agrega también comentarios o respuestas escritas cuando se solicite explicación.
No borres las secciones anteriores del archivo python desarrollado para esta guía de trabajo, simplemente agrega tus respuestas al final.
Puedes auxiliarte de tu herramienta IA preferida, pero recuerda las buenas prácticas para su uso. Somos responsables de comprender el resultado.
'''

#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5_dia5 = consumo[4]
print("1.", consumo_hogar5_dia5[4])

#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
print("2.", consumo[-3:,6])

#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
dias = np.array([5, 6])
promedio_fin_semana = np.mean([consumo[:,dias]])
print("3.", promedio_fin_semana)

#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviacion = np.std(consumo, axis = 0)
print("4.", np.argmax(desviacion))

#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
consumo_hogar = np.sum(consumo, axis = 1) 
menor_a_mayor = np.argsort(consumo_hogar)
print("5.", menor_a_mayor[:3])

#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
consumo_casa3 = np.sum(consumo[2])
print("6.", consumo_casa3*1.10)