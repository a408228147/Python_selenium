import unittest
from unittestfile.count import Count

#必须要继承TestCase类

class CountTest(unittest.TestCase):
    '''计算'''
    #每条用例开始执行setup和结束teardown都会执行
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

        #必须要以test_开头
    def test_add(self):
        c = Count(3,5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_add2(self):
        c = Count(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_add3(self):
        c = Count(5, 5)
        result = c.add()
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()