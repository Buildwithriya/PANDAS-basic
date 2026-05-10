
import pandas as pd 

df= pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\PANDAS basic\6. mini project - data cleaning (pyhton)\dirty_cafe_sales.csv")

print("shape:",df.shape)
print(df.head())
print (df.info())
print(df.describe())

# null value check 

print(df.isnull().sum())

# unique value in columns

print(df['Item'].unique())
print(df['Payment Method'].unique())
print(df['Location'].unique())


