# Ctrl+B to run in Sublime Text 3
# Sublime Text Indentation Tip/Fix: Ctrl+Shift+P or View -> Command Palette -> Convert Indentation to Spaces
import unittest
import SupportingFunctions

class TestStringMethods(unittest.TestCase):

    def test_generic_datab_generator_MySQL(self):
        populator = SupportingFunctions.GenericDataGenerator()
        sql = populator.generate(10, True)
        self.assertTrue(10 == len(sql))
    
    def test_generic_data_generator_Mongo(self):
        populator = SupportingFunctions.GenericDataGenerator()
        docs = populator.generate(10, False)
        self.assertTrue(10 == len(docs))

    def test_generic_data_generator_Both(self):
        populator = SupportingFunctions.GenericDataGenerator()
        sql = populator.generate(5, True)
        docs = populator.generate(5, False)
        self.assertTrue(5 == len(sql))
        self.assertTrue(5 == len(docs))

    def test_verify_data_MySQL(self):
        populator = SupportingFunctions.GenericDataGenerator()
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

    def test_verify_data_Mongo(self):
        populator = SupportingFunctions.GenericDataGenerator()
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

    def test_first_names_should_be_equal_Both(self):
        populator = SupportingFunctions.GenericDataGenerator()
        docs = populator.generate(1, False)
        sql = populator.generate(1, True)
        self.assertTrue(docs[0]['first_name'] == sql[0][2])

    def test_last_names_should_be_equal_Both(self):
        populator = SupportingFunctions.GenericDataGenerator()
        docs = populator.generate(1, False)
        sql = populator.generate(1, True)
        self.assertTrue(docs[0]['last_name'] == sql[0][3])

    def test_num_should_be_equal_Both(self):
        populator = SupportingFunctions.GenericDataGenerator()
        docs = populator.generate(1, False)
        sql = populator.generate(1, True)
        self.assertTrue(docs[0]['num'] == sql[0][1])

    def test_place_should_be_equal_Both(self):
        populator = SupportingFunctions.GenericDataGenerator()
        docs = populator.generate(1, False)
        sql = populator.generate(1, True)
        self.assertTrue(docs[0]['place'] == sql[0][0])

    def test_all_data_should_be_equal_Both(self):
        populator = SupportingFunctions.GenericDataGenerator()
        docs = populator.generate(1, False)
        sql = populator.generate(1, True)
        self.assertTrue(docs[0]['last_name'] == sql[0][3])
        self.assertTrue(docs[0]['first_name'] == sql[0][2])
        self.assertTrue(docs[0]['num'] == sql[0][1])
        self.assertTrue(docs[0]['place'] == sql[0][0])

if __name__ == '__main__':
    unittest.main()