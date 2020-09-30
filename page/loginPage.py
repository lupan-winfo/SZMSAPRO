#coding=utf-8
from base.findelement import FindElement
import os
'''
author:lupan
remark:page层，针对页面元素进行相应操作，实现页面元素与数据分离
'''
class LoginPage(object):
    def __init__(self,driver):
        file_name = os.path.join(os.path.abspath('..') + "/config/" + "GlobalElement.ini")
        node = "loginElement"
        self.driver = driver
        self.fe = FindElement(file_name,node,driver)

    # 获取用户名元素
    def get_username_element(self):
        return self.fe.get_element("user_pwd")[0]

    # 获取密码框元素
    def get_pwd_element(self):
        return self.fe.get_element("user_pwd")[1]

    # 获取密码框显示/隐藏标识元素
    def get_pwdIcon_element(self):
        return self.fe.get_element("pwdIcon")

    # 获取错误提示信息
    def get_errormsg_element(self):
        return self.fe.get_element("error_msg")

    # 获取记住密码复选框元素
    def get_rememberPwd_element(self):
        return self.fe.get_element("rememberPwd")

    # 获取记住密码选框选中状态
    def get_checkedPwd_element(self):
        return self.fe.get_element("checkedPwd")

    # 获取登录按钮元素
    def get_loginBtn_element(self):
        return self.fe.get_element("loginBtn")

    # 获取用户名错误或密码错误弹框元素
    def get_alertmsg_element(self):
        self.driver.implicitly_wait(8)
        return self.fe.get_element("alert_msg")

