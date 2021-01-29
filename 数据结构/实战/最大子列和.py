#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/17 21:56
# @File 最大子列和.py.py

ll = [-1, 3, -2, 4, -6, 1, 7, -1]

the_sum = 0
max_sum = 0

for i in range(len(ll)):
    the_sum += ll[i]
    if the_sum > max_sum:
        max_sum = the_sum
    elif the_sum < 0:
        the_sum = 0

print(max_sum)
