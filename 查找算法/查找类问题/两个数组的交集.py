#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/20 14:39
# @File 两个数组的交集.py


"""
给定两个数组，编写一个函数来计算它们的交集。
"""

def find_intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    if len(set1) < len(set2):
        set1, set2 = set2, set1
    return [x for x in set2 if x in set1]

