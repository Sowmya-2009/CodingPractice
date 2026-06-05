import pandas as pd
data={'a':0,'b':1,"c":2}
s=pd.Series(data ,index=['b','c','d','a'])
print(s)