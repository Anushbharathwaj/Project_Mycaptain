import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTEL (NAME TEXT ,ADDRESS TEXT,PRICE INTEGER, RATING INTEGER ,AMENITIES TEXT)")
    conn.commit()
    conn.close()

def insert_into_values(dbname,values):
    conn = sqlite3.connect(dbname)
    print("inserted values"+ str(values))
    conn.execute("INSERT INTO OYO_HOTEL (NAME,ADDRESS,PRICE,RATING,AMENITIES)VALUES(?,?,?,?,?)",values)
    conn.commit()
    conn.close()
def get_all_values(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM OYO_HOTEL")
    table_oyo = cursor.fetchall()
    for table in table_oyo:
        print(table)

    conn.close()

