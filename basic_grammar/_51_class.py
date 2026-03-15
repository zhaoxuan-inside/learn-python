# 定义类
class Human():
    """
    定义一个Human类
    """

    def __init__(self, id, name, age, gender='male'):
        """
        初始化Human对象，根据类创建对象时，python会自动运行该方法
        """
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        print(self.name + " is sleeping")
    
    def eat(self, food):
        print(self.name + " is eating " + food)

    def action(self, action):
        print(self.name + " is " + action)


human = Human(1, 'zhangsan', 20)
human.sleep()
human.eat('apple')
human.action('running')


class Class():
    """
    定义一个Class类
    """

    def __init__(self, id, cls_grade, cls_name):
        """
        初始化Class对象，根据类创建对象时，python会自动运行该方法
        """
        self.id = id
        self.cls_grade = cls_grade
        self.clas_name = cls_name


class Score():
    """
    定义一个Score类
    """

    def __init__(self, id, course_name, score):
        """
        初始化Score对象，根据类创建对象时，python会自动运行该方法
        """
        self.id = id
        self.course_name = course_name
        self.score = score


# 类的继承
class Student(Human):
    """
    定义一个Student类，继承Human类
    """

    def __init__(self, id, name, age, gender, stu_id, class_info, scores):
        """
        初始化Student对象，根据类创建对象时，python会自动运行该方法
        """
        super().__init__(id, name, age, gender)
        self.stu_id = stu_id
        self.class_info = class_info
        self.scores = scores

    def study(self, course_name):
        print(self.name + " is studying " + course_name)

    def show_scores(self):
        print(self.name + "'s scores:")
        for score in self.scores:
            print(score.course_name + ": " + str(score.score))

class_info = Class(1, '一年级', '一班')
scores = [Score(1, '语文', 90), Score(2, '数学', 80), Score(3, '英语', 70)]
student = Student(1, 'lisi', 18, 'female', '2021001', class_info, scores)
student.sleep()
student.eat('banana')
student.study('math')
student.show_scores()