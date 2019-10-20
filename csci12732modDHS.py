#Name: Shane Bastien
#Email: sachabastien@gmail.com
#Date: October 20, 2019

#ask the user to specify the input file,
#ask the user to specify the output file,
#make a plot of the fraction of the total population that are children over time from the data in input file, and
#store the plot in the output file the user specified.

import pandas as pd
import matplotlib.pyplot as plt



homeless = pd.read_csv(input("please enter name of file:"))
outfile= input("please enter name of output file:")
homeless["Fraction Children"]= homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
                                                                           
homeless.plot(x= "Date of Census", y= "Fraction Children")
plt.gca().invert_xaxis()
plt.show()

fig= plt.gcf()
fig.savefig(outfile)
