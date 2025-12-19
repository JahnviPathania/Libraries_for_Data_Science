import pandas as pd
data={"name":['ram','shyam','krishna','jahnvi','ashish'],
      "age":[10,20,40,30,56],
      "salary":[30000,56000,45000,23000,67000],
      "performace_score":[85,89,87,65,78]}
df=pd.DataFrame(data)
print("sample data frame")
print(df)
print("stats")
print(df.describe())