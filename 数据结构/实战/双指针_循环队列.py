#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/30 21:02
# @File 双指针_循环队列.py


"""
为了避免队空和队满的判断条件，
设计中浪费了一个空间.
"""


class MyCircleQueue:

    def __init__(self, k):
        self.queue = [0 for _ in range(k)]
        self.head = 0
        self.tail = 0
        self.maxsize = k

    def enQueue(self, value):
        if self.is_full():
            return False
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.maxsize
        return True

    def deQueue(self):
        if self.is_empty():
            return False
        else:
            data = self.queue[self.head]
            self.queue[self.head] = 0
            self.head = (self.head + 1) % self.maxsize
        return True

    def is_empty(self):
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        if (self.tail + 1) % self.maxsize == self.head:
            return True
        return False

    def show(self):
        for i in range(self.maxsize):
            print(self.queue[i], sep=',')

    def show_tail(self):
        """打印队尾元素"""
        return self.queue[self.tail - 1]  # 双指针的时候,队尾的索引指向下一个待插入的元素

    def show_head(self):
        return self.queue[self.head]


d = MyCircleQueue(8)
d.show()
d.enQueue(1)
d.enQueue(2)
d.enQueue(3)
d.enQueue(4)
d.enQueue(5)
d.enQueue(6)
d.enQueue(7)
d.enQueue(8)
d.enQueue(9)
d.show()
print(d.show_tail())  # 7
print(d.show_head())  # 1
