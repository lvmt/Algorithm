#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/24 20:39
# @File 字母异位词分组.py


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in range(len(strs)):
            # print(set(strs[i]))
            k = '-'.join(sorted(list(strs[i])))
            if k in d:
                d[k].append(strs[i])
            else:
                d[k] = [strs[i]]

        return [l for l in d.values()]


strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(Solution().groupAnagrams(strs))

# 执行效率超过91%, 万万没想到.

"""
骚气操作:
1.在美版leetcode上看到大神的思路，用质数表示26个字母，把字符串的各个字母相乘，这样可保证字母异位词的乘积必定是相等的。其余步骤就是用map存储，和别人的一致了。（这个用质数表示真的很骚啊！！!）


"""

