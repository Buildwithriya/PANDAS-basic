
# import pandas library

import pandas as pd

# loading data from local/csv file

df= pd.read_csv(r'C:\Users\Riya\OneDrive\Documents\PANDAS basic\job_salary_prediction_dataset.csv')

#  type of data frame
print(type(df))  

# display the data frame 
print(df)


# show first 5 rows of data frame
print (df.head() )
print (df.head(10) ) # for first 10 rows


# show last 5 rows of data frame 
print (df.tail())
print (df.tail(10)) # for last 10 rows

# show total no of row and column
print(df.shape)

# list of all column names 
print(df.columns.tolist())

# datatype of each column 
df.info()

# checks for missing values
print(df.isnull().sum())

# statistical summary

print(df.describe())

print(df.describe(include='all')) # include all data types

print(df['salary'].mean())
print(df['experience_years'].max())
print(df['job_title'].unique())

# selecting a column
print(df['job_title'])
print(df['certifications'].value_counts())
