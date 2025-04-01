"""1. i) Create a list of empids and names (10 employees).
   ii) Convert list into Series.
   iii) Convert Series into DataFrame.
   iv) a) Display all records.
      b) Display first five records.
      c) Display last five records.
   v) Save the record in csv file (MyRecord.csv)"""

import pandas as pd

Emp_list = [{'empids':1 , 'name':'abc'},
            {'empids':2 , 'name':'bcd'},
            {'empids':3 , 'name':'cde'},
            {'empids':4 , 'name':'efg'},
            {'empids':5 , 'name':'fgh'},
            {'empids':6 , 'name':'ghi'},
            {'empids':7 , 'name':'hij'},
            {'empids':8 , 'name':'ijk'},
            {'empids':9 , 'name':'jkl'},
            {'empids':10 , 'name':'klm'},
            ]

panda_series = pd.Series(Emp_list)

#print(f"series is {panda_series}, and its type is {type(panda_series)}")

panda_dataframe = pd.DataFrame(panda_series)

#print(f"data frame  is {panda_dataframe}, and its type is {type(panda_dataframe)}")

# print(panda_dataframe.head())
# print(panda_dataframe.tail())

# with open("./record.csv","wt") as file1:
#     file1.write(panda_dataframe)


panda_dataframe.to_csv('./assignment1/MyRecord.csv')