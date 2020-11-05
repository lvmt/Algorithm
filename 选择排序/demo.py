#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''选择排序
每次找出数组中最小的元素
'''

def find_small(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
            
    return smallest_index


def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_small(arr)
        newArr.append(arr.pop(smallest))
    
    return newArr



print(selection_sort([5, 3, 6, 2, 10]))
        
        