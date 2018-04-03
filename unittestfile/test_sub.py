import unittest
from unittestfile.count import Count

#必须要继承TestCase类

class CountTest(unittest.TestCase):
    #每条用例开始执行setup和结束teardown都会执行
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

        #必须要以test_开头
    def test_sub(self):
        c = Count(13,5)
        result = c.sub()
        self.assertEqual(result, 8)

    def test_sub2(self):
        c = Count(3, 5)
        result = c.sub()
        self.assertEqual(result, -2)

    def test_sub3(self):
        c = Count(8, 5)
        result = c.sub()
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()