#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
   def char2num(ss):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ss]
        t = len(s)            #默认t的值为小数点位置，即默认小数点位置在字符串尾端
   for i in range(len(s) - 1):
       if s[i] == '.':
           t = i
           break
   s1 = s[0:t]         #s1存放小数点前的字符串，s2存放小数点后的字符串并反转
   if t != len(s):     #如果小数点位置不在字符串尾端，则s2正常赋值
       s2 = s[-1:t - len(s):-1]
   else:               #如果小数点位置在字符串尾端，则字符串s2的值赋值为‘0’
       s2 = ['0']
   return reduce(lambda x, y: x * 10 + y, map(char2num, s1)) + 0.1 * reduce(lambda a, b: a * 0.1 + b, map(char2num, s2))
print('str2float(\'123.456\') =', str2float('123.456'))