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

#if you use MAC prove with this / .. points NO . point
#x = pd.read_csv("../datasets/x.csv") 

#if youse use Windows don't worry and you can use these following lines!
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
df_merged.rename(columns={'rank':'fastest_lap_rank', 'name_x':'gp_name', 'nationality_x':'driver_nationality', 'name_y':'constructor_name', 'nationality_y':'constructor_nationality', 'driver_ref':'driver', 'round':'raceNumber'},inplace=True)
#reorder the dataframe to do a efficient analysis
df_merged=df_merged[['year', 'gp_name', 'raceNumber', 'driverRef', 'constructor_name', 'grid', 'positionOrder', 'points', 'time', 'milliseconds', 'fastest_lap_rank', 'fastestLapTime', 'fastestLapSpeed', 'driver_nationality', 'constructor_nationality']]

#season 2019 is incompleted, deleted
df_merged=df_merged[df_merged['year']!=2019]

#sort different values
df_merged=df_merged.sort_values(by=['year', 'raceNumber', 'positionOrder'], ascending=[False, True, True])

#\\N and Nan none valid to analyze, we use 0's, could be not the best option...
df_merged.time.replace('\\N', 0, inplace=True)
df_merged.milliseconds.replace('\\N', 0, inplace=True)
df_merged.fastest_lap_rank.replace('\\N', 0, inplace=True)
df_merged.fastestLapTime.replace('\\N', 0, inplace=True)
df_merged.fastestLapSpeed.replace('\\N', 0, inplace=True)

#delete index 0, because repeat axis 1 head
df_merged=df_merged.drop(df_merged.index[0])

#now, we change the different dtypes values to adapt to the analysis
df_merged.fastestLapSpeed=df_merged.fastestLapSpeed.astype(float)
df_merged.fastest_lap_rank=df_merged.fastest_lap_rank.astype(float)
df_merged.milliseconds=df_merged.milliseconds.astype(float)

#change more params to adapt...
df_merged.year=df_merged.year.astype('int64')
df_merged.raceNumber=df_merged.raceNumber.astype('int64')
df_merged.grid=df_merged.grid.astype('int64')
df_merged.positionOrder=df_merged.positionOrder.astype('int64')
df_merged.points=df_merged.points.astype(float)

df_merged.reset_index(drop=True, inplace=True)

#now, we just prepare the dataframe and we explore all posibilities
print(df_merged.shape)
df_merged.info()
df_merged.head(10)

#graphic tools
#sns.set_palette('Set3')
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize']=10,6

#plot the the most gp winner in hole history of f1
driver_winner= df_merged.loc[df_merged['positionOrder']==1].groupby('driverRef')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
sns.barplot(data=driver_winner, y='driverRef', x='positionOrder')
plt.title('Most GP winners')
plt.ylabel('Driver')
plt.xlabel('Num GP wins')
plt.yticks([])

#top10 driver_winner in the history of f1!
top10Drivers=driver_winner.head(10)
print(top10Drivers)

#we graphic these top10 drivers
sns.barplot(data=top10Drivers, y='driverRef', x='positionOrder')
plt.title('Most GP winners in history of F1')
plt.ylabel('Driver')
plt.xlabel('Num GP wins')


#now we go into constructor winners section!
constructor_winner= df_merged.loc[df_merged['positionOrder']==1].groupby('constructor_name')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
sns.barplot(data=constructor_winner, y='constructor_name', x='positionOrder')
plt.title('Most GP wins for constructors of F1')
plt.ylabel('Constructor')
plt.xlabel('Num GP wins')
plt.yticks([])

#top10 constructor_winner in the history of f1!
top10Constructors=constructor_winner.head(10)
print(top10Constructors)
#we graphic these top10 drivers
sns.barplot(data=top10Constructors, y='constructor_name', x='positionOrder')
plt.title('Most GP constructor winners in history of F1')
plt.ylabel('Constructor')
plt.xlabel('Num GP wins')

#stats grid finish position
df_merged_no_zero = df_merged[df_merged['grid']!=0]

sns.set_theme(color_codes=True)
sns.regplot(data=df_merged_no_zero, x='grid', y='positionOrder', marker='+')
plt.title('Starting position vs Finish place')
plt.ylabel('Finish place')
plt.xlabel('Starting position')

#but what is happens in the last 3 years (more recent)
df_merged_speed=df_merged[df_merged['year']>=2000]
df_merged_group_speed=df_merged_speed.groupby(['gp_name', 'year'])['fastestLapSpeed'].mean().to_frame().reset_index()

g=sns.FacetGrid(data=df_merged_group_speed, col='gp_name', col_wrap=6)
g.map(plt.scatter, 'year', 'fastestLapSpeed')
g.set_titles("{col_name}")
g.set_xlabels("Year")
g.set_ylabels("Average fastest speed (km/h)")
plt.subplots_adjust(top=0.92)
g.fig.suptitle('Average speed among with all teams during the fastest lap at individual GPs')

#-----------------------------------------------------------------------------
#this part is not necessary run, it's only for test

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

#-----------------------------------------------------------------------------
#end test part, in the last part we go with machine learning!
#in this part we will present two different tools for machine learning: statsmodels and scikit-learn

#first linear simple regression with only one variable

#dep. variable = wins, indep. variable = final position
y=df_merged['points']
#if we want two wariables X=df_results[['grid', 'other']]
x=df_merged['grid']

df_merged.plot(kind='scatter', x='grid', y='points')

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

#-----------------------------------------------------------------------------
#linear multiple regression with two variables

df_merged.info()
y=df_merged['points']
df_merged.fastest_lap_rank=df_merged.fastest_lap_rank.astype('int64')
X=df_merged[['grid', 'fastestLapSpeed']]

#add a constant
X=sm.add_constant(X)
lm=sm.OLS(y,X).fit()
lm.summary()
#with fastestLapSpeed the R-squared increases to 24.6% & std errr=0.043

#-----------------------------------------------------------------------------
#scikit-learn linear multiple regression with two variables

df_merged.info()
#dep. variable = wins, indep. variable = final position
y=df_merged['points']
df_merged.fastest_lap_rank=df_merged.fastest_lap_rank.astype('int64')
#df_merged['fastest_lap_rank'].astype(str).astype(float)
#if we want two wariables X=df_results[['grid', 'other']]
X=df_merged[['grid','fastest_lap_rank']]

lm2=linear_model.LinearRegression()
lm2.fit(X, y)

#5 first values
lm2.predict(X)[5]

#indivual results
#r2 score, in this case 13.85%
lm2.score(X, y)

#coefficient
lm2.coef_

#intercept
lm2.intercept_

#-----------------------------------------------------------------------------