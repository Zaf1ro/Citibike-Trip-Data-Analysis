# !/usr/bin/python
# coding: utf-8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def analyze(data):
    # 更改star_time字段为日期格式
    data['starttime'] = pd.to_datetime(data['starttime'])
    data['hour'] = data['starttime'].dt.hour

    # 设置star_time为表索引
    data = data.set_index('hour')

    # 按小时对数据进行汇总
    hour_group = data.groupby('hour').size()

    # 绘制24小时折线图
    plt.rc('font', family='Times New Roman', size=15)
    a = np.array([x for x in range(23)])
    plt.plot(hour_group, '8', hour_group, 'g-',
             color='#052B6C', linewidth=3, markeredgewidth=3,
             markeredgecolor='#052B6C', alpha=0.8)
    plt.xlabel('24 Hours')
    plt.ylabel('Ride Times')
    plt.title('Distribution of Citibike ride time per hour')
    plt.grid(color='#95a5a6',
             linestyle='--',
             linewidth=1,
             axis='y',
             alpha=0.4)
    plt.xticks(a, [str(x) for x in range(23)])
    plt.show()
