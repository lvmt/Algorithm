#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Author lvmengting
# @Time   2020/12/21 15:05
# @Email  13554221497@163.com
# @File   括号匹配.py


"""
利用栈实现括号匹配问题
"""


from 栈 import Stack


def matches(string):  #运行效率高, 内存占用较大
    BRANKETS = {'}': '{', ']': '[', ')': '('}

    s = Stack()
    for i in string:
        if i in '{[(':
            s.push(i)
        elif i in '}])':
            if s.size() and s.peek() == BRANKETS.get(i):  # 如果栈不为空,且元素匹配
                s.pop()
            else:
                return False

    # 栈里面还存在元素, 左括号太多
    print(s.items)
    return not s.items


# print(matches('[[[[{{()}}]]]]'))



def matches2(string): # 效率较慢, 内存运行较快的程序
    while '{}' in string or '[]' in string or '()' in string:
        string = string.replace('{}', '').replace('[]', '').replace('()', '')

    return string == ''


print(matches2('[[]]}'))