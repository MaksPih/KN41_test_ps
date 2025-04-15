import unittest
from main import print_list_elements

class TestPrintListElements(unittest.TestCase):
    def test_returns_true(self):
        result = print_list_elements([10, 20, 30])
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()