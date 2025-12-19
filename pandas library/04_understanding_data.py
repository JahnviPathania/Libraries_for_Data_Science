#why understand data
#to know no. of columns and rows 
# to know the type of data
#to know if missing data exists



#in python we use info() method- gives no.of rows and columns, column name,data type,null values,data size
import pandas as pd
df=pd.read_csv(r"C:\Users\Yoga\Downloads\archive (1)\data.csv", encoding="latin1")
print("displaying info of the data set")
print(df.info())

