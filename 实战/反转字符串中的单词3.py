#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/29 12:51
# @File 反转字符串中的单词3.py


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = ''
        ans = ''
        for i in s:
            if i.strip():
                tmp += i
            else:
                ans += tmp[::-1]
                ans += ' '
                tmp = ''
        ans += tmp[::-1]
        return ans


print(Solution().reverseWords("Let's take LeetCode contest "))
