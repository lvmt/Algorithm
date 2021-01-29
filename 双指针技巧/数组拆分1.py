#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/27 4:27
# @File 数组拆分1.py


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        return sum([x for index,x in enumerate(nums) if index % 2 == 0])


print(Solution().arrayPairSum([5, 3, 2, 1, 9, 8, 0, 7]))