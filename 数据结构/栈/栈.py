#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/21 14:49
# @Email  13554221497@163.com
# @File   栈.py


"""
特点:
先进后出： LIFO（last in first out）
线性数据结构
添加操作和移除操作总发生在同一侧，即“顶端”
栈具有反转（元素）特性，栈的应用很多，比如浏览器的返回（后退back）按钮，利用了一个栈，存储浏览过的网页的URL，单击按钮式，最新加入栈的URL弹出。
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):  # 查看栈顶元素
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

#
# s = Stack()
# s.push(1)
# s.push(2)
# print(s.size())
# s.pop()
# print(s.peek())

