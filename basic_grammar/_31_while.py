# while 循环

# while 循环的语法
num = 0
while num < 5:
    print(num)
    num += 1
    if (num % 2 == 0):
        break

end = False
while not end:
    content = input()
    if (content == 'end'):
        end = True
    else:
        print(content)


invalid_list = ['zhangsan', 'lisi']
valid_list = []
while True:
    invalid_list_len = len(invalid_list)
    if (invalid_list_len == 0):
        break
    else:
        ele = invalid_list.pop(0)
        print('varify: ' + ele)
        valid_list.append(ele)

print(invalid_list)
print(valid_list)