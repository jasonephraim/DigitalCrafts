# Unit tests for the Pool Table Management App
from main import Table
import unittest
class TableTests(unittest.TestCase):
    def setUp(self):
       self.pool_tablea_app = Table()

    def testTableData(self):
        self.table_view({"Table Number": "Table 1"}, {"Table Status": "Occupied"})
        self.assertEqual("Table 1", self.table_view.table_number)
   
    def tearDown(self): # clean up the resources
        # deleting the file 
        # removing records from database 
        print("TEAR DOWN")
unittest.main()