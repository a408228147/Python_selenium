from selenium import webdriver
from time import sleep, ctime

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#可模块化
#获得百度搜索窗口的句柄
baidu_index_handle = driver.current_window_handle

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("注册").click()

#获取所有打开窗口的句柄
all_handle = driver.current_window_handles

#进入注册窗口
for handle in all_handle:
    if handle !=baidu_index_handle:
        driver.switch_to.window(handle)
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("password").send_keys("password")

driver.switch_to.window(baidu_index_handle)
