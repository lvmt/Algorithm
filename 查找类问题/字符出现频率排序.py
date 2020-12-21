#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/21 22:24
# @File 字符出现频率排序.py


from collections import Counter


def frequency_sort(s):
    result = ''
    d = Counter(s)
    values = sorted(d, key=lambda v: d[v], reverse=True)

    for v in values:
        result += v * d[v]

    return result


print(frequency_sort('aabbbccccc'))
