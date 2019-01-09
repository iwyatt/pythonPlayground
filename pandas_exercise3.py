import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# Get Data
## Create our own data
### set seed
np.seed(111)

### function to generate test data
def CreateDataSet(Number=1):

    Output = []

    for i in range(Number):

        # Create a weekly (Mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25,high=1000,size=len(rng))

        # Satus pool
        status = [1,2,3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0,high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA','FL','fl','NY','NJ','TX']

        # Make a rando list of states
        random_states = [states[np.randint(low=0,high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output

### create data and add to data frame
dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])

### check
df.info()
df.head()

### save results to Excel
df.to_excel('Lesson3.xlsx', index=False) ### had to pip3 install openpyxl for some reason
print('Done')

## Grab Data from Excel
### set location of file
Location = r'Lesson3.xlsx' #the whole string escape is probably unnecessary but leaving for posterity

### parse a specific sheet
df = pd.read_excel(Location, 0, index_col='StatusDate') #had to pip3 install xlrd

### check this 
df.head()
df.dtypes
df.index

# Prepare Data
## Clean up data for analysis:
## 1) state column to upper case
## 2) Only select records where accoutn status is equial to "1"
## 3) Merg NJ and NY in the sate column
## 4) Remove any outliers (any odd results in the data set)

### examine unique state values
df['State'].unique()

### use lambda to apply function to all data in a set
df['State'] = df.State.apply(lambda x: x.upper())

### check it
df['State'].unique()

### filter to where status == 1
mask = df['Status'] == 1
df = df[mask]

df
### turn NJ states to NY
mask = df.State =='NJ'
df['State'][mask] = 'NY'

df['CustomerCount'].plot(figsize=(15,5))

### show me the graph!
plt.show()

### lets change around the data to make a more informative graph
sortdf = df[df['State']=='NY'].sort_index(axis=0)
sortdf.head(10)

### Group by State and StatusDate
Daily = df.reset_index().groupby(['State','StatusDate']).sum()
Daily.head()

### Delete Status since it is all =1 ?(?? - at least according to the tutorial. Not sure about 4/6/2009)
del Daily['Status']

### confirm delete:
Daily.head()

### check index of the dataframe
Daily.index


### select the state index
Daily.index.levels[0]

### Select the statusdate index
Daily.index.levels[1]

type(Daily)

### plot each by state
Daily.loc['FL'].plot()
plt.show()

Daily.loc['GA'].plot()
plt.show()

Daily.loc['NY'].plot()
plt.show()

Daily.loc['TX'].plot()
plt.show()

### plot by specific date
Daily.loc['FL']['2012':].plot()
plt.show()

Daily.loc['GA']['2012':].plot()
plt.show()

Daily.loc['NY']['2012':].plot()
plt.show()

Daily.loc['TX']['2012'].plot()
plt.show()

## more cleaning of the data
### Calculate Outliers
### note: interesting method for finding outliers for non-normal distributions
StateYearMonth = Daily.groupby([Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.25) - (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Upper'] = StateYearMonth['CustomerCount'].transform( lambda x: x.quantile(q=.75) + (1.5*x.quantile(q=.75)-x.quantile(q=.25)) )
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])

Daily['Lower']
Daily['Upper']
Daily['Outlier']

### remove the outliers!
Daily = Daily[Daily['Outlier'] == False]

### check to make sure we have dataframe that is acceptable
Daily.head()

### create new data frame to get rid of state column and show max customer count per month
### combine all markets

### get the max customer count by date
ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount']
ALL.head()

### group by year and month - lambda functions are nice and concise
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])

### What is the max customer count per year and month
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
ALL.head()

## Check customer counts vs goals (Big Hairy Annual Goal)
### create goal data frame
data = [1000,2000,3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])

### combine data frames
### NOTE: axis = 0 we append row-wise in the concat function
### NOTE: there is some functionality changing that is a warning on the tutorial page
combined = pd.concat([ALL,BHAG], axis=0)
combined = combined.sort_index(axis=0)
combined.tail()

fig, axes = plt.subplots(figsize=(12, 7))
combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best');
plt.show()
### NOTE: I'm not 100% convinced this is the right visualization. It's the future goal? or attainment of past goals?

### Group by year and then get the max vcalue per year
Year = combined.groupby(lambda x: x.year).max()
Year

### add a column representing the percent change per year
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
Year

### get next year's end customer count assume same growth rate
(1 + Year.loc[2012, 'YR_PCT_Change']) * Year.loc[2012,'Max']

# Present Data
## Create individuals graphs per state
### First Graph
ALL['Max'].plot(figsize=(10,5));plt.title('ALL Markets')

### Last four graphs NOTE: creating subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20,10))
fig.subplots_adjust(hspace=1.0) ## create space between plots

Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0,0])

### add titles
axes[0,0].set_title('Florida')
axes[0,1].set_title('Georgia')
axes[1,0].set_title('Texas')
axes[1,1].set_title('North East')

### show plot
plt.show()

### NOTE: the rendering doesn't follow what is in the tutorial. Probably because the tutorial uses ANACONDA
