## DataFrame= Multi Dimensional Data set

import pandas as pd

data = {
    "Name": ['sahil', 'subbu', 'sarita', 'dilip'],
    'Age': [27, 30, 55, 63],
    'Gender': ['M', 'F', 'F', 'M']
}

df = pd.DataFrame(data)
print(df)

print('\n######################## list of dictionary #######################\n')

data = [
    {"Name": 'sahil', 'Age': 27, "Gender": 'M'},
    {"Name": 'subbu', 'Age': 31, "Gender": 'F'},
    {"Name": 'sarita', 'Age': 55, "Gender": 'F'},
    {"Name": 'dilip', 'Age': 63, "Gender": 'M'}
]

df = pd.DataFrame(data)
print(df)

print('\n######################## Accessing the data #######################\n')

name = df['Name'].array
print(name)

print(df.loc[0])  # use foe row with index value

print(df.iloc[1][0])  # use for row index

print(df.at[2, 'Age'])  # index with specific column name

print(df.iat[2, 2])  # index column

print('\n######################## Manipulation of data #######################\n')

# should match to the length
# df['City']=['Pune','Jaipur','Katol']

df['City'] = ['Pune', 'Jaipur', 'Katol', 'Katol']
print(df)

print("\n########## dropping of column where inplace=False\n")
df.drop('Gender', axis=1, inplace=False)
print(df)
print("\n########## dropping of column where inplace=True\n")
df.drop('Gender', axis=1, inplace=True)  # inplace = true helps for permanent drop in same df
print(df)

print("\n########## Addition of 1 in age\n")
df['Age'] = df['Age'] + 1
print(df)

print('\n\n########################## Data Set #########################\n')

df = pd.read_csv("../File/Coffe_sales.csv")
print(df.head())
print(df.describe())

print("Missing Values:\n", df.isnull().any(), "\n")
print("Sum of Missing Values:\n", df.isnull().sum(), "\n")
print("Fill Missing Values:\n", df.fillna(0), "\n")

print("Fill Missing Values with mean os tht column:\n",
      df['hour_of_day'].fillna(df['hour_of_day'].mean()), "\n")

print("Rename a column:\n",
      df.rename(columns={'hour_of_day': 'Hours_day'}), "\n")

df['extended_money'] = df['money'].apply(lambda x: x ** 2)
print("Apply value to new column:\n", df['extended_money'].head(), "\n")

print("\n########### Data Aggregating and Grouping:\n")

grouped_mean = df.groupby('coffee_name')['money'].mean()
print(grouped_mean)
