# Lesson index: https://pandas.pydata.org/pandas-docs/stable/tutorials.html under Lessons for new pandas users
# Pandas exercises on https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/06%20-%20Lesson.ipynb

# Import Libraries
from pprint import pprint
import pandas as pd
import sys

# Check versions
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

# Build a small data set
d = {'one':[1,1,1,1,1],
     'two':[2,2,2,2,2],
     'letter':['a','a','b','b','c']}

# create a dataframe
df = pd.DataFrame(d)
df

## NOTE: the output results don't match the tutorial. letter comes in the first column in the tutorial but last in my data results

# Create a group-by object
one = df.groupby('letter')

# Apply sum aggregate function
one.sum()

# Group by two selections
letterone = df.groupby(['letter','one']).sum()
letterone

# index of group by
letterone.Index

# avoid having columns being grouped becoming the index. use as_index=False
letterone = df.groupby(['letter','one'], as_index=False).sum()
letterone

# index of above
letterone.index




