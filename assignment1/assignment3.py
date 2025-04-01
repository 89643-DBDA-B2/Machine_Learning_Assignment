""""3. Refer the dataset "Salaries.csv" and perform following tasks.
i) Read the dataset in dataframe.

ii) display first five records.

iii) display first ten records.

iv) display last five records.

v) display last ten records.

vi) display the columns inside the dataset.

vii) display shape of data.

viii) describe the dataset.

ix) display the information about the dataset and analyse the data.

x) display types of each columns.

xi) Find out maximum,minimum,mean,median,standard deviation value of each column.

xii) check for null values in the dataset and display the sum of null values inside the column.

xiii) Replace all null values by mean or mode acoording to the type of column.
"""

import pandas as pd

df = pd.read_csv('D:/DBDA_Official10/Machine_Learning/Machine_Learning/datasets/Salary_Data.csv')

# df.head()
# df.head(10)
# df.tail()
# df.tail(10)
#print(df.keys())
df.describe()
df.info()