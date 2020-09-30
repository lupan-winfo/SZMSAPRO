#coding=utf-8
from page.loginPage import LoginPage
'''
author:lupan
remark:handle层，进行页面元素数据操作步骤的封装
'''
class LoginHandle(object):
    def __init__(self,driver):
        self.loginP = LoginPage(driver)

    # 输入用户名
    def set_username_value(self,username):
        return self.loginP.get_username_element().send_keys(username)

    # 输入密码
    def set_pwd_value(self,pwd):
        return self.loginP.get_pwd_element().send_keys(pwd)

    # 点击密码框显示/隐藏
    def set_pwdIcon_btn(self):
        return self.loginP.get_pwdIcon_element().click()

    # 记住密码复选框勾选或取消
    def set_rememberPwd_btn(self):
        return self.loginP.get_rememberPwd_element().click()

    # 点击登录按钮
    def set_login_btn(self):
        return self.loginP.get_loginBtn_element().click()

    # 获取用户名或密码错误弹框元素
    def set_alertmsg_exit(self):
        return self.loginP.get_alertmsg_element()

    # 获取错误信息
    def set_error_info(self,error,error_info):
        try:
            # 验证用户名或密码为空
            if error == "user_pwd":
                text = self.loginP.get_errormsg_element().text
            # 验证用户名或密码错误
            elif error == "alert_msg":
                text = self.loginP.get_alertmsg_element()
            # 验证密码显示/隐藏
            elif error == "pwdIcon":
                text = self.loginP.get_pwd_element().get_attribute('type')
            # 验证记住密码
            elif error == "checkedPwd":
                text = self.loginP.get_checkedPwd_element()
            # 登录成功
            elif error == "loginBtn":
                text = self.loginP.get_loginBtn_element()
            else:
                text = None
            return text
        except:
            return None