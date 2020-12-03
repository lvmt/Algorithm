# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def num:


class Solution(object):


    def guessNumber(self, n, num):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        
        
        if num > right:
            print('太大了')
            return 1

        if num < left:
            print('太小了')
            return -1
        
        while left < right:
            mid = (left + right ) // 2
            if mid == num:
                return num
            elif mid > num:
                print('<<x 小')
                right = mid - 1
            else:
                print('>>x 大')
                left = mid + 1


print(Solution().guessNumber(10, 2))