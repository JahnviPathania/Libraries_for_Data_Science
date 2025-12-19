import pandas as pd
#read data from csv file into a dataframe
df=pd.read_csv(r"C:\Users\Yoga\Downloads\archive (1)\data.csv", encoding="latin1")
print(df)
# df=pd.read_excel("path of file") to read excel
#df=pd.read_json("path of file") to read json
#if your file is in some sort of cloud use gcsfs library

