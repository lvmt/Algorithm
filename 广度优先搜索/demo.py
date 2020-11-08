#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
一种基于图的算法
解决的问题:
1.从节点A出发,有无前往B的路径.
2.从节点A出发,前往B节点那些路径最短.
## 思路
先在一类关系中查找,再在二类关系中查找.
## 推荐数据结构
队列 deque
先进先出
## 只有按照顺序的添加元素,才能实现该算法
'''

graph = {} 
graph["you"] = ["alice", "bob", "claire"]  # 你的朋友,理解为一级关系

graph["bob"] = ["anuj", "peggy"]  #朋友的朋友, 二级关系
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"]  
graph["anuj"] = [] 
graph["peggy"] = [] 
graph["thom"] = [] 
graph["jonny"] = [] 

from collections import deque 
search_queue = deque() 
search_queue += graph["you"] 


def person_is_seller(name): 
    return name[-1] == 'm'  #这个函数检查人的姓名是否以m结尾

while search_queue: 
    person = search_queue.popleft() 
    if person_is_seller(person):
        print(person + " is a mango seller!")
    else: 
        search_queue += graph[person]
    
    
    
