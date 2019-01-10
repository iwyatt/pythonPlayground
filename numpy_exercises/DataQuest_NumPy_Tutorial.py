# DataQuest_NumPy_Tutorial.py
# https://www.dataquest.io/blog/numpy-tutorial-python/
# Leverages data in this web resource directory: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/

# import modules
import pandas as pd
from pprint import pprint

# get the data via web resource with pandas and save. Easiest method
url = r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(url,sep=";")
data.to_csv(r'winequality-read.csv',index=False,header=True)
# note that this saved it in the main folder instead of the sub folder that I'd intended. Will need to learn how to set relative paths.

# now read it in using the tutorial's method
# NOTE: we should just use pandas for these exercises probably
import csv
with open(r'C:\Users\isaac\Documents\dev\pythonPlayground\winequality-read.csv','r') as f:
    wines = list(csv.reader(f, delimiter=','))

print(wines[:3])

# now we math
## this converts the last item of each row to a float and puts them in qualities
qualities = [float(item[-1]) for item in wines[1:]]

# get the average: this divides the sum of all elements in qualities by total number of elments in qualities
sum(qualities) / len(qualities)

## In Numpy, Rank = # of dimensions, each dimension is called an "axis"

# Create a numpy array:
import numpy as np
wines = np.array(wines[1:], dtype=np.float)
wines

# check number of rows and columns in data using shape property
wines.shape

# create empty array of x,y dimensions
empty_array = np.zeros((3,4))
empty_array

# create numpy arrays with random values
np.random.rand(3,4)

# Use numpy to read in files
wines = np.genfromtxt(r'C:\Users\isaac\Documents\dev\pythonPlayground\winequality-read.csv', delimiter=";", skip_header=1)

# testing the above function to see if it can read in web locations
wines = np.genfromtxt(url, delimiter=";", skip_header=1)
wines
## NOTE: Numpy's genfromtxt function appears to successfully pull in from URL

# Indexing NumPy Arrays
## retrieving elements
## NOTE: this returns 2.3 for me and 2.299999998 in tutorial
wines[2,3]

# Slicing NumPy Arrays
## select the first three items from the fourth column
## : is inclusive, exclusive
wines[0:3,3]

## or ommit the zero to retrieve all elements of 3
wines[:3,3]

## select all rows of column by just using a colon :
wines[:,3]

## select entire row using similar syntax
wines[3,:]

## party trick
wines[:,:]

# Assigning Values to NumPy Arrays
## assign value to specific row/column
wines[1,5] = 10
wines[1,5]

## or assign for slices and entire columns
wines[:,10] = 50
wines[:,10]

# 1-Dimensional NumPy arrays
third_wine = wines[3,:]
third_wine

## retrieve second item in array (0-based index)
third_wine[1]
## note that the tutorial returns  0.28000000000000003 and mine returns 0.28

## generate random vector (1-dim array)
np.random.rand(3)

# N-dimension arrays (3 + dims = "list of lists")
## sample data set of monthly sales for year one
year_one = [
    [500,505,490],
    [810,450,678],
    [234,897,430],
    [560,1023,640]
]

## retrieve january earnings
year_one[0][0]

## get results for each month of entire quarter
year_one[0]
year_one[1]

## add results for another year by adding third dimension
earnings = [
            [
                [500,505,490],
                [810,450,678],
                [234,897,430],
                [560,1023,640]
            ],
            [
                [600,605,490],
                [345,900,1000],
                [780,730,710],
                [670,540,324]
            ]
          ]

## get earnings of Jan of the first year
earnings[0][0][0]

## convert to numpy
earnings = np.array(earnings)
earnings[0,0,0]

## check shape Year, Quarter, Month
earnings.shape

## get january earnings for all years
earnings[:,0,0]

## get first quarter earnings for both years
earnings[:,0,:]

# NumPy data types
## Pick up here: https://www.dataquest.io/blog/numpy-tutorial-python/
