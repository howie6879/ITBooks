import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ITBooks.database.SqliteDb import SqliteDb
import ITBooks.con.config


class TestDb(unittest.TestCase):
    """
    Test database class
    """

    def setUp(self):
        self.db = SqliteDb()

    def tearDown(self):
        self.db = None

    def test_sql_search_allitebooks(self):
        result = self.db.sql_search(
            table="allitebooks",
            title="Mastering Python",
            author="Rick van Hattem")
        self.assertTrue(result)

    def test_sql_search_blah(self):
        result = self.db.sql_search(table="blah", title="射雕英雄传", author=" 金庸")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
