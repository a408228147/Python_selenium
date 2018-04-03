import  csv #导入csv包

#读取csv本地文件
date = csv.reader(open('text.csv', 'r'))

for user in date:
    print(user)

