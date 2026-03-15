# 字典（Dictionary）是一种可变的、无序的数据结构，用于存储键值对（key-value pairs）。每个键（key）与一个值（value）相关联，可以通过键来访问对应的值。字典使用花括号 {} 来定义，键和值之间用冒号 : 分隔，多个键值对之间用逗号 , 分隔。

# 字典的定义
score_dic = {"zhangsan": 90, "lisi": 80, "wangwu": 70}

print(score_dic)

# 获取指定key的value
score = score_dic["zhangsan"]
print(score)

# 修改指定的key的元素
score_dic["zhangsan"] = 95
print(score_dic)

# 给字典添加元素
score_dic["wudi"] = 100
print(score_dic)

# 删除指定key的元素
del score_dic["wudi"]
print(score_dic)

# 获取字典的所有key
names = score_dic.keys()
print(names)

# 获取字典的所有value
scores = score_dic.values()
print(scores)

