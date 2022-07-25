mydb=mysql.connector.connect(   #establishing connection with database
        host="localhost",
        user="root",
        password="",
        database="inventory")
        mycursor=mydb.cursor()
        mycursor.execute("select * from users")