#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/25 16:13
# @Email  13554221497@163.com
# @File   优先队列.py


import heapq
from queue import PriorityQueue as PQ


class SmallestQueue:

    def __init__(self):
        self.q = []

    def enqueue(self, value):
        heapq.heappush(self.q, value)

    def dequeue(self):
        """默认删除最小元素"""
        return heapq.heappop(self.q)

    def show(self):
        print(self.q)


# q = SmallestQueue()
# q.enqueue(4)
# q.enqueue(2)
# q.enqueue(5)
# q.show()  # 2, 4, 5


class PriorityQ:
    def __init__(self):
        self.q = PQ()

    def enqueue(self, value):
        self.q.put(value)

    def dequeue(self):
        return self.q.get()

    def show(self):
        print(self.q.queue)

    def size(self):
        return len(self.q.queue)


q = PriorityQ()
q.enqueue(5)
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
q.show()  # 1,2,3,5
print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.size())

