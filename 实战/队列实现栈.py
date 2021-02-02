#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/2 19:43
# @File 队列实现栈.py


"""
利用队列, 实现栈
队列: FIFO
栈: LIFO
"""


class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        data = self.q.pop(0)
        return data

    def is_empty(self):
        return not self.q


class Stack:
    def __init__(self):
        self.q1 = Queue()   # 入栈.全部元素存储在q1中
        self.q2 = Queue()   #  中间过渡队列.

    def push(self, value):
        while self.q1.q:
            self.q2.enqueue(self.q1.dequeue())
        self.q1.enqueue(value)
        while self.q2.q:
            self.q1.enqueue(self.q2.dequeue())

    def pop(self):
        data = self.q1.dequeue()
        return data

    def is_empty(self):
        return self.q1.is_empty()

    def peek(self):
        data = self.q1.dequeue()
        self.q2.enqueue(data)
        while self.q1.q:
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, Queue()
        return data




ss = Stack()
ss.push(1)
ss.push(2)
ss.push(3)
print(ss.q1.q)
print('弹出栈顶', ss.pop())
ss.push(4)
ss.push(5)
print(ss.q1.q)
print('栈顶', ss.peek())
print(ss.q1.q)