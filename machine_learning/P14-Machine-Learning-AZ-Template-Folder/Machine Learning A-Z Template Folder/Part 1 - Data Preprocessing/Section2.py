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

#Set working directory that contains dataset by saving this script in the same folder then running the script

#Import the dataset with Pandas
dataset = pd.read_csv('Data.csv')

#Put data into a matrix of features
X = dataset.iloc[:, :-1].values #the expression means all the rows (:) and all the columns except last one (:-1)

#Create "dependant Variable vector"
Y = dataset.iloc[:, 3].values #get the last column and all rows

