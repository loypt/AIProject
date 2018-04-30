# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 08:27:18 2018

@author: susmote
"""

from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

train_dataset_url = "http://download.tensorflow.org/data/iris_training.csv"
train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url), origin=train_dataset_url)

print("文件保存路径：{}".format(train_dataset_fp))