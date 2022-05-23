import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

data = pd.read_csv("../datasets/qualifyingOK3.csv")

X = data[['q1','q2']]
y = data['q3']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[117013, 116040]])

predictedq3 = regr.predict([scaled[0]])
print(predictedq3)


