# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:53:12 2018

@author: susmote
"""
import numpy as np

def save_result(file_name, result):
    """
    保存最终的预测结果
    input: file_name(string):预测结果保存的文件名
        result(mat):预测的结果
    """
    m = np.shape(result)[0]
    tmp = []
    for i in range(m):
        tmp.append(str(h[i, 0]))
        f_result = open(file_name, "w")
        f_result.write("\t".join(tmp))
        f_result.close()