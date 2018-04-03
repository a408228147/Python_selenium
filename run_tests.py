import smtplib
import unittest
from email.header import Header
from email.mime.text import MIMEText

import HTMLTestRunner
import time
#测试一个文件夹里面的用例

def send_mail(test_report):
    with open(test_report,'rb') as f:
        mail_body =f.read()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("自动化测试报告","utf-8")
    smtp = smtplib.SMTP()
    smtp.connect("smtp.qq.com")
    smtp.login("408228147@qq.com","zheng9669932159")
    smtp.sendmail("408228147@qq.com","810724394@qq.com",msg.as_string())
    msg.quit()

if __name__ =='__main__':
    suit = unittest.defaultTestLoader.discover("./unittestfile", "test_*.py", )
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S")
    test_report =nowtime+"report.html"
    with open(test_report, 'rb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f)
        runner.run(suit)
    send_mail("2018-04-03 12-42-38report.html")
#执行顺序 还是a-z,A-Z，0-9
'''
runner = unittest.TextTestRunner()
runner.run(suit)
'''
