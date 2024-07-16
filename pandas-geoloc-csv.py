#!/usr/bin/python

import pandas as pd

csvfile = 'geoloc.tsv.a-f.csv'
data = pd.read_csv(csvfile, encoding="utf-8")

match_substring = 'Bay'
for i in range (10,1000):
    # we use iat instad of iloc so the headers don't get printed
    loc_name = str(data.iat[i,5])
    if match_substring in loc_name:
        print("match found: " + str(i) + ". " + loc_name)
