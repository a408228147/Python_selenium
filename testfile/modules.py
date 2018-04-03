class BaiDu:
    #初始化
    def __init__(self, driver):
        self.driver = driver

    def search(self, search_key):
        driver = self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(search_key)
        driver.find_element_by_id("su").click()

    def close(self):
        driver = self.driver
        driver.quit()


class email:
    def __init__(self, dirver):
        self.dirver = dirver

    def login(self,login_name_key,login_pwd_key):
        dirver = self.dirver
        dirver.switch_to.frame('x-URS-iframe')
        dirver.find_element_by_name("email").clear()
        dirver.find_element_by_name("email").send_keys(login_name_key)
        dirver.find_element_by_name("password").clear()
        dirver.find_element_by_name("password").send_keys(login_pwd_key)
        dirver.switch_to.default_content()

    def close(self):
        dirver = self.dirver
        dirver.quit()

