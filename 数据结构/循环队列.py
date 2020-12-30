#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/29 17:43
# @Email  13554221497@163.com
# @File   循环队列.py


class CircleQueue:
    def __init__(self, maxsize):
        self.q = [None for _ in range(maxsize)]
        self.maxsize = maxsize
        self.head = 0
        self.tail = 0

    def lenght(self):
        """
        返回队列的长度
        """
        return (self.tail - self.head + self.maxsize) % self.maxsize

    def enqueue(self, value):
        """
        先判断队列是否满,
        队列满的情况, tail的位置在head的左边一个位置
        转换为数学公式: (self.tail + 1) % self.maxsize == self.head
        注意：self.tail是即将插入元素的位置,此次的self.tail上面是没有元素的.
        有一个闲置的格子：
        """
        if (self.tail + 1) % self.maxsize == self.head:
            raise IndexError('队列已经满了')
        else:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.maxsize

    def dequeue(self):
        """
        删除元素,队列的属性, 从队首删除元素,
        判断对空, self.head == self.tail
        """
        if self.head == self.tail:
            raise IndexError('队列是空的.')
        else:
            data = self.q[self.head]
            self.q[self.head] = None
            self.head = (self.head + 1) % self.maxsize
            return data

    def show_item(self):
        for i in range(self.maxsize):
            print(self.q[i])



q = CircleQueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
q.enqueue(11)
q.show_item()
