#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/29 9:52
# @File 最大连续1的个数.py



class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
            else:
                if max_length < tmp:
                    max_length = tmp
                tmp = 0
        if max_length < tmp:
            max_length = tmp

        print('最大长度为：', max_length)



Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1])