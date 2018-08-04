# !/usr/bin/python
# coding: utf-8

from tools import reader, time, ride_month, travel_time, speed

# Read data from csv of all Citibike in 2015
start = 1
end = 1
data = reader.read_data(2015, start, end)
# ride_month.analyze(data)
# gender.analyze(data)
# age.analyze(data)
# membership.analyze(data)
# time.analyze(data)
# travel_time.analyze(data)
s = speed.analyze(data)

# overall_analysis = overall.analyze(data, end-start+1)
'''
{
    'station_count': 330, 
    'bike_count': 4271, 
    'count_ride': 285552, 
    'freq_rental_year': 66.85834699133693, 
    'freq_rental_day': 2.228611566377898, 
    'avg_rental_period': 10.905426390523152
}
'''




