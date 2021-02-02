#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/15 22:09
# @File 最长公共前缀.py


"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_num = min(map(len, strs))  # 最短字符的长度
        while min_num >= 0:
            ll = []
            tmp = strs[0][0:min_num]  # 第一个元素
            for i in strs[1:]:
                if i[0:min_num] == tmp:  # 遍历列表中的元素
                    ll.append(True)
                else:
                    ll.append(False)

            if all(ll):
                return tmp[0:min_num]

            min_num -= 1

        return ""


print(Solution().longestCommonPrefix(['flowers', 'filters', 'fnmae']))