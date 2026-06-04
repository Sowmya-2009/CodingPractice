import pandas as pd
import numpy as np
data= np.array(["abdul","tina","yogesh","sowmya"])
s= pd.Series(data, index=[101,102,103,104])
print(s)