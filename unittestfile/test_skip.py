import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

#python 装饰器
    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("12")

    @unittest.skipIf(3>2, "条件为true时跳过")
    def test_skipIf(self):
        print("12")

    @unittest.skipUnless(3>2, "条件为true时执行")
    def test_skipunless(self):
        print("12")

    @unittest.expectedFailure
    def test_expect_Failure(self):
        print("不管true or false 都显示为false")