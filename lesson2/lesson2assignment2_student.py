#import packages required
import csv
import datetime
import matplotlib.pyplot as plt
from operator import itemgetter

#data file name, change the file name if different
datafile='rainfall-monthly-total.csv'
#initialize df as a list
df=[]
#read in csv file into 2d array call data
data=list(csv.reader(open(datafile)))

#this is for the first item
#convert the date string to datetime object and also the rainfall value read in as string to float
dd=[datetime.datetime.strptime(data[1][0],"%Y-%m"),float(data[1][1])]
#append  to the list
df.append(dd)

#to append  the rest of the value to the list df
for i in range(2,len(data)-1,1):
  dd=[datetime.datetime.strptime(data[i][0],"%Y-%m"),float(data[i][1])]
  df.append(dd)
  
#Assignment 2 start here compute the average rainfall


#split the two column in the list to x and y for ploting of graph
x=map(itemgetter(0),df)
y=map(itemgetter(1),df)
line=plt.plot_date(x,y,'-')
# use keyword args
plt.setp(line, color='r', linewidth=2.0)
plt.show()



  
  

