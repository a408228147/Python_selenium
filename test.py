from telnetlib import EC

from selenium import webdriver
from time import sleep, ctime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.set_window_size(100,200)
driver.maximize_window()
#调用js
js = "windows.scrollTo(400,400)"
driver.execute_script(js)

#显式等待 单个元素
element = WebDriverWait(driver,5,0.5).unitl(
            EC.presence_of_element_located((By.ID,"KW"))
)
element.send_keys("qweq")

for i  in range(10):
    try:
        el= driver.find_element_by_id("kw")
        if el.is_displayed():
            break
    except:pass
else:
    print("time out")
#切换表单 嵌套页面
driver.switch_to.frame("xxxx")#id/name

#退出表单
driver.switch_to.default_content()
#隐式等待 当前页面所有元素
driver.implicitly_wait(10)
driver.get("www.baidu.com")
#截图
driver.get_screenshot_as_file("D://")

try:
     print(ctime())
     driver.find_element_by_id("kw").send_keys("qw")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())

driver.find_element_by_id("kw").send_keys("郑浩强")#输入
driver.find_element(By.ID,"kw").send_keys()
driver.find_element(By.CLASS_NAME)
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)#删除
driver.find_element_by_id("kw").send_keys(Keys.SPACE)#空格
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')#全选 x 剪切 c v
driver.find_element_by_id("kw").send_keys(Keys.ENTER)#回车
driver.find_element_by_id("kw").size
driver.find_element_by_id("kw").text#断言常用方法
driver.find_element_by_id("kw").get_attribute("maxlength")#获取属性
driver.find_element_by_id("kw").is_displayed()#是否可见 返回true false
driver.find_element_by_css_selector("span.bg.s_btn_wr input#su").click()
driver.find_element(By.CSS_SELECTOR)
for i in range(1,11):
    if "_百度搜索" in driver.title:#页面标题
       break
    else:
     sleep(0.5)
else:
    raise NameError("time out,title no displa")
assert driver.title == "selenium_百度搜索"#断言失败 下面就不执行  验证失败 仍可以继续


for i in range(1,11):
    title = driver.find_element_by_xpath("//div["+str(i)+"]//h3//a")
    print(title.text)
    assert "elenium" in title.text

driver.find_element_by_xpath("//img[@title='到百度首页']").click()

above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_link_text("搜索设置").click()

sel = driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value("20")
sleep(2)
driver.find_element_by_class_name("prefpanelgo").click()
alert_text = driver.switch_to.alert.text
print(alert_text)
driver.switch_to.alert.accept()
driver.back()#页面倒退
driver.forward()#页面前进
driver.refresh()#页面刷新

driver.close()


