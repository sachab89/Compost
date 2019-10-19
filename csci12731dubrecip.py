#Name: ...Shane Bastien...
#Email: ...Shane.Bastien46@myhunter.cuny.edu
#Date:10.18.2019
#multiplies first column of csv file by two


import numpy as np
import pandas as pd
#fileinput = str(input("Which file do you want?"))
#if not ".csv" in fileinput:
  #fileinput += ".csv"
  
recip= str(input("Enter recipe in CSV format btwn quotes:"))
if not ".csv" in recip:
    recip += ".csv"

pd.read_csv(recip)
recip['Amount']=recip['Amount']*2 
#print("Double your recipe is:", recip)

print(data)
