import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt


# Load iris dataset
iris = pd.read_csv("..\datasets\iris.csv")
print(iris.dtypes)

X = iris.iloc[:, :-1]
print(X.describe(include='all'))

# Standardization 
std_scale = StandardScaler().fit(X)
X_std = std_scale.transform(X)
X_std = pd.DataFrame(X_std)
print(X_std.describe(include='all'))

# Normalization
minmax_scale = MinMaxScaler().fit(X)
X_minmax = minmax_scale.transform(X)
X_minmax = pd.DataFrame(X_minmax)
print(X_minmax.describe(include='all'))

import seaborn as sns

# Feature distribution plots
iris.hist(figsize=(16, 20));


# Feature distribution plots
X_std.hist(figsize=(16, 20));


# Feature distribution plots
X_minmax.hist(figsize=(16, 20));




# The bi-attribute distribution plots 
sns.pairplot(iris)

for i in range(0, len(iris.columns), 5):
    sns.pairplot(data=iris,
                x_vars=iris.columns[i:i+5],
                y_vars=['variety'])
    
    


# For categorical attributes: frequency distributions
plt.subplots(figsize=(10, 8))
sns.countplot(data=iris_cat, x='variety')
