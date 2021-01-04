#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/3 22:07
# @File 旋转矩阵.py


"""
思想：
先交换x,y
然后更新同一行的元素位置信息, y = N - y0  # N为数组的长度,y0为原始的索引.
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        题目要求,原地修改.
        辅助数组法：
        """
        new_mat = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                value = matrix[i][j]
                new_mat[j][len(matrix) - i - 1] = value
        matrix[:] = new_mat
        # return matrix


print(Solution().rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
