# adding the library
import pandas as pd
import numpy as np

# playing with dataframe
df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], columns=[
                  "column1", "column2", "column3", "column4"])
print(df.head())  
df.to_csv('test1.csv')
print(type(df.head()))
##Accessing the elements 
##1. .loc 2. .iloc
print(df.loc['Row1'].values)
print(type(df.loc['Row2']))
print(df.iloc[1:2,1:])
