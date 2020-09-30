#coding=utf-8
from selenium import webdriver
from business.loginBusiness import LoginBusiness
from util.cread_file import CreadFlie
import unittest
import os
import time
import ddt
import HTMLTestRunner
@ddt.ddt
class LoginCase(unittest.TestCase):

    def setUp(self):
        url = "http://192.168.0.176:1234/WebGIS/index.html#/login"
        self.driver = self.get_driver(url)
        self.loginB = LoginBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        # 判断当前case是否存在错误，语法为固定语法，其中method_name不用使用，直接传即可
        # self._outcome.errors获取当前错误信息，返回为一个集合，所以需要for循环去取值
        for method_name,error in self._outcome.errors:
            if error:
                # 获取当前case名字
                case_name = self._testMethodName
                # 文件路径
                file_path = os.path.join(os.path.abspath('..') + "/Image/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # 开启浏览器
    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 封装的登录case
    @ddt.data(
        ['卢攀', '', False, False, True, 'user_pwd','请完整输入用户名/密码'],
        ['', '123456', False, False, True, 'user_pwd','请完整输入用户名/密码'],
        ['卢攀', '123456', True, True, True, 'loginBtn', '请完整输入用户名/密码']
    )
    @ddt.unpack
    def test_login_case(self,username,pwd,pwdIcon,remPwd,status,error,error_info):
        result = self.loginB.login_function(username,pwd,pwdIcon,remPwd,status,error,error_info)
        self.assertTrue(result)

# if __name__ == '__main__':
#     path = os.path.abspath('..') + "/report/"
#     filename = "LoginCase"
#     cd = CreadFlie(path,filename)
#     f = open(cd.creatName(), 'wb')
#     # 数据驱动构建用例集
#     suite = unittest.TestLoader().loadTestsFromTestCase(LoginCase)
#     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="基础产品PC端-登录", description=u"基础产品PC端登录服务测试报告",
#                                            verbosity=2)
#     runner.run(suite)
#     f.close()