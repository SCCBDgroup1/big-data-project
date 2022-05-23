import pandas as pd

# Load results dataset
data = pd.read_csv("../datasets/results.csv") 
data2 = pd.read_csv("../datasets/drivers.csv") 

print(data['driverId'].nunique())
numeropilotos = data['driverId'].value_counts().shape[0]

result = data[(data['positionOrder'] == 1)]
pilotomasvictorias = result['driverId'].value_counts().idxmax()

result = data[(data['driverId'] == pilotomasvictorias) & (data['positionOrder'] == 1)]
print(result)
numerovictorias = result.shape[0] 

result2 = data2[(data2['driverId'] == pilotomasvictorias)]
pilotconmasvictorias = (result2['driverRef'])

