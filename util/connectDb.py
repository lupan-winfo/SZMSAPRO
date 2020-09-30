#coding=utf-8
import cx_Oracle
'''
author:lupan
remark:封装数据库
'''
class ConnectDb():
    # 初始化oracle链接
    def __init__(self,username=None,password=None,host=None,port=None,sid=None):
        # 连接数据
        # 用户名、密码、监听分开写
        self.db = cx_Oracle.connect(username,password,host+":"+port+"/"+sid)
        # 创建游标
        self.cur = self.db.cursor()

    # 查询，不带参数，返回一行
    def Ora_Select_one(self,strsql):
        self.cur.execute(strsql)
        data =  self.cur.fetchon()
        self.cur.close()
        return data

    # 查询，不带参数，返回多行
    def Ora_Select_many(self, strsql,line):
        self.cur.execute(strsql)
        data = self.cur.fetchmany(line)
        self.cur.close()
        return data

    # 查询，不带参数，返回所有数据
    def Ora_Select_all(self,strsql):
        self.cur.execute(strsql)
        data = self.cur.fetchall()
        self.cur.close()
        return data

