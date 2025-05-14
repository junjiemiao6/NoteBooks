# 1.条件测试
# 每条 if 语句的核⼼都是⼀个值为 True 或 False 的表达式，这种表达式就是条件测试

# 2.在检查【相等】时忽略大小写
# 在Python中检查相等时是区分大小写的，但大小写无关紧要时，转为小写（或大写）再比较
user_name = 'Mjj'
print(f"区分大小写：{user_name == 'mjj'}")
print(f"不区分大小写：{user_name.lower() == 'mjj'}")

# 3.检查【不相等】
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 4.检查多个条件
# 4.1 使用【and】检查多个条件 —— “与”
a = 10
b = 11
if a<20 and b<20:
    print(a<20 and b<20)
# 4.2 使用【or】检查多个条件 —— “或”

# 5.检查特定的值【在/不在】列表当中 —— 【in】关键字与【not in】关键字
players = ["Mike","MJJ","SRQ"]
people_1 = "John"
if people_1 in players:
    print(f"{people_1} 在列表中！")
else:
    print(f"{people_1} 不在列表中！")

# 6.布尔表达式
# 不过是【条件测试】的别名罢了，其结果要么是 True，要么是False
# 【布尔表达式】常常用于记录条件
game_active = True
can_edit = False