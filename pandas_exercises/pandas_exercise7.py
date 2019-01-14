# Lesson index: https://pandas.pydata.org/pandas-docs/stable/tutorials.html under Lessons for new pandas users
# Pandas exercises https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/07%20-%20Lesson.ipynb

# Configuration
## Import Libraries
from pprint import pprint
import pandas as pd
import sys

## Check versions
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

# Prepare Data

## Create dataframe with dates as index
States = ['NY', 'NY', 'NY', 'NY', 'FL', 'FL', 'GA', 'GA', 'FL', 'FL'] 
data = [1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
idx = pd.date_range('1/1/2012', periods=10, freq='MS')
df1 = pd.DataFrame(data, index=idx, columns=['Revenue'])
df1['State'] = States
df1

## Create a second dataframe
data2 = [10.0, 10.0, 9, 9, 8, 8, 7, 7, 6, 6]
idx2 = pd.date_range('1/1/2013', periods=10, freq='MS')
df2 = pd.DataFrame(data2, index=idx2, columns=['Revenue'])
df2['State'] = States

## Combine the data frames
df = pd.concat([df1,df2])
df
len(df)

# Calculating Outliers
## NOTE: AVG and StDev only work for Normal distribution
## Method 1

### make a copy of original df
newdf = df.copy()

### layer in the distance from average of revenue into new column
newdf['x-Mean'] = abs(newdf['Revenue'] - newdf['Revenue'].mean())

### derive the threshold for statistical outlier: 1.96*standard deviation of the revenue
newdf['1.96*std'] = 1.96*newdf['Revenue'].std() 

### determine if mean of each month's revenue is more than 1.96 * standard deviations
newdf['Outlier'] = abs(newdf['Revenue'] - newdf['Revenue'].mean()) > 1.96*newdf['Revenue'].std()

### 
newdf

## Method 2
### Group by item, in this case the state

### make a copy of original df
newdf = df.copy()

### group by the state column
State = newdf.groupby('State')

### use of lambda function to determine if calculated distance from mean is greater than 1.96*the standard deviation of the state's revenue
newdf['Outlier'] = State.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )
### NOTE: the bottom two functions are unncessary, as the clever use of a lambda does the entire necessary function in a single pass

### determine the mean
newdf['x-Mean'] = State.transform( lambda x: abs(x-x.mean()) )

### determine the standard deviation
newdf['1.96*std'] = State.transform( lambda x: 1.96*x.std() )

newdf

## Method 2.5
### Group by multiple items

### make a copy of original df
newdf = df.copy()

### group by state and month
StateMonth = newdf.groupby(['State', lambda x: x.month])

### calculate if the month is an outlier using same lambda as Method 2 above
newdf['Outlier'] = StateMonth.transform( lambda x: abs(x-x.mean()) > 1.96*x.std() )

### calculation methods for supporitng data, but unecessary
newdf['x-Mean'] = StateMonth.transform( lambda x: abs(x-x.mean()) )
newdf['1.96*std'] = StateMonth.transform( lambda x: 1.96*x.std() )
newdf

## Method 3
## Group by item

### make a copy of original df
newdf = df.copy()

### group by the a particular item
State = newdf.groupby('State')

### define a function taking the input of calling .apply object (.apply applies a specific custom function - weird but clever)
### NOTE: Examples of .apply(s)
def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96*group['Revenue'].std()  
    group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
    return group

Newdf2 = State.apply(s)
Newdf2


## Method 3.5
## Group by multiple items

### make a copy of original df
newdf = df.copy()

### apply group by function
StateMonth = newdf.groupby(['State', lambda x: x.month])

### another custom function to be applied using .apply call
def s(group):
    group['x-Mean'] = abs(group['Revenue'] - group['Revenue'].mean())
    group['1.96*std'] = 1.96*group['Revenue'].std()  
    group['Outlier'] = abs(group['Revenue'] - group['Revenue'].mean()) > 1.96*group['Revenue'].std()
    return group

### apply custom function
Newdf2 = StateMonth.apply(s)
Newdf2


## Method 4: Find outliers Assuming a non-gaussian distribution:
### make a copy of original df
newdf = df.copy()

### apply the group by
State = newdf.groupby('State')

### calculate upper/lower bounds of revenue using quantiles
newdf['Lower'] = State['Revenue'].transform( lambda x: x.quantile(q=.25) - (1.5*(x.quantile(q=.75)-x.quantile(q=.25))) )
newdf['Upper'] = State['Revenue'].transform( lambda x: x.quantile(q=.75) + (1.5*(x.quantile(q=.75)-x.quantile(q=.25))) )
newdf['Outlier'] = (newdf['Revenue'] < newdf['Lower']) | (newdf['Revenue'] > newdf['Upper']) 
newdf

