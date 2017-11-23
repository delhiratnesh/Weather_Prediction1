# -*- coding: utf-8 -*-
"""
Created on Mon 23-Nov-2017
@author:    Ratnesh
@contact:   delhi_ratnesh@yahoo.com
Script Name : generate_test_data.py
Description : This script is used to generate test data for weather prediction machine learning exercise.
"""
from datetime import datetime
from datetime import timedelta
from random import randint

testdata = open("C:\Weather_Prediction\sample_data_file.csv", "w")
testdata.write('Location,Position,LocalTime,Conditions,Temperature,Pressure,Humidity\n')
for i in range(1,25):
 testdata.write('Sydney,"-33.86,151.21,39",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Brisbane,"-27.46,153.02",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Melbourne,"-37.83,144.98,7",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Adelaide,"-34.92,138.62,48",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Perth,"-31.95,115.86",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Darwin,"-12.46,130.84",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Canberra,"-35.28,149.13",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('GoldCoast,"-28.07,153.44",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Hobart,"-42.85,147.29",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
 testdata.write('Cairns,"-16.92,145.75",'+(datetime.now()+timedelta(hours=i)).strftime('%Y-%m-%dT%H:%M:%SZ')+',,,'+str(randint(980,1020))+','+str(randint(1,100))+'\n')
testdata.close()

