people = ["毕加索","秦始皇","汉武帝","爱因斯坦"]
print(people)
print(f"{people[2]}无法赴约！改为邀请 唐三藏。")
people[2] = "唐三藏"
print(people)

# 再邀请三位
people.insert(0,"朱棣")
people.insert(3,"朱高炽")
people.append("朱瞻基")
print("只能邀请两位嘉宾！")
p1 = people.pop(6)
print(f"{p1}对不起，人太多了！")
p2 = people.pop(5)
print(f"{p2}对不起，人太多了！")
p3 = people.pop(4)
print(f"{p3}对不起，人太多了！")
p4 = people.pop(3)
print(f"{p4}对不起，人太多了！")
p5 = people.pop(2)
print(f"{p5}对不起，人太多了！")
print(people)

del people[1]
del people[0]

print(people)
