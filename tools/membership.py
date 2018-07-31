# !/usr/bin/python
# coding: utf-8

import matplotlib.pyplot as plt


def analyze(data):
    # Group the user by the type of membership
    # And calculate the proportion
    membership_group = data.groupby('usertype')['bikeid'].agg(len) / data["bikeid"].count()*100

    # Draw the pie chart
    plt.rc('font', family='Times New Roman', size=15)
    colors = ["#fafccb", "#2e99b0"]
    name = ['Customer', 'Subscriber']
    plt.pie(membership_group,
            labels=name,
            colors=colors,
            explode=(0, 0),
            startangle=43,
            autopct='%1.1f%%')
    plt.title('Distribution of Citibike Membership')
    plt.legend(['Customer', 'Subscriber'], loc='upper left')
    plt.axis('equal')
    plt.show()

