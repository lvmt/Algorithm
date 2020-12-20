#!/usr/bin/python
# -*- coding:utf-8 -*-

#@Author: lvmengting
#@Date: 2020-12-13 17:40:37
#@Last Modified by:   lvmengting
#@Last Modified time: 2020-12-13 17:40:37
 
class Solution:
    
    def removeDuplicates(self, nums):
        '''
        nums: List[int]
        rtype: int
        双指针, 原地修改数组, 时间复杂度O(n), 空间复杂度O(1)
        '''
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        print(nums[:i+1])
        return  nums[:i+1]
Solution().removeDuplicates([1,1,2])
Solution().removeDuplicates([1,2,3,3,4,4,5,9,9,11])