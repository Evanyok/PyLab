
import unittest

def add(a, b):
    return a + b

class UT(unittest.TestCase):
    
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(self):
        print("setUpClass")

    @classmethod
    def tearDownClass(self):
        print("tearDownClass")
    
    def test_add(self):
        print("test_add")
        self.assertEqual(add(1,3), 4)

if __name__ == '__main__':
    unittest.main()