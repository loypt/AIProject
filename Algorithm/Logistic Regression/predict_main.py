# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:25:02 2018

@author: susmote
"""
import numpy as np
from load_weight import load_weight
from predict_load_data import load_data
from predict_func import predict
from save_result import save_result

if __name__ == "__main__":
    # 导入模型
    print("1.load model".center(30, "-"))
    w = load_weight("weights")
    n = np.shape(w)[1]
    # 导入测试数据
    print("2.load data".center(30, "-"))
    testData = load_data("test_data", n)
    # 对测试数据进行预测
    print("3.get prediction".center(30, "-"))
    h = predict(testData, w)
    # 保存最终的预测结果
    print("4.save prediction".center(30, "-"))
    save_result("result", h)    