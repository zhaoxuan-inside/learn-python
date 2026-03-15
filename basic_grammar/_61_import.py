# 导入模块
# 1. 交互模式下，python会扫描当前工作目录下的模块，以及默认的扫描路径
# 2. 脚本模式下，python会扫描当前脚本所在目录下的模块，以及默认的扫描路径
# 交互模式，当前工作目录查看方法
# import os   
# print(os.getcwd())
# 模块j 加载路径查看方法
# import sys
# print(sys.path)

import _60_module

_60_module.say_hello()

# ❓ 模块导入问题
# 通过import导入模块因为python加载module的路径不存在目标模块，导致模块加载失败，这会有缓存；
# 导致即使通过将模块所处的路径加入到python加载路径后，虽然可以import导入模块，但是无法通过模块调用方法
# 解决方法：
# 1. 退出当前交互模式
#    exit()
# 2. 重新进入交互模式
#    python
# 3. 将模块所在路径加入到python加载路径
#    import sys
#    sys.path.append('/home/hardstone/CodeSpace/GitHub/learn-python/basic_grammar')
# 4. 重新import导入模块
#    import _60_module

# 重新加载模块
from importlib import reload
import _60_module
reload(_60_module)
_60_module.say_other()

# 导入模块的部分方法
from _60_module import say_hello as hello

# 导入类
from _51_class import Student, Class, Score
class_info = Class(1, '一年级', '一班')
scores = [Score(1, '语文', 90), Score(2, '数学', 80), Score(3, '英语', 70)]
student = Student(1, 'lisi', 18, 'female', '2021001', class_info, scores)
student.study('math')
student.show_scores()
student.action("running")
student.sleep()
student.eat('banana')