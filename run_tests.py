import unittest
import HTMLTestRunner
import time
#测试一个文件夹里面的用例

suit = unittest.defaultTestLoader.discover("./unittestfile", "test_*.py", )
#执行顺序 还是a-z,A-Z，0-9
'''
runner = unittest.TextTestRunner()
runner.run(suit)
'''
nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
file = open(nowtime+"report.html", "wb")
runner = HTMLTestRunner.HTMLTestRunner(file)
runner.run(suit)
file.close()#关闭文件