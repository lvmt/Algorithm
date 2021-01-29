#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/29 13:10
# @File 移动零.py


"""
题目描述:
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        此种方法遍历的2词
        """
        slow = 0
        fast = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow, len(nums)):
            nums[i] = 0


class Solution2(object):
    def moveZeroes(self, nums):
        """中间只涉及到一次遍历
        利用了python数据交换的特性"""
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


nums = [0, 1, 0, 3, 12]
Solution2().moveZeroes(nums)
print(nums)