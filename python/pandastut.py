# adding the library
import pandas as pd
import numpy as np
from io import StringIO, BytesIO
import json

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
data = ('a,b,c\n' '4,apple,bat,5.7\n' '8,orange,cow,10')
print(pd.read_csv(StringIO(data), index_col=3))
# index_col can make any colums as coumn index
# While extracting the use of usecols can be used for extracting specific columns in the data frame
data = ('a,b,c\n' '4,laptop,bat,5.7\n' '8,keyboard,cow,10')
print(pd.read_csv(StringIO(data), index_col=3, escapechar='k'))
#   using escapechar skips specific character in the data frame

# Read Json using pandas

Data = '{"employee_name": {"0":"James"}, "email": {"0":"james@gmail.com"}}'
print(pd.read_json(Data))
df1 = pd.read_json(Data)
# I successfully created json using python and displayed using pandas. one thing to note a json is always nested because when
# I tried to read this Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}' while omitting the nested part it was showing me a error
print(df1.to_json())
print(df1.to_json(orient="records"))  # it is created record by record

# json done

# Reading HTML

url = 'https://en.wikipedia.org/wiki/Minnesota'
dfs = pd.read_html(
    url, match='United States presidential election results for Minnesota')
print(dfs[0])

# reading html is self explanatory
