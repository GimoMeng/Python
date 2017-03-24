#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))  #计算str包含多少个字符，bytes包含多少个字节数
print('classmates[0] =', classmates[0])      #tuple(元组)中第一个元素
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])    #tuple中最后一个元素

# cannot modify tuple:                       #tuple一旦初始化不能修改
classmates[0] = 'Adam'