# 文件操作

# 文件读取，with可以用来自动的管理资源，with块结束后会自动关闭文件
with open('_61_import.py') as import_file:
    content = import_file.read()
    print(content)

# 文件读取，手动管理资源
import_file = open('_61_import.py')
content = import_file.read()
print(content)
import_file.close()


# 按行读取文件 mode=r
with open('_61_import.py') as import_file:
    print(type(import_file))
    for line in import_file:
        print(line, end='')

# 按字符读取文件 mode=r
with open('_61_import.py') as import_file:
    file_buffer = import_file.buffer
    file_buffer_read = file_buffer.read()
    while file_buffer_read:
        print(file_buffer_read)
        file_buffer_read = file_buffer.read()

def read_file(file_name):
    with open(file_name) as file:
        content = file.read()
        print(content)

# 文件写入，将本次文件打开过程中输入的内容覆盖原有的内容 mode=w
with open('output.txt', mode='w') as output_file:
    emperors = ['嬴政', '刘彻', '李世民', '赵匡胤']
    for emperor in emperors:
        output_file.write(emperor)

# 文件写入，将本次文件打开过程中输入的内容追加到原有内容之后 mode=a
with open('output.txt', mode='a') as output_file:
    emperors = ['嬴政', '刘彻', '李世民', '赵匡胤']
    for emperor in emperors:
        output_file.write(emperor)

read_file('output.txt')