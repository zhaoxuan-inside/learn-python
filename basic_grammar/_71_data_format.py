# 数据存储格式

# json 数据格式
import json

emperors = ['嬴政', '刘彻', '李世民', '赵匡胤']

# 将json格式的数据写入到文件中
with open('emperors.json', mode='w') as emperors_json_file:
    json.dump(emperors, emperors_json_file)

# 从文件中读取json格式的数据
with open('emperors.json') as emperors_json_file:
    print(json.load(emperors_json_file))

