#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Quick Introduction to pandas

import math

from IPython import display
from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset

log = tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv("./resources/california_housing_train.csv")

# randomize the data
california_housing_dataframe = california_housing_dataframe.reindex(
    np.random.permutation(california_housing_dataframe.index))
california_housing_dataframe["median_house_value"] /= 1000.0
print(california_housing_dataframe)


# define input feature: total_rooms
my_features = california_housing_dataframe[["total_rooms"]]

# configure a numeric feature column for total_rooms
feature_colums = [tf.feature_column.numeric_column("total_rooms")]

# define the label
targets = california_housing_dataframe["median_house_value"]

# use gradient descent as the optimizer for training the model
my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0000001)
my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
