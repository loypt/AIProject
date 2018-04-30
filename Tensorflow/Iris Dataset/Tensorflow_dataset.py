# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:22:23 2018

@author: susmote
"""

from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

from parse_dataset import parse_csv

train_dataset = tf.data.TextLineDataset('iris_training.csv')
train_dataset = train_dataset.skip(1)   # 跳过第一行的数据信息
train_dataset = train_dataset.map(parse_csv)    # 解析每一行
train_dataset = train_dataset.shuffle(buffer_size=1000)     # 打乱数据排列
train_dataset = train_dataset.batch(32)     # 每32行数据为一次训练

# 查看一个示例数据
features, label = tfe.Iterator(train_dataset).next()
print("示例特征 ：", features[0])
print("示例标签 ：", label[0])