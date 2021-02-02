#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/3 17:08
# @File 搜索插入位置.py


"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1  # 包含
        if nums[0] > target:
            return 0

        if nums[-1] < target:
            return len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1


print(Solution().searchInsert([1, 3, 5, 6], 4))
