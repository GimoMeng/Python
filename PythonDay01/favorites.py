#把你的爱好列出来，并把这个列表起个变量名games.现在把你喜欢的食物列出来，起个变量名为foods.把这两个列表连在一起并把结果命名为favorites.最后，把变量favorites打印出来
games = ['computer','phone','ball']
foods = ['apple','banana','pear']
favorites = games + foods
print(favorites)


#创建两个变量：一个指向你的姓一个指向你的名.创建一个字符串，用占位符使用这两个变量来打印带有你名字的信息，比如“你好,某某某！”
name1 = 'song'
name2 = 'meng'
print('Hello,%s' % name1+name2,'!')




#用turtle模块的Pen函数来创建一个新画布，然后画一个长方形
import turtle
t = turtle.Pen()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)



#创建另一个画布，这次画一个三角形.
import turtle
t = turtle.Pen()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
