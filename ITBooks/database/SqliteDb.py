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

    def sql_search(self, title=None, author=None):
        """
        Search book from title or author
        return result if True else None
        """
        if title and author:
            condition = '{title} AND {author}'
        elif title and not author:
            condition = '{title}'
        elif author and not title:
            condition = '{author}'
        else:
            return None
        condition = condition.format(
            title="title LIKE \"%{0}%\"".format(title) if title else "",
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


if __name__ == "__main__":
    a = SqliteDb()
    print(
        a.sql_search(
            title='Building Embedded Systems', author="Vaibhav Bhandari"))
