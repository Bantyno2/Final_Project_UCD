import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\draftery\OneDrive - ESRI (UK) Ltd\Clodagh DA Course\Final Project UCD\Dataset/international_football_results.csv")

print(df)
print(df.head())
print(df.tail())
print(df.shape)
nRow, nCol = df.shape
print(f'This dataset contains {nRow} rows and {nCol} columns')

print(type(df))
print(len(df))
print(df.describe())
print(df.index)
print(df.values)
print(df.columns)

print(df.isnull())
print(df.isnull().sum())

#i now want to add some columns to my dataset to help with data manipulization and to gain better insights into the dataset
# the output will show a series of booleans depending on the below formulas
df['home_wins'] = df['home_score'] > df['away_score']
df['away_wins'] = df['home_score'] < df['away_score']
df['draw'] = df['home_score'] == df['away_score']

print(df.head())
print(df.shape)

#add new column for the total goals scored in the game
df['total_goals'] = df['home_score'] + df['away_score']
print(df.head())
print(df.shape)

# i want to isolate the year as i will use this to see how many games played per year.
df['Month']=pd.to_datetime(df['date']).dt.month
df['year'] = pd.to_datetime(df['date']).dt.year
print(df.head())
print(df.shape)
#There are now 15 Columns in the dataset.
#Now that i have the month and year as seperate columns i will remove the date column using a short for loop - the actual day the game was played do not concern me
for col in df.columns:
    if 'date' in col:
        del df[col]

print(df.head())

#games broken down per year with most games showing at the top - Given the size of the dataset i am limiting this to top 50
games_per_year = df['year'].value_counts()
print(games_per_year.head(50))
#from this we can see most games were played in 2019, 2008, 2011,2004 and 2000 across all tournaments

#In previous steps i added columns which returned a set of boolean values against "home/away wins and draw games.
home_wins = df[df['home_wins'] ==True].home_wins.count()
away_wins = df[df['away_wins']==True].away_wins.count()
draw = df[df['draw']==True].draw.count()
print('In this dataset there are',home_wins, 'home team wins', away_wins, 'away team wins', 'and',draw, 'draw games')

#Now i am creating a python dictionary with status (home/away/draw) and the number of games relating to each
#this will show if playing at home is advantagous
data = {"Status":["home_wins", "away_wins", "draw"], "result":[20511,11944,9728]}
dataFrame = pd.DataFrame(data=data)
dataFrame.plot.bar(x="Status", y="result", rot=70, title="Number of wins")
plt.show(block=True)

#indexing/slicing - using double brackets for dataframe not series
print(df[["country"]])
print(df[["home_team"]])
print(df[["away_team"]])

#dropping duplicates
drop_dup_country = df.drop_duplicates(subset=['country'])
print(drop_dup_country.shape)
#there are 266 country locations where tournaments are held

#DROP DUPLICATES HOME
drop_dup_home = df.drop_duplicates(subset= ["home_team"])
print(drop_dup_home.shape)
#DROP DUPLICATES AWAY
drop_dup_away = df.drop_duplicates(subset= ["away_team"])
print(drop_dup_away.shape)


