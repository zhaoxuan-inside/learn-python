content = "hello python"

# 计算字符串长度
print(len(content))

# 将字符串的首字母大写
print(content.title())

# 所有字母转成小写
print(content.lower())

# 所有字母转成大写
print(content.upper())

# 删除字符串末尾的空格
print(len(((content + " ").rstrip())))

# 删除字符串开头的空格
print(((" " + content).lstrip()))

# 删除字符串首尾的空格
print(len(((" " + content + " ").strip())))

# 字符串的分割
print(content.split(" "))