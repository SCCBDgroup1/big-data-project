import pandas as pd

# Load results dataset
data = pd.read_csv("../datasets/resultsMonaco.csv") 
data2 = pd.read_csv("../datasets/drivers.csv") 

print(data['driverId'].nunique())
numeropilotos = data['driverId'].value_counts().shape[0]

result = data[(data['grid'] == 1)]
pilotomaspole = result['driverId'].value_counts().idxmax()

result = data[(data['driverId'] == pilotomaspole) & (data['grid'] == 1)]
print(result)
numeropoles = result.shape[0] 

result2 = data2[(data2['driverId'] == pilotomaspole)]
pilotconmaspole = (result2['driverRef'])

