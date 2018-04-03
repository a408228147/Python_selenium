import pytest
import time

#pytest vs unittest
'''
1.一次打开浏览器运行所有用例
2.只有用例运行失败的时候才截图
3.参数化
4.po设计模式
5.selenium二次封装
 目的：简化 增强
'''

if __name__ == '__main__':
    nowtime = time.strftime("%Y-%m-%d_%H_%M_%S")
    pytest.main("-s ./  --html=./report/"+nowtime+"result.html")
    #执行全部test_*.py