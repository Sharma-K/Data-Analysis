## Data Analysis

Data Science is about finding and exploring data in real world, and then using that knowledge to solve business problems.

## Python libraries for data analysis:

- pandas     : used for structured data operations like CSV files and data manipulations.
- numPy      : focuses on array manipulation and other features of Scipy
- SciPy      : Scientific tools like Linear algebra, Fourier transform, built on top of NumPy
- Matplotlib : visualisation of data





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


### Series VS DataFrame :

1. Series :  A series is a one dimensional object that can hold any data type such as integers, floats and string

`x = pd.Series([6,4,31,5])`


2. DataFrame : A Dataframe is a two dimensional object that can have columns with potential different data types.
like a Table

`XYZ_web = {'Day': [1,2,3,4,5,6], "Visitors": [1000,700,6000,1000,400,350], "Bounce_Rate": [20,20,43,65,23,65]}`
`df = pd.DataFrame(XYZ_web)`


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

