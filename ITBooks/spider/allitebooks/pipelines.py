# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem


class AllitebooksPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        _sqlite_file = settings["SQLITE_FILE"]
        self._sqlite_table = settings["SQLITE_TABLE_ALLITEBOOKS"]
        self.conn = sqlite3.connect(_sqlite_file)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            data = {}
            for key, value in dict(item).items():
                data[key] = value[0] if value[0] else None
            column = ','.join(data.keys())
            value = tuple(data.values())
            if spider.name == "allitebooks":
                insert_sql = "insert into {0}({1}) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(
                    spider.name, column)
            elif spider.name == "blah":
                insert_sql = "insert into {0}({1}) values (?,?,?,?,?,?,?,?,?,?,?,?)".format(
                    spider.name, column)
            self.conn.execute(insert_sql, value)
            self.conn.commit()
            return item

    def search_url(self, table, url):
        select_sql = "SELECT url FROM {0} WHERE url = \"{1}\"".format(table,
                                                                      url)
        result = self.conn.execute(select_sql).fetchall()
        self.conn.close()
        return True if result else False


class BlahPipeline(AllitebooksPipeline):
    def __init__(self):
        settings = get_project_settings()
        _sqlite_file = settings["SQLITE_FILE"]
        self._sqlite_table = settings["SQLITE_TABLE_BLAH"]
        self.conn = sqlite3.connect(_sqlite_file)
        self.cur = self.conn.cursor()


class TaiwanebookPipeline(AllitebooksPipeline):
    def __init__(self):
        settings = get_project_settings()
        _sqlite_file = settings["SQLITE_FILE"]
        self._sqlite_table = settings["SQLITE_TABLE_TAIWANEBOOK"]
        self.conn = sqlite3.connect(_sqlite_file)
        self.cur = self.conn.cursor()
