import pymysql

conn = pymysql.connect(
    host='sql12.freesqldatabase.com',
    user='sql12671900',
    password='PHXcBpVhjL',
    database='sql12671900',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


cursor = conn.cursor()

sql_querry = """ CREATE TABLE book(
    id INTEGER PRIMARY KEY,
    author TEXT NOT NULL,
    language TEXT NOT NULL,
    title TEXT NOT NULL
)
"""

cursor.execute(sql_querry)
conn.close()