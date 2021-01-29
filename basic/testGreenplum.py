import psycopg2
import psycopg2.extras
import time

'''
    连接数据库
    returns:db
'''
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
    print(conn)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    # 这里创建的是一个字典Cursor, 这样返回的数据, 都是字典的形式, 方便使用
    ret = cur.execute("CREATE TABLE public.gp_test (id serial PRIMARY KEY, num integer, data varchar);")
    conn.commit()
    # 提交到数据库中
    print(ret)
    ret = cur.execute("INSERT INTO public.gp_test (num, data) VALUES (%s, %s);",(300, "abc'def"))

    conn.commit()
    # 提交到数据库中
    print(cur.rowcount)  # 1
    # 返回数据库中的行的总数已修改，插入或删除最后 execute*().

    ret_sql = cur.mogrify("select * from pg_tables where tablename = %s;", ('gp_test',))
    # 返回生成的sql脚本, 用以查看生成的sql是否正确.
    # sql脚本必须以;结尾, 不可以省略.其次, 不管sql中有几个参数, 都需要用 % s代替, 只有 % s, 不管值是字符还是数字, 一律 % s.
    # 最后, 第二个参数中, 一定要传入元组, 哪怕只有一个元素, 像我刚才的例子一样, ('gp_test')这样是不行的.
    print(ret_sql.decode('utf-8'))  # select * from pg_tables where tablename = E'gp_test';

    cur.execute("select * from gp_test where num = %s;", (300,))
    pg_obj = cur.fetchone()
    print(pg_obj) # {'id': 1, 'num': 300, 'data': "abc'def"}

    conn.close() # 关闭连接