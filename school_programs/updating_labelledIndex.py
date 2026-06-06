import pandas as pd
s = pd.Series([100, 230, 560, 575], index=['v', '#', '*', '$'])
s['#'] = 500
print(s)