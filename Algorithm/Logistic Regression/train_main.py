# -*- coding: utf-8 -*-
"""
Created on 2018/5/1 

@author: susmote
"""
from load_data import load_data
from train_model import lr_train_bgd
from save_model import save_model


if __name__ == "__main__":
    # 导入数据
    print("load data".center(30, '-'))
    feature, label = load_data("data.txt")
    # 训练LR模型
    print("training".center(30, '-'))
    w = lr_train_bgd(feature, label, 1000, 0.01)
    # 保存模型
    print("save model".center(30, '-'))
    save_model("weights", w)