# -*- coding: utf-8 -*-
"""
Created on 2018/5/1 

@author: susmote
"""

import numpy as np
from sigmoid_func import sig
from error_rate import error_rate


def lr_train_bgd(feature, label, maxCycle, alpha):
    """
    梯度下降法训练LR模型
    :param feature: 特征
    :param label: 标签
    :param maxCycle: 最大迭代次数
    :param alpha: 学习率
    :return: w(mat) 权重
    """
    n = np.shape(feature)[1]
    w = np.mat(np.ones((n, 1)))
    i = 0
    while i <= maxCycle:
        i += 1
        h = sig(feature * w)
        err = label - h
        if i % 100 == 0:
            print("\t-------iter=" + str(i) + ", train error rate = " + str(error_rate(h, label)))
        w = w + alpha * feature.T * err
    return w
