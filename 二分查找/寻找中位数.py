#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''题目描述:
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
# 中位数的计算方式
(m+n+1) // 2
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # target_index = (m+n+1) // 2
        # # 先归并排序数组  
        # largest = m if m > n else n # 求出哪个数组比较长
        new_list = []

        m = 0 
        n = 0

        while m < len(nums1) and n < len(nums2):
            if nums1[m] < nums2[n]:
                new_list.append(nums1[m])
                m += 1
            else:
                new_list.append(nums2[n])
                n += 1
            print(new_list)

Solution().findMedianSortedArrays([1,2,4,5,7], [3,6,9]) 


# 失败啦
