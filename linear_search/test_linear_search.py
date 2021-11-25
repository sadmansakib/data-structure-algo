import linear_search.linear_search as lsearch
import unittest

class Test_linear_search(unittest.TestCase):

    def test_linear_value_found(self):
        self.assertEqual(lsearch.linear_search([1,2,3,4,5], 3), 2)

    def test_first_value_is_query(self):
        self.assertEqual(lsearch.linear_search([1,2,3,4,5], 1), 0)

    def test_last_value_is_query(self):
        self.assertEqual(lsearch.linear_search([1,2,3,4,5], 5), 4)

    def test_linear_value_not_found(self):
        self.assertEqual(lsearch.linear_search([1,2,3,4,5], 6), -1)