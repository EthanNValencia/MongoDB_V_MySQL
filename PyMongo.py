# Ctrl+B to run in Sublime Text 3
import pymongo
from pymongo import MongoClient
import SupportingFunctions
import ConnectionURLs

cluster = MongoClient(ConnectionURLs.mongodb_url)
db = cluster["test"]
collection = db["database"]

# print(type(collection))

populator = SupportingFunctions.MongoDatabasePopulator();
deleting = SupportingFunctions.MongoDeleteOperations();
printing = SupportingFunctions.MongoPrintOperations();
finding = SupportingFunctions.MongoFindOperations();

printing.printCollectionCount(collection)

documents = populator.generateDocuments(1000) # Generates the data documents. 
populator.insertDocuments(collection, documents)


# printing.printCollection(newCollection)

# collection.insert_one(document1) # inserts one document

# collection.insert_many([document1, document2]) # inserts two documents

results = finding.findDocuments({"first_name":"Abraham"}, collection)

# printing.printResultsSize(results)

# printing.printResults(results) # This isn't useful when dealing with large result sets. 

printing.printResultsSize(results)

# results = collection.find({"first_name":"Abraham", "last_name":"Lincoln"})

# results = collection.find({"first_name":"Fred"})

# deleting.deleteResults(collection, results)

deleting.deleteAll(collection)