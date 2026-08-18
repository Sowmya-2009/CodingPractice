import pandas as pd
import numpy as np
data={'raj':100,'john':200,'anu':300,'tina':400,'emy':800}
print('original dictionary:', data)
s=pd.Series(data)
print('created seriess from dictionary:',s)
print('numpy array')
a=np.array([10,20,30,40])
s=pd.Series(a)
print('created series from numpy array:',s)