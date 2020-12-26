#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fib_loop_while(n):
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


print(fib_loop_while(100), ' ')
