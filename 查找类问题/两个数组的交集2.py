#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/20 20:29
# @File 两个数组的交集2.py

"""
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
"""


from collections import Counter

def intersect(nums1, nums2):
    d1 = Counter(nums1)
    d2 = Counter(nums2)

    if len(d1) > len(d2):
        d1, d2 = d2, d1

    result = []
    for key in d1:
        if d2.get(key):
            if d2[key] > d1[key]: # 数值
                result.extend([key for x in range(d1[key])])
            else:
                result.extend([key for x in range(d1[key])])

    print(result)


intersect([1, 2, 2, 2, 3, 4, 5], [2, 2, 3, 4, 6])