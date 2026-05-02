import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\PANDAS basic\job_salary_prediction_dataset.csv")

print(df.info())
# apply()

def experience_level(years):
    if years < 2 :
        return 'entry level'
    elif years < 5 :
        return 'mid level'
    elif years < 10 :
        return 'senior level'
    else:
        return  'expert level'
    
df['experience_level']= df['experience_years'].apply(experience_level)

print(df[['experience_years', 'experience_level']].head(10))

# lambda ()
df['salary_usd'] = df['salary'].apply(lambda x: round(x/90,2))  
print(df[['job_title','salary','salary_usd']].head(10))

# string operations
df['job_title']=df['job_title'].str.upper()
print(df['job_title'].head(10))

# Remove extra spaces from both sides
df['job_title'] = df['job_title'].str.strip()
print(df['job_title'].head(10))

# Replace a word
df['location']=df['location'].str.replace('newyork', 'ny')
print(df['location'].head(10))

# Check if column CONTAINS a word
print(df[df['job_title'].str.contains('ANALYST')])

# Get length of each string
df['JOB_title_length'] = df['job_title'].str.len()
print(df[['job_title', 'JOB_title_length']].head(10))

# map ()
df['education_level']=df['education_level'].map({'Bachelor': 'B','Master':'M','PhD': 'p','Diploma': 'D'})
print(df['education_level'].head(20))


# Replace port codes with full names
df['education_level'] = df['education_level'].map({
    'B': 'Bachelor',
    'M': 'Masters',
    'P': 'PhD',
    'D':'Diploma'})
print(df['education_level'].head(20))


# np.where()

df['salary_category'] = np.where(df['salary'] > 100000, 'High', 'Low')

print(df[['salary', 'salary_category']].head(10))



