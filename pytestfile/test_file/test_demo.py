from selenium import webdriver
from time import sleep
import pytest

def setup_function(function):
    global driver
    global  base_url
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "https://www.baidu.com"

def teardown_function(function):
    driver.quit()

def test_baidu():
    driver.get(base_url)
    driver.find_element_by_id("kw").send_keys("pytest")
    driver.find_element_by_id("su").click()
    sleep(2)
    assert  driver.title == "pytest_百度搜索"


if __name__ == "__main__":
    pytest.main("-q test_demo.py")