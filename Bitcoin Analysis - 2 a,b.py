#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 17:10:35 2021

@author: marcobergamin
"""

# 1 - Import data

import json

myfile_1 = open('miners-revenue.json')
data_r = json.load(myfile_1)
myfile_1.close()

myfile_2 = open('difficulty.json')
data_dif = json.load(myfile_2)
myfile_2.close()

# 2 - Isolate values

r = [i for i in data_r['values']]
dif = [el for el in data_dif['values']]

xs_r = [i['x'] for i in r]
ys_r = [i['y'] for i in dif]

xs_dif = [el['x'] for el in dif]
ys_dif = [el['y'] for el in dif]

# 3 - Smooth the curve of reward

def smooth(delta):
    avg = []
    
    for d in r:
        s = 0
        interval = range(d['x'] - delta, d['x'] + delta)
        count = 0
        for d in r:
            if (d['x'] in interval):
                s = s + d['y']
                count = count + 1
        avg.append(s/count)
    return avg

avg_r = smooth(604800)

# 4 - Convert time

def timeconvert(x):
    dates = []

    for d in x:
        from datetime import datetime
        timestamp = d['x']
        dt_object = datetime.fromtimestamp(timestamp).date()
        dates.append(dt_object)
    return dates

dates_r = timeconvert(r)
dates_dif = timeconvert(dif)

# 5 - Plot the smoothed revenue

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.plot(dates_r, avg_r, color='green', label = 'Miners Revenue')
# ax.plot(xss, ys, color= 'blue', label = '') we can use this one to plot another 
# curve in the plot

ax.set_xlabel('time')
ax.set_ylabel('Reward [USD]')
ax.set_title('Miners Reward')
#ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.grid()
plt.gcf().autofmt_xdate()
#ax.legend(loc = 'upper left')
#plt.savefig('Miners revenue.pdf')

# 6 - Plot the difficulty curve 

fix, ax = plt.subplots()
ax.plot(dates_dif, ys_dif, color='red', label = 'Mining Difficulty')
# ax.plot(xss, ys, color= 'blue', label = '') we can use this one to plot another 
# curve in the plot

ax.set_xlabel('time')
ax.set_ylabel('Difficulty level')
ax.set_title('Mining Difficulty')
#ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.grid()
plt.gcf().autofmt_xdate()
#ax.legend(loc = 'upper left')
#plt.savefig('Mining Difficulty.pdf')