#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/25 16:11
# @Email  13554221497@163.com
# @File   双端队列.py


class TwoSideQueue:
    # 利用列表实现实现双端队列

    def __init__(self):
        self.q = []
        self.max = 100

    def left_enqueue(self, values):
        if self.size() == self.max:
            raise IndexError('队列已满')
        self.q.insert(0, values)

    def right_enqueue(self, values):
        if self.size() == self.max:
            raise IndexError('队列已满')
        self.q.append(values)

    def left_dequeue(self):
        if self.size() == 0:
            raise IndexError('队空')
        return self.q.pop(0)

    def right_dequeue(self):
        if self.size() == 0:
            raise IndexError('队空')
        return self.q.pop()

    def size(self):
        return len(self.q)


q = TwoSideQueue()
q.left_enqueue(1)
q.right_enqueue(2)
q.right_enqueue(3)

print(q.right_dequeue())