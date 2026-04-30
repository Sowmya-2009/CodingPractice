import pandas as pd

s1=pd.Series([16,17,18],index=['p','q','r'])

s2=pd.Series([-5,12,8],index=['r','q','b'])

print(s1.add(s2, fill_value=0))

print(s1.sub(s2, fill_value=0))

print(s1.mul(s2, fill_value=1))

print(s1.div(s2, fill_value=1))
