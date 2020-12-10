#!/usr/bin/env python3
#-*- coding:;utf-8 -*-

'''
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。
返回的结果必须要是按升序排好的。
'''


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i, j = 0, len(arr)-k
        while i < j:
            mid = (i + j) // 2
            if x - arr[mid] > arr[mid+k] - x: 
                i = mid + 1
            else: 
                j = mid
        return arr[i:i+k]

print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))
print(Solution().findClosestElements([1,1,1,10,10,10], 1, 9))      
print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))      
print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4))      
print(Solution().findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9))      
print(Solution().findClosestElements([1,2,3,3,6,6,7,7,9,9], 8, 8))      
print(Solution().findClosestElements([1,10,15,25,35,45,50,59], 1, 30))      





            




        

        



    


            




        

        