# Importing pandas library.
import pandas as pd


# Creating a data frame
hardcoded = pd.DataFrame({'Date':['2018-01-11  00:00:00', '2018-01-12  00:00:00', '2018-01-19  00:00:00', '2018-01-21 00:00:00', '2018-01-25 00:00:00', '2018-01-26 00:00:00'], \
                          'Time Worked': [3, 3, 4, 3, 3, 4], \
                          'Money Earned': [33.94, 33.94, 46, 33.94, 33.94, 46]})
print('Hard coded data')
# Head displays only the top 5 rows from the data frame.
print(hardcoded.head())
print(hardcoded.dtypes)
hardcoded['Time Worked'] = hardcoded['Time Worked'].astype('int64')
hardcoded['Time Worked'] = hardcoded['Time Worked'].astype(int)
hardcoded['Date'] = pd.to_datetime(hardcoded.Date) 
print(hardcoded.dtypes)


# Load from a CSV
iris = pd.read_csv("../datasets/iris.csv") 
print('CSV')
print(iris.head())
print(iris.dtypes)
# Clase: categorical to numerical
iris['variety'] = iris['variety'].astype('category')
iris['variety'] = iris['variety'].cat.codes
print(iris.dtypes)
print(iris.head())
print(iris.describe(include='all'))


# Load from sklearn datasets
from sklearn import datasets
sklearn_dataset = datasets.load_iris()
iris = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)
iris['target'] = pd.Series(sklearn_dataset.target)
print('SKLearn Datasets')
print(iris.head())
print(iris.dtypes)


# Load from a HTML table
html = pd.read_html('https://www.w3schools.com/html/html_tables.asp')
print('HTML Table')
print(html[0])


# Load from JSON
json = pd.read_json('https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json')
print(json.head())
print(json.dtypes)
