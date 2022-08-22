# Ctrl+B to run in Sublime Text 3
import mysql.connector
import SupportingFunctions
import ConnectionURLs

mydb = mysql.connector.connect(host=ConnectionURLs.mysql_host, user=ConnectionURLs.mysql_user, password=ConnectionURLs.mysql_password, auth_plugin=ConnectionURLs.mysql_auth_plugin, database=ConnectionURLs.mysql_database)

myCursor = mydb.cursor()
# myCursor.execute("select * from data_table")

populator = SupportingFunctions.GenericDatabasePopulator()

values = populator.generate(2, True) # Working on this.

sql = "INSERT INTO data_table (place, num, first_name, last_name) VALUES (%s, %s, %s, %s)"

myCursor.executemany(sql, values)

mydb.commit()

print(myCursor.rowcount, "was inserted.") 