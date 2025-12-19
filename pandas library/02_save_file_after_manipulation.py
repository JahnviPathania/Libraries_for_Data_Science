#how to save file 
import pandas as pd
data={"name":['jahnvi','karan','ashish'],
      "age":[10,20,30],
      "city":['nagpur','mumbai','delhi']}
df=pd.DataFrame(data)
print(df)
#how to save this file into csv
# df.to_csv("output.csv",index=False)to not take the index
#how to save it into excel
# df.to_excel("output.xlsx",index=False)
#how to save it into json
df.to_json("output.json",index=False)