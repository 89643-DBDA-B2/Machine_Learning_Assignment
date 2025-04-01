""""2. Refer the dataset "Advertising.csv" and perform following tasks.
i) Read the dataset "Advertising.csv" in data frame.

ii) Print first five records of dataset.

iii) print last five records from dataset.

iv) display the column names of the dataset.

v) display last three records from dataset.

vi) display the information about the dataset.

vii) display data types of each columns.
 
viii) check for null values in the dataset and display the sum of null values inside the column.

ix) drop all null values.

x) drop a column 'radio' from a dataset and display first ten records.

xi) increase the sales by 10% and add a new column "updated_sales" in dataframe.

xii) display shape of data.
"""

import pandas as pd

df = pd.read_csv('D:/temporary/Machine_Learning/assignment1/Advertising.csv')

#print(df.head(3))
# df.tail()
#df.tail(3)
# df.info()

# df.isnull().sum()

# #How to drop null values in dataframe
#print(df.isna().sum())



df = df.drop(['radio'],axis=1)

# print(df.info())

#print(df.head())

df['new_sales'] = df['sales']*1.1

print(df.shape)