# !/usr/bin/python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analyze(data):
    # set date format
    data['starttime'] = pd.to_datetime(data['starttime'])

    # filter month from datetime
    data['starttime'] = data['starttime'].dt.strftime('%m')

    # set starttime as dataframe index
    data = data.set_index('starttime')

    # Count the ride time by month
    data_month = data.groupby('starttime').size()

    # Draw a line chart
    plt.rc('font', family='Times New Roman', size=15)
    plt.plot(data_month, 'g8', data_month, 'g-',
             color='#39A2E1', linewidth=3, markeredgewidth=3,
             markeredgecolor='#39A2E1', alpha=0.8)
    plt.xlabel('Month')
    plt.ylabel('Ride time')
    plt.title('2015 Citibike ride time per month')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    month_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.xticks(month_array,
               ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    plt.show()
