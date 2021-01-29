import unittest
import psycopg2
import psycopg2.extras
import pandas as pd

import numpy as np

def gp_connect():
    try:
        db = psycopg2.connect(dbname="postgres",
                              user="gpadmin",
                              password="gpadmin",
                              host="192.168.123.22",
                              port="5432")
        # connect()也可以使用一个大的字符串参数,
        # 比如”host=localhost port=5432 user=postgres password=postgres dbname=test”
        return db
    except psycopg2.DatabaseError as e:
        print("could not connect to Greenplum server",e)

if __name__ == '__main__':


    conn = gp_connect()
    cur = conn.cursor()
  #  cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select sjsl_z from T_JS_SJ_ZQ_FQTFSJYLDJSLXX;", ())

    #单条处理
    pg_obj = cur.fetchall()
    pg_arry = np.asarray(pg_obj)
    print(pg_arry) # {'id': 1, 'num': 300, 'data': "abc'def"}
    print(np.mean(pg_arry))
    print(pd.asarray(pg_obj))

    # print("开始循环")
    # count=0
    # while True:
    #     count = count + 1
    #     # 每次获取时会从上次游标的位置开始移动size个位置，返回size条数据
    #     data = cur.fetchmany(1)
    #     # 数据为空的时候中断循环
    #     if not data:
    #         break
    #     else:
    #         print(data)  # 得到最后一条(通过元祖方式返回)


    conn.close() # 关闭连接

