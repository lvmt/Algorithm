#!/usr/bin/env python
#-*- coding:utf-8 -*-

# def countdown(i):
#     print(i)
#     if i < 0:
#         return 
#     else:
#         countdown(i-1)
        
# print(countdown(8))

def lenList(list):
    if list == []:
        return 0
    else:
        return 1+lenList(list[1:])
print(lenList([1,2,3]))
