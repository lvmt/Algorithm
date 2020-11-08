#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
权重图
'''

graph = {}

graph["start"] = {} 
graph["start"]["a"] = 6 
graph["start"]["b"] = 2

graph["a"] = {} 
graph["a"]["fin"] = 1 
graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["fin"] = 5

graph["fin"] = {}


## 各个节点的开销
infinity = float("inf") 
costs = {} 
costs["a"] = 6  #跟新后的值为：5
costs["b"] = 2 
costs["fin"] = infinity

# 各个节点的父节点
parents = {} 
parents["a"] = "start" 
parents["b"] = "start" 
parents["fin"] = None

# 记录已经处理过的节点数目
processed = []

def find_lowest_cost_node(costs): 
    lowest_cost = float("inf") 
    lowest_cost_node = None 
    for node in costs:
        cost = costs[node] 
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node 
    return lowest_cost_node 

node = find_lowest_cost_node(costs)  # b

while node is not None:
    cost = costs[node] # 2
    neighbors = graph[node] 
    for n in neighbors.keys(): # a, fin
        new_cost = cost + neighbors[n] 
        if costs[n] > new_cost:
            costs[n] = new_cost  # 更新开销
            parents[n] = node    # 跟新父节点
    processed.append(node)
    node = find_lowest_cost_node(costs)
    
print(costs)
print(parents) # 通过parent,可以知道这条路径是怎么达到的.


l = []
p = parents.get('fin', 'None')
while p:
    l.insert(0,p)
    p =  parents.get(p, '') # b 

print('最短路径图：{}-->final'.format("-->".join(l)))