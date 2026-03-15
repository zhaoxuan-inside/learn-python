# 元组就是不可变的列表

# 元组定义
number_tuple = (1, 2, 3, 4, 5)

# 元组不能进行删除，会报错
del number_tuple[0]
""""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
"""

# 根据元组的元素创建列表
tuple_list = list(number_tuple)
del tuple_list[0]

# 元组元素数量
tuple_length = len(number_tuple)
print(tuple_length)

# 元组计算最大最小值y以及和
print("max: " + str(max(number_tuple)) +
      "\nmin: " + str(min(number_tuple)) +
      "\nsum: " + str(sum(number_tuple)))

# 根据列表的元素创建元组
numbers = [1, 2, 3, 4, 5]
number_tuple = tuple(numbers)