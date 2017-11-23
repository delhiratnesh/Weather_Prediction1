# -*- coding: utf-8 -*-
"""
Created on Mon 23-Nov-2017
@author:    Ratnesh
@contact:   delhi_ratnesh@yahoo.com
Script Name : weather_prediction.py
Description : This script is used to predict future weather prediction based on the sample learning file provided.
"""


import pandas
pandas.set_option('display.width', 150)

# Read in the training data.
training = pandas.read_csv("C:\Weather_Prediction\weather_history_training_dataset.csv")
# Print the names of the columns in training.
print(training.columns)

print(training.shape)

print(training)

#reduce data sample for prototyping
#training=training[training["Location"] == 'Sydney']
#print((training.LocalTime.str[11:13].astype(int)))

training['hour']=training.LocalTime.str[11:13].astype(int)
training['xcoordloc']=training.Position.str[0:3].astype(float)
training['ycoordloc']=training.Position.str[7:10].astype(float)


#training=training.drop(['Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10'],axis=1)
print(training)


training.corr()["Temperature"] # this tells us which column is most closely related to the column that we are trying to predict.

#good_columns
#plot_columns
#kmeans_model

training.columns.tolist()

# Get all the columns from the dataframe.
columns = training.columns.tolist()
# Filter the columns to remove ones we don't want. All non numeric columns have to be removed else model can not be generated/fit.
columns = [c for c in columns if c not in ["Temperature","Location","Position",'LocalTime','Conditions']]
columns 
# Store the variable we'll be predicting on.
target = "Temperature"

# Import a convenience function to split the sets.
#from sklearn.cross_validation import train_test_split

testing = pandas.read_csv("C:\Weather_Prediction\sample_data_file.csv")

# Print the shapes of both sets.
#print(training.shape)
#print(testing.shape)

training
testing

# Import the linearregression model.
from sklearn.linear_model import LinearRegression

# Initialize the model class.
model = LinearRegression()
# Fit the model to the training data.
model.fit(training[columns], training[target])


testing['hour']=testing.LocalTime.str[11:13].astype(int)
testing['xcoordloc']=testing.Position.str[0:3].astype(float)
testing['ycoordloc']=testing.Position.str[7:10].astype(float)

# Generate our predictions for the test set.
predictions = model.predict(testing[columns])

testing['Temperature']=model.predict(testing[columns])

testing.loc[testing['Temperature'] < 10,'Conditions'] = 'Very Cold'
testing.loc[(testing.Temperature > 10) & (testing.Temperature < 15),'Conditions'] = 'Cold'
testing.loc[testing.Temperature > 15,'Conditions'] = 'Sunny'
testing.loc[testing.Humidity > 80,'Conditions'] = 'Rain'

#testing['Temperature']

testing

testing[testing.Location=='Sydney']
testing[testing.Location=='Darwin']
testing[testing.Location=='Canberra']
testing[testing.Location=='Hobart']

print(predictions)

list(predictions)

testing.to_csv("C:\Weather_Prediction\predicted_data_file_linear_regression_method.csv")

#print(predictions[4])

#print(model)

# not generating MSE since I didnt generate test dataset with expected values.
# Import the scikit-learn function to compute error.
#from sklearn.metrics import mean_squared_error
# Compute error between our test predictions and the actual values.
#mean_squared_error(predictions, testing[target])

#below is the data for which above values were predicted.

###----------------------------
#before using another algorithm, emptying the predicted and computed column values.
###

testing['Temperature']=''
testing['Conditions']=''

testing

# Import the random forest model.
from sklearn.ensemble import RandomForestRegressor

# Initialize the model with some parameters.
model = RandomForestRegressor(n_estimators=100, min_samples_leaf=10, random_state=1)
model = RandomForestRegressor()
# Fit the model to the data.
model.fit(training[columns], training[target])
# Make predictions.
predictions = model.predict(testing[columns])

testing['Temperature']=model.predict(testing[columns])

testing.loc[testing['Temperature'] < 10,'Conditions'] = 'Very Cold'
testing.loc[(testing.Temperature > 10) & (testing.Temperature < 15),'Conditions'] = 'Cold'
testing.loc[testing.Temperature > 15,'Conditions'] = 'Sunny'
testing.loc[testing.Humidity > 80,'Conditions'] = 'Rain'

#testing['Temperature']

print(testing)

testing[testing.Location=='Sydney']
testing[testing.Location=='Darwin']
testing[testing.Location=='Canberra']
testing[testing.Location=='Hobart']

#not generating MSE since I didnt create testdataset with expected values.
#list(predictions)
# Compute the error.
#mean_squared_error(predictions, testing[target])#427

#list(predictions)
testing.to_csv("C:\Weather_Prediction\predicted_data_file_random_forest_method.csv")
