#why explore data 
#to understand the dataset
#to identify the problem
#plan next steps
import pandas as pd 
#to see top 5 rows or bottom five rows
#we use head() and tail() method respectively
df=pd.read_csv(r"C:\Users\Yoga\Downloads\archive (1)\data.csv", encoding="latin1")
print("displayinf first 10 rows")
print(df.head(10))
print("displaying last 10 rows")
print(df.tail(10))
#if you dont give any value in the brackets by default its 5

