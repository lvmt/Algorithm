#!/usr/bin/env python
#-*- coding:utf-8 -*-

def serial_find(li, item):
    '''顺序查找
    '''
    for i in range(len(li)):
        if li[i] == item:
            return i 
    return None 


print(serial_find([1,2,3,4,5,6,7,8], 3))