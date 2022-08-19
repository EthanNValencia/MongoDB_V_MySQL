import time
from random import seed
from random import random

class MongoDeleteOperations:

	def deleteResults(self, collection, results):
		for result in results:
			print("Deleting: ", result)
			start = time.time()
			collection.delete_one({"_id": result["_id"]})
			end = time.time()
			print("Document deleted from MongoDB. Time: ", end-start)

	def deleteAll(self, collection):
		print("Deleting all documents from MongoDB...")
		start = time.time()
		collection.delete_many({})
		end = time.time()
		print("All documents deleted. Time: ", end-start)

class MongoPrintOperations:

	def printResults(self, results):
		for result in results:
			print(result)
			print(result["_id"])

	def printCollection(self, collection):
		for item in collection:
			print(item)

	def printResultsSize(self, results):
		counter = 0
		print("Counting the result set...")
		start = time.time()
		for result in results:
			counter += 1
		end = time.time()
		print("Result set has been counted. Time: ", end-start)
		print("Total size of the returned result set is: ", counter)

	def printCollectionCount(self, collection):
		post_count = collection.count_documents({})
		print("Results size is: ", post_count)


class GenericDatabasePopulator:

	mysql_data = []
	mongodb_data = []
	# firstNames and lastNames are selected using a random function. The idea is to generate pseudo-unique data that is readily queryable. 
	firstNames = ['George','John','Thomas','James','John','Andrew','Zachary','Millard','Franklin','Abraham']
	lastNames = ['Washington','Adams','Jefferson','Madison','Monroe','Jackson','Tyler','Polk','Taylor','Fillmore']

	# TO-DO
	# I want to make this generic so that it returns a different dataset depending on the parameters.
	# Also, maybe I should think about storing the data in such a way that allows me to use the exact same data in both database.
	def generateDocuments(self, size, isSQL):
		values = []
		if len(self.mysql_data) != size or len(self.mongodb_data) != size: # Objective: Only generate the data if it does not match the size or is empty. 
			self.populateDataArrays(size)
		if isSQL is True:
			return self.mysql_data;
		if isSQL is False:
			return self.mongodb_data;

	def populateDataArrays(self, size): # I only want this method to be called if data has not been generated or if the size of the data structure does not match the size parameter. 
		print("Beginning generation of documents...")
		start = time.time()
		for x in range(size):
			place = x
			num = int(random()*1000)
			firstName = self.firstNames[int(random()*10)]
			lastName = self.lastNames[int(random()*10)]
			doc = {"place":place,'num':num,"first_name":firstName, "last_name":lastName} # This is a doc for MongoDB.
			self.mongodb_data.append(doc)
			entry = {place, num, firstName, lastName} # This is an entry for MySQL.
			self.mysql_data.append(entry)
		end = time.time()
		print("Documents have been generated. Time: ", end-start)


class MongoDatabasePopulator:

	def insertOneDocument(self, collection):
		document = {"first_name":"Abraham", "last_name":"Lincoln"}
		collection.insert_one(document)

	def insertTwoDocuments(self, collection):
		document1 = {"first_name":"Fred", "last_name":"Polk"}
		document2 = {"first_name":"Alfred", "last_name":"Polk"}
		collection.insert_many([document1, document2])

	def generateDocuments(self, size):
		firstNames = ['George','John','Thomas','James','John','Andrew','Zachary','Millard','Franklin','Abraham']
		lastNames = ['Washington','Adams','Jefferson','Madison','Monroe','Jackson','Tyler','Polk','Taylor','Fillmore']
		values = []
		print("Beginning generation of documents...")
		start = time.time()
		for x in range(size):
			doc = {"place":x,'num':int(random()*1000),"first_name":firstNames[int(random()*10)], "last_name":lastNames[int(random()*10)]}
			values.append(doc)
		end = time.time()
		print("Documents have been generated. Time: ", end-start)
		return values;

	def insertDocuments(self, collection, documents):
		print("Beginning insertion of documents...")
		start = time.time()
		collection.insert_many(documents) # Inserts the documents into MongoDB. 
		end = time.time()
		print("All documents inserted into MongoDB. Time: ", end-start)

class MongoFindOperations:

	def findDocuments(self, criteria, collection): # This function doesn't take much time. It doesn't do what you think it does. 
		print("Searching for: ", criteria)
		start = time.time()
		results = collection.find(criteria) # TO-DO: Look into what .find() is really doing under the hood. 
		end = time.time()
		print("MongoDB has been searched. Time: ", end-start) 
		return results