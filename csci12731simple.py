import numpy as np
import pandas as pd



recip=pd.read_csv('meringues.csv')
recip['Amount']=recip['Amount']*2
print(recip)
