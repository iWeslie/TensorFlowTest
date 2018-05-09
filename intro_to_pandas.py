#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

# Quick Introduction to pandas

import pandas as pd
import os

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
