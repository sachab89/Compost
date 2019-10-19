import numpy as np

#fileinput = str(input("Which file do you want?"))
#if not ".csv" in fileinput:
  #fileinput += ".csv"
  
recip= str(input("Enter recipe in CSV format btwn quotes:"))
if not ".csv" in recip:
    recip += ".csv"
import pandas as pd
data= pd.read_csv(recip)
#dubrecip= recip['Amount']*2
#print("Double your recipe is:", recip)

print(data)
