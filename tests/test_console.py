import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ITBooks.console import Console


class TestDb(unittest.TestCase):
    """
    Tset database class
    """

    def setUp(self):
        self.console = Console()

    def tearDown(self):
        self.console = None

    def test_search_book(self):
        # result = self.console.search_book(title='Mastering Python')
        result = self.console.search_book(author='村上春树')


if __name__ == '__main__':
    unittest.main()
