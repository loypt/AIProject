# -*- coding: utf-8 -*-
"""
Created on 2018/5/3 

@author: susmote
"""

from train_model import grad,loss
import tensorflow as tf
import tensorflow.contrib.eager as tfe
import Tensorflow_dataset
import keras_model

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

train_loss_results = []
train_accuracy_results = []

num_epochs = 201

for epoch in range(num_epochs):
    epoch_loss_avg = tfe.metrics.Mean()
    epoch_accuracy = tfe.metrics.Accuracy()

    for x, y in tfe.Iterator(train_dataset):
        grads = grad(model, x, y)
        optimizer.apply_gradients(zip(grads, model.variables),
                                  global_step=tf.train.get_or_create_global_step())

        epoch_loss_avg(loss(model, x, y))

        epoch_accuracy(tf.argmax(model(x), axis=1, output_type=tf.int32), y)

    train_loss_results.append(epoch_loss_avg.result())
    train_accuracy_results.append(epoch_accuracy.result())

    if epoch % 50 == 0:
        print("时期 : {:03d}； 损失 : {:.3f};  精度 ： {:.3%}".format(epoch, epoch_loss_avg.result(), epoch_accuracy.result()))