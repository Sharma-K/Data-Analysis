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

# Pandas Operations:
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

`merge = pd.merge(df1, df2, on="HPI")`



