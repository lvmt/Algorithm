#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/25 11:36
# @Email  13554221497@163.com
# @File   约瑟夫问题.py, 利用队列实现.

"""
利用队列解决约瑟夫问题
"""


from 队列 import Queue


class Solution:

    def circle(self, k, nums):
        """
        k: which num to remove.
        nums: all numbers
        """
        remove = []
        q = Queue()  # 初始化一个空队列
        for item in nums:
            q.push(item)  # 入队

        i = 1
        while q.size() != 1:
            tmp = q.pop()
            if i != k:
                q.push(tmp)
            else:
                remove.append(tmp)
                i = 0
            i += 1
        print(remove)
        return q.pop()


nums = list(range(1, 8))
print(Solution().circle(3, nums))