import unittest
import SupportingFunctions

class TestStringMethods(unittest.TestCase):

    def test_genericDatabasePopulator_MySQL(self):
        populator = SupportingFunctions.GenericDatabasePopulator()
        sql = populator.generateDocuments(10, True)
        self.assertTrue(10 == len(sql))
    
    def test_genericDatabasePopulator_Mongo(self):
        populator = SupportingFunctions.GenericDatabasePopulator()
        docs = populator.generateDocuments(10, False)
        self.assertTrue(10 == len(docs))

    def test_genericDatabasePopulator_All(self):
        populator = SupportingFunctions.GenericDatabasePopulator()
        sql = populator.generateDocuments(10, True)
        docs = populator.generateDocuments(10, False)
        self.assertTrue(10 == len(sql))
        self.assertTrue(10 == len(docs))

    

if __name__ == '__main__':
    unittest.main()