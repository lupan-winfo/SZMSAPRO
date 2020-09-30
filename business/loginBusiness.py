#coding=utf-8
from handle.loginHandle import LoginHandle
'''
author:lupan
remark:业务层，进行业务逻辑的封装
'''
class LoginBusiness(object):
    def __init__(self,driver):
        self.loginH = LoginHandle(driver);

    # 封装共有公共方法
    def common_operation(self,username,pwd,pwdIcon,remPwd,status):
        # 输入用户名
        self.loginH.set_username_value(username)
        # 输入密码
        self.loginH.set_pwd_value(pwd)
        # 点击密码显示/隐藏
        if pwdIcon:
            self.loginH.set_pwdIcon_btn()
        # 勾选记住密码
        if remPwd:
            self.loginH.set_rememberPwd_btn()
        # 点击登录
        if status:
            self.loginH.set_login_btn()

    # 执行登录操作
    def login_function(self,username,pwd,pwdIcon,remPwd,status,error,error_info):
        self.common_operation(username,pwd,pwdIcon,remPwd,status)
        if error == "user_pwd":
            if self.loginH.set_error_info(error,error_info) == "请完整输入用户名/密码":
                return True
            else:
                return False
        elif error == "alert_msg":
            if self.loginH.set_error_info(error,error_info):
                return  True
            else:
                return False
        elif error == "pwdIcon":
            if self.loginH.set_error_info(error,error_info) == "text":
                return True
            else:
                return False
        elif error == "checkedPwd":
            if self.loginH.set_error_info(error,error_info):
                return True
            else:
                return False
        elif error == "loginBtn":
            if self.loginH.set_error_info(error,error_info) != None:
                return True
            else:
                return False






