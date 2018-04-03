from time import sleep

from selenium import webdriver

from test.modules import BaiDu


#数据驱动 就是 把代码和数据分离

class mytest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.baiDu = BaiDu(self.driver)
        self.search_keys =["selenium", "python", ]
    def test_case1(self):
        for i in self.search_keys:
            self.baiDu.search(i)
            sleep(2)

    def test_case3(self):
        self.baiDu.close()

if __name__ == '__main__':
    MY = mytest()
    MY.test_case1()
    MY.test_case3()