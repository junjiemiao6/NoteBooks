# 1.修改列表元素
# 可指定列表名和要修改的元素的索引，再【赋予】该元素的新值
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 2.在列表中添加元素
# 2.1 在列表末尾添加元素 —— append(variable)方法
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# 2.2 在列表中插入元素 —— insert(index,variable)方法
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.从列表中删除元素
# 3.1 根据索引位置index删除元素 —— del语句
del motorcycles[0]
print(motorcycles)
# 3.2 删除列表末尾的元素并接着使用这个元素 —— pop()方法
# 列表就像⼀个栈，⽽删除列表末尾的元素相当于弹出并返回栈顶元素
popped_motorcycle = motorcycles.pop() # 使用新变量来

# 接收pop方法的返回值
# 3.3 删除列表任意位置元素 —— pop(index)方法
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# 【补充】如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，就使⽤ del 语句；
# 如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅法
# 3.4 根据元素值删除元素 —— remove(variable)方法
motorcycles.remove('ducati')
print(motorcycles)
# 需要注意的是，remove只能删除第一个列表元素，若列表中有多个重复值，需要多次remove
