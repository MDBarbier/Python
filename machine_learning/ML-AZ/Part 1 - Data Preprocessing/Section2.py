# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:51:45 2019

@author: matth
"""

#Data Preprocessing

#Import required libraries
import numpy as np #mathematical functions
import matplotlib.pyplot as plt #chart plotting
import pandas as pd #importing and managing datasets
from sklearn.impute import SimpleImputer #Taking care of missing data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# NB Set working directory that contains dataset by saving this script in the same folder then running the script

#### Importing and preparing data

#Import the dataset with Pandas
dataset = pd.read_csv('Data.csv')

#Put data into a matrix of features
X = dataset.iloc[:, :-1].values #the expression means all the rows (:) and all the columns except last one (:-1)

#Create "dependant Variable vector"
Y = dataset.iloc[:, 3].values #get the last column and all rows

#Tell the imputer what to do
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

#Fit the imputer to some data
imputer = imputer.fit(X[:,1:3]) #fit to columns 1 & 2, all rows

#Apply the transformation
X[:,1:3] = imputer.transform(X[:,1:3])

####Encoding categorical data 

#Apply labelEncoder to a column
labelEncoder_X = LabelEncoder() 
X[:,0] = labelEncoder_X.fit_transform(X[:,0]);

#Convert country to non-ordered data (because there are 3 possible values it ends up as 3 columns)
oneHotEncoder = OneHotEncoder(categorical_features=[0])
X = oneHotEncoder.fit_transform(X).toarray()

#Convert purchased to non ordered-data (will be converted to binary column)
labelEncoder_Y = LabelEncoder() 
Y = labelEncoder_Y.fit_transform(Y);

##### Splitting training data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


#### Feature scaling

sc_X  = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


print(X)