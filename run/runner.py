#coding=utf-8
from selenium import webdriver
from util.cread_file import CreadFlie
import unittest
import HTMLTestRunner
import os
class RunCase(unittest.TestCase):
    def test_case001(self):
        path = os.path.abspath('..') + "/report/"
        filename = "szCase"
        cd = CreadFlie(path, filename)
        f = open(cd.creatName(), 'wb')
        # 获取当前文件的路径。其中os.getcwd()是获取当前工作目录
        case_path = os.path.abspath('..') + "/case/"
        suite = unittest.defaultTestLoader.discover(case_path,'loginCase*.py')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is SZPro UI automation report", description=u"基础产品PC端登录服务测试报告",
                                               verbosity=2)
        runner.run(suite)
        f.close()

if __name__ == '__main__':
    unittest.main()