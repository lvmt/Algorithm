#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/21 17:20
# @Email  13554221497@163.com
# @File   进制转换.py


from 栈 import Stack


def transver_base(number, base):
    digits = '0123456789ABCDEF'
    s = Stack()

    while number > 0:
        tmp = number % base  # 存储余数
        s.push(tmp)
        number = number // base

    new_string = ''
    while not s.is_empty():
        new_string += digits[s.pop()]

    return new_string


print(transver_base(8, 2))  # 1000
print(transver_base(8, 10))  # 8
print(transver_base(233, 16))