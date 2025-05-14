# 第一部分 Python基础语法

## Chapter01 入门

要点1：当程序存在严重错误时，会显示【traceback】去回溯寻找错误点

要点2：如果没有为python配置【环境变量】，无法在命令行运行python代码及文件

## Chapter02 变量与数据类型

### 2.1 变量

**顶级理解：**变量是可以被赋值的标签，它指向特定的值

### 2.2 格式化输出字符串

要点1：【f字符串】

Python 通过把花括号内的变量替换为其值来设置字符串的格式

```python
school = "henu"
name = "MJJ"
# 需要注意的是，花括号内可以是变量，也可以是调用了方法后的变量
print(f"{name}的学校是{school.title()}")
```

还可以使⽤ f 字符串来【创建消息】，再把整条消息赋给变量

```python
message = f"Hello!{school.upper()}!"
print(message.lower())
```

要点2：【通过**加法**实现字符串拼接】

### 2.3 可读性输出

要点1：制表符与换行符

可以在同⼀个字符串中同时包含制表符和换⾏符

```python
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```

要点2：字符串处理之Python中的空白

<u>空⽩泛指任何⾮打印字符，如空格、制表符和换⾏符</u>

```python
# rstrip，lstrip和strip三种方法
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
# 要永久删除这个字符串中的空⽩，必须将删除操作的结果关联到变量
favorite_language = favorite_language.rstrip()
```

要点3：字符串处理之删除前后缀

<u>注意参数传递</u>

```python
# 删除前缀：removeprefix() 保持原始字符串不变，在括号内输⼊了要从原始字符串中删除的前缀
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

# 删除后缀：removesuffix()
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
```

### 2.4 Python中的数number

要点1：Python的两个重要【特性】

1. 任意两个数相除，结果总是**浮点数**，即便这两个数都是整数且能整除
2. 如果⼀个操作数是整数，另⼀个操作数是浮点数，结果也总是浮点数（类似于C++）

要点2：数中的下划线可增强可读性

```python
# 在书写很⼤的数时，可使⽤下划线将其中的位分组，使其更清晰易读
universe_age = 14_000_000_000
print(universe_age)
# Python 不会打印其中的下划线，适⽤于整数，也适⽤于浮点数
```

## Chapter03 列表简介

### 3.1 认识列表

要点1：【方法】与【函数】的区别

1. 对象.方法()
2. 函数(操作对象/参数传递)

要点2：列表是<u>可变的</u>——例如append()方法

```python
# 变量s使用upper()方法后，只是返回了一个改变后的新字符串，而变量s本身并没有发生变化，需要重新赋值，与原变量s建立联系才能改变s

# 使用append()方法后，列表本身发生了变化，而不用与变量建立联系
shopping_list = ["键盘"]
shopping_list.append("鼠标")
print(shopping_list)
```

要点3：通过【索引位置】访问列表中的元素（下标从0开始）

```python
# Python 为访问最后⼀个列表元素提供了⼀种特殊语法通过将索引指定为-1，可让 Python 返回倒数第一个列表元素
bicycles = ['trek', 'one', 'redline', 'specialized']
print(bicycles[-1])   
```

### 3.2 列表操作

要点1：可以通过索引访问元素并赋予其新的值

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
```

要点2：在列表中添加元素的两种方法——【append()和insert()】

```python
# 在列表末尾添加元素 —— append(variable)方法
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# 在列表中插入元素 —— insert(index,variable)方法
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

要点3：在列表中删除元素的三种方法——【del语句、pop()方法和remove()方法】

```python
# 根据索引位置index删除元素 —— del语句
del motorcycles[0]
print(motorcycles)

# 删除列表末尾的元素并接着使用这个元素 —— pop()方法
# 列表就像⼀个栈，⽽删除列表末尾的元素相当于弹出并返回栈顶元素
popped_motorcycle = motorcycles.pop() # 使用新变量来接收pop方法的返回值
# 删除列表任意位置元素 —— pop(index)方法
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# 根据元素值删除元素 —— remove(variable)方法
motorcycles.remove('ducati')
print(motorcycles)
# 需要注意的是，remove只能删除第一个列表元素，若列表中有多个重复值，需要多次remove
```

> [!NOTE]
>
> 如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，就使⽤ del 语句；如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅法

### 3.3 列表管理

要点1：列表排序——sort()方法

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()             
# sort() ⽅法能永久地修改列表元素的排列顺序，是不可恢复的
print(cars)
# 改变 sort() 中的参数传递，实现与字母顺序相反的排序
cars.sort(reverse=True) # 这种排序同样也是永久的
print(cars)
```

要点2：临时排序——sorted()方法

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))     
# 这种方法只是在打印时进行了排序输出，而不影响列表本身
# 改变 sorted() 中的参数传递，实现与字母顺序相反的排序
```

要点3：反向打印列表元素——reverse()方法

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()          
# 调用reserve()方法后，列表本身改变，不可逆
print(cars)
```

## Chapter04 操作列表

### 4.1 列表的遍历

要点1：对列表中每一个元素做相同处理——for循环

```python
magicians = ['alice', 'david', 'carolina']
# 从列表中取出一个元素，与magician变量关联
for magician in magicians:          
    print(magician)
```

要点2：使用range()函数生成一系列的数，且传递的参数是左闭右开区间

要点3：创建数值列表——range()方法与list()方法

```python
# 使用list()函数将range()的结果直接转化为列表元素
python_arry = list(range(1, 6))
print(python_arry)
```

在使用range()函数时还可以指定【步长】作为第三个参数

```python
even_numbers = list(range(2, 11, 2))    # range()函数从2开始数，然后不断地加2
print(even_numbers)
```

要点4：列表推导式——将for循环和创建新元素的代码合并成1行，自动追加新元素

```python
# 第一部分：表达式。  value**2 就是表达式，它计算平方值
# 第二部分：for循环。 表示生成元素的基本范围，这里是没有冒号的
squares = [value**2 for value in range(1, 11)]

print(squares)
```

### 4.2 使用列表中的一部分

要点1：切片——list_name[index_begin : index_end] （左闭右开的区间）

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])             
# 其中的player[0:3]也是一个列表，可以赋值给一个新的列表
players_slice = players[0:3]
print(players_slice)
```

【特性1】如果没有指定第⼀个索引，Python 将⾃动从列表开头开始；要让切⽚终⽌于列表末尾，也可使⽤类似的语法

【特性2】负数索引返回与列表末尾有相应距离的元素，因此可以输出列表末尾的任意切⽚

```python
# 索引号-3表示倒数第三个元素，这一行代码将输出列表末尾的后3个元素
print(players[-3:])       
```

要点2：遍历切片——在for循环中使用切片

```python
for player in players[:3]:
    print(player)
```

要点3：复制列表——【不传递索引参数】而切片整个列表

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
my_friend_foods = my_foods[:]
```

> [!WARNING]
>
> 不使用切片实现复制列表：【直接赋值】
> 【friend_foods = my_foods】   这一行代码是行不通的！
>
> 这其实是让新变量 friends_foods 关联到已存在变量 my_foods，即两个变量指向同一个列表，当其中一个变量发生变化时，列表本体随之改变，而另一个变量也会改变

### 4.3 元组

要点1：元组的定义 —— tuple_name = (..,..,...)

定义元组后，就可使⽤索引来访问其元素，就像访问列表元素⼀样。元组是由逗号标识的，因此哪怕只有一个元素，也必须带上逗号

```python
my_tuple1 = (1,2)
my_tuple2 = (1,)
```

要点2：修改元组变量

【注意】元组中的数据元素是不允许被修改的，只能直接覆盖整个元组（赋值语句）或删除整个元组（del语句）

```python
test_tuple1 = (1,2)
# 这样可以直接覆盖原来的元组
test_tuple1 = (3,4)
for t in test_tuple1:
    print(t)
    
tup = ('physics', 'chemistry', 1997, 2000)
del tup
```

## Chapter05 if语句



# 第二部分 实践项目1——外星人入侵



# 第三部分 实践项目2——数据可视化



# 第四部分 实践项目3——Web应用程序
