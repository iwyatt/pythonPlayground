# Pandas Lesson 5
# "We will be taking a brief look at the stack and unstack functions."
# https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/05%20-%20Lesson.ipynb

# Import
import pandas as pd
import sys
from pprint import pprint

print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)

# build a small dataset
d = {'one':[1,1],'two':[2,2]}

# examine data structure for my own efficacy
type(d)
pprint(d)
d['one'][1]

i = ['a','b']

# create dataFrame
df = pd.DataFrame(data = d, index = i)
df

df.index

# bring columns back in
stack = df.stack()
stack
type(stack)
# NOTE: This is like pivoting a table into an association array

# the index now includes the column names
stack.index


# now do an unstack
unstack = df.unstack()
unstack

unstack.index

# do a transpose
transpose = df.T
df
transpose
## NOTE: transpose swaps columns and rows and their respective index

# do the index
transpose.index
pprint(transpose.index)