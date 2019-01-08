# Lesson index: https://pandas.pydata.org/pandas-docs/stable/tutorials.html under Lessons for new pandas users
# Lesson 2: https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/02%20-%20Lesson.ipynb

# import necessary libs
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #strictly for python version number
import matplotlib 
from pprint import pprint

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# create random set of baby names for 1880, duplicate names means different hospitals

# initial set of baby names to use
names = ['Bob','Jessica','Mary','John','Mel']

#set seed
random.seed(500)

# generate a number between 0 and length of list of names
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

#print names from list
type(random_names)
random_names[:10]

#generate number of births that will be used for each name
births = [random.randint(low=0,high=1000) for i in range(1000)]
type(births[0])
births[:10]

BabyDataSet = list(zip(random_names,births))
pprint(BabyDataSet[:10])

#set up the data frame
df = pd.DataFrame(data = BabyDataSet, columns=['Names','Births'])
df[:10]

# export data to csv
df.to_csv('births1880.txt',index=False,header=False)

#read from csv
Location = r'births1880.txt'
df = pd.read_csv(Location)

#examine data
df.info()
df.head()

#fix header
df = pd.read_csv(Location, header=None)

#examine
df.info()
df.tail()

#set header names
df = pd.read_csv(Location, names=['Names','Births'])
df.head(5)

#delete the text file
import os
os.remove(Location)

# Prepare Data

## verify count of uniques
df['Names'].unique()

## print uniques
for x in df['Names'].unique():
    print(x)

## another way of examining structure via  df.describe()
print(df['Names'].describe())

## do some group by
name = df.groupby('Names')

## apply sum function to the groupby object
df = name.sum()

# Analyze the Data
## find most popular baby name with the highest birth rate
## either sort and select top row
## or use the max() attribute (function/method??)

## start by trying out sort
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)
### Spoiler: It's Bob!! w/ 106,817

## using Max:
df['Births'].max()
### this only tells us 106,817

# Present the data
## plot births

### create graph
df['Births'].plot.bar()

print("The most popular name")
df.sort_values(by='Births',ascending=False)

plt.show()