#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/7 21:22
# @File 对角线遍历.py


"""
矩阵大小： (M x N) (行 * 列)

边界条件：
x为行， y为列

x为0： y+=1, 往左下角跑 （y-1, x+1）
y为0: x+=1, 往右上角跑 （y+=1, x-=1）

y为N, x-=1, 往左下角跑, x+=1, y-=1
x为M, y+=1, 往右上角跑, x-=1, y+=1

"""

max_x = 5
max_y = 4


