# 1.列表排序 —— sort()方法
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()             # sort() ⽅法能永久地修改列表元素的排列顺序，是不可恢复的
print(cars)
# 改变 sort() 中的参数传递，实现与字母顺序相反的排序
cars.sort(reverse=True) # 这种排序同样也是永久的
print(cars)
# 1.1 使用sorted()函数对列表元素进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))     # 这种方法只是在打印时进行了排序输出，而不影响列表本身
# 改变 sorted() 中的参数传递，实现与字母顺序相反的排序
# 1.2 反向打印列表元素 —— reserve()方法
cars.reverse()          # 调用reserve()方法后，列表本身改变，不可逆
print(cars)
# 1.3 len()函数可以返回列表中元素的数量
print(len(shopping_list))

# 2.使用列表时避免索引错误
# 在发⽣索引错误却找不到解决办法时，请尝试将列表或其⻓度打印出来
# 列表可能与你以为的截然不同，在程序对其进⾏了动态处理时尤其如此。