#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: yanyongjun
@file: mysqlUtil.py
@time: 2017/06/27
"""

import MySQLdb


def insert_many_database(sql, param):
    db = MySQLdb.connect("localhost", "root", "123456", "data", charset='utf8')
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.executemany(sql, param)
        # 提交到数据库执行
        cursor.close()
        db.commit()
    except Exception as e:
        print e
        db.rollback()
    # 关闭数据库连接
    db.close()


def insert_database(sql, param=None):
    db = MySQLdb.connect("localhost", "root", "123456", "data", charset='utf8')
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql, param)
        # 提交到数据库执行
        cursor.close()
        db.commit()
    except Exception as e:
        print e
        db.rollback()
    # 关闭数据库连接
    db.close()

# if __name__ == '__main__':
#     sql="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#     inster_database(sql)
