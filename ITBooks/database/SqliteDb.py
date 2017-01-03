import sys
sys.path.append(
    '/Users/howie/Documents/programming/python/2016/12-06/ITBooks/')
import sqlite3
from ITBooks.conf import config


class SqliteDb():
    """
    Connect Sqlite3
    """

    def __init__(self):
        _sqlite_file = config.SQLITE_FILE
        self._sqlite_table = config.SQLITE_TABLE
        self.conn = sqlite3.connect(_sqlite_file)
        self.cur = self.conn.cursor()

    def sql_search(self, name=None, author=None):
        """
        Search book from name or author
        return result if True else None
        """
        if name and author:
            condition = '{name} AND {author}'
        elif name and not author:
            condition = '{name}'
        elif author and not name:
            condition = '{author}'
        else:
            return None
        condition = condition.format(
            name="name LIKE \"%{0}%\"".format(name) if name else "",
            author="author LIKE \"%{0}%\"".format(author) if author else "")
        select_sql = "SELECT * FROM {0} WHERE {1}".format(self._sqlite_table,
                                                          condition)
        try:
            result = self.conn.execute(select_sql).fetchall()
            if result:
                return result
            else:
                return None
        except:
            return None

    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    sql = SqliteDb()
    sql.sql_search(name=None, author='Changyi Gu')
