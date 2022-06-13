#import modules
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

#import scikit-learn
from sklearn import linear_model

#first we prepare our dataframe for a better analysis

#using csv's!
df_drivers=pd.read_csv('./datasets/driver_standings.csv', names=['driverStandingsId','raceId','driverId','points','position','positionText','wins'], header=None)
#drivers dataset
df_name=pd.read_csv('./datasets/drivers.csv', names=['driverId','driverRef','number','code','forename','surname','dob','nationality','url'], header=None)
df_results=pd.read_csv('./datasets/results.csv', names=['resultId','raceId','driverId','constructorId','number','grid','position','positionText','positionOrder','points','laps','time','milliseconds','fastestLap','rank','fastestLapTime','fastestLapSpeed','statusId'], header=None)
df_pit=pd.read_csv('./datasets/pit_stops.csv', names=['raceId','driverId','stop','lap','time','duration','milliseconds'], header=None)
df_races=pd.read_csv('./datasets/races.csv', names=['raceId','year','round','circuitId','name','date','time','url'], header=None)
df_constructors=pd.read_csv('./datasets/constructors.csv', names=['constructorId','constructorRef','name','nationality','url'], header=None)

#merge all datasets, df=df_merged
df_merged=pd.merge(df_results, df_races[['raceId', 'year', 'name', 'round']],on='raceId', how='left')
df_merged=pd.merge(df_merged, df_name[['driverId', 'driverRef', 'nationality']],on='driverId', how='left')
df_merged=pd.merge(df_merged, df_constructors[['constructorId', 'name', 'nationality']],on='constructorId', how='left')


#delete innecesary columns
df_merged.drop(['number', 'position', 'positionText', 'laps', 'fastestLap', 'statusId', 'resultId', 'raceId', 'driverId', 'constructorId'], axis=1, inplace=True)
#rename the columns
df_merged.rename(columns={'rank':'fastest_lap_rank', 'name_x':'gp_name', 'nationality_x':'driver_nationality', 'name_y':'constructor_name', 'nationality_y':'constructor_nationality', 'driver_ref':'driver'},inplace=True)
#sort the dataframe
df_merged=df_merged[['year', 'gp_name', 'round', 'driverRef', 'constructor_name', 'grid', 'positionOrder', 'points', 'time', 'milliseconds', 'fastest_lap_rank', 'fastestLapTime', 'fastestLapSpeed', 'driver_nationality', 'constructor_nationality']]

#season 2019 is incompleted, deleted
df_merged=df_merged[df_merged['year']!=2019]

#sort different values
df_merged=df_merged.sort_values(by=['year', 'round', 'positionOrder'], ascending=[False, True, True])

df_merged.time.replace('\\N', np.nan, inplace=True)
df_merged.milliseconds.replace('\\N', np.nan, inplace=True)
df_merged.fastest_lap_rank.replace('\\N', np.nan, inplace=True)
df_merged.fastestLapTime.replace('\\N', np.nan, inplace=True)
df_merged.fastestLapSpeed.replace('\\N', np.nan, inplace=True)

df_merged.fastestLapSpeed=df_merged.fastestLapSpeed.astypes(float)
df_merged.fastest_lap_rank=df_merged.fastest_lap_rank.astypes(float)
df_merged.milliseconds=df_merged.milliseconds.astypes(float)

df_merged.reset_index(drop=True, inplace=True)

#now, we just prepare the dataframe and we explore all posibilities
print(df_merged.shape)
df_merged.info()
df_merged.head(10)

#graphic tools
#sns.set_palette('Set3')
#plt.rcParams['figure.figsize']=10,6

#plot the first component
driver_winner= df_merged.loc[df_merged['positionOrder']==1].groupby('driverRef')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
#sns.barplot(data=driver_winner, y='driverRef', x='positionOrder', color='green', alpha=0.8)
#plt.title('Most GP winners')
#plt.ylabel('Driver')
#plt.xlabel('Num GP wins')
#plt.yticks([])

driver_winner

top10Drivers=driver_winner.head(10)
print(top10Drivers)



df_drivers

#5 first rows & last 5 rows
df_drivers.head()
df_drivers.tail()

df_drivers.shape

pd.set_option('display.max_rows', 1000)
df_drivers

#atributes of dataframe, atribute columns df.columns

#check the atributes
df_drivers.shape
df_drivers.index

df_drivers.columns

#object equals to text chain = string
df_drivers.dtypes
df_drivers.info()

#info about our dataframe
df_drivers.describe()

#rows number
len(df_drivers)

max(df_drivers.index)

#round all values with 2 decimals
round(df_drivers, 2)

#select a column
type(df_drivers['points'])

df_drivers['points'].head()

df_drivers['points'].index

df_drivers.points
#best option!
df_drivers['points']

#select one or more columns interesting, to obtain dataframe!
df_drivers[['driverRef', 'points', 'position', 'wins']]

type(df_drivers[['driverId', 'points', 'position', 'wins']])

#create a new column
name_drivers=df_name['driverRef']
df_drivers['driverRef']=name_drivers
df_drivers

df_results2=pd.read_csv('./datasets/results.csv')

#dep. variable = wins, indep. variable = final position
y=df_results2['points']
#if we want two wariables X=df_results[['grid', 'other']]
x=df_results2['grid']

df_results2.plot(kind='scatter', x='grid', y='points')

#add a constant
x=sm.add_constant(x)
#fit the model
lm=sm.OLS(y,x).fit()
#two variables not use
lm.predict(x)

lm.summary()

#linear equation y = ax + b
#coef grid = -0.2068 = a
#coef const = 4.1441 = b

y_pred=-0.2068*x['grid'] +4.1441

#points
plt.figure(figsize=(6, 4), tight_layout=True)
sns.scatterplot(x=x['grid'], y=y)

#line
sns.lineplot(x=x['grid'], y=y_pred, color='red')

#axis
plt.xlim(0)
plt.ylim(0)
plt.savefig('linear_regression')
plt.show()


#new resolution and we will see another params

#scikit-learn
#dep. variable = wins, indep. variable = final position
y=df_merged['points']
df_merged['fastest_lap_rank'].astype(str).astype(float)
#if we want two wariables X=df_results[['grid', 'other']]
X=df_merged[['fastest_lap_rank','grid']]

lm2=linear_model.LinearRegression()
lm2.fit(X, y)

#5 first values
lm2.predict(X)[5]

#indivual results
#r2 score
lm2.score(X, y)

#coefficient
lm2.coef_

#intercept
lm2.intercept_





