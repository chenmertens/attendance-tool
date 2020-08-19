#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 04:12:40 2020

@author: williamchen
"""


import pandas as pd
import os
import glob

cl_name = input("Enter class list name:")
min_time = input("Enter minimum duration of attendance (minutes):")
min_time = int(min_time)
classlist = pd.read_csv("%s.csv" %cl_name, header = None)

classlist.rename(columns={0: 'id', 1: 'last', 2: 'first', 3: 'User Email', 4: '4', 5: '5', 6: '6', 7: '7'}, inplace=True)
classlist['User Email'] = classlist['User Email'].str.strip()
os.chdir("lists")
path = os.getcwd()

all_files = glob.glob(path + "/*.csv")

df = pd.concat((pd.read_csv(f) for f in all_files))
filter_ = df['Total Duration (Minutes)'] >= min_time
good = df[filter_]
good['User Email'] = good['User Email'].str.lower()

counts = good.groupby('User Email').count()
counts = counts.reset_index()
counts.columns = ['User Email', 'Count', 'scrum']
del counts['scrum']
results = classlist.merge(counts, how = 'left')
os.chdir("..")
results.to_csv('results.csv')