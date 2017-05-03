#猜数游戏
import random
num = random.randint(1,100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
            print('You guessed right')
            break
    elif i < num:
            print('Try higher')
    elif i > num:
            print('Try lower')




#画星星
import turtle
t = turtle.Pen()
t.reset
for x in range(1,9):
    t.forward(100)
    t.left(225)
t.reset
for x in range(1,38):
    t.forward(100)
    t.left(175)
t.reset
for x in range(1,19):   #创建一个运行18次的循环
    t.forward(100)      #向前移动100个像素
    if x % 2 == 0:      #检查变量x是否包含一个偶数
        t.left(175)     #左转175度
    else:               #否则
        t.left(225)     #左转225度




#画盒子
import tkinter as tk
base = tk.TK()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_rectangle(10,10,50,50)
