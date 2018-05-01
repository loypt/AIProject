# -*- coding: utf-8 -*-
"""
Created on 2018/5/1 

@author: susmote
"""
import numpy as np


def load_data(file_name):
    """
    导入训练数据
    :param file_name: 训练数据的位置
    :return: feature_data（mat) 特征
            label_data(mat)标签
    """
    f = open(file_name, "r")
    feature_data = []
    label_data = []
    for line in f.readlines():
        feature_tmp = []
        label_tmp  = []
        lines = line.strip().split("\t")
        feature_tmp.append(1)
        for i in range(len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        label_tmp.append(float(lines[-1]))
        feature_data.append(feature_tmp)
        label_data.append(label_tmp)
    f.close()
    return np.mat(feature_data), np.mat(label_data)