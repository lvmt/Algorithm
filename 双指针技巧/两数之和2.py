#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/27 4:53
# @File 两数之和2.py


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        双指针, 二分查找的思想.
        """
        #for i in range(numbers):
        if len(numbers) == 2:
            return (1, 2)

        i = 0
        while i < len(numbers) - 1:
            tmp = target - numbers[i]  # 需要查找的值

            # # 跳过相同的值
            # while numbers[i] == numbers[i+1]:
            #     i += 1

            left = i + 1  # 1
            right = len(numbers) - 1  # 2

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tmp:
                    return i + 1, mid + 1
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
            i += 1




class Solution2:  ## 好好利用有序数组这个条件
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return left + 1, right + 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1


print(Solution2().twoSum([5, 25, 75], 100))



