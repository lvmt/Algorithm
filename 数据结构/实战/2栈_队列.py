#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/2 19:02
# @File 2栈_队列.py


"""
使用2个栈,实现队列的操作.
"""


class Stack:

    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)

    def pop(self):
        data = self.s.pop()
        return data

    def is_empty(self):
        return not self.s

    def show(self):
        for i in self.s:
            print(i)


# s = Stack()
# s.push(12)
# s.push(8)
# print('---', s.pop())
# print(s.s)

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):  # 进队
        self.s1.push(value)

    def dequene(self):  # 队列, 先进先出,
        if self.s2.s:  #s2中存在元素
            data = self.s2.pop()
            return data
        else:
            while self.s1.s:
                self.s2.push(self.s1.pop())  # 把s1中的元素,压入到s2中
            data = self.s2.pop()
            return data

    def is_empty(self):
        if self.s1.is_empty() and self.s2.is_empty():
            return True
        return False

    def show(self):
        for i in self.s1.s:
            print(i)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.s1.s)
print(q.dequene())
print(q.dequene())
q.enqueue(5)
q.enqueue(6)
print('栈1', q.s1.s)
print('栈2', q.s2.s)
print(q.dequene())
