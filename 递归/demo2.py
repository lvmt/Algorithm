#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/2/3 10:11
# @File demo2.py


"""
测试递归的使用
"""


def demo(x):
    if x == 1:
        return 1
    else:
        return demo(x-1) + x



print(demo(6))
