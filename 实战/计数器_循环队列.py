#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/30 21:41
# @File 计数器_循环队列.py


"""
利用计数器，实现循环队列
"""


class CountCircleQueue:
    def __init__(self, k):
        self.q = [0 for _ in range(k)]
        self.maxsize = k
        self.head = 0
        self.count = 0  # 队列中的元素

    def enqueue(self, value):
        if self.is_full():
            raise IndexError('queue is full')
        self.q[(self.head + self.count) % self.maxsize] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        data = self.q[self.head]
        self.q[self.head] = 0  # 并将删除的位置重置为0
        self.head = (self.head + 1) % self.maxsize  # 删除元素之后, head的位置需要右移一位
        self.count -= 1
        return data

    def is_full(self):
        if self.count == self.maxsize:
            return True
        return False

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def show(self):
        for i in range(self.maxsize):
            print(self.q[i], end=',')
        print()

    def show_head(self):
        return self.q[self.head]

    def show_tail(self):
        return self.q[(self.head + self.count - 1) % self.maxsize]

q = CountCircleQueue(8)
q.show()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.show()
print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.dequeue())  # 3

q.show()

print(q.show_head())  # 4
print(q.show_tail())  # 8
