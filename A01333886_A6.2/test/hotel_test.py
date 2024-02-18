import unittest
import os

class HotelTest(unittest.TestCase):

    def test_new_hotel(self):
        self.assertTrue(os.path.isfile("../app/Hotel.txt"))
        self.assertFalse(os.path.isfile("../app/Hotels.txt"))


    if __name__ == '__main__':
        unittest.main()