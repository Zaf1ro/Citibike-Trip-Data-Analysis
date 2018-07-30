# !/usr/bin/python
# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def analyze(data):
    # 对骑行时间进行分组
    bins = [0, 300, 600, 1200, 1800, 2700, 2825827]

    # 为每个分组命名
    group_tripduration = ['5min', '10min', '20min', '30min', '45min', '更长时间']

    # 在原数据表中增加时间分组字段
    data['group_tripduration'] = pd.cut(data['tripduration'], bins, labels=group_tripduration)

    # 按分组对数据进行汇总计数
    group_minute = data.groupby('group_tripduration')['group_tripduration'].agg(len)

    # 汇总骑行时间分组柱状图
    plt.rc('font', family='Times New Roman', size=15)
    plt.bar([1, 2, 3, 4, 5, 6],
            group_minute,
            color='#9F713F',
            alpha=0.8,
            align='center',
            edgecolor='white')
    plt.xlabel('Time Group')
    plt.ylabel('Ride Frequency')
    plt.title('Distribution of Citibike ride time')
    plt.legend(['Time'], loc='upper right')
    plt.grid(color='#95a5a6',
             linestyle='--',
             linewidth=1,
             axis='y',
             alpha=0.4)
    arr = np.array([1, 2, 3, 4, 5, 6])
    plt.xticks(arr, ('5min', '10min', '20min', '30min', '45min', 'more'))
    plt.show()

