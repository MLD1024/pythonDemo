import MySQLdb
conn = MySQLdb.connect(host='172.16.50.135',port=4000,user='shtelecom_query',passwd='c7K2TWGRW1hyMMccSZG6WUNy6sWoBj',db='telecom-wx')
cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
cursor.execute('SELECT  a.openid, a.deviceno, a.crmid FROM dx_weixin_bind a where a.crmid = %s AND a.status = 100',('202134233792'))
r = cursor.fetchall()
for r in r:
    print r
cursor.close()
conn.close()