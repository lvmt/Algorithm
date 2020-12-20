#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/20 16:28
# @File 存在重复元素.py


"""
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。
如果数组中每个元素都不相同，则返回 false 。
"""


def contains_duplicate(nums):
    return not len(nums) == len(set(nums))

