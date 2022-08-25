import pymongo
from pymongo import MongoClient
import mysql.connector
import time
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

def insert_all():
    start = time.time()
    mongo_insert.insert_documents(collection, mongo_data)
    mysql_insert.insert_many(mysql_data, myCursor, mysql_db)
    end = time.time()
    print("Total Insertion Time: ", end-start)

def delete_all():
    start = time.time()
    mysql_delete.delete_all(myCursor, mysql_db)
    mongo_delete.delete_all(collection)
    end = time.time()
    print("Total Delete Time: ", end-start)

def main():
    print("\nMain Begin\n")
    insert_all()
    print()
    delete_all()
    print("\nMain End\n")
    # print(mysql_data)
    # print(mongo_data)
    # mysql_insert.insert_many(values, myCursor, mydb)

if __name__ == "__main__":
    main()

### Size = 1000000
### Mongo Insert All Time:   12.36253571510315
### MySQL Insert All Time:  122.42020583152771
### Total Insertion Time:   134.78274154663086

### MySQL Delete All Time:   4.777234077453613
### Mongo Delete All Time:  26.815054893493652
### Total Deletion Time:    31.592288970947266