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
## check current data type (it's float64)
wines.dtype


## reimporting original wine matrix to get proper data
url = r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
wines = np.genfromtxt(url, delimiter=";", skip_header=1)

#cast as integer
wines.astype(int)
## NOTE: the output numbers dont all match what is in the tutorial since we did some array options earlier in the lesson

## cast and check the numpy datatype as opposed to the python data type
int_wines = wines.astype(int)
int_wines.dtype.name

## also can convert to smaller data types than int64 like int32
np.int32

wines.astype(np.int32)

# numpy array operations
## add 10 points to each quality score and return new array
wines[:11] + 10

## or we can modify the array in-place:
wines[:,11] += 10
wines[:,11]

## all operations work this way: 
wines[:,11] * 2

## can also do operations between arrays
wines[:,11] + wines[:,11]

## can multiple arrays as well
wines[:,10] * wines[:,11]

# Broadcasting

## incompatible shapes:
wines * np.array([1,2])

## compatible shapes:
array_one = np.array(
    [
        [1,2],
        [3,4]
    ]
)
array_two = np.array([4,5])

## "add the contents of each shorter array, to each element of matching dimension size in the second array"
array_one + array_two

## example with wines data
rand_array = np.random.rand(12)
rand_array
wines + rand_array

## finds the sum of all the elements in an array by default
wines[:,11].sum()

## sum across an axis
## axis=0 is confusing. The tutorial's explanation is:
## If we call sum across the wines matrix, and pass in axis=0, we'll find the sums over the first axis of the array. This will give us the sum of all the values in every column. This may seem backwards that the sums over the first axis would give us the sum of each column, but one way to think about this is that the specified axis is the one "going away". So if we specify axis=0, we want the rows to go away, and we want to find the sums for each of the remaining axes across each row:
wines.sum(axis=0)

# can verify the shape
wines.sum(axis=0).shape

# axis = 1 will find sums over the second axis of the array, the sum of each row
wines.sum(axis=1)

# other functions that can operate on arrays like the sum method:
# mean
wines.mean(axis=1)
# std
wines.std(axis=0)
# min
wines.min(axis=1)
# max
wines.max(axis=0)

# ArrayComparisons
## check if any wines have quality rating above 5
wines[:,11] > 5

## check if any have quality equal to 10
wines[:,11] == 10

# Subsetting
## select wines > 7
high_quality = wines[:,11] > 7

## do the subsetting on the data set
wines[high_quality,:][:3,:]

## multiple condition subsetting
high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7)
wines[high_quality_and_alcohol,10:]

## combine subsetting and assignment
high_quality_and_alcohol = (wines[:,10] > 10) & (wines[:,11] > 7)
wines[high_quality_and_alcohol,10:] = 20
wines[high_quality_and_alcohol,10:]

# Reshaping NumPy arrays
## transpose the x and y
np.transpose(wines).shape

## ravel function turn array into one dimension (flatten)
wines.ravel()

## visible example:
array_one = np.array(
    [
        [1, 2, 3, 4], 
        [5, 6, 7, 8]
    ]
)

array_one.ravel()

## reshape function to reshape to a specified shape
wines[1,:].reshape((2,6))
wines[1,:].reshape((6,2))

## Combining numpy arrays

### read in the white wines
url = r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
white_wines = np.genfromtxt(url, delimiter=";", skip_header=1)
white_wines.shape

### reimport the red wines
url = r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
wines = np.genfromtxt(url, delimiter=";", skip_header=1)

### use vstack to combine wines and white_wines NOTE: this is like adding rows to a table
### or use hstack like adding columns to a table (no example)
all_wines = np.vstack((wines, white_wines))
all_wines.shape

### numpy.concatenate as general purpose version of hstack and vstack
### concatenating along first axis is like vstack, second axis is hstack
np.concatenate((wines, white_wines), axis=0)

### numpy array challenge
### Create a 3 x 4 array filled with all zeros, and a 6 x 4 array filled with all 1s.
### Concatenate both arrays vertically into a 9 x 4 array, with the all zeros array on top.
### Assign the entire first column of the combined array to first_column.
### Print out first_column.

### Create a 3 x 4 array filled with all zeros, and a 6 x 4 array filled with all 1s.
zeros_array = np.zeros((3,4))
ones_array = np.zeros((6,4))
ones_array[:,:] = 1
zeros_array
ones_array

### Concatenate both arrays vertically into a 9 x 4 array, with the all zeros array on top.
combined_arrays = np.vstack((zeros_array, ones_array))

### Assign the entire first column of the combined array to first_column.
first_column = combined_arrays[:,0]

#Print out first_column
print(first_column)



