#coding=utf-8
from selenium import webdriver
import time
url = 'http://47.106.167.97/#/'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element_by_id('normal_login_username').send_keys('test02')
driver.find_element_by_id('normal_login_password').send_keys('123456')
driver.find_element_by_class_name('login-form-button').click()
time.sleep(5)
driver.find_element_by_class_name('ant-select-search__field').clear()
driver.find_element_by_class_name('ant-select-search__field').send_keys('413906777')
driver.find_element_by_css_selector('.ant-btn.ant-btn-primary.ant-btn-lg').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="modals-container"]/div/div/div[2]/div/div[2]/button[2]').click()
driver.find_elements_by_class_name('ant-calendar-range-picker-input')[0].click()
driver.find_elements_by_class_name('ant-calendar-input ')[0].clear()
driver.find_elements_by_class_name('ant-calendar-input ')[1].clear()
# driver.find_elements_by_class_name('ant-calendar-input ')[0].send_keys('2020-08-01 00:00:00')
# driver.find_elements_by_class_name('ant-calendar-input ')[1].send_keys('2020-09-01 23:59:59')

'''
 # 判断元素是否存在
    def isElementExist(self,by,element):
        flag = True
        browser = self.driver
        try:
            if by == "id":
                browser.find_element_by_id(element)
                return flag
            elif by == "name":
                browser.find_element_by_name(element)
                return flag
            elif by == "className":
                browser.find_element_by_class_name(element)
                return flag
            elif by == "classNames":
                browser.find_elements_by_class_name(element)
                return flag
            elif by == "tagName":
                browser.find_element_by_tag_name(element)
                return flag
            elif by == "cssSelect":
                browser.find_element_by_css_selector(element)
                return flag
            else:
                return flag
        except:
            flag = False
            return flag
'''
