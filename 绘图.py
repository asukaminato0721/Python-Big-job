"""
Copyright (c)2020
All rights reserved.
文件名称：绘图.py
摘    要：简要描述本文件的内容
当前版本：1.0
作    者：wuyudi
完成日期：2020 年 05 月 19 日 星期二
"""
import matplotlib.pyplot as plt
import numpy as np


def query(year):
    x = np.linspace(1, 4, 100)
    y = 3 * np.sin(x)
    plt.plot(x, y)
    plt.show()
