import unittest
import os

class CustomerTest(unittest.TestCase):

    def test_new_customer(self):
        self.assertTrue(os.path.isfile("../app/Customer.txt"))
        self.assertFalse(os.path.isfile("../app/Customers.txt"))


    if __name__ == '__main__':
        unittest.main()