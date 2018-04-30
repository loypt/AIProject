# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 08:08:40 2018

@author: susmote
"""
from __future__ import absolute_import, division, print_function

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow.contrib.eager as tfe

tf.enable_eager_execution()

print("Tensorflow version : {}".format(tf.VERSION))
print("Eager execution : {}".format(tf.executing_eagerly()))
