#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/2 14:34
# @File 最小栈.py



class MinStack:

    def __init__(self):
        self.s = []  # 存储2个数字, index0:data, index1:min

    def push(self, x):
        """
        栈不为空, 栈为空
        """
        if not self.s:
            self.s.append((x, x))
        else:
            if self.s[-1][1] > x:   # 更新最小值.
                self.s.append((x, x))
            else:
                self.s.append((x, self.s[-1][1]))

    def pop(self):
        data = self.s[-1][0]
        self.s.pop()
        return data

    def top(self):
        return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]


ss = MinStack()
ss.push(5)
ss.push(4)
ss.push(3)
ss.push(8)
print(ss.s)
print(ss.pop())
print(ss.getMin())
print(ss.top())
