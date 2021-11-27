import MySQLdb
db=MySQLdb.connect(host="localhost", user="root", password="w123741852", db="filedata")
cur=db.cursor()
cur.execute("select * from Type")
# 該資料庫 (schema)的權限必須開放select (custom)給該user
for emp in cur.fetchall():
    print(emp)