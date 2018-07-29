# !/usr/bin/python
# coding: utf-8

import matplotlib.pyplot as plt


def analyze(data):
    # Group user by gender and calculate the proportion
    user_gender = data.groupby('gender')['bikeid'].agg(len) / data["bikeid"].count()*100

    # Draw a pie chart
    plt.rc('font', family='Times New Roman', size=15)
    colors = ["#FFC300", "#4CAF50", "#448AFF"]
    # name = ['Unspecified', 'Male', 'Female']
    plt.pie(user_gender, colors=colors, explode=(0, 0, 0),
            startangle=60, autopct='%1.1f%%')
    plt.title('Distribution of Citibike user gender')
    plt.legend(['Unspecified', 'Male', 'Female'], loc='upper left')
    plt.axis('equal')
    plt.show()
