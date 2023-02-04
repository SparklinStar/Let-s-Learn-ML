# adding the library
import pandas as pd
import numpy as np

# playing with dataframe
df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], columns=[
                  "column1", "column2", "column3", "column4"])
print(df.head())
df.to_csv('test1.csv')
print(type(df.head()))
# Accessing the elements
# 1. .loc 2. .iloc
print(df.loc['Row1'].values)
print(type(df.loc['Row2']))
print(df.iloc[:, 3:4])
print(df.isnull())

# reading excel data
df = pd.read_excel('physics stephen.xlsx')
print(df.head())
print(df.describe())
# reading csv data
# when the separation is ;
# retrieving only column1 and column2 from csv
# where column1 is in int and column2 is in float

df1 = pd.read_csv('test.csv', sep=';', usecols=['column1', 'column2'], dtype={
                  'column1': int, 'column2': float})
print(df1.head())

# creating csv from scratch
