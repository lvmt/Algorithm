#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/25 11:56
# @Email  13554221497@163.com
# @File   分发饼干.py


"""
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j]。
如果 s[j]>= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int] # 胃口
        :type s: List[int] # 饼干
        :rtype: int
        先排序，在贪心算法
        """

        g.sort()
        s.sort()

        result = 0
        # 双指针

        start = 0
        for i in range(len(g)):
            for j in range(start, len(s)):  # start代表从哪里开始找饼干
                if s[j] >= g[i]:
                    start += 1
                    result += 1
                    break
                else:  # 饼干不满足胃口
                    start += 1
        return result


print(Solution().findContentChildren([1, 3, 5], [2, 2, 4]))



class Solution2:
    def findContentChildren(self, g, s):
        g.sort()  # 胃口
        s.sort()  # 饼干

        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:  # 不满足胃口
                j += 1
            if j < m:
                count += 1
            i += 1  # 下一个胃口
            j += 1  # 下一个饼干

        return count


print(Solution2().findContentChildren([1, 3, 5], [2, 2, 4]))



class Solution3:  # 执行效率超过96%
    def findContentChildren(self, g, s):
        """
        遍历胃口列表,如果当前饼干无法满足胃口,则下个孩子,
        如果满足胃口, 下个孩子, 下个饼干
        """
        g.sort()
        s.sort()
        index = 0
        count = 0
        for i in range(len(s)):  # 需要明确到底是遍历谁.
            if index < len(g) and g[index] <= s[i]:  # 满足胃口
                # i += 1
                index += 1
                count += 1
        return count

print(Solution3().findContentChildren([1, 3, 5], [2, 2, 4]))


