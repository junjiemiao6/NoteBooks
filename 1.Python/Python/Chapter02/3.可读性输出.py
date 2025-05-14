# 1.制表符与换行符
# 制表符\t
print("\tPython")
# 换行符\n
print("1.XiJie\n2.ZhangZhong\n3.Henu")
# 可以在同⼀个字符串中同时包含制表符和换⾏符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 2.字符串处理——Python中的“空白”
# 删除左右空白和同时删除两边空白，空⽩泛指任何⾮打印字符，如空格、制表符和换⾏符
# rstrip，lstrip和strip
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
# 要永久删除这个字符串中的空⽩，必须将删除操作的结果关联到变量
favorite_language = favorite_language.rstrip()

# 3.字符串处理——前后缀
# 删除前缀：removeprefix() 保持原始字符串不变，在括号内输⼊了要从原始字符串中删除的前缀
nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

# 删除后缀：removesuffix()
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
