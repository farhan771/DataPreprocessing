#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 04:42:54 2018

@author: user
"""

import pandas as pd

filepath='/Users/user/Desktop/Big Data 2018/Capstone Project/Milestone4/Botnet Files/BotnetRawMerged.csv'
botnet=pd.read_csv(filepath,header=0,error_bad_lines=False)

botnet_Rand=botnet.sample(n=532686).reset_index(drop=True)
#print(botnet1_DNSRand.head())                                 
print(botnet_Rand.columns)

#Exporting file as CSV
out_csv='/Users/user/Desktop/Big Data 2018/Capstone Project/Milestone4/BotnetRawFinal.csv'
botnet_Rand.to_csv(out_csv)
