import pandas as pd

# Load results dataset
data = pd.read_csv("../datasets/results.csv") 

print(data['grid'].value_counts()[1]) 
print(data['positionOrder'].value_counts()[1])


result = data[(data['grid'] == 1) & (data['positionOrder'] == 1)]
print(result)
VictoriaPole = result.shape[0] 
Porcentaje = VictoriaPole / data['grid'].value_counts()[1] * 100


result = data.loc[(data['grid'] == 1) & (data['position'] == 1)]
print(result)

result = data[(data.grid == 1) & (data.position == 1)]
print(result)

result = data[(data['grid'].value_counts()[1]) & (data['position'].value_counts()[1])]
print(result)