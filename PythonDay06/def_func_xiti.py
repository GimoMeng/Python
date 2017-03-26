#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#的两个解。
#提示：计算平方根可以调用math.sqrt()函数：

import math

def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('Bad operand type')
    if not isinstance(b,(int,float)):
        raise TypeError('Bad operand type')
    if not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
    d = b*b-4*a*c
    if d < 0:
        print('此方程无解')
    elif  d == 0:
        print('方程只有一个根')
        x=b/(2*a)
        return x
    else :
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print('方程两个解为')
        return x1,x2

print (quadratic(1,2,1))