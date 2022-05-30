import pandas as pd

# Load results dataset
data = pd.read_csv("../datasets/resultsMonaco.csv") 

print(data['driverId'].nunique())
numeropilotos = data['driverId'].value_counts().shape[0]

result = data[(data['positionOrder'] == 1)]
victoriaspilotodiferente = result['driverId'].value_counts().shape[0]
print(victoriaspilotodiferente)