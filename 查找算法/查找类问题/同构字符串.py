#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/21 20:38
# @File 同构字符串.py


"""
示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false

"""


from copy import deepcopy


class Solution:
    def is_isomorphic(self, s, t):
        """
        egg, add
        {'e': 'a',
         'g': 'd'
        """
        d = {}

        for i in range(len(s)):  # 索引
            if s[i] in d:
                # print(s[i])
                if d[s[i]] == t[i]:
                    pass
                else:
                    return False
            else:
                d[s[i]] = t[i]

        # print(d)
        return len(d.keys()) == len(set(d.values()))


# print(Solution().is_isomorphic('aa', 'ab'))


def is_isomorphic2(s, t):
    d = {}

    for index, char in enumerate(s):
        if char in d:  # key
            if d[char] != t[index]:
                return False
        else:
            # 两个字符不能映射到同一个字符
            if t[index] in d.values():
                return False
            d[char] = t[index]
    return True









