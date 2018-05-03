# -*- coding: utf-8 -*-
"""
Created on 2018/5/3 

@author: susmote
"""

import tensorflow as tf


model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu", input_shape=(4, )),
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(3)
])
