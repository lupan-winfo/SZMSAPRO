#coding=utf-8
import configparser
import os
# 读取配置文件思路：通过导入扩展包configparser
# 将配置文件转换为对象
class Read_ini(object):
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = os.path.join(os.path.abspath('..') + "/config/" + "GlobalElement.ini")
        else:
            self.file_name = file_name
        if node == None:
            self.node = "loginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    # 加载配置文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data
if __name__ == '__main__':
    file_name = os.path.join(os.path.abspath('..') + "/config/" + "GlobalElement.ini")
    node = "loginElement"
    r = Read_ini(file_name,node)
    s = r.get_value('user_pwd')
    print(s)