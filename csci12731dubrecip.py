import numpy as np
import pandas as pd
#fileinput = str(input("Which file do you want?"))
#if not ".csv" in fileinput:
  #fileinput += ".csv"
  
recip= str(input("Enter recipe in CSV format btwn quotes:"))
if not ".csv" in recip:
    recip += ".csv"

data= pd.read_csv(recip)
#dubrecip= recip['Amount']*2
#print("Double your recipe is:", recip)

print(data)
