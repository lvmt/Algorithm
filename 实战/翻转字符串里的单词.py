#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/22 21:02
# @File 翻转字符串里的单词.py

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(filter(str, s.split(' ')))
        l.reverse()
        return ' '.join(l)


print(Solution().reverseWords('you bike his'))
