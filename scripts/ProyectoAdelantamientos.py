import pandas as pd
  
# Load results dataset
data = pd.read_csv("../datasets/F1_Overtaking_Data.csv") 

result = data[(data['overtakes'] <= 0)]
adelantamientocircuito = result['race'].value_counts().idxmax()
result2 = data[(data['race'] == adelantamientocircuito) & (data['overtakes'] <= 0)]
adelantamientonumeroveces = result2.shape[0] 

mediaadelantamientos = result['overtakes'].mean()




