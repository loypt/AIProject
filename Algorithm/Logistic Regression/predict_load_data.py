# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:37:29 2018

@author: susmote
"""

import numpy as np


def load_data(file_name, n):
    """
    导入测试数据
    input: file_name(string)测试集的位置
        n(int) 特征的个数
    output: np.mat(feature_data)(mat)测试集的特征
    """
    f = open(file_name, "r")
    feature_data = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        if len(lines) != n - 1:
            continue
        feature_tmp.append(1)
        for x in lines:
            feature_tmp.append(float(x))
        feature_data.append(feature_tmp)
    f.close()
    return np.mat(feature_data)