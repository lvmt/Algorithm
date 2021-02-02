#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/4 21:01
# @File 零矩阵.py


"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_index = []
        col_index = []
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_index.append(i)
                    col_index.append(j)

        for i in range(r):
            for j in range(c):
                if i in row_index or j in col_index:
                    matrix[i][j] = 0

        return matrix


print(Solution().setZeroes([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]))

