#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2020/12/20 14:56
# @File 快乐数.py


# 用hashset检测循环体
def is_happy(n):

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()

    while n != 1 and not n in seen:  # 要么n==1, 推出; 要么n重复
        seen.add(n)
        n = get_next(n)  # 下一个数

    return n == 1



# 快慢指针法
def is_happy2(n):

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1



print(is_happy(29))