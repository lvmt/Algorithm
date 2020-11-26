#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
冒泡排序的思想:
遍历数组, 比较相邻的2个数,找到最小的数,将其放在前面.
'''


def bubblo_sort_simple(li):
    '''原地排序
    '''

    for i in range(len(li) - 1):  # 遍历的趟数, 第几趟.
        for j in range(len(li)- i - 1): # 每趟需要比较的次数
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j] 

        print(li)

    
def bubblo_sort(li):
    '''对冒泡算法进行优化
    冒泡算法中,涉及到数据位置交换,
    如果在一趟中,没有进行任何的数据交换,认为这个是有序数据.

    '''
    for i in range(len(li) - 1):  # 遍历的趟数, 第几趟.
        exchange = False
        for j in range(len(li)- i - 1): # 每趟需要比较的次数
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j] 
                exchange = True
        print(li)
        if not exchange:
            return li
    
li = [9,8,7,6,5,4,3,2,1]
#li = [1,2,3,4,5,6,7,8,9]
print(li)
bubblo_sort(li)
