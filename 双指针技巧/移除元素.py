#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/29 9:44
# @File 移除元素.py


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        length = len(nums)

        for fast in range(length):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow


print(Solution().removeElement([1, 2, 2, 3], 2))