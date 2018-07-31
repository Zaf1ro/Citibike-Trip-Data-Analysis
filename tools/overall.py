# !/usr/bin/python
# coding: utf-8


def analyze(data, months):
    overall = dict()

    # Count of bike station
    overall['station_count'] = len(data['start station name'].unique())

    # Count for unique ID of bike
    overall['bike_count'] = len(data['bikeid'].unique())

    # Count for ride times
    overall['count_ride'] = data['starttime'].count()

    # Frequency of rentals for each bike in one year
    overall['freq_rental_year'] = data['bikeid'].count()/len(data['bikeid'].unique())

    # Frequency of rentals for each bike in one day
    overall['freq_rental_day'] = data['bikeid'].count()/len(data['bikeid'].unique())/(30*months)

    # Average rental period(minutes)
    overall['avg_rental_period'] = data['tripduration'].sum()/data['bikeid'].count()/60

    return overall
