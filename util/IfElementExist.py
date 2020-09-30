#coding=utf-8
'''
@author lupan
remark:通过传入定位方式和定位元素判定当前页面元素是否加载成功；成功则返回True，否则返回False
'''
class IfElementExist(object):

    def __init__(self,by=None,element=None,driver=None):
        self.driver = driver
        self.IsElementExits(by,element)

    def IsElementExits(self,by,element):
        flag = True
        try:
            if by == '':
                self.driver.find_element_by_id(element)
                return flag
            elif by == "name":
                self.driver.find_element_by_name(element)
                return flag
            elif by == "className":
                self.driver.find_element_by_class_name(element)
                return flag
            elif by == "classNames":
                self.driver.find_elements_by_class_name(element)
                return flag
            elif by == "tagName":
                self.driver.find_element_by_tag_name(element)
                return flag
            elif by == "cssSelect":
                self.driver.find_element_by_css_selector(element)
                return flag
            else:
                return flag
        except:
            flag = False
            return flag