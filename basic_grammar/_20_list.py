# 列表定义
names = ['zhangsan', 'lisi', 'wangwu']

# 定义空列表
empty_list = []

# 计算列表长度
length_names = len(names)
length_empty_list = len(empty_list)

print(length_names)
print(length_empty_list)

# 访问指定索引的元素
idx = 1
name = names[idx]
print(name)

# 第1个元素的索引
idx = 0
print(names[idx])
# 最后一个元素的索引
idx = -1
print(names[idx])
# 倒数第二个元素的索引
idx = -2
print(names[idx])

# 追加元素到列表的最后
names.append('wudi')
print(names[-1])

# 插入元素到列表的指定位置，该位置之后的元素因此向后后移一位
names.insert(0, 'leichi')
print(names[0])

# 删除指定索引位置的元素
del names[0]
print(names[0])

# 从列表尾弹出一个元素
name = names.pop()
print(name)

# 从指定位置弹出一个元素
name = names.pop(0)
print(name)

# 按照元素内容进行删除第一个遇到的该元素，元素不存在会报错
emperors = ['嬴政', '刘彻', '刘彻', '李世民', '赵匡胤']
emperors.remove('刘彻')
print(emperors)

# 对列表元素进行排序(正序)，改变本列表的顺序
numbers = [4, 3, 2, 1]
numbers.sort(reverse=True)
print(numbers)

# 对列表元素进行排序(倒序)，改变本列表的顺序
numbers.sort(reverse=True)
print(numbers)

# 将列表中的元素进行排序并输出(正序)，不改变原列表顺序
asc = sorted(numbers)
print(asc)

# 将列表中的元素进行排序并输出(倒序)，不改变原列表顺序
desc = sorted(numbers, reverse=True)
print(desc)

# 数值类型的列表的最大最小值以及和
print('max: ' + str(max(numbers)) + 
      "\nmin: " + str(min(numbers)) + 
      "\nsum: " + str(sum(numbers)))

# 反序列表元素
emperors.reverse()
print(emperors)

# 将集合类型转成列表
range_list = list(range(0, 5))
print(range_list)

# 数据集合生成
range_list_step3 = list(range(0, 20, 3))
print(range_list_step3)

range_list_square = list(num ** 2 for num in range(0, 5))
print(range_list_square)

# 列表切片(从索引为1到索引小于3）
subnumbers = numbers[1:3]
print(subnumbers)

# 列表切片(从索引为0到索引小于3）
subnumbers = numbers[:3]
print(subnumbers)

# 列表切片(从索引为3到结尾）
subnumbers = numbers[3:]
print(subnumbers)

# 列表切片(从索引为倒数第2个到结尾）
subnumbers = numbers[-2:]
print(subnumbers)

# 深拷贝列表（通过切片实现)
deep_copy_numbers = numbers[:]
del numbers[0]
print("numbers: " + str(numbers) + "\ndeep_copy_numbers: " + str(deep_copy_numbers))

# 深拷贝列表(通过list()函数实现)
copy_numbers = list(numbers)
del numbers[0]
print("numbers: " + str(numbers) + "\ncopy_numbers: " + str(copy_numbers))

# 浅拷贝列表
shallow_copy_numbers = numbers
del numbers[0]
print("numbers: " + str(numbers) + "\nshallow_copy_numbers: " + str(shallow_copy_numbers))

