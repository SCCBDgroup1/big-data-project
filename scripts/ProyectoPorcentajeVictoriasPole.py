import pandas as pd

# Load results dataset
data = pd.read_csv("../datasets/results.csv") 
data2 = pd.read_csv("../datasets/drivers.csv") 

print(data['grid'].value_counts()[1]) 
print(data['positionOrder'].value_counts()[1])


result = data[(data['grid'] == 1) & (data['positionOrder'] == 1)]
print(result)
VictoriaPole = result.shape[0] 
Porcentaje = VictoriaPole / data['grid'].value_counts()[1] * 100
Piloto = result['driverId'].value_counts().idxmax()

result2 = data2[(data2['driverId'] == Piloto)]
pilotovictoriapole = (result2['driverRef'])



