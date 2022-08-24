import pymongo
from pymongo import MongoClient
import mysql.connector
import SupportingFunctions
import ConnectionURLs

mysql_db = mysql.connector.connect(host=ConnectionURLs.mysql_host, user=ConnectionURLs.mysql_user, password=ConnectionURLs.mysql_password, auth_plugin=ConnectionURLs.mysql_auth_plugin, database=ConnectionURLs.mysql_database)
myCursor = mysql_db.cursor()
mysql_generate = SupportingFunctions.GenericDataGenerator()
mysql_insert = SupportingFunctions.MySQLInsertOperations()
mysql_delete = SupportingFunctions.MySQLDeleteOperations()
mysql_find = SupportingFunctions.MySQLFindOperations()

cluster = MongoClient(ConnectionURLs.mongodb_url)
db = cluster["test"]
collection = db["database"]
generator = SupportingFunctions.GenericDataGenerator()
mongo_insert = SupportingFunctions.MongoInsertOperations()
mongo_delete = SupportingFunctions.MongoDeleteOperations()
mongo_console = SupportingFunctions.MongoPrintOperations()
mongo_find = SupportingFunctions.MongoFindOperations()

def main():
    values = mysql_generate.generate(20, True)
    mysql_insert.insert_many(values, myCursor, mydb)
    results = mysql_find.select_last_name('Washington', myCursor)

if __name__ == "__main__":
    main()