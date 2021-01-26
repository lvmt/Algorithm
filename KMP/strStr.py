#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/27 3:09
# @File strStr.py


"""
求救模式字符串在目标字符串位置
"""


class Solution:
    def strStr(self, haystack, needle):
        """滑动窗口"""
        length = len(needle)

        for i in range(len(haystack)):
            if haystack[i:i+length] == needle:
                return '开始位置', i


print(Solution().strStr('aabaabaaf', 'aaf'))

