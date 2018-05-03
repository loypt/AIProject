# -*- coding: utf-8 -*-
"""
Created on 2018/5/3 

@author: susmote
"""

import tensorflow as tf
import tensorflow.contrib.eager as tfe


def loss(model, x, y):
    y_ = model(x)
    return tf.losses.sparse_softmax_cross_entropy(labels=y, logits=y_)

def grad(model, inputs, targets):
    with tfe.GradientTape() as tape:
        loss_value = loss(model, inputs, targets)
    return tape.gradient(loss_value, model.variables)