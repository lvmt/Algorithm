#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/29 11:59
# @File 杨辉三角.py


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        if numRows > 2:
            ans.append([1])
            ans.append([1, 1])
            for i in range(3, numRows + 1):  # 行数
                tmp = []
                tmp.append(1)
                for j in range(len(ans[-1]) - 1):  # 与杨辉三角的上一个元素相关
                    t = ans[-1][j] + ans[-1][j + 1]
                    tmp.append(t)
                tmp.append(1)
                ans.append(tmp)

        return ans


print(Solution().generate(5))
