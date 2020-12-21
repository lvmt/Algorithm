#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/21 14:04
# @Email  13554221497@163.com
# @File   气球问题.py


"""
用最少数量的箭引爆气球
"""


def min_ballon(array):
    new_array = sorted(array, key=lambda item: item[0])

    if not array:
        return 0

    numbers = 1

    min_right = new_array[0][1]  # 最小右边界
    for i in range(1, len(new_array)):
        if new_array[i][0] > min_right:
            numbers += 1
            min_right = new_array[i][1]
        else:
            min_right = min(min_right, new_array[i][1])  # 更新最小右边界

    print(new_array)
    print(numbers)

min_ballon([[1, 4], [2, 5], [4, 6], [5, 7]])