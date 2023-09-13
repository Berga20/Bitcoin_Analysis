#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:18:28 2021

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

# 3 - Select the omogeneous time span

while dif[0]['x'] != r[0]['x']:
    dif.remove(dif[0])
    
while r[-1]['x'] != dif[-1]['x']:
    r.remove(r[-1])
    
xs = [i['x'] for i in r]
ys_r = [i['y'] for i in r]
ys_dif = [el['y'] for el in dif]

# 4 - Compute the reward per difficulty 

def reward_difficulty(x, y):
    l = []
    p = 0
    for i in x:
        l.append(x[p]/y[p])
        p = p+1
    return l

ratios = reward_difficulty(ys_r, ys_dif)

def rew_dif_f (x, y):
    l = []
    p = 0
    for i in x:
        l.append ((x[p], y[p]))
        p = p+1
    return l

r_d_fun = rew_dif_f(xs, ratios)

# 5 - Smooth the curve 

def smooth(delta):
    avg = []
    
    for t in r_d_fun:
        s = 0
        interval = range(t[0] - delta, (t[0] + delta))
        count = 0
        for t in r_d_fun:
            if (t[0] in interval):
                s = s + t[1]
                count = count + 1
        avg.append(s/count)
    return avg

sm_ratios = smooth(604800)

# 6 - Convert time

def timeconvert(x):
    dates = []

    for i in x:
        from datetime import datetime
        timestamp = i
        dt_object = datetime.fromtimestamp(timestamp).date()
        dates.append(dt_object)
    return dates

dates = timeconvert(xs)

# 7 - Plot the curves

import matplotlib.pyplot as plt

fix, ax = plt.subplots()
ax.plot(dates, ratios, color='orange', label = 'R-D', linestyle = 'dashed')
ax.plot(dates, sm_ratios, color='brown', label = 'Smoothed R-D')

ax.set_xlabel('time')
ax.set_ylabel('Reward-Difficulty')
ax.set_title('Reward-Difficulty')
#ax.xaxis.set_major_locator(plt.MaxNLocator(5))
ax.grid()
plt.gcf().autofmt_xdate()
ax.legend(loc = 'upper center')
#plt.savefig('Reward - Difficulty.pdf')

# 8 - Define the most profitable periods

def highest(x):
    l = []
    x.sort()
    p = -1
    while (len(l) < (0.1*len(x))):
        l.append(x[p])
        p = p-1
    return l

high_prof = highest(ratios)

def periods(x):
    l = []
    for t in x:
        if t[1] in high_prof:
            l.append(t[0])
    return l
    
periods = periods(r_d_fun)

# 9 - Convert dates

profitable_dates = timeconvert(periods)