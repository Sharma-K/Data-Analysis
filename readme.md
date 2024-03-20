## Data Analysis

# Data Life Cycle:
  1. Data
  2. Data Warehouse
  3. Data Analysis
  4. Data Visualization


## Pandas
Pandas is a software library written for the Python programming language for data manipulation and analysis.

Pandas is well suited for many different kinds of data:
- Tabular data with heterogeneously-typed columns.
- Ordered and unordered time series data.
- Arbitary matrix data with row and column labels.
- Any other form of observational/statistical data sets.

### Pandas Operations:
1. Slicing
2. Joining
3. Changing the index
4. Concatenation
5. Data Conversion
6. Changing the column headers


1 - Slicing: 

`print(df.head(2)) #Print first two rows`

`print(df.tail(2)) #Print last two rows`

2 - It will merge the common columns only

`merge = pd.merge(df1, df2)`

`merge = pd.merge(df1, df2, on="HPI")  #On common column else all fields will be col2_X, col2_Y`

3 - Joining

Combine both the data by columns

4 - Concat 

Combine data by rows

5 - Munging

Convert the particular format of data into another data
e.g CSV file to HTML. 

`import pandas as pd`

`country = pd.read_csv('path..')`

`country.to_html(edu.html)` 


## Statistics


`from statistics import mean`

### Operations:
1. Mean
2. Mode
3. Median
4. Variance


## Python for Hadoop: Pydoop

### Hadoop : 
Apache Hadoop is an open source framework that iss used to efficeintly store and process large datasets ranging in size from gigabytes to petabytes of data. It clusters multiple compu=uters to analyze massive datasets in parallel more quickly.

### Pydoop :

Pydoop is a python interface to Hadoop that allows you to write MapReduce applications and interact with HDFS in pure python

