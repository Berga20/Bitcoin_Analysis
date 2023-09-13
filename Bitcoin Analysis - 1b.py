#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:34:22 2021

@author: marcobergamin
"""

# 1 - Import data

import json
myfile = open('market-cap.json')
data = json.load(myfile)
myfile.close()

# 2 - Isolate values

v = [i for i in data['values']]

xs = [el['x'] for el in v]
ys = [el['y'] for el in v]

# 3 - Smooth timestamp values

def smooth(delta):
    avg = []
    
    for d in v:
        s = 0
        interval = range(d['x'] - delta, (d['x'] + delta))
        count = 0
        for d in v:
            if (d['x'] in interval):
                s = s + d['y']
                count = count + 1
        avg.append(s/count)
    return avg

smoothed_ys = smooth(1296000)

# 4 - Convert time

def timeconvert(x):
    dates = []

    for el in x:
        from datetime import datetime
        timestamp = el
        dt_object = datetime.fromtimestamp(timestamp).date()
        dates.append(dt_object)
    return dates

dates = timeconvert(xs)

# 5 - Plot the smoothed graph

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.plot(dates, smoothed_ys, color='red', label = 'Smoothed Capitalization')

ax.set_xlabel('time')
ax.set_ylabel('Cap [USD]')
ax.set_title('Market Capitalization')
#ax.xaxis.set_major_locator(plt.MaxNLocator(5))
plt.gcf().autofmt_xdate()
ax.grid()
#plt.savefig('smoothed capitalization.pdf')
