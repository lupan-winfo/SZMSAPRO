#coding=utf-8
from selenium import webdriver
from util.read_ini import Read_ini
class FindElement(object):
    # 构造函数
    def __init__(self,filename=None,node=None,driver=None):
        self.filename = filename
        self.node = node
        self.driver = driver

    # 对selenium进行二次封装，获取元素的方法
    def get_element(self,key):
        read_ini = Read_ini(self.filename,self.node)
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "className":
                return self.driver.find_element_by_class_name(value)
            elif by == "classNames":
                return self.driver.find_elements_by_class_name(value)
            elif by == "tagName":
                return self.driver.find_element_by_tag_name(value)
            elif by == "cssSelect":
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None