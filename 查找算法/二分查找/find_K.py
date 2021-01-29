#!/usr/bin/env python3
#-*- coding:;utf-8 -*-

'''
给定一个排序好的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。
返回的结果必须要是按升序排好的。
'''
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
        
        if x <= arr[0]:
            return arr[0:k]
        
        if x >= arr[-1]:
            return arr[-k:]

        # 二分查找, 先找到x的左右边界
        left = 0
        right = len(arr) 

        while left < right:
            mid = (left+right) // 2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                right = mid  
            else:
                left = mid + 1
        
        if abs(arr[mid]-x) <= abs(arr[mid+1]-x):  # 最接近x的值索引为left.
            left = mid
            right = left + 1
        else:
            left = mid + 1
            right = left + 1

        print('>> 索引:', left, right,mid)

        from collections import deque
        d = deque()
        
        #while left >= 0 and right < len(arr):
        while right - left - 1 < k:
        
            if left < 0:
                d.append(arr[right])
                right += 1
                continue

            if right >= len(arr):
                d.appendleft(arr[left])
                left -= 1
                continue

            if abs(arr[left]-x) < abs(arr[right]-x):
                print('写入左侧值：', arr[left])
                d.appendleft(arr[left])
                left -= 1
            elif abs(arr[left]-x) > abs(arr[right]-x):
                print('写入右侧值: ', arr[right])
                d.append(arr[right])
                right += 1
            else:
                print('写入左侧值：', arr[left])
                d.appendleft(arr[left])
                left -= 1
                # print('写入右侧值：', arr[right])  # 这个思考下为什么可以删除，只有删除这个才能保证代码运行正确.
                # d.append(arr[right])
                # right += 1
        
            if len(d) >= k:
                left = -1

        print(d)
            
        l = []
        for _ in range(k):
            l.append(d.popleft())
        return l 

#print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))
#print(Solution().findClosestElements([1,1,1,10,10,10], 1, 9))      
#print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))      
#print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4))      
#print(Solution().findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9))      
#print(Solution().findClosestElements([1,2,3,3,6,6,7,7,9,9], 8, 8))      
print(Solution().findClosestElements([1,10,15,25,35,45,50,59], 1, 30))      





            




        

        



    


            




        

        