# Ctrl+B to run in Sublime Text 3
# Purpose: The purpose of this class is develop the MySQL-side as an independent entry point. 
import mysql.connector
import SupportingFunctions
import ConnectionURLs

mydb = mysql.connector.connect(host=ConnectionURLs.mysql_host, user=ConnectionURLs.mysql_user, password=ConnectionURLs.mysql_password, auth_plugin=ConnectionURLs.mysql_auth_plugin, database=ConnectionURLs.mysql_database)

myCursor = mydb.cursor()
# myCursor.execute("select * from data_table")

generate = SupportingFunctions.GenericDataGenerator()
insert = SupportingFunctions.MySQLInsertOperations()
delete = SupportingFunctions.MySQLDeleteOperations()
find = SupportingFunctions.MySQLFindOperations()

values = generate.generate(20, True) # Working on this.

insert.insert_many(values, myCursor, mydb)

results = find.select_last_name('Washington', myCursor)

delete.delete_all(myCursor, mydb)