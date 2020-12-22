#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/22 21:18
# @File 两数之和.py



class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            tmp = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == tmp:
                    return [i, j]


print(Solution().twoSum([3, 2, 4, 15], 6))
