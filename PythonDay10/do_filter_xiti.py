#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
def is_palindrome(n):
    strA = str(n)   #将n转化为字符串
    strB = strA[::-1]      #利用切片操作将字符串倒序
    if strA == strB:
        return True
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))