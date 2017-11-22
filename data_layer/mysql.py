# import libaray
import MySQLdb

# connect to db
db = MySQLdb.connect(host="localhost",
    user="db_user", passwd="db_pass", db="db_name", charset="utf8")

cursor = db.cursor()

# excute sql statement
cursor.execute("SELECT * FROM db_table")

# fetch result
results = cursor.fetchall()
count = cursor.rowcount

# output result data 1
for record in results:
    col1 = record[0]
    col2 = record[1]
    print "%s, %s" % (col1, col2)


# output result data 2 
for i in range(0, count):
    record = cursor.fetchone()
    col1 = record[0]
    col2 = record[1]
    print "%s, %s" % (col1, col2)


# close connection
db.close()
