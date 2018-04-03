import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

#服务器地址
smtpserver= 'smtp.qq.com'

#发送者信息
usermail= "XXXX@qq.com"
pwd = "XXXXXX"
#发送邮箱
sender = "XXXX@qq.com"
#接收邮箱
receiver = "XXXX@qq.com"
#主题
subject ="python send mail test"

#发送附件
sendfile= open("D:/project/pytestfile/2018-04-03 12-42-38report.html", 'rb').read()
att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"]="application/octet-stream"
att["Content-Disposition"]='acctachment;filename="2018-04-03 12-42-38report.html"'
msgRoot = MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(usermail, pwd)
smtp.sendmail(sender,[receiver],msgRoot.as_string())
smtp.close()