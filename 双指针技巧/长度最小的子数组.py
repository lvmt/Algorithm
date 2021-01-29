#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/29 10:19
# @File 长度最小的子数组.py


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        时间复杂度：O(n^2)
        """
        max_num = len(nums)
        if sum(nums) < s:
            return 0

        for i in range(len(nums)):
            if nums[i] >= s:
                return 1
            else:
                for j in range(i+1, len(nums)):
                    if sum(nums[i:j+1]) < s:
                        j += 1
                    else:
                        max_num = min(max_num, j - i + 1)
                        break

        return max_num



class Solution2(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        双指针
        """
        if not nums or sum(nums) < s:
            return 0

        n = len(nums)
        ans = n + 1
        start = 0
        end = 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return ans


print(Solution2().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))


