# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:32:42 2018

@author: susmote
"""
import numpy as np


def load_weight(w):
    """
    导入LR模型
    input : w(string) 权重所在的文件位置
    output:np.mat(w)(mat) 权重的矩阵
    """
    f = open(w, 'r')
    w = []
    for line in f.readlines():
        lines = line.strip().split("\t")
        w_tmp = []
        for x in lines:
            print(x)
            w_tmp.append(float(x))
        w.append(w_tmp)
        f.close()
        return np.mat(w)