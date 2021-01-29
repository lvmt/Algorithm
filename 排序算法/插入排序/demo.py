#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
- 保持原地排序
- 摸牌的次数
- 如何移动牌

'''

def insert_sort(li):
    for i in range(1, len(li)): # 摸牌的次数
        for j in range(i, 0, -1):
            if li[j] < li[j-1]:
                li[j],li[j-1] = li[j-1],li[j]

        #print('第{}次排序: {}'.format(i, li))





import random
li = list(range(1000))
random.shuffle(li)
print(f'原始列表为:{li}')
insert_sort(li)
print(li) 



