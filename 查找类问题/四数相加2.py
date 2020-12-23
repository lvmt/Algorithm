#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/23 21:57
# @File 四数相加2.py


"""
给定四个包含整数的数组列表A , B , C , D ,计算有多少个元组 (i, j, k, l)，
使得A[i] + B[j] + C[k] + D[l] = 0。
默认数组的长度相等
"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)

        for i in A:
            for j in B:
                d[i+j] += 1

        result = 0
        for i in C:
            for j in D:
                result += d[-i-j]

        return result


A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(Solution().fourSumCount(A, B, C, D))
