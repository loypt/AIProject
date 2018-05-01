# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:10:02 2018

@author: susmote
"""

import numpy as np


def sig(x):
    """
    Sigmoid函数
    :param x: feature * w
    :return: Sigmoid值
    """
    return 1.0 / (1 + np.exp(-x))