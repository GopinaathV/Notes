import unittest
from binary_search import binary_search



class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(binary_search([1,2,3],3), True)

    def test_add_negative_numbers(self):
        self.assertEqual(binary_search([1,2,3],4), False)


if __name__ == '__main__':
    unittest.main()


