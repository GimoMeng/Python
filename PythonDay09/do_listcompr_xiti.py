#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 期待输出: ['hello', 'world', 'apple']
# print(L2)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 =  [d.lower() for d in L1 if isinstance(d, str) is True]
