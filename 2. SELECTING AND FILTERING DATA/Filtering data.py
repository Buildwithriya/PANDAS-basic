import pandas as pd

df= pd.read_csv(r'C:\Users\Riya\OneDrive\Documents\PANDAS basic\job_salary_prediction_dataset.csv')

# selecting one or multiple columns 
print (df['job_title']) # single column

print (df[['job_title' , 'salary','certifications']]) # multiple columns

# to save the selected columns to a new variable

new= df[[ 'job_title','salary','certifications','education_level','location']]

print (new.head())

# FILTER ROWS AND CONDITIONS

# filter rows where job_title is 'Data Analyst
print(df[df['job_title']== 'Data Analyst'])


# filter rows where salary is > 100000

print (df[df['salary']>100000])

print (len(df[df['salary']>100000]))

# MULTIPLE CONDITIONS
# filter rows where job_title is 'Data Scientist' and salary is > 100000
print(df[(df['job_title']== 'Data Scientist')&(df['salary']>100000)])

# filter rows where job_title is 'Frontend Developer' and experience is>10 years

print(df[(df['job_title']== 'Frontend Developer') & (df['experience_years']>10)])

print(df['location'].unique())
# filter rows where job_title is 'frontend developer' and location is 'india'or 'uk'

print(df[(df['job_title']=='Frontend Developer') & ((df['location']=='India')|(df['location']=='UK'))])


# LOC AND ILOC 
# loc ( filter row and columns by label)

print(df.loc[0])  # show the first row of dataframe
print(df.loc[0,'industry'])  # show the industry of first row
print(df.loc[0:3 ,['job_title','salary']])   # row 0-4 and columns job_title and salary

# iloc ( filter rows and columns by index )

print(df.iloc[1]) # show 2nd row of df
print(df.iloc[1,3]) #show the 4th column of second row 
print(df.iloc[0:3,0:5]) # show first 3 rows and first 5 columns
print(df.iloc[-1]) # show the last row of df


# insin() and between() function

# filter rows where location is in 'India','UK','USA'
print(df[df['location'].isin(['India','UK','USA'])])

# filter rows where salary is between 50000 and 100000
print(df[df['salary'].between(50000,100000)])

# sort rows  -- sort_values() function

# sort rows by salary in ascending order
print(df.sort_values('salary'))

# sort rows by salary in descending order
print(df.sort_values('salary', ascending=False))

# sort multiple column 

print(df.sort_values(['job_title','salary'],ascending=[True,False]))

# top 10 highest paid jobs
print(df.sort_values(['job_title','salary'],ascending=[True,False]).head(10))
print(df.sort_values('salary',ascending=False)[['job_title','salary']].head(10))
