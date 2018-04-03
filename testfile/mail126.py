from time import sleep

from selenium import webdriver

from testfile.modules import email


class mailTest:
    def __init__(self):
        self.dirver = webdriver.Chrome()
        self.dirver.get("http://www.126.com")
        self.mail = email(self.dirver)
        #读取文件
        user_file  = open('user_info.txt', 'r')
        lines  = user_file.readlines()
        user_file.close()
        self.username = []
        self.password = []
        for line in lines:
            self.username.append(line.split(';')[0])
            self.password.append(line.split(';')[1])

    def test_case(self):
        print(self.username[0])
        self.mail.login(self.username[0], self.password[0])

    def test_case2(self):
        self.mail.login(self.username[1], self.password[1])

    def close(self):
        self.mail.close()

if __name__ =='__main__':
    mailtest  = mailTest()
    sleep(10)
    mailtest.test_case()
    mailtest.test_case2()
    mailtest.close()
