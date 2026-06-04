import pandas as pd
import numpy as np
data= np.array([10,20,30,40])
s= pd.Series( data, index=["a","b","c","d"], dtype= float)
print(s)