
import pandas as pd 
import numpy as np

df= pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\PANDAS basic\6. mini project - data cleaning (pyhton)\dirty_cafe_sales.csv")

print("shape:",df.shape)
print(df.head())
print (df.info())
print(df.describe())

# null value check 

print(df.isnull().sum())

# unique value in columns

print(df['Item'].unique().value_counts())
print(df['Payment Method'].unique())
print(df['Location'].unique())


# handling missing values

df['Location'] = df['Location'].replace(['ERROR', '', np.nan], 'Takeaway')
print (df['Location'].unique())


df['Payment Method'] = df['Payment Method'].replace(['ERROR', '', np.nan], 'Digital Wallet')
print (df['Payment Method'].unique())

df['Item'] = df['Item'].replace(['ERROR', '', np.nan], 'UNKNOWN')
print (df['Item'].unique())

df['Quantity'] = df['Quantity'].replace(['ERROR','UNKNOWN', ''], np.nan)
print (df['Quantity'].unique())

df['Price Per Unit'] = df['Price Per Unit'].replace(['ERROR','UNKNOWN', ''], np.nan)
print (df['Price Per Unit'].unique())

df['Total Spent'] = df['Total Spent'].replace(['ERROR','UNKNOWN', ''], np.nan)
print (df['Total Spent'].unique())


df['Transaction Date'] = df['Transaction Date'].replace(['ERROR', '', np.nan], 'UNKNOWN')
print (df['Transaction Date'].unique())



# change data type 


df['Price Per Unit'] = df['Price Per Unit'].astype(float)

df['Total Spent'] = df['Total Spent'].astype(float)

print(df.info())