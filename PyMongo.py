# Ctrl+B to run in Sublime Text 3
import pymongo
from pymongo import MongoClient
import SupportingFunctions
import ConnectionURLs

cluster = MongoClient(ConnectionURLs.mongodb_url)
db = cluster["test"]
collection = db["database"]

generator = SupportingFunctions.GenericDatabasePopulator()

inserting = SupportingFunctions.MongoInsertOperations()
deleting = SupportingFunctions.MongoDeleteOperations()
printing = SupportingFunctions.MongoPrintOperations()
finding = SupportingFunctions.MongoFindOperations()

printing.printCollectionCount(collection)

documents = generator.generate(10, False) # Generates the data documents. 
inserting.insertDocuments(collection, documents)

results = finding.findDocuments({"first_name":"Abraham"}, collection)

printing.printResultsSize(results)

deleting.deleteAll(collection)


# Syntax Examples 

# print(type(collection))

# printing.printCollection(newCollection)

# collection.insert_one(document1) # inserts one document

# collection.insert_many([document1, document2]) # inserts two documents

# printing.printResultsSize(results)

# printing.printResults(results) # This isn't useful when dealing with large result sets. 

# results = collection.find({"first_name":"Abraham", "last_name":"Lincoln"}) 

# results = collection.find({"first_name":"Fred"})

# deleting.deleteResults(collection, results)