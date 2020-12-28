#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/28 16:42
# @Email  13554221497@163.com
# @File   链表.py


"""
链表是由节点组成的,
常见的链表有单链表, 双链表

链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，
而是在每一个节点里存到下一个节点的指针(Pointer)
"""


class Node:
    """定义单链表节点类"""
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, newdata):
        """
        头部插入
        """
        node = Node(newdata, _next=self.head)
        self.head = node
        # 新节点称为新的头结点

    def append(self, newdata):
        """
        尾部插入
        """
        node = Node(newdata)
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def insert(self, pos, newdata):
        """
        将newdata插入pos位置之后
        """
        if pos < 0:
            self.add(newdata)
        elif pos > self.length() - 1:
            self.append(newdata)
        else:
            node = Node(newdata)
            current_node = self.head
            count = 0
            while count < pos - 1:
                count += 1
                current_node = current_node.next
            node.next = current_node

    def length(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return True
            cur = cur.next
        return False






