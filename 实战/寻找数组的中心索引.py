#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/3 16:23
# @File 寻找数组的中心索引.py


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            if sum(nums[0: i]) == sum(nums[i + 1:]):
                return i
        return -1


class Solution2:
    def pivotIndex(self, nums):
        """参考别人的代码,牛逼plus"""
        SUM = sum(nums)
        LEFTSUM = 0

        for index,value in enumerate(nums):
            if 2 * LEFTSUM == SUM - value:
                return index
            LEFTSUM += value
        return -1



print(Solution2().pivotIndex([1, 7, 3, 6, 5, 6]))
