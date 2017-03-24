#!/usr/bin/env python3
# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5

bmi = weight/(height*height)
if bmi<18.5:
  print('过轻')
elif bmi>=18.5 and bmi<25:
  print('正常')
elif bmi>=25 and bmi<28:
  print('过重')
elif bmi>=28 and bmi<32:
  print('肥胖')
elif bmi>32:
  print('严重肥胖')




name=input('请输入你的名字：')
weight=input('请输入你的体重：')
height=input('请输入你的身高：')
weight=float(weight)
height=float(height)

BMI=weight/(height*height)
if BMI<0:
    print('数据有误')
elif BMI<18.5:
    print('BMI为%d%%，%s过轻'%(BMI,name))
elif BMI<25:
    print('BMI为%d%%，%s正常'%(BMI,name))
elif BMI<28:
    print('BMI为%d%%, %s过重'%(BMI,name))
elif BMI<32:
    print('BMI为%d%%, %s肥胖'%(BMI,name))
elif BMI<100:
    print('BMI为%d%%, %s严重肥胖'%(BMI,name))
else:
    print('你一定不是人类')