import pandas as pd 

df=pd.read_csv(r"C:\Users\Riya\OneDrive\Documents\PANDAS basic\3. HANDLING NULL VALUES\MOVIE.csv")


# finding missing values 

# count null per column
print(df.isnull().sum())

# as percentage
print((df.isnull().sum()/len(df))*100)

# single column check for null values
print (df['RATING'].isnull().sum())

# rows where rating is null
print(df[df['RATING'].isnull()])

# rows where rating is not null
print(df[df['RATING'].notnull()])


# drop missing values ---dropna()

# drop rows where a specific columns are null
print(df.dropna(subset=['YEAR']))

# DROP rows where all columns are null
print(df.dropna(how='all'))

# drop all rows that have any null values
# print(df.dropna())


# save the result
df_clean=df.dropna(subset=['RATING'])
print(df_clean.shape)

# fill missing values ---fillna()

# fill with the fixed value 
df['RATING']=df['RATING'].fillna(0)
print(df['RATING'])

print(df.info())

# FILL with mean value
mean_RunTime= df['RunTime'].mean()
df['RunTime']= df['RunTime'].fillna(mean_RunTime)
print(df['RunTime'])
print(mean_RunTime)

# fill with median 


# df['RunTime']= df['RunTime'].fillna(df['RunTime'].median())
# print(df['RunTime'])

# # fill with mode
# df['RunTime']= df['RunTime'].fillna(df['RunTime'].mode()[0])
# print(df['RunTime'])


# fill with text 
df['MOVIES']= df['MOVIES'].fillna('unknown')
print(df['MOVIES'])

df['YEAR']= df['YEAR'].fillna('unknown')
print(df['YEAR'])

df['GENRE']= df['GENRE'].fillna('unknown')
print(df['GENRE'])

df['ONE-LINE']= df['ONE-LINE'].fillna('unknown')
print(df['ONE-LINE'])

df['STARS']= df['STARS'].fillna('unknown')
print(df['STARS'])

df['VOTES']= df['VOTES'].fillna('unknown')
print(df['VOTES'])


# RENAME AND DROP
# RENAME column name 

df= df.rename(columns={'ONE-LINE':'DESCRIPTION',
                       'MOVIES':'MOVIE_NAME'})

print(df)

# MAKE all column names lowercase

df.columns= df.columns.str.lower()
print(df.columns)


# drop a single column
df_drop=df.drop(columns=['gross'])
print(df_drop)

# drop multiple columns

df_drop=df.drop(columns=['gross','description','stars'])
print(df_drop)

# add new column
# combine two column

df['movie-info']=df['genre']+ df['movie_name']
print(df['movie-info'])

print(df['rating'])
# create a new column based on condition
df['top-rated']= df['rating']> 8.0
print(df['top-rated'])

# rating using cut 
df['rating_category']= pd.cut(df['rating'],
                              bins=[0,5,7,10],
                              labels=['low','medium','high'])
print(df['rating_category'])

# change data type ---astype()

# check current data type
print(df.dtypes)

# convert into integer

print(df['rating'].astype(int))

# convert into float
print(df['rating'].astype(float))

