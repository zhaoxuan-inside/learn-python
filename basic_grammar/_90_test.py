# 测试

import unittest

class TestStringMethods(unittest.TestCase):
    """
    这是一个测试类，继承自unittest.TestCase
    """
    
    def test_upper(self):
        """
        测试方法，断言是否相等
        """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


unittest.main()


import unittest

from _51_class import Student, Class, Score

class TestStudent(unittest.TestCase):
    """
    这是一个测试类，继承自unittest.TestCase
    """

    def setUp(self):
        """
        初始化方法，在每个测试方法执行前运行
        """

        scores = [Score(1, '语文', 90), Score(2, '数学', 80), Score(3, '英语', 70)]
        cls = Class(1, '一年级', '一班')
        self.student = Student(1, 'lisi', 18, 'female', '2021001', cls, scores)
    
    def test_study(self):
        """
        测试study方法，断言输出是否正确
        """
        curr_scores = self.student.scores;
        for curr in curr_scores:
            if curr.score < 80:
                print("not good. score: " + curr.course_name + ", score: " + str(curr.score))
    
unittest.main()