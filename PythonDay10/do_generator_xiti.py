#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#把杨辉三角每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
 L = [1]
 while True:
     yield L
     L = [1] + [L[i-1]+L[i] for i in range(len(L)) if i > 0] + [1]
