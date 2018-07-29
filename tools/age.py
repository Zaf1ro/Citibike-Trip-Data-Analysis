# !/usr/bin/python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt


def analyze(data):
    # Calculate the age of user
    data['age'] = 2018 - data['birth year']

    # Print the min and max age of user
    print('The youngest user\'s age: ' + str(data['age'].min()))
    print('The oldest user\'s age: ' + str(data['age'].max()))

    # Group users by their age
    bins = [0, 18, 45, 65, 140]
    data['group_age'] = pd.cut(data['age'], bins)

    # Count number of user by age
    user_age = data.groupby('group_age')['group_age'].agg(len)

    # Draw a bar chart of user age
    plt.rc('font', family='Times New Roman', size=15)
    plt.bar([1, 2, 3, 4], user_age, color='#052B6C', alpha=0.8, align='center', edgecolor='white')
    plt.xlabel('Age Group')
    plt.ylabel('Ride Times')
    plt.title('Distribution of Citibike user age')
    plt.legend(['Times'], loc='upper right')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.4)
    plt.xticks([1, 2, 3, 4], ('Young', 'Adult', 'Middle-age', 'Old-Age'))
    plt.show()
