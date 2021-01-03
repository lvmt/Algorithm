#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/3 18:06
# @File 合并区间.py


""""
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda item: item[0])
        start = intervals[0][0]
        end = intervals[0][1]
        ans = []

        for s, e in intervals[1:]:  # 遍历, 更新
            # print(s, e)
            if end > s:  # 有交集
                end = max(end, e)
            else:
                ans.append([start, end])
                start = s
                end = e
        ans.append([start, end])
        return ans


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
