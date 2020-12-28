#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/25 17:41
# @Email  13554221497@163.com
# @File   直线上最多的点数.py


"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
"""


from collections import defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        """
        按照斜率计算的话, 2种情况需要特殊考虑.
        x1 = x2,
        y1 = y2,
        此时的key为对应的x与y.
        """
        d = defaultdict(list)

        for i in range(len(points) - 1):  # 遍历的趟数
            for j in range(i+1, len(points)):  # 其余的点数

                if points[i][1] == points[j][1]:  # y相等
                    d[points[i][1]].append(points[j])
                elif points[i][0] == points[j][0]:  # x相等
                    d[points[i][0]].append(points[j])
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    print(k)
                    print(points[j], points[i])
                    d[k].append(points[j])
                    d[k].append(points[i])

        return d


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(Solution().maxPoints(points))

