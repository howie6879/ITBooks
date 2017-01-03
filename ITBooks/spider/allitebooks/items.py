# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class AllitebooksItem(Item):
    # Primary fields
    title = Field()
    cover = Field()
    author = Field()
    isbn = Field()
    year = Field()
    pages = Field()
    language = Field()
    file_size = Field()
    file_format = Field()
    category = Field()
    description = Field()
    download = Field()

    # Housekeeping fields
    url = Field()
    spider = Field()
    date = Field()
