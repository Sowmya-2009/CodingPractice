import pandas as pd
a= [{'name':'raj','last name':'kumar'},{'name':'vinodh', 'last name':'sharma'}]
df= pd.DataFrame(a, index=["row1", "row2"])
print(df)