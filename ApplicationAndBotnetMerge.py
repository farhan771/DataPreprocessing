#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:13:56 2018

@author: user
"""
import pandas as pd
from sklearn.utils import shuffle

#Script to add column "is botnet" and broadcast value "1" to the botnet data file and "0" to application data file.
#Merge Application and Botnet datasets and shuffle them for final input for machine learning

#Reading Application Data Packet Capture CSV file
filepath_AppRawData='/Users/user/Desktop/Big Data 2018/Capstone Project/Milestone4/App Files/ApplicationRawMerged.csv'
AppRawData=pd.read_csv(filepath_AppRawData,header=0,error_bad_lines=False)

#Randonizing Application Data file
AppRawData=AppRawData.sample(frac=1).reset_index(drop=True)

#Additing Target Attribute Lable
AppRawData['Is botnet'] = '0'

print(AppRawData.info)

#Reading Botnet Data Packet Capture CSV file
filepath_BotnetSubset='/Users/user/Desktop/Big Data 2018/Capstone Project/Milestone4/BotnetRawFinal.csv'
BotnetSubset=pd.read_csv(filepath_BotnetSubset,header=0)


#Randonizing BotnetSubset Data file
BotnetSubset=BotnetSubset.sample(frac=1).reset_index(drop=True)

#Additing Target Attribute Lable
BotnetSubset['Is botnet'] = '1'

print(BotnetSubset.info)

#Merging Application and Botnet data files together
frames1=[AppRawData,BotnetSubset]
SemiApplicationBotnetData=pd.concat(frames1)

#Resampling the entire file to randomize contents
MasterApplicationBotnetData=SemiApplicationBotnetData.sample(frac=1).reset_index(drop=True)


MasterApplicationBotnetData.info()
print(MasterApplicationBotnetData.columns)

#Reaggraing the coloums as concat function arrages colums alphabetically
cols1=['Source', 'Destination', 'Protocol', 'Length',
       'DNS_Questions','Domain Name System', 'Answer RRs',
       'Time to live', 'Name Length','Is botnet']

MasterApplicationBotnetData=MasterApplicationBotnetData[cols1]

print(MasterApplicationBotnetData.columns)

#Futher randomizing the data
MasterApplicationBotnetData= shuffle(MasterApplicationBotnetData)

#Taking care of the missing values by assigning them to 0
MasterApplicationBotnetData['Length'] = MasterApplicationBotnetData['Length'].fillna(0)
MasterApplicationBotnetData['DNS_Questions'] = MasterApplicationBotnetData['DNS_Questions'].fillna(0)
MasterApplicationBotnetData['Name Length'] = MasterApplicationBotnetData['Name Length'].fillna(0)
MasterApplicationBotnetData['Domain Name System'] = MasterApplicationBotnetData['Domain Name System'].fillna(0)
MasterApplicationBotnetData['Answer RRs'] = MasterApplicationBotnetData['Answer RRs'].fillna(0)
MasterApplicationBotnetData['Time to live'] = MasterApplicationBotnetData['Answer RRs'].fillna(0)
MasterApplicationBotnetData['Name Length'] = MasterApplicationBotnetData['Name Length'].fillna(0)

#Exporting file as CSV
out_csv33='/Users/user/Desktop/Big Data 2018/Capstone Project/Milestone4/ApplicationBotnetMergeFinal_33.csv'
MasterApplicationBotnetData.to_csv(out_csv33)


