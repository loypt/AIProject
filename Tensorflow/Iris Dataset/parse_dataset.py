# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:06:31 2018

@author: susmote
"""

from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

def parse_csv(line):
    example_defaults = [[0.], [0.], [0.], [0.], [0]] # 设置字段的类型
    parsed_line = tf.decode_csv(line, example_defaults) 
    feature = tf.reshape(parsed_line[:-1], shape=(4,)) # 前四个字段为特征，合并为一个张量
    label = tf.reshape(parsed_line[-1], shape=())   # 最后一个字段是标签
    return feature, label