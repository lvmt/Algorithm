#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/22 21:26
# @File 三数之和.py


"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，
使得a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
"""


class Solution:
    def threeSum(self, nums):
        nums.sort()

        if len(nums) < 3:
            return []

        n = len(nums)
        result = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue  # 去重, 没有理解, 妙
            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.append(nums[i], nums[l], nums[r])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1  # 为了去重, 妙
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r += 1
                elif sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
        return result
