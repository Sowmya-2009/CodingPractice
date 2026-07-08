import pandas as pd
data=[{'a':1, 'b':2 ,'c':3},{'a':2, 'b':3}]
df=pd.DataFrame(data, index= ['first','second'], columns=['a','c'])
print(df)