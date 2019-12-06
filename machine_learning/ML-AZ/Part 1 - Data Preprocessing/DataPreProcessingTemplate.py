# -*- coding: utf-8 -*-
"""
Data Preprocessing Template
  - Created on Friday Dec  6 2019 @author: matth
  
"""

#Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split

#### Parameters
columnsToRemove = -1
dependantVariableVector = 3
datafilePath = 'Data.csv'
testSize = 0.2
randomState = 0

#### Importing and preparing data
dataset = pd.read_csv(datafilePath)
X = dataset.iloc[:, :columnsToRemove].values
Y = dataset.iloc[:, dependantVariableVector].values

##### Splitting training data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = testSize, random_state = randomState)

#### Feature scaling
"""sc_X  = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#### Tests
assert X_train[0][0] == "Germany" and X_train[0][1] == 40.0, "Unexpected value in first element"
assert len(X_train) == 8, "Unexpected number of items in the training data"