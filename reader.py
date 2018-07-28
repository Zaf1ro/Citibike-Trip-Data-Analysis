# !/usr/bin/python
# coding: utf-8


import numpy as np
import pandas as pd
import time, datetime
import matplotlib.pyplot as plt


# Read Citibike data from csv file in one mouth
def read_data_one_mouth(csv_file_s):
    return pd.DataFrame(pd.read_csv(csv_file_s))


def read_data(year, start_month, end_month):
    data = None
    while start_month <= end_month:
        csv_filename = '%d%02d%s' % (year, start_month, '-citibike-tripdata.csv')
        month_data = read_data_one_mouth('data/' + csv_filename)
        if data is None:
            data = month_data
        else:
            data = data.append(month_data, ignore_index=False)
        start_month += 1
    return data
