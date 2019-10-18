import MySQLdb
import csv
import codecs


def get_conn():
    db = MySQLdb.connect(host='172.16.50.145', port=4000, user='shtelecom_query',
                         passwd='c7K2TWGRW1hyMMccSZG6WUNy6sWoBj', db='telecom-wx')
    return db


def execute_all(cursor, sql, args):
    cursor.execute(sql, args)
    return cursor.fetchall()


def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        conn = get_conn()
        cur = conn.cursor()
        sql = 'select * from  dx_weixin_bind limit 10'
        results = execute_all(cursor=cur, sql=sql, args=None)
        for result in results:
            print(result)
            write.writerow(result)


if __name__ == '__main__':
    read_mysql_to_csv(r"D:\results4.csv")
