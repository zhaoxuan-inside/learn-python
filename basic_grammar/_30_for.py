emperors = ['嬴政', '刘彻', '李世民', '赵匡胤']

for emperor in emperors:
    print(emperor)

for id in range(0, len(emperors)):
    emperor = emperors[id]
    print(emperor)

# 遍历字典
for key, value in {"wudi": 100, "zhangsan": 90}.items:
    print(key + ": " + str(value))

for item in {"wudi": 100, "zhangsan": 90}.items():
    print(item)

