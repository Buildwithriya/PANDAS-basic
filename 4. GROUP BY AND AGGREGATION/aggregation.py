import pandas as pd

df= pd.read_csv(r'C:\Users\Riya\OneDrive\Documents\PANDAS basic\job_salary_prediction_dataset.csv')

print(df.info())
# GROUP BY 
# average salary by job title

print(df.groupby ('job_title')['salary'].mean())

# average salary by experience years
print(df.groupby ('experience_years')['salary'].mean())

# how many location are there for each job title
print(df.groupby('job_title')['location'].nunique())


# AGGREGATION FUNCTION

# all aggregation functions 
print(df.groupby ('job_title')['salary'].mean())
print(df.groupby ('experience_years' )['salary'].max())
print(df.groupby ('experience_years' )['salary'].min())
print(df.groupby ('experience_years' )['salary'].count())
print(df.groupby ('job_title')['salary'].median())
print(df.groupby ('job_title')['salary'].sum())
print(df.shape)


# Get ALL stats at once with describe()
print(df.groupby ('job_title')['salary'].describe())

# multiple stats
print(df.groupby ('job_title')['salary'].agg(['mean','max','min']))

# different stats from different column
print(df.groupby ('job_title').agg({'salary':'mean','experience_years':'max'}))


# Clean column names with reset_index()
print(df.groupby ('job_title')['salary'].mean().reset_index())


# group by multiple columns

print(df.groupby(['job_title','location'])['salary'].mean())

# Save as a clean DataFrame
salary_by_job_location=df.groupby(['job_title','location'])['salary'].mean().reset_index()
salary_by_job_location.columns=['job_title','location','average_salary']
print(salary_by_job_location)

# valuecount vs group by 
print(df['job_title'].value_counts())
print(df.groupby('job_title')['salary'].count())

# value_counts with percentage
print(df['job_title'].value_counts(normalize=True)*100)

# Sort groupby result
print(df.groupby('job_title')['salary'].mean().sort_values(ascending=False))


# pivot_table() — Excel pivot in Python

print(pd.pivot_table(df,values='salary', index='job_title', columns='location', aggfunc='mean'))

# fill empty cell with 0
print(pd.pivot_table(df,values='salary', index='job_title', columns='location', aggfunc='mean', fill_value=0))