# Lesson index: https://pandas.pydata.org/pandas-docs/stable/tutorials.html under Lessons for new pandas users
# Pandas exercises https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/08%20-%20Lesson.ipynb

# Configuration
## Import Libraries
import sys
from pprint import pprint
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, select, engine
import psycopg2

## Check versions
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

# Required for querying tables
conn = psycopg2.connect(dbname = 'postgres', user='iwyatt', password='abc123',
                        host='35.185.249.169', port='5432')

# open a cursor to perform DB ops
cur = conn.cursor()

# create a table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
response = cur.fetchone()
response
type(response)
response = None

cur.execute("DROP TABLE test;")

# make my own damn table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar, third varchar);")

cur.execute("INSERT INTO test (num, data, third) VALUES (%s, %s, %s)",(300, "dahdahdah","2019-01-17"))
cur.execute("INSERT INTO test (num, data, third) VALUES (%s, %s, %s)",(100, "abc'def", "row 2"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
response = cur.fetchall()
response
pd.DataFrame(response)
response = None

# query users
sql = 'SELECT * FROM pg_catalog.pg_user u ORDER BY 1;'
cur.execute(sql)
response = cur.fetchall()
response
pd.DataFrame(response)
response = None

sql = 'select * from information_schema.tables'
cur.execute(sql)
response = cur.fetchall()
response
pd.DataFrame(response)
response = None

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

