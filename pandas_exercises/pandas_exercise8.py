# Lesson index: https://pandas.pydata.org/pandas-docs/stable/tutorials.html under Lessons for new pandas users
# Pandas exercises https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/08%20-%20Lesson.ipynb

# Configuration
## Import Libraries
import sys
from pprint import pprint
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select, engine

## Check versions
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

### NOTE: holding off since I don't have a db I want to connect to at the moment
