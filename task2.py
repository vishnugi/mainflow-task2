import pandas as pd
data = pd.read_csv('C:\\Users\\HP\\Downloads\\01.Data Cleaning and Preprocessing.csv')

print(data.info) # To know the info  of data frame

print(data.shape) #To Know No.of rows & columns in Data

print(data.describe()) #Descriptive statistics

print(data.drop_duplicates()) #To form the duplicates values

print(data.isnull()) #Check for  null value returns in boolean

print(data.isnull().sum()) #Return the number of null values per columns

print(data.notnull()) # Returns a Boolean series denoting whether each element is not null or not

print(data.isnull().sum().sum())#Returns the total no.of null values present

print(data.fillna(value=0)) #Fill NaN with some Value, Here I have filled

print(data.isnull().sum().sum()) #After filling NaN with Zero it will show that

print(data.fillna(method='pad')) #Using method pad we can fill NaN with forward non-NaN valid observation.

print(data.fillna(method='bfill')) # Using bfill we can fill NaN with backword non-NaN valid observation.

import numpy  as np
from scipy import stats

print(data.columns) #It shows all column names
print(data.drop(['observation'],axis=1,inplace=True))  # It drops the column named 'observation' from dataframe

Q1=data.quantile(0.25)
Q2=data.quantile(0.75)
IQR=Q2-Q1

print(IQR)
