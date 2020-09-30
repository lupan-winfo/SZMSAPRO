#coding=utf-8
from selenium import webdriver
import time
import os
import unittest
import ddt
import HTMLTestRunner
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class TTTT(unittest.TestCase):
    def setUp(self):
        url = 'http://47.106.167.97/#/'
        self.driver = self.get_driver(url)

    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def tearDown(self):
        self.driver.close()

    @ddt.data(*data)
    def testSavaPic(self,data):
        username,pwd,mmsi = data
        pngName = str(mmsi)
        self.driver.find_element_by_id('normal_login_username').send_keys(username)
        self.driver.find_element_by_id('normal_login_password').send_keys(pwd)
        self.driver.find_element_by_class_name('login-form-button').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('ant-select-search__field').clear()
        self.driver.find_element_by_class_name('ant-select-search__field').send_keys(pngName)
        self.driver.find_element_by_css_selector('.ant-btn.ant-btn-primary.ant-btn-lg').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="modals-container"]/div/div/div[2]/div/div[2]/button[2]').click()
        self.driver.find_elements_by_class_name('ant-calendar-range-picker-input')[0].click()
        self.driver.find_elements_by_class_name('ant-calendar-input ')[0].clear()
        self.driver.find_elements_by_class_name('ant-calendar-input ')[0].send_keys('2020-08-01 00:00:00')
        time.sleep(3)
        self.driver.find_elements_by_class_name('ant-calendar-input ')[1].clear()
        self.driver.find_elements_by_class_name('ant-calendar-input ')[1].send_keys('2020-09-01 23:59:59')
        self.driver.find_element_by_class_name('ant-calendar-ok-btn').click()
        self.driver.find_element_by_class_name('saveBtn').click()
        self.driver.implicitly_wait(8)
        flag = self.isElementExist('className','f-track-button')
        if flag:
            self.driver.find_element_by_class_name('f-track-button').find_elements_by_tag_name('i')[0].click()
            self.file_path = os.path.join(os.path.abspath('..') + "/Image/" + pngName + ".png")
            self.driver.save_screenshot(self.file_path)
            self.assertTrue(True)
        else:
            self.file_path = os.path.join(os.path.abspath('..') + "/Image/" + pngName + ".png")
            self.driver.save_screenshot(self.file_path)
            self.assertTrue(False)

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


if __name__ == '__main__':
    path = os.path.abspath('..') + "/test/"
    file_path = os.path.join(os.path.abspath('..') + "/report/" + "savaPng.html")
    f = open(file_path, 'wb')
    # 数据驱动构建用例集
    suite = unittest.defaultTestLoader.discover(path,"t*.py")
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is save Picture", description=u"图片截图报告",
                                           verbosity=2)
    runner.run(suite)