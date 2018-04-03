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
    def test_add(self):
        c = Count(3,5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_add2(self):
        c = Count(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_add3(self):
        c = Count(3, 5)
        result = c.sub()
        self.assertEqual(result, -2)
class AssertTestDemo(unittest.TestCase):

    def test_ae(self):
        self.assertEqual("a", "a")

    def test_tf(self):
        a = True
        self.assertTrue(a)

    def test_in(self):
        a = "dasdas"
        self.assertIn("da",a)

if __name__ == '__main__':
    #unittest.main()
    #执行顺序 a-z,A-Z，0-9

#测试套件 ----》运行测试的集合
    suit = unittest.TestSuite()
    suit.addTest(AssertTestDemo("test_ae"))
   # suit.addTest(CountTest("test_add2"))
    runner = unittest.TextTestRunner()
    runner.run(suit)

#testfixtrue 环境 包括了setup teardown（方法） 用例   还包括setUpModule tearDownModule（模块）
# @classmethod
#def setUpClass(cls)  def tearDownClass(cls) (类)