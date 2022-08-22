# Ctrl+B to run in Sublime Text 3
import pymongo
from pymongo import MongoClient
import SupportingFunctions
import ConnectionURLs

cluster = MongoClient(ConnectionURLs.mongodb_url)
db = cluster["test"]
collection = db["database"]

generator = SupportingFunctions.GenericDataGenerator()

insert = SupportingFunctions.MongoInsertOperations()
delete = SupportingFunctions.MongoDeleteOperations()
console = SupportingFunctions.MongoPrintOperations()
find = SupportingFunctions.MongoFindOperations()

console.print_collection_count(collection)

documents = generator.generate(10, False) # Generates the data documents. 
insert.insert_documents(collection, documents)

results = find.find_documents({"first_name":"Abraham"}, collection)

console.print_results_size(results)

delete.delete_all(collection)

# Syntax Examples 

# print(type(collection))

# console.print_collection(newCollection)

# collection.insert_one(document1) # inserts one document

# collection.insert_many([document1, document2]) # inserts two documents

# console.print_results_size(results)

# console.print_results(results) # This isn't useful when dealing with large result sets. 

# results = collection.find({"first_name":"Abraham", "last_name":"Lincoln"}) 

# results = collection.find({"first_name":"Fred"})

# delete.delete_results(collection, results)