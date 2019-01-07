from pprint import pprint

# Pandas exercises on https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
## from (library) import (specific library function)

from pandas import DataFRame, read_csv

# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# Initialize set of baby names and birth rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

#combine both arrays into list with table structure
BabyDataSet = list(zip(names,births))
pprint(BabyDataSet)

# read into a Panadas data frame
df = pd.DataFrame(data = BabyDataSet, columns=['Names','Births'])

# write dataframe to csv
df.to_csv('births1880.csv',index=False,header=False)

# find path of locally saved csv
location = r'C:\Users\isaac\Documents\dev\pythonPlayground\births1880.csv'
# the 'r' preceding the path escapes special characters in the path for the entire string

# import the data from the path
df = pd.read_csv(location)

# import the data with specific column names
df = pd.read_csv(location, names=['Names','Births'])

# delete the csv now that we are done
import os

os.remove(location)

# check data type of columns
df.dtypes

# check data type of births column
df.Births.dtype

# find most popular name using sort or max
# using the sort method
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)

# using the MAX method
df['Births'].max()

# present/plot data
## Create graphi
df['Births'].plot()

## Maximum value in the data set
MaxValue = df['Births'].max()

## Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

## Text to display on graph
Text = str(MaxValue) + " - " + MaxName

## add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8,0),
                xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
df[df['Births'] == df['Births'].max()]
plt.show()