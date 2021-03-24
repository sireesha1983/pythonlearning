import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                         database='sakila',
                                         user='root',
                                         password='password@123')
def conn_db():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("select * from sakila.actor;")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

conn_db()
connection.close()




