import pandas as pd
import numpy as np
data= np.array([True,False])
s= pd.Series(data, index=["t","f"])
print(s)
