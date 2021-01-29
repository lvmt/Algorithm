#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/27 3:58
# @File 反转字符串.py


def reverse_string(s):
    i, j = 0, len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return s


print(reverse_string(['a', 'b', 'c', 'd']))
