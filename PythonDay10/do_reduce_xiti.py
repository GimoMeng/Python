#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
	def mul(x, y):
		return x*y
	return reduce(mul, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))