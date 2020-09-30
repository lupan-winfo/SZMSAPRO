#coding=utf-8
import cx_Oracle
db = cx_Oracle.connect('msaoss','msaoss','192.168.0.160:1521/msaoss')
cur = db.cursor()
sql = "SELECT * FROM users"
cur.execute(sql)
ad = cur.fetchmany(8)
print(type(ad))
print(len(ad))
print(ad)


'''
# 有参数
sql = "SELECT * FROM users WHERE user_id = :id"
param = {"id":'460022197307290010'}
cur.execute(sql,param)
ad = cur.fetchall()
print(type(ad))
print(ad)
'''

'''
# 更新
sql = "update users set user_name = '吕青' where user_id = '460022197307290010'"
cur.execute(sql)
'''
cur.close()
db.commit()
db.close