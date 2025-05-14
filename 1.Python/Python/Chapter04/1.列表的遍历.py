# 1. 对列表中每一个元素做相同处理 —— for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:          # 从列表中取出一个元素，与magician关联
    print(magician)

# 2. 避免缩进错误
# Python根据缩进来判断代码⾏与程序其他部分的关系

# 3. 创建数值数组 —— 列表
# 3.1 使用 range() 函数生成一系列的数
for value in range(1, 5):           # 注意range()函数是左闭右开的区间
    print(value)
# 3.2 range()方法 与 list()函数 —— 使用 range() 函数创建数值列表
# 使用list()函数将range()的结果直接转化为列表元素
python_arry = list(range(1, 6))
print(python_arry)
# 在使用range()函数时还可以指定【步长】
even_numbers = list(range(2, 11, 2))    # range()函数从2开始数，然后不断地加2
print(even_numbers)
# 3.3 列表推导式 —— 将 for 循环和创建新元素的代码合并成⼀⾏，并自动追加新元素
squares = [value**2 for value in range(1, 11)]
# 第一部分：表达式。  value**2 就是表达式，它计算平方值
# 第二部分：for循环。 表示生成元素的基本范围，这里是没有冒号的
print(squares)

# 4.使用列表中的一部分
# 4.1 切片 —— list_name[index_begin : index_end] （左闭右开的区间）
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])             # 其中的player[0:3]也是一个列表，可以赋值给一个新的列表
players_slice = players[0:3]
print(players_slice)
# 【特性】如果没有指定第⼀个索引，Python 将⾃动从列表开头开始；要让切⽚终⽌于列表末尾，也可使⽤类似的语法
# 【特性】负数索引返回与列表末尾有相应距离的元素，因此可以输出列表末尾的任意切⽚
print(players[-3:])             # 输出名单中最后三位队员的名字
# 4.2 遍历切片 —— 在for循环中使用切片
for player in players[:3]:
    print(player)               # 遍历前三名队员的姓名
# 4.3 复制列表 —— 不传递起始索引而切片整个列表
my_foods = ['pizza', 'falafel', 'carrot cake']
my_friend_foods = my_foods[:]
# 【注意】不使用切片实现复制列表：直接赋值
# friend_foods = my_foods   这一行代码是行不通的！
# 这其实是让新变量 friends_foods 关联到已存在变量 my_foods，即两个变量指向同一个列表
# 当其中一个变量发生变化时，列表本体随之改变，而另一个变量也会改变

# 5.元组 —— 不可变的列表
# 5.1 元组的定义 —— tuple_name = (..,..)
# 定义元组后，就可使⽤索引来访问其元素，就像访问列表元素⼀样
# 元组是由逗号标识的，因此哪怕只有一个元素，也必须带上逗号
my_tuple1 = (1,2)
my_tuple2 = (1,)
# dimensions[0] = 25            # 试图修改元组的操作是被禁止的！
# 5.2 遍历元组中的元素值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
# 5.3 修改元组变量
# 虽然不能修改元组的元素，但可以给表⽰元组的变量赋值
test_tuple1 = (1,2)
for t in test_tuple1:
    print(t)
# 这样可以直接覆盖原来的元组
test_tuple1 = (3,4)
for t in test_tuple1:
    print(t)