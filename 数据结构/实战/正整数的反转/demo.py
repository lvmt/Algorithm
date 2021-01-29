#!/usr/bin/env python
#-*- coding:utf-8 -*-

num = int(input('请输入一个数字: num = '))
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num = num // 10

print(reversed_num)