# Importing pandas library.
import pandas as pd

data = pd.read_csv("../datasets/UJIIndoorLoc/UJIIndoorLoc_B0-ID-01.csv") 
print(data.info())


# Attributes distributions
attribute_distribution = data.describe(include='all')
print(attribute_distribution)

# Class distribution
class_distribution = data.groupby('ID').size()
class_distribution = class_distribution.sort_values(ascending=False)
print(class_distribution)

# Correlation: correlation matrix
data_corr = data.corr()
print(data_corr)

# Correlation: attributes vs class
data_corr_values = data.corr()['ID'][:-1]
data_corr_values = data_corr_values.sort_values(ascending=False)
print(data_corr_values)


# Value distribution for each WAPXXX
# .iloc[:, :-1] all attributes but not the class
value_distribution = data.iloc[:, :-1].apply(pd.value_counts)

# Not NaN attributes
null_cols = value_distribution.isnull().any()
null_cols2 = value_distribution.isnull().sum()/len(value_distribution)