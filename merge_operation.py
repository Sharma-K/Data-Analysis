import pandas as pd

val1 = {"HPI": [80,90,70,60], "Int_rate": [2,1,2,3], "IND_GDP": [50,45,45,67]}
val2 = {"HPI": [80,90,70,60], "Int_rate": [2,1,2,3], "IND_GDP": [50,45,45,67]}

df1 = pd.DataFrame(val1, index =[2001,2002,2003,2004])
df2 = pd.DataFrame(val2, index =[2005,2006,2007,2008])

merge = pd.merge(df1, df2, on="HPI")

print(merge)
