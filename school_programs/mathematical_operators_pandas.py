import pandas as pd
s1= pd.Series([16,17,18], index=['p','q','r'])
s2= pd.Series([-5,12,8], index=['r','q','b'])
print(s1+s2)
print(s1*s2)
print(s1-s2)
print(s1/s2)