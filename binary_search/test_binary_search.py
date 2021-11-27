import binary_search.binary_search as bsearch
import unittest

class Test_binary_search(unittest.TestCase):

    def test_binary_mid(self):
        self.assertEqual(bsearch.binary_search([1,2,3,4,5], 3), True)

    def test_binary_value_found(self):
        self.assertEqual(bsearch.binary_search([1,2,3,4,5], 4), True)

    def test_binary_value_is_query(self):
        self.assertEqual(bsearch.binary_search([1,2,3,4,5], 1), True)

    def test_last_value_is_query(self):
        self.assertEqual(bsearch.binary_search([1,2,3,4,5], 5), True)

    def test_binary_value_not_found(self):
        self.assertEqual(bsearch.binary_search([1,2,3,4,5], 6), False)
    
    def test_empty_list(self):
        self.assertEqual(bsearch.binary_search([], 1), False)

    def test_bin_str_found(self):
        self.assertEqual(bsearch.binary_search(['a','b','c','d','e'], 'a'),True)