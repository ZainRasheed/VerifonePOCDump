# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 09:30:12 2019

@author: MohammedS2
"""

#Import tha libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#Importing the data
Uber = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/Uber data/Uber_Request_Data.csv")
#Data imported into a dataframe 'Uber'



#Checking for duplicate rows in RequestID
#And removing if no duplicates
''' FAILED or bad strategy
X = Uber["Request id"]
X_Count = X.value_counts()
X_Count_max = X_Count.max()   #if te max od count is 1, no duplicate
plt.plot(X,X_Count)     #if the grapg is not being plotted, duplicate exist 
'''
X = Uber["Request id"]
#Copied the column into 'X'

'''X_Count = X.repeat(repeats > n) // doesn't work '''
'''Another strategy exist using df.describe()'''
#set true for every deuplicated value
X_Bool = X.duplicated(keep = False)
#Result : a series of bool, true for every dulpicated value

#Check if there is any True in the series
print(any(X_Bool))                     
# Result : Prints False, Hence no repeatation

#remove the col
Uber = Uber.iloc[:,1:6]
#Result : ReqID is sliced from the dataset



#Removing the Drop timestamp
#Removing the Driver id
#As there is no reqment of that column
Uber = Uber[["Pickup point","Status","Request timestamp"]]
#Result : Dataset with "Pickup point","Status","Request timestamp"



#Removing month, day, year from the time stamps and getting a single format
#month and year are same
#days is linear
X = Uber["Request timestamp"] 
X = pd.to_datetime(X) #converting to numpy datetime type dtype('<M8[ns]')
X = X.dt.strftime('%H:%M:%S') #converting the timetsamp to ss:mm:hh
Uber["Request timestamp"] = X

#Result : Dataset with converted timestamp ss:mm:hh


#early morning 12.00 am -- 5.59 am
#morning 6.00 am -- 10.59 am
#around noon 11.00 am -- 2.59pm
#evening 3.00pm -- 7.50 pm
#late evening 8.00 pm -- 11.59 am

#12-6 early morning
#7-11 morning
#12-2 noon
#3-8 evening
#9-12 late evening

X = Uber["Request timestamp"].copy() 
Uber["Request timestamp discrete"] = pd.to_datetime(X, format='%H:%M:%S').dt.hour
X = pd.cut(Uber["Request timestamp discrete"],bins=[0, 6, 11, 14, 16, 23],include_lowest=True,labels=["early morning", "morning", "noon", "evening","late evening"])
Uber["Request timestamp discrete"] = X
Uber = Uber[["Pickup point","Status","Request timestamp discrete"]]





"""Uni analysis"""
#Describe the dataset
Uber.describe()
#Result : Shows te count,unique values,etc of the datafraem
Uber["Pickup point"].value_counts()
Uber["Status"].value_counts()
Uber["Request timestamp discrete"].value_counts()

#Uber["Pickup point"].plot.hist(bins=5) // this will not work if the seried or dataframe is not numeric data
Uber["Pickup point"].apply(pd.value_counts).plot.hist(bins=3)
Uber["Status"].apply(pd.value_counts).plot.hist(bins=2)
Uber["Request timestamp discrete"].apply(pd.value_counts).plot
Uber.apply(pd.value_counts).plot(style = "k.")
