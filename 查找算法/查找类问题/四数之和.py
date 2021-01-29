#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/23 20:26
# @File 四数之和.py


"""
给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，
使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。

"""


# def four_sum(nums, target):
#     nums.sort()
#     result = []
#
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             l = j + 1
#             r = len(nums) - 1
#
#             while l < r:
#                 if nums[i] + nums[j] + nums[l] + nums[r] == target:
#                     if not [nums[i], nums[j], nums[l], nums[r]] in result:
#                         result.append(nums[i], nums[j], nums[l], nums[r])
#                     l += 1
#                     r -= 1
#                 elif nums[i] + nums[j] + nums[l] + nums[r] < target:
#                     l += 1
#                 elif nums[i] + nums[j] + nums[l] + nums[r] > target:
#                     r -= 1
#     return result
#


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        if not [nums[i], nums[j], nums[l], nums[r]] in result:
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                        # while nums[i] == nums[i+1] and l < r:
                        #     l += 1
                        # while nums[r] == nums[r-1] and l < r:
                        #     r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                j += 1
            i += 1
        return result