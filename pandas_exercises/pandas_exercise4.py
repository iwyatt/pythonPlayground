# Pandas Lesson 4
# "In this lesson were going to go back to the basics. We will be working with a small data set so that you can easily understand what I am trying to explain. We will be adding columns, deleting columns, and slicing the data many different ways. Enjoy!"
# https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/04%20-%20Lesson.ipynb
import pandas as pd
import sys
from pprint import pprint

print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)

# build array of numbers for data set
d = [0,1,2,3,4,5,6,7,8,9]

# make the data frame
df = pd.DataFrame(d)
df

# change the column name
df.columns = ['Rev']
df
pprint(df)

# add a column
df['NewCol'] = 5
df

# modify the column
df['NewCol'] = df['NewCol'] + 1
df

# delete column 
del df['NewCol']
df

# add some more columns
df['test'] = 3
df

df['col'] = df['Rev']
df

# change name of index
i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i
df

# select from dataframe using 'loc'
df.loc['a']
type(df.loc['a'])
pprint(df.loc['a'])

# referencing using loc is inclusive
df.loc['a':'d']
df.loc['b':'i']

# integer based position is inclusive:exclusive
# NOTE:I find this less intuitive than inclusive:inclusive
df.iloc[0:3]

# select using column name
df['Rev']

df[['Rev','test']]

# The below syntax replaces df.ix[rows,columns] - a deprecated ix function (??) df.ix[0:3,'Rev']
df.loc[df.index[0:3],'Rev']

# another example which replaces ix function
df.loc[df.index[5:],'col']

# another example that replaces the ix function
df.loc[df.index[:3],['col','test']]

# select top of dataframe
df.head()

# select bottom
df.tail()