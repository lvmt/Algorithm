# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if len(nums) == 1 and nums[0] == target:
#             return 0
#         else:
#             return -1

        # left = 0 
        # right = len(nums) 
        # while left <= right:
        #     mid = (left + right) // 2
        #     #print(mid)
        #     if nums[mid] == target:
        #         return mid 
        #     elif target >= nums[left]:
        #         right = mid - 1 
        #     elif target <= nums[left]:
        #         print('猜测')
        #         ## 确定旋转边界
        #         if left <= nums[mid] :  # 
        #             print('边界在右侧')
        #             # 肯定在右边查找
        #             left = mid + 1
        #         elif left >= nums[mid]:   #  旋转数字在左边.
        #             print('边界在左侧')
        #             if target <= nums[mid]:
        #                 right = mid - 1 
        #             else:
        #                 #target > nums[mid]:
        #                 left = mid + 1 
              

#print(Solution().search([4,5,6,7,0,1,2], 0))



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 1 and nums[0] == target:
            return 0
        # else:
        #     return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:  # 左区间有序, 不要漏掉等号.
                if nums[left] <= target <= nums[mid]:
                    right = mid -1 
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]: # 右区间有序
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1 

print(Solution().search([3,1], 0))