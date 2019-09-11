# -*- coding: utf-8 -*-
"""
@assignment name: DS6001
@filename: triplecrown.py
@author: Brigitte Hogan (bwh5v)
@author: Cedric Harper
@language: Python v3
@date: 10 Sep 2019
    
Work in your Capstone Teams to code the solution with an output that 
reads “[Horse’s Name] averaged [ x ] mph across the three triple crown races. 

American Pharaoh won the Triple Crown.  He won the Belmont, a 12 furlong track,
with a time of 2:26.65, the Kentucky Derby, a 10 furlong track, with a time of
2:03.02, and the Preakness Stakes, a 9.5 furlong track, with a time of 1:58.46.
What was his average speed in mph?

"""
import re # for re.split

horse = input("Enter the horse's name: ")
belmont   = input("Enter " + horse + "'s time for the Belmont: ")
kentucky  = input("Enter " + horse + "'s time for the Kentucky Derby: ")
preakness = input("Enter " + horse + "'s time for the Preakness Stakes: ")

#print(belmont)
#print(kentucky)
#print(preakness)

def time_in_hrs(time):
    time_hr  = int(re.split(':|\.', time)[0])
    time_min = int(re.split(':|\.', time)[1])
    time_sec = int(re.split(':|\.', time)[2])
    time_total = time_hr + (time_min/60) + (time_sec/3600)
    return time_total

#print(time_in_hrs(belmont))

# furlong-mile conversion
fpm = 7.99998
mpf = 0.125

belmont_dist   = 12 * mpf
kentucky_dist  = 10 * mpf 
preakness_dist = 9.5 * mpf

average_mph = ((time_in_hrs(belmont)/belmont_dist) + (time_in_hrs(kentucky)/kentucky_dist) + (time_in_hrs(preakness)/preakness_dist))/3
print_mph = str(round(average_mph, 2))

print('\n')
print(horse + " averaged " + print_mph + " mph across the three triple crown races.")

