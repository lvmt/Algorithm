#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/14 20:38
# @File lcs_length.py.py


def lcs_length(x, y):
    m = len(x)   # 行
    n = len(y)   # 列

    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):   # 先遍历列
            if x[i-1] == y[j-1]:  # 如果末尾的数字相等. 理解为什么减去1.
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


print(lcs_length("ABC", "ABCDE"))



