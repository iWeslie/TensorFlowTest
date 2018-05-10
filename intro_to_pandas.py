#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Quick Introduction to pandas

import pandas as pd
import os
import numpy as np

# pandas __version__
print("pandas version == " + pd.__version__)

# define two panda series
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

# init a panda data DataFrame from dict
data = pd.DataFrame({ 'City name': city_names, 'Population': population })

# load an entire file into a DataFrame from url
# california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

# get the csv file from repo
# /Users/Weslie/Documents/TensorFlowTest/resources/california_housing_train.csv
california_housing_dataframe = pd.read_csv("./resources/california_housing_train.csv")

# the describe of the DataFrame
print("the describe of the DataFrame: ")
print(california_housing_dataframe.describe())

# displays the first few records of a DataFrame:
print("displays the first few records of a DataFrame:")
print(california_housing_dataframe.hist('housing_median_age'))

# access DataFrame data using Python dict/list operations
cities = pd.DataFrame({'City name': city_names, 'Population': population})
print("---> type of DataFrame is: %s" %type(cities))
print("---> type of cities['City name'] is: \n %s" %cities['City name'])
print("---> type of cities['City name'][1] is: %s" %cities['City name'][1])
print("---> type of cities[0:2] is: %s" %type(cities[0:2]))

print("---> population numpy log is: \n %s" %np.log(population))

# the example below creates a new Series that indicates whether population is over one million
population.apply(lambda val: val > 1000000)

# adds two Series to an existing DataFrame:
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)

"""
Modify the cities table by adding a new boolean column that is True if and only if both of the following are True:
- The city is named after a saint.
- The city has an area greater than 50 square miles.
"""
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities['Is wide and has saint name'])

print("----> city_names index: \n %s" %city_names.index)
cities.reindex([2, 0, 1])
print(cities)
