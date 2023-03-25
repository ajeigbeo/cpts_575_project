#this file contains methods to clean the sequences.
#for ease of use, I will be splitting the date obect into ,year, month, day
#then the data is organized based on date

import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

def clean(somDataFrame: DataFrame):
    length = len(somDataFrame.index)

    listOfDates = [['year', 'month', 'day']]

    somDataFrame = somDataFrame.dropna(how='any').copy() #remom

    print(type(somDataFrame))

    for index, row in somDataFrame.iterrows():
        newDate = splitDate(row['date'])
        listOfDates = np.append(listOfDates, [newDate], axis = 0)
    

    listOfDates = np.delete(listOfDates, (0), axis = 0) #gets rid of the first row of listOfDates


    somDataFrame["year"] = listOfDates[:,0] #this adds all of the listOfDates columns to the dataframe
    somDataFrame["month"] =  listOfDates[:,1]
    somDataFrame["day"] =  listOfDates[:,2]

    #this sorts in order of year, than month than day
    somDataFrame = somDataFrame.sort_values(by=['year', 'month','day'], ascending=True)

    somDataFrame.to_csv("cleaned_sequences.csv") #turns the current dataframe into a csvfile
    return somDataFrame


def splitDate(date):

    year = 0 #default values if something goes wrong
    month = 0
    day = 0
    try:
        if('-' in date): #assume only 2 types of date formats in either yyyy-mm or mm/dd/yyyy
            newSplit = date.split("-")
            year = newSplit[0]
            month = newSplit[1]
            day = 1
        elif('/' in date): #if mm/dd/yyy
            newSplit = date.split("/")

            if(len(newSplit) == 3):
                year = newSplit[2]
                month = newSplit[0]
                day = newSplit[1]
        else: 
            if(len(date) == 4): #if yyyy
                year = date
    except:
        print(date)



    newList = [year, month, day]

    return newList