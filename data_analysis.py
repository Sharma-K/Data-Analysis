import pandas as pd

XYZ_web = {'Day': [1,2,3,4,5,6], "Visitors": [1000,700,6000,1000,400,350], "Bounce_Rate": [20,20,43,65,23,65]}

# Data Frame
df = pd.DataFrame(XYZ_web) # It will convert it into a table
print(df)

#Slicing

print(df.head(2)) #Print first two rows
print(df.tail(2)) #Print last two rows

