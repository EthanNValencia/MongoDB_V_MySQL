import time
from random import seed
from random import random

class MongoDeleteOperations:

	def delete_results(self, collection, results):
		for result in results:
			print("Deleting: ", result)
			start = time.time()
			collection.delete_one({"_id": result["_id"]})
			end = time.time()
			print("Document deleted from MongoDB. Time: ", end-start)

	def delete_all(self, collection):
		print("Deleting all documents from MongoDB...")
		start = time.time()
		collection.delete_many({})
		end = time.time()
		print("All documents deleted. Time: ", end-start)

class MongoPrintOperations:

	def print_results(self, results):
		for result in results:
			print(result)
			print(result["_id"])

	def print_collection(self, collection):
		for item in collection:
			print(item)

	def print_results_size(self, results):
		counter = 0
		print("Counting the result set...")
		start = time.time()
		for result in results:
			counter += 1
		end = time.time()
		print("Result set has been counted. Time: ", end-start)
		print("Total size of the returned result set is: ", counter)

	def print_collection_count(self, collection):
		post_count = collection.count_documents({})
		print("Results size is: ", post_count)


class GenericDataGenerator:

	mysql_data = []
	mongodb_data = []
	# firstNames and lastNames are selected using a random function. The idea is to generate pseudo-unique data that is readily queryable. 
	firstNames = ['George','John','Thomas','James','John','Andrew','Zachary','Millard','Franklin','Abraham']
	lastNames = ['Washington','Adams','Jefferson','Madison','Monroe','Jackson','Tyler','Polk','Taylor','Fillmore']

	def generate(self, size, returnSQL):
		values = []
		if len(self.mysql_data) != size or len(self.mongodb_data) != size: # Objective: Only generate the data if it does not match the size or is empty. 
			self.mysql_data.clear()
			self.mongodb_data.clear()
			self.populate_data_arrays(size)
		if returnSQL is True:
			return self.mysql_data
		if returnSQL is False:
			return self.mongodb_data

	def populate_data_arrays(self, size): # I only want this method to be called if data has not been generated or if the size of the data structure does not match the size parameter. 
		print("Beginning generation of documents...")
		start = time.time()
		for x in range(size):
			place = x
			num = int(random()*1000)
			firstName = self.firstNames[int(random()*10)]
			lastName = self.lastNames[int(random()*10)]
			doc = {"place":place,'num':num,"first_name":firstName, "last_name":lastName} # This is a doc for MongoDB.
			# Note: The doc will be unordered. This isn't necessarily a problem for MongoDB. 
			self.mongodb_data.append(doc)
			entry = (place, num, firstName, lastName) # This is an entry for MySQL.
			# Note: Python Dictionaries are unordered, so using a dictionary for the entry would cause insertion mismatch errors. I need to use a list or a tuple. 
			self.mysql_data.append(entry)
		end = time.time()
		print("Documents have been generated. Time: ", end-start)


class MongoInsertOperations:

	def insertOneDocument(self, collection):
		document = {"first_name":"Abraham", "last_name":"Lincoln"}
		collection.insert_one(document)

	def insertTwoDocuments(self, collection):
		document1 = {"first_name":"Fred", "last_name":"Polk"}
		document2 = {"first_name":"Alfred", "last_name":"Polk"}
		collection.insert_many([document1, document2])

	def insert_documents(self, collection, documents):
		print("Beginning insertion of documents...")
		start = time.time()
		collection.insert_many(documents) # Inserts the documents into MongoDB. 
		end = time.time()
		print("All documents inserted into MongoDB. Time: ", end-start)

class MongoFindOperations:

	def find_documents(self, criteria, collection): # This function doesn't take much time. It doesn't do what you think it does. 
		print("Searching for: ", criteria)
		start = time.time()
		results = collection.find(criteria) # TO-DO: Look into what .find() is really doing under the hood. 
		end = time.time()
		print("MongoDB has been searched. Time: ", end-start)
		return results

class MySQLInsertOperations:

	def insert_many(self, values, myCursor, mydb):
		sql = "INSERT INTO data_table (place, num, first_name, last_name) VALUES (%s, %s, %s, %s)"
		print("Beginning insertion of entries...")
		start = time.time()
		myCursor.executemany(sql, values)
		mydb.commit()
		end = time.time()
		print(myCursor.rowcount, "was inserted.", "Time: ", end-start)

class MySQLDeleteOperations:

	def delete_all(self, myCursor, mydb):
		sql = "DELETE FROM data_table"
		print("Beginning deletion of all entries...")
		start = time.time()
		myCursor.execute(sql)
		mydb.commit()
		end = time.time()
		print("Delete Time:", end-start)

class MySQLFindOperations:

	def select_last_name(self, criteria, myCursor):
		sql = "SELECT * FROM data_table WHERE last_name = %s"
		param = [criteria]
		print("Beginning deletion of entries where last_name is", criteria)
		start = time.time()
		myCursor.execute(sql, param)
		results = myCursor.fetchall()
		end = time.time()
		print("Entries matching", criteria, "found:", len(results), "Time:", end-start)
		return results