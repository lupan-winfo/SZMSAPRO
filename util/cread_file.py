#coding=utf-8
import os
import time
class CreadFlie(object):
    def __init__(self,path,file_name):
        self.file_name = file_name
        self.path = path
        self.newfile = self.creatName()
        self.cread(self.newfile)

    # 文件生成%H%M%S
    def creatName(self):
        t = time.strftime('%Y%m%d',time.localtime())
        suffix = ".html"
        newFileName =  self.file_name + "_" + t + suffix
        newfile = os.path.join(self.path + newFileName)
        return newfile


    # 文件创建
    def cread(self,newfile):
        if not os.path.exists(newfile):
            f = open(newfile,'wb')
            f.close()
        else:
            return None