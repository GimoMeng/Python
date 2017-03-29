#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
#!/urs/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)
move(3, 'A', 'B', 'C') 
#当 n=3  a=’A’ b=’B’ c=’C’时
#分析：
#i.    Move(3,’A’,’B’,’C’)
#按照def,执行Move(n-1,a,c,b)--> Move(2,’A’,’C’,’B’)
#Move(2,’A’,’C’,’B’)
#返回def,执行Move(n-1,a,c,b) -->Move(1，’A’,’B’,’C’)
#打印（A-->C）
#按照def执行Move(1,a,b,c) --> Move(1，’A’,’C’,’B’)
#打印（A-->B）
#按照def执行Move(n-1,b,a,c) --> Move(1，’C’,’A’,’B’)
#打印（C-->B）
#ii.    Move(3,’A’,’B’,’C’)
#按照def,执行Move(1,a,b,c) --> Move(1，’A’,’B’,’C’)
#打印（A-->C）
#iii.    Move(3,’A’,’B’,’C’)
#按照def,执行Move(n-1,b,a,c) -->Move(2,’B’,’A’,’C’) 
#Move(2,’B’,’A’,’C’)
#返回def,执行Move(n-1,a,c,b) -->Move(1，’B’,’C’,’A’)
#打印（B-->A）
#按照def执行Move(1,a,b,c) --> Move(1，’B’,’A’,’C’)
#打印（B-->C）
#按照def执行Move(n-1,b,a,c) --> Move(1，’A’,’B’,’C’)
#打印（A-->C）