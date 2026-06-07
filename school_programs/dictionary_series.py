import pandas as pd
d = {'A':10, 'B':20, 'C':30, 'D':40}
s = pd.Series(d)
print(s[[3,0,2]])