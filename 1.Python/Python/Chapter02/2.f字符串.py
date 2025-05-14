# 1. 关于大小写字母的三种方法：title，upper，lower
# 每个⽅法后⾯都跟着⼀对括号，这是因为⽅法通常需要额外的信息来完成⼯作
# 这种信息是在括号内提供的
name = "ada Lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 2.格式化输出字符串“f”
# f字符串：format（设置格式），Python 通过把花括号内的变量替换为其值来设置字符串的格式
school = "henu"
name = "MJJ"
# 如利⽤与变量关联的信息来创建完整的消息
# 需要注意的是，花括号内可以是变量，也可以是调用了方法后的变量
# eg：
print(f"{name}的学校是{school.title()}")
# C++: cout<<name<<"的学校是"<<school;

# 还可以使⽤ f 字符串来创建消息，再把整条消息赋给变量
message = f"Hello!{school.upper()}!"
print(message.lower())

# 3.Python中也有类似的字符串拼接功能
name1 = "MJJ"
name2 = "SRQ"
love = " love "
print(f"{name1} love {name2}")
print(name1 + love + name2)

