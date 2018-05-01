# -*- coding: utf-8 -*-
"""
Created on 2018/5/1 

@author: susmote
"""

import numpy as np


def error_rate(h, label):
    """
    计算当前的损失函数值
    :param h: 预测值
    :param label:实际值
    :return:错误率
    """
    m = np.shape(h)[0]
    sum_err = 0.0
    for i in range(m):
        if h[i, 0] > 0 and (1 - h[i, 0]) > 0:
            sum_err -= (label[i, 0] * np.log(h[i, 0]) + (1 - label[i, 0] * np.log(1 - h[i, 0])))
        else:
            sum_err -= 0

    return sum_err / m