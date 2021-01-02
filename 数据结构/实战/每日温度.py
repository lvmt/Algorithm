#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/2 15:57
# @File 每日温度.py


"""
letcode：
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用0 来代替。

例如，给定一个列表temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是[1, 1, 4, 2, 1, 1, 0, 0
"""


class Stack:

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('空栈.')
        data = self.s.pop()
        return data

    def peek(self):
        return self.s[-1]

    def is_empty(self):
        return not self.s

    def len(self):
        return len(self.s)


class Solution2:
    def dailyTemperatures(self, T, List):
        """
        T: 温度列表
        List: 日期间隔.
        """

        for index in range(len(T) - 1):  # 最后一个元素不遍历
            day = 0
            if T[index] < T[index + 1]:
                List.append(day + 1)
            else:
                s = Stack()
                tmp = index
                while T[tmp] >= T[index+1] and index < len(T) - 2:
                    s.push(T[index+1])
                    index += 1
                s.push(T[index+1])
                if s.peek() > T[tmp]:
                    List.append(s.len())
                else:
                    List.append(0)

        List.append(0)
        return List


class Solution:
    def dailyTemperatures(self, T):
        """
        T: 温度列表
        List: 日期间隔.
        """
        List = []
        for index in range(len(T) - 1):  # 最后一个元素不遍历
            day = 0
            if T[index] < T[index + 1]:
                List.append(day + 1)
            else:
                tmpl = []
                tmp = index
                while T[tmp] >= T[index+1] and index < len(T) - 2:
                    tmpl.append(T[index+1])
                    index += 1
                tmpl.append(T[index+1])
                if tmpl[-1] > T[tmp]:
                    List.append(len(tmpl))
                else:
                    List.append(0)
                tmpl.clear()

        List.append(0)
        return List


class Solution3:
    def dailyTemperatures(self, T):
        """
        使用单调栈方法
        """
        stack = []  # 如果栈中有元素: 如果下一个元素小于栈顶元素,加入栈; 否则时间为1.
        ans = [0 for _ in range(T)]

        for i in range(len(T)):
            tmp = T[i]  # 当前的温度
            while stack and tmp > T[stack[-1]]:  # 栈中存储的是温度的索引.
                previous_index = stack.pop()
                ans[previous_index] = i - previous_index  # 索引只差
            stack.append(i)

        return ans






print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))