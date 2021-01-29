#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/20 20:49
# @File 字母异位词.py

"""
输入: s = "anagram", t = "nagaram"
输出: true
输入: s = "rat", t = "car"
输出: false
"""


from collections import Counter

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d1 = Counter(s)
    d2 = Counter(t)
    return d1 == d2


print(isAnagram('baby', 'abby'))
print(isAnagram('abay', 'abdy'))