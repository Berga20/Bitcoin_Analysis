#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:17:50 2021

@author: marcobergamin
"""
# 1 - Import data

import json
myfile = open('market-cap.json')
data = json.load(myfile)
myfile.close()

# 2 - Isolate values and convert time

v = [i for i in data['values']]

xs = [el['x'] for el in v]
ys = [el['y'] for el in v]

#timestamp_isolated = [el['x'] for el in v]

def timeconvert(x):
    dates = []

    for el in x:
        from datetime import datetime
        timestamp = el
        dt_object = datetime.fromtimestamp(timestamp).date()
        dates.append(dt_object)
    return dates

dates = timeconvert(xs)

# 3 - Plotting the graph 

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.plot(dates, ys, color='blue', label = 'Capitalization')

ax.set_xlabel('time')
ax.set_ylabel('Cap [USD]')
ax.set_title('Market Capitalization')
#ax.xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gcf().autofmt_xdate()
ax.grid()
#plt.savefig('capitalization.pdf')