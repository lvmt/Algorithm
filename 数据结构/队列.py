#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/21 17:30
# @Email  13554221497@163.com
# @File   队列.py


"""
队列是一种有次序的数据集合，其特征为：“先进先出”
（1）新数据的添加总是从尾端发生(rear端）
（2）新数据的移除总是在首端发生(front端）

生活中应用案例：
（1）一台打印机面向多个用户/程序提供服务
（2）操作系统核心采用多个队列对系统中同时运行的进程进行调度，原则为“先到先服务”，“资源充分利用”
（3）键盘缓冲，键盘敲击打字并不是马上显示在屏幕上，
"""


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # 队尾进

    def pop(self):
        return self.items.pop(0)  # 队首删除

    def is_empty(self):
        return self.items == 0

    def clear(self):  # 清空队列
        del self.items

    def size(self):
        return len(self.items)

    def print(self):  # 打印队列
        print(self.items)



class Queue2:
    def __init__(self):
        self.q = []
        self.max = 8

    def enqueue(self, value):
        # 解决栈上溢
        if self.size() == 8:
            raise IndexError('超过栈的指定长度')
        self.q.append(value)

    def dequeue(self):
        if self.size() == 0:
            raise IndexError('栈为空, 无法删除元素')
        return self.q.pop()

    def size(self):
        return len(self.q)


q = Queue2()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
# q.enqueue(9)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(q.dequeue())


#
# q = Queue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.print()
#
# q.pop()
# q.print()