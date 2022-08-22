import unittest
import SupportingFunctions

class TestStringMethods(unittest.TestCase):

    def test_genericDatabasePopulator_MySQL(self):
        populator = SupportingFunctions.GenericDatabasePopulator()
        sql = populator.generate(10, True)
        self.assertTrue(10 == len(sql))
    
    def test_genericDatabasePopulator_Mongo(self):
        populator = SupportingFunctions.GenericDatabasePopulator()
        docs = populator.generate(10, False)
        self.assertTrue(10 == len(docs))

    def test_genericDatabasePopulator_All(self):
        populator = SupportingFunctions.GenericDatabasePopulator()
        sql = populator.generate(10, True)
        docs = populator.generate(10, False)
        self.assertTrue(10 == len(sql))
        self.assertTrue(10 == len(docs))

    def test_verifyContent_MySQL(self):
    	populator = SupportingFunctions.GenericDatabasePopulator()
    	sql = populator.generate(1, True) # Ex: [(0, 648, 'George', 'Fillmore')]
    	firstNameExists = False
    	lastNameExists = False
    	for firstName in populator.firstNames:
    		if sql[0][2] == firstName:
    			firstNameExists = True
    	for lastName in populator.lastNames:
    		if sql[0][3] == lastName:
    			lastNameExists = True
    	self.assertTrue(firstNameExists)
    	self.assertTrue(lastNameExists)

    def test_verifyContent_MongoDB(self):
    	populator = SupportingFunctions.GenericDatabasePopulator()
    	docs = populator.generate(1, False) # Ex: [{'place': 0, 'num': 645, 'first_name': 'Franklin', 'last_name': 'Fillmore'}]
    	firstNameExists = False
    	lastNameExists = False
    	for firstName in populator.firstNames:
    		if docs[0]['first_name'] == firstName:
    			firstNameExists = True
    	for lastName in populator.lastNames:
    		if docs[0]['last_name'] == lastName:
    			lastNameExists = True
    	self.assertTrue(firstNameExists)
    	self.assertTrue(lastNameExists)

if __name__ == '__main__':
    unittest.main()