# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:47:01 2018

@author: susmote
"""
import numpy as np
from sigmoid_func import sig

def predict(data, w):
    """
    对测试数据进行预测
    input: data(mat) 测试数据的特征
        w(mat) 模型的参数
    output: h(mat) 最终的预测结果
    """
    h = sig(data * w.T)
    m = np.shape(h)[0]
    for i in range(m):
        if h[i, 0] < 0.5:
            h[i, 0] = 0.0
        else:
            h[i, 0] = 1.0
    return h
