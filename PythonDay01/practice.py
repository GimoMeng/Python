#第三章：字符串、列表、元组和字典
#把你的爱好列出来，并把这个列表起个变量名games.现在把你喜欢的食物列出来，起个变量名为foods.把这两个列表连在一起并把结果命名为favorites.最后，把变量favorites打印出来
games = ['computer','phone','ball']
foods = ['apple','banana','pear']
favorites = games + foods
print(favorites)




#有三座建筑，每座藏了25个忍者，有两个地道，每个藏了40个武士，问一共有多少人可以投入战斗？
building = 3
ninja_per_building = 25
tunnel = 2
samurai_per_tunnel = 40
total = building * ninja_per_building + tunnel * samurai_per_tunnel
print(total)




#创建两个变量：一个指向你的姓一个指向你的名.创建一个字符串，用占位符使用这两个变量来打印带有你名字的信息，比如“你好,某某某！”
name1 = 'song'
name2 = 'meng'
print('Hello,%s' % name1+name2,'!')




#第四章：用海龟画图
#用turtle模块的Pen函数来创建一个新画布，然后画一个长方形
import time
import turtle

width = 100
height = 50

t = turtle.Pen()
t.forward(width)
t.left(90)
t.forward(height)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height)
t.left(90)



#创建另一个画布，这次画一个三角形.
import math
import time
import turtle

t = turtle.Pen()

#画一个等边三角形
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

#把坐标换到另一个位置
t.up()
t.right(90)
t.forward(200)
t.left(90)
t.down()

#画一个内角分别为30',30',120'的三角形
t.forward(80 * math.sqrt(3))
t.left(150)
t.forward(80)
t.left(60)
t.forward(80)
t.left(150)

time.sleep(5)





#写个程序来画出没有角的方格
import time
import turtle

t = turtle.Pen()

#下
t.forward(100)
t.up()
t.forward(20)
t.left(90)
t.forward(20)
t.down()

#右
t.forward(100)
t.up()
t.forward(20)
t.left(90)
t.forward(20)
t.down()

#上
t.forward(100)
t.up()
t.forward(20)
t.left(90)
t.forward(20)
t.down()

#左
t.forward(100)
t.up()
t.forward(20)
t.left(90)
t.forward(20)
t.down()

time.sleep(5)




#你是富翁么
money = 2000
if money > 1000:
    print('I\'m rich!!')
else:
    print('I\'m not rich!!')
    print('But I might be later...')




#用if语句判断一个数是否少于100或大于500，如果这个条件为真则打印“不是太少就是太多”
#twinkies = 50
#twinkies = 300
twinkies = 550

if twinkies < 100 or twinkies > 500:
    print("Too less or too more")




#用一个if语句检查变量money是否在100到500之间，或是1000到5000之间
#money = 250
#money = 2500
money = 9999

if (money >= 100 and money <= 500) or (money >= 1000 and money <= 5000):
    print("money in [100, 500] or in [1000, 5000]")
else:
    print("Neither in [100, 500] nor in [1000, 5000]")




#创建一组if语句，在变量ninja小于10时打印“我能打过”、小于30时打印“有点难”、小于50时打印“太多了”
#ninjas = 10
#ninjas = 30
ninjas = 5
if ninjas < 10:
    print("I can beat them")
elif ninjas < 30:
    print("It's a little difficult but I can deal with it")
elif ninjas < 50:
    print("Too more ninjas there!")




#
hugehairypants = ['huge','hairy','pants']
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
	    print (j)




#解释下面的代码会发生什么
for x in range(0,20):
    print('Hello %s' % x)
    if x < 9:
        break
#第一次循环时就因x<9触发了break，因此只能打印一次 hello 0




#如果你的年龄是偶数，从2开始打印知道你的年龄为止，如果是你的年龄是奇数，从1开始
age = 23

start = 2
if age % 2 != 0:
    start = 1

for x in range(start, age + 2, 2):
    print(x)




#创建一个列表，它包含五种不同的制作三明治的材料
#创建一个循环来打印这个列表（包括序号）
ingredients = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
for x in range(0,5):
    print(x + 1,ingredients[x])




#月球上你的体重是在地球上的16.5%，假设你每年增长1公斤，打印未来15年你的体重状况
weight = 9999       #体重
increment = 1       #体重年增量
coefficient = 0.165 #体重转换系数

for x in range(1, 16):
    print("%d years later: %f" % (x, (weight + increment * x) * coefficient))
