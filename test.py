from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("郑浩强")
driver.find_element_by_css_selector("span.bg.s_btn_wr input#su").click()
for i in range(1,11):
    if "_百度搜索" in driver.title:
       break
    else:
     sleep(0.5)
else:
    raise NameError("time out,title no displa")

assert driver.title == "selenium_百度搜索"

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

driver.close()


