import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Load results dataset
data = pd.read_csv("../datasets/pit_stops_2021.csv") 

#-------------------------------------------------------------

result = data[(data['raceId'] == 1053) & (data['stop'] == 1)]
print(result)


df = pd.DataFrame(result)
Duracionmedia = df['milliseconds'].mean() /1000
print(Duracionmedia)

#-------------------------------------------------------------

result2 = data[(data['raceId'] == 1054) & (data['stop'] == 1)]
print(result2)


df = pd.DataFrame(result2)
Duracionmedia2 = df['milliseconds'].mean() / 1000
print(Duracionmedia2)

#-------------------------------------------------------------

result3 = data[(data['raceId'] == 1055) & (data['stop'] == 1)]
print(result3)


df = pd.DataFrame(result3)
Duracionmedia3 = df['milliseconds'].mean() /1000
print(Duracionmedia3)

#-------------------------------------------------------------

result4 = data[(data['raceId'] == 1056) & (data['stop'] == 1)]
print(result4)


df = pd.DataFrame(result4)
Duracionmedia4 = df['milliseconds'].mean() / 1000
print(Duracionmedia4)

#-------------------------------------------------------------

result5 = data[(data['raceId'] == 1057) & (data['stop'] == 1)]
print(result5)


df = pd.DataFrame(result5)
Duracionmedia5 = df['milliseconds'].mean() /1000
print(Duracionmedia5)

#-------------------------------------------------------------

result6 = data[(data['raceId'] == 1058) & (data['stop'] == 1)]
print(result6)


df = pd.DataFrame(result6)
Duracionmedia6 = df['milliseconds'].mean() / 1000
print(Duracionmedia6)

#-------------------------------------------------------------

result7 = data[(data['raceId'] == 1059) & (data['stop'] == 1)]
print(result7)


df = pd.DataFrame(result7)
Duracionmedia7 = df['milliseconds'].mean() /1000
print(Duracionmedia7)

#-------------------------------------------------------------

result8 = data[(data['raceId'] == 1060) & (data['stop'] == 1)]
print(result8)


df = pd.DataFrame(result8)
Duracionmedia8 = df['milliseconds'].mean() / 1000
print(Duracionmedia8)

#-------------------------------------------------------------

result9 = data[(data['raceId'] == 1061) & (data['stop'] == 2)]
print(result9)


df = pd.DataFrame(result9)
Duracionmedia9 = df['milliseconds'].mean() /1000
print(Duracionmedia9)

#-------------------------------------------------------------

result10 = data[(data['raceId'] == 1062) & (data['stop'] == 1)]
print(result10)


df = pd.DataFrame(result10)
Duracionmedia10 = df['milliseconds'].mean() / 1000
print(Duracionmedia10)

#-------------------------------------------------------------

result11 = data[(data['raceId'] == 1064) & (data['stop'] == 1)]
print(result11)


df = pd.DataFrame(result11)
Duracionmedia11 = df['milliseconds'].mean() /1000
print(Duracionmedia11)

#-------------------------------------------------------------

result12 = data[(data['raceId'] == 1065) & (data['stop'] == 1)]
print(result12)


df = pd.DataFrame(result12)
Duracionmedia12 = df['milliseconds'].mean() / 1000
print(Duracionmedia12)

#-------------------------------------------------------------

result13 = data[(data['raceId'] == 1066) & (data['stop'] == 1)]
print(result13)


df = pd.DataFrame(result13)
Duracionmedia13 = df['milliseconds'].mean() /1000
print(Duracionmedia13)

#-------------------------------------------------------------

result14 = data[(data['raceId'] == 1067) & (data['stop'] == 1)]
print(result14)


df = pd.DataFrame(result14)
Duracionmedia14 = df['milliseconds'].mean() / 1000
print(Duracionmedia14)

#-------------------------------------------------------------

result15 = data[(data['raceId'] == 1069) & (data['stop'] == 1)]
print(result15)


df = pd.DataFrame(result15)
Duracionmedia15 = df['milliseconds'].mean() /1000
print(Duracionmedia15)

#-------------------------------------------------------------

result16 = data[(data['raceId'] == 1070) & (data['stop'] == 1)]
print(result16)


df = pd.DataFrame(result16)
Duracionmedia16 = df['milliseconds'].mean() / 1000
print(Duracionmedia16)

#-------------------------------------------------------------

result17 = data[(data['raceId'] == 1071) & (data['stop'] == 1)]
print(result17)


df = pd.DataFrame(result17)
Duracionmedia17 = df['milliseconds'].mean() / 1000
print(Duracionmedia17)

#-------------------------------------------------------------

result18 = data[(data['raceId'] == 1072) & (data['stop'] == 1)]
print(result18)


df = pd.DataFrame(result18)
Duracionmedia18 = df['milliseconds'].mean() /1000
print(Duracionmedia18)

#-------------------------------------------------------------

result19 = data[(data['raceId'] == 1073) & (data['stop'] == 1)]
print(result19)


df = pd.DataFrame(result19)
Duracionmedia19 = df['milliseconds'].mean() / 1000
print(Duracionmedia19)

#-------------------------------------------------------------

#Definimos una lista con circuitos como string
circuitos = ['Emilia Romagna Grand Prix', 'Portuguese Grand Prix', 'Spanish Grand Prix', 'Monaco Grand Prix', 'Azerbaijan Grand Prix', 'Styrian Grand Prix', 'French Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 'Hungarian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix', 'Russian Grand Prix', 'Turkish Grand Prix', 'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix', 'Saudi Arabian Grand Prix', 'Abu Dhabi Grand Prix']
#Definimos una lista con tiempos como entero
tiempos = [Duracionmedia, Duracionmedia2, Duracionmedia3, Duracionmedia4, Duracionmedia5, Duracionmedia6, Duracionmedia7, Duracionmedia8, Duracionmedia9, Duracionmedia10, Duracionmedia11, Duracionmedia12, Duracionmedia13, Duracionmedia14, Duracionmedia15, Duracionmedia16, Duracionmedia17, Duracionmedia18, Duracionmedia19]

fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Tiempo de parada')
#Colocamos una etiqueta en el eje X
ax.set_title('Relacion entre tiempo de parada y Circuito')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'tiempo' como eje y.
plt.bar(circuitos, tiempos)
plt.savefig('barras_simple.png')
plt.xticks(rotation=90)
#Finalmente mostramos la grafica con el metodo show()
plt.show()

