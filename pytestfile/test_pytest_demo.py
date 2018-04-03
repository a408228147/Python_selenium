#文件名 开头必须为test_
import pytest


class Count:
    def add(self, a, b):
        return a+b

def setup_function(function): #固定名称
    print("start------------")

def teardown_function(function):#固定名称
    print("end-----------")

def test_demo():#固定test_
    c = Count()
    result = c.add(3, 5)
    assert result == 8

    '''
cmd 目录下执行
pytest -s test_*.py
'''

    '''
if __name__ == "__main__":
    pytest.main("-s test_pytest_demo.py")
    '''