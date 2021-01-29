#!/usr/bin/env python
#-*- coding:utf-8 -*-


'''
理解排序原理
节约空间:原地排序
'''


def select_sort(li):
    
    for i in range(len(li)-1):  # 第几趟
        print('第几趟:', i)
        small_idx = i  # 中间变量, 记录最小值的索引
        for j in range(i+1, len(li)): # 遍历未排序的列表, 列表的左边是排好序的.
            if li[j] < li[small_idx]:
                small_idx = j
        li[i], li[small_idx] = li[small_idx], li[i]  # 交换值的位置
        print(li)
 
        
li = [9,8,7,6,5,4,3,2,1]

select_sort(li) 