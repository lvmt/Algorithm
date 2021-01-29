class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0 
        r = len(nums) - 1

        # # 没有旋转：
        # if nums[r] >= nums[0]:
        #     return nums[0]

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]: # 左边有序
                l = mid + 1
            else: # 右边有序
                r = mid 
        return nums[l]

#print(Solution().findMin([4,5,6,7,0,1,2]))



            