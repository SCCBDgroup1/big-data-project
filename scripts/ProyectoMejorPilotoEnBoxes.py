import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Load results dataset
data = pd.read_csv("../datasets/pit_stops_2021.csv") 


Ocon = data[(data['driverId'] == 839) & (data['stop'] == 1)]
print(Ocon)
df = pd.DataFrame(Ocon)
DuracionmediaOcon = df['milliseconds'].mean() /1000
print(DuracionmediaOcon)

Vettel = data[(data['driverId'] == 20) & (data['stop'] == 1)]
print(Vettel)
df = pd.DataFrame(Vettel)
DuracionmediaVettel = df['milliseconds'].mean() /1000
print(DuracionmediaVettel)

Schumacher = data[(data['driverId'] == 854) & (data['stop'] == 1)]
print(Schumacher)
df = pd.DataFrame(Schumacher)
DuracionmediaSchumacher = df['milliseconds'].mean() /1000
print(DuracionmediaSchumacher)

Mazepin = data[(data['driverId'] == 853) & (data['stop'] == 1)]
print(Mazepin)
df = pd.DataFrame(Mazepin)
DuracionmediaMazepin = df['milliseconds'].mean() /1000
print(DuracionmediaMazepin)

Gasly = data[(data['driverId'] == 842) & (data['stop'] == 1)]
print(Gasly)
df = pd.DataFrame(Gasly)
DuracionmediaGasly = df['milliseconds'].mean() /1000
print(DuracionmediaGasly)

Tsunoda = data[(data['driverId'] == 852) & (data['stop'] == 1)]
print(Tsunoda)
df = pd.DataFrame(Tsunoda)
DuracionmediaTsunoda = df['milliseconds'].mean() /1000
print(DuracionmediaTsunoda)

Russel = data[(data['driverId'] == 847) & (data['stop'] == 1)]
print(Russel)
df = pd.DataFrame(Russel)
DuracionmediaRussel = df['milliseconds'].mean() /1000
print(DuracionmediaRussel)

Raikkonen = data[(data['driverId'] == 8) & (data['stop'] == 1)]
print(Raikkonen)
df = pd.DataFrame(Raikkonen)
DuracionmediaRaikkonen = df['milliseconds'].mean() /1000
print(DuracionmediaRaikkonen)

Verstappen = data[(data['driverId'] == 830) & (data['stop'] == 1)]
print(Verstappen)
df = pd.DataFrame(Verstappen)
DuracionmediaVerstappen = df['milliseconds'].mean() /1000
print(DuracionmediaVerstappen)

Sainz = data[(data['driverId'] == 832) & (data['stop'] == 1)]
print(Sainz)
df = pd.DataFrame(Sainz)
DuracionmediaSainz = df['milliseconds'].mean() /1000
print(DuracionmediaSainz)

Ricciardo = data[(data['driverId'] == 817) & (data['stop'] == 1)]
print(Ricciardo)
df = pd.DataFrame(Ricciardo)
DuracionmediaRicciardo = df['milliseconds'].mean() /1000
print(DuracionmediaRicciardo)

Stroll = data[(data['driverId'] == 840) & (data['stop'] == 1)]
print(Stroll)
df = pd.DataFrame(Stroll)
DuracionmediaStroll = df['milliseconds'].mean() /1000
print(DuracionmediaStroll)

Hamilton = data[(data['driverId'] == 1) & (data['stop'] == 1)]
print(Hamilton)
df = pd.DataFrame(Hamilton)
DuracionmediaHamilton = df['milliseconds'].mean() /1000
print(DuracionmediaHamilton)

Giovinazzi = data[(data['driverId'] == 841) & (data['stop'] == 1)]
print(Giovinazzi)
df = pd.DataFrame(Giovinazzi)
DuracionmediaGiovinazzi = df['milliseconds'].mean() /1000
print(DuracionmediaGiovinazzi)

Leclerc = data[(data['driverId'] == 844) & (data['stop'] == 1)]
print(Leclerc)
df = pd.DataFrame(Leclerc)
DuracionmediaLeclerc = df['milliseconds'].mean() /1000
print(DuracionmediaLeclerc)

Perez = data[(data['driverId'] == 815) & (data['stop'] == 1)]
print(Perez)
df = pd.DataFrame(Perez)
DuracionmediaPerez = df['milliseconds'].mean() /1000
print(DuracionmediaPerez)

Norris = data[(data['driverId'] == 846) & (data['stop'] == 1)]
print(Norris)
df = pd.DataFrame(Norris)
DuracionmediaNorris = df['milliseconds'].mean() /1000
print(DuracionmediaNorris)

Bottas = data[(data['driverId'] == 822) & (data['stop'] == 1)]
print(Bottas)
df = pd.DataFrame(Bottas)
DuracionmediaBottas = df['milliseconds'].mean() /1000
print(DuracionmediaBottas)

Alonso = data[(data['driverId'] == 4) & (data['stop'] == 1)]
print(Alonso)
df = pd.DataFrame(Alonso)
DuracionmediaAlonso = df['milliseconds'].mean() /1000
print(DuracionmediaAlonso)

#Definimos una lista con pilotos como string
circuitos = ['Schumacher','Giovinazzi', 'Ocon',  'Norris', 'Ricciardo', 'Stroll', 'Tsunoda' , 'Russel', 'Mazepin', 'Perez', 'Gasly', 'Sainz', 'Raikkonen', 'Alonso','Leclerc', 'Vettel','Verstappen', 'Hamilton', 'Bottas']
#Definimos una lista con tiempos como entero
tiempos = [DuracionmediaSchumacher, DuracionmediaGiovinazzi, DuracionmediaOcon, DuracionmediaNorris, DuracionmediaRicciardo, DuracionmediaStroll, DuracionmediaTsunoda, DuracionmediaRussel, DuracionmediaMazepin, DuracionmediaPerez, DuracionmediaGasly, DuracionmediaSainz, DuracionmediaRaikkonen, DuracionmediaAlonso, DuracionmediaLeclerc,  DuracionmediaVettel,DuracionmediaVerstappen,  DuracionmediaHamilton,  DuracionmediaBottas]

fig, ax = plt.subplots()
#Colocamos una etiqueta en el eje Y
ax.set_ylabel('Tiempo de parada')
#Colocamos una etiqueta en el eje X
ax.set_title('Relacion entre tiempo de parada y Piloto')
#Creamos la grafica de barras utilizando 'paises' como eje X y 'tiempo' como eje y.
plt.bar(circuitos, tiempos)
plt.savefig('barras_simple.png')
plt.xticks(rotation=90)
#Finalmente mostramos la grafica con el metodo show()
plt.show()




