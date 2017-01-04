import sys
sys.path.append("/Users/howie/Documents/programming/python/git/ITBooks")
import unittest
from ITBooks.database.SqliteDb import SqliteDb


class TestDb(unittest.TestCase):
    """
    Tset database class
    """

    def setUp(self):
        self.db = SqliteDb()

    def tearDown(self):
        self.db = None

    def test_sql_search(self):
        result = self.db.sql_search(
            title="Mastering Python", author="Rick van Hattem")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
