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

#number of matches played in each year - Lets plot this using seaborn
plt.figure(figsize=(20,8))
sns.lineplot(games_per_year.index, games_per_year.values, color='blue')
plt.title('Number of matches played in each year', fontsize=18)
plt.ylabel('No of matches', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.show()

#i want to see how many games england played at home/away - using loc function
eng_home_games = df.loc[df['home_team']=='England']
print(eng_home_games.head())
print(eng_home_games.shape)
eng_away_games = df.loc[df['away_team']=='England']
print(eng_away_games.head())
print(eng_away_games.shape)
#england have played 507 home games and 515 away games

# Going to look at top months for goals scored and then games played per month to see if any correlation
#for total goals i will demonstrate the groupby function
tot_goals = df.groupby("Month")["total_goals"].sum()
print(tot_goals)
#from this i can see that June has the most goals scored
games_per_month = df['Month'].value_counts()
print(games_per_month)
#there appears to be some correlation as June also has the most games however a graph will be easier to see this

# 1st games per month (fig3)
plt.figure(figsize=(20,8))
sns.lineplot(games_per_month.index, games_per_month.values, color='red', marker='o')
plt.title('Number of matches played in each month', fontsize=18)
plt.ylabel('No of matches', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.show

#2nd total goals per month (fig4)
plt.figure(figsize=(20,8))
sns.lineplot(tot_goals.index, tot_goals.values, color='blue', marker='*')
plt.title('Number of matches and goals per month', fontsize=18)
plt.ylabel('No of Goals / Matches', fontsize=12)
plt.xlabel('Month', fontsize=12)
plt.show

#Explore Groupby and see the hometeam wins
print(df.groupby("home_team")["home_wins"].sum())
top_team_scores = df.groupby(["home_team", "away_team"])["total_goals"].sum()
print(top_team_scores)

#how has the number of participating countries changes over the course of the period 1872-2021
country_nums=df[['year','country']]
country_nums = country_nums.drop_duplicates()
country_nums_group=country_nums.groupby('year').count()
print(country_nums_group.head())
print(country_nums_group.tail())

#plot this to see across years (fig5)
plt.plot(country_nums_group.index, country_nums_group['country'], color='green', marker='o')
plt.title('Changes in Number of Participating Countries ', fontsize=14)
plt.xlabel('year', fontsize=14)
plt.ylabel('country', fontsize=14)
plt.grid(True)
plt.show()

