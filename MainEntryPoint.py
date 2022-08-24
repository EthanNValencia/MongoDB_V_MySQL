import pymongo
from pymongo import MongoClient
import mysql.connector
import SupportingFunctions
import ConnectionURLs

data = SupportingFunctions.GenericDataGenerator()
size = 1000
mysql_data = data.generate(size, True)
mongo_data = data.generate(size, False)

mysql_db = mysql.connector.connect(host=ConnectionURLs.mysql_host, user=ConnectionURLs.mysql_user, password=ConnectionURLs.mysql_password, auth_plugin=ConnectionURLs.mysql_auth_plugin, database=ConnectionURLs.mysql_database)
myCursor = mysql_db.cursor()
mysql_insert = SupportingFunctions.MySQLInsertOperations()
mysql_delete = SupportingFunctions.MySQLDeleteOperations()
mysql_find = SupportingFunctions.MySQLFindOperations()

cluster = MongoClient(ConnectionURLs.mongodb_url)
db = cluster["test"]
collection = db["database"]
mongo_insert = SupportingFunctions.MongoInsertOperations()
mongo_delete = SupportingFunctions.MongoDeleteOperations()
mongo_console = SupportingFunctions.MongoPrintOperations()
mongo_find = SupportingFunctions.MongoFindOperations()

def main():
    print("Main Begin")
    mongo_insert.insert_documents(collection, mongo_data)
    mysql_insert.insert_many(mysql_data, myCursor, mysql_db)
    
    mysql_delete.delete_all(myCursor, mysql_db)
    mongo_delete.delete_all(collection)
    print("Main End")
    # print(mysql_data)
    # print(mongo_data)
    # mysql_insert.insert_many(values, myCursor, mydb)

if __name__ == "__main__":
    main()