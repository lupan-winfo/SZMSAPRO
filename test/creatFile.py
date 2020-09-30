#coding=utf-8
import time
import os
from util.cread_file import CreadFlie
# 将指定格式的当前时间以字符串输出
path = os.path.abspath('..') + "/report/"
filename = "loginCase"
cd = CreadFlie(path,filename)
print(cd.creatName())