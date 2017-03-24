#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates) 
print('len(classmates) =', len(classmates))   #计算str包含多少个字符，bytes包含多少个字节数
print('classmates[0] =', classmates[0])       #list中第一个元素
print('classmates[1] =', classmates[1])       
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])     #list中最后一个元素
classmates.pop()                              #删除list末尾的元素
print('classmates =', classmates)
classmates.append("Adam")                     #像list中追加元素到末尾
print('classmates = ',classmates)
classmates.insert(1, 'Jack')                  #把元素插入到指定位置
print('classmates = ',classmates)
classmates.pop(1)                             #删除指定位置的元素
print('classmates = ',classmates)
classmates[1] = 'Sarah'                       #把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print('classmates = ',classmates)
