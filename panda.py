import pandas as pd
import numpy as np

df1 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], columns=["A","B","C"], index=['x','y','z','zz'])

print(df1.head())
print(df1.tail())