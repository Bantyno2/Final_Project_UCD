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



