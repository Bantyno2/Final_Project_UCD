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
