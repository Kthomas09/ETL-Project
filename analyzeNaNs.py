#Write file creates a module that can be imported with dependencies, %%writefile -a analyzeNaNs.py appends, remove if func is changed
#This function analyzes the NaN's in a DF
#Print/Returns a Dataframe with the NaN's count and the list of columns without NaN's
import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from datetime import date, datetime

def analyzeNaNs(dataFrameName):
    columnNames = dataFrameName.columns.tolist()
    NaNslist = []
    noNaNs =[]
    counter = 0
    for i in columnNames:
        colNaNs = dataFrameName[i].isna().sum()
        NaNslist.append(colNaNs)
        #print(f'{colNaNs} NaNs in {columnNames[counter]}')
        counter += 1
    #print(NaNslist)
    #print(columnNames)
    NaNsDF = pd.DataFrame(NaNslist, index = columnNames, columns =['NaNsCount'])
    transposeDF = NaNsDF.T
    for i in columnNames:
        if transposeDF[i][0] == 0:
            noNaNs.append(i)
            transposeDF = transposeDF.drop([i], axis=1)
    print('---------------------')
    print('Columns with no NaNs::')
    print('---------------------')
    for j in range(len(noNaNs)):
        alphaCols = sorted(noNaNs)
        print(f'{alphaCols[j]}')
    print('\n\n\n---------------------')
    print('DataFrame of NaNs::')
    print('---------------------')
    display(HTML(transposeDF.to_html()))
    #print(transposeDF)
#by ph1-6180
