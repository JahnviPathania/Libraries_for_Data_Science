import pandas as pd
#selecting columns can return a series or a dataframe
#filtering rows-extractring rows on a specific condition
#we use boolean indexing for filtering rows
data={"name":['ram','shyam','krishna','jahnvi','ashish'],
      "age":[10,20,40,30,56],
      "salary":[30000,56000,45000,23000,67000],
      "performace_score":[85,89,87,65,78]}
df=pd.DataFrame(data)
#selecting columns
column=df[["name","salary"]]
print(column)
#filter rows on condition
#single condition
maxsalary=df[df["salary"]>50000]
print(maxsalary)
#multiple conditions
filrows=df[(df["salary"]>50000) & (df["age"]>30)]
print(filrows)