import sqlite3
from ITBooks.con import config


class SqliteDb():
    """
    Connect Sqlite3
    """

    def __init__(self):
        _sqlite_file = config.SQLITE_FILE
        self.conn = sqlite3.connect(_sqlite_file)
        self.cur = self.conn.cursor()

    def sql_search(self, table, title=None, author=None):
        """
        Search book from title or author
        return result if True else None
        """
        title = title.strip() if title else title
        author = author.strip() if author else author
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
        select_sql = "SELECT * FROM {0} WHERE {1}".format(table, condition)
        try:
            result = self.conn.execute(select_sql).fetchall()
            return result if result else None
        except:
            return None

    def __del__(self):
        self.cur.close()
        self.conn.close()
