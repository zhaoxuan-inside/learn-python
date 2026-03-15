# 函数

# 函数定义
def say_hello():
    """say hello"""
    print("agent: hello, world")

# 函数调用
say_hello()

# 型参
def param_function(param):
    print("param: " + param)

param_function("hello")

# 位置实参
def multi_param_function(param1, param2):
    print(param1 + ": " + param2)

multi_param_function('zhangsan', 'hello')

# 关键词实参
def keyword_param_function(param1, param2):
    print(param1 + ": " + param2)

keyword_param_function(param2='hello', param1='zhangsan')

# 为型参设置默认值
def default_param_function(param1, param2='world'):
    print(param1 + ": " + param2)

default_param_function(param1='[zhangsan]')

# 返回值
def return_function():
    return "hello, world"

print(return_function())

# 方法操作集合类型参数，通过型参传入的集合类型参数在函数内被修改后，函数外的集合类型参数也会被修改，因为它们指向同一个对象
def list_param_function(scores):
    failed_names = []
    for name, score in scores.items():
        if score < 60:
            print(name + " failed")
            failed_names.append(name)
        else:
            print(name + " passed")

    for name in failed_names:
        del scores[name]

scores = {'zhangsan': 90, 'lisi': 50, 'wangwu': 70}
list_param_function(scores)
print(scores)

# 方法操作d对象本身记录内容的对象，则传入的就是内容本身，修改的是型参对象对应的内容
def change_score(score):
    if (score < 60):
        score = 60

score = 59
change_score(score)
print(score)

# 接受任意个数的型参，相当于python创建了一个名为params的元组来接收这些型参，函数内可以通过遍历这个元组来访问这些型参
def multi_param_function_tuple(*params):
    print(str(type(params)))
    for param in params:
        print("type: " + str(type(param)) + 
              "\nvalue: " + str(param))

multi_param_function(1, 'hello', [1, 2, 3], {'name': 'zhangsan'})

# 接受任意个数的关键词型参，相当于python创建了一个名为params的字典来接收这些关键词型参
def multi_param_function_dict(**params):
    print(str(type(params)))
    for key, value in params.items():
        print("key: " + str(key) + 
              "type: " + str(type(value)) +
              "\nvalue: " + str(value))
        
multi_param_function_dict(name='zhangsan', age=20, score=90)

