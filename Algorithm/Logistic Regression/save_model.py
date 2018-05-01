# -*- coding: utf-8 -*-
"""
Created on 2018/5/1 

@author: susmote
"""

import numpy as np


def save_model(file_name, w):
    """
    保存最终的模型
    :param file_name: 模型保存的文件名
    :param w: LR模型的权重
    :return: NONE
    """
    m = np.shape(w)[0]
    f_w = open(file_name, "w")
    w_array = []
    for i in range(m):
        w_array.append(str(w[i, 0]))
        f_w.write("\t".join(w_array))
    f_w.close()