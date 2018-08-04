# !/usr/bin/python
# coding: utf-8

from math import radians, cos, sin, asin, sqrt
import numpy as np


# 通过经纬度计算距离的函数
def haversine(lon1, lat1, lon2, lat2):  # longitude, latitude
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1 = map(radians, np.array(lon1))
    lat1 = map(radians, np.array(lat1))
    lon2 = map(radians, np.array(lon2))
    lat2 = map(radians, np.array(lat2))
    lon1 = np.array(list(lon1)).reshape(-1, 1)
    lon2 = np.array(list(lon2)).reshape(-1, 1)
    lat1 = np.array(list(lat1)).reshape(-1, 1)
    lat2 = np.array(list(lat2)).reshape(-1, 1)
    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000


def analyze(data):
    # 计算每次骑行的米数并增加骑行距离字段
    data["meter"] = haversine(data["start station longitude"],
                             data["start station latitude"],
                             data["end station longitude"],
                             data["end station latitude"])

    # 将原数据表中的骑行时间由秒转化为小时
    data["duration_hour"] = data["tripduration"] / 3600

    # 将米转化为公里并与小时计算出速度
    data["speed"] = data["meter"] / 1000 / data["duration_hour"]

    # 将每次骑行的秒数求和并转化为小时
    hour = data["tripduration"].sum()/3600

    # 计算平均速度
    km = data["meter"].sum() / 1000
    return km / hour
    # 平均速度为6.31公里/小时
