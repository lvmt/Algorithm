#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time 2021/1/2 21:02
# @File 字符串解码.py


"""
输入：s = "3[a2[c]]"
输出："accaccacc"
"""


class Stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)

    def pop(self):
        data = self.s.pop()
        return data

    def peek(self):
        return self.s[-1]

# class Solution(object):
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         ss = Stack()
#         tmp1 = ''
#         tmp = ''
#         for index in range(len(s)):  # 遍历索引
#             print('index', index)
#             if not s[index] == ']':
#                 # print('---压入')
#                 ss.push(s[index])
#             else:
#                 tmp = ''
#                 while ss.peek() != '[':  # 不是左括号
#                     # print('hhh')
#                     tmp += ss.pop()
#                 print('字符', tmp)
#                 print('左括号', ss.pop())  # 弹出左括号
#                 num = int(ss.pop())  # 前缀数字
#                 tmp = tmp[::-1]
#                 tmp = num * tmp  # 3cd
#                 tmp1 += tmp
#
#         return tmp1


# print(Solution().decodeString('3[a2[c]]'))
# print(Solution().decodeString('2[abc]3[cd]'))


class Solution2:
    def decodeString(self, s):
        stack, res, mutil = [], '', 0

        for c in s:
            if c == '[':
                stack.append([mutil, res])
                res, mutil = '', 0
            elif c == ']':
                cur_mutil, last_res = stack.pop()
                res = last_res + cur_mutil * res
            elif '0' <= c <= '9':
                mutil = mutil * 10 + int(c)
            else:
                res += c  #
        return res


print(Solution2().decodeString('3[a2[c]]'))
print(Solution2().decodeString('3[a]2[bc]'))